import math
import multiprocessing as mp
import numpy as np
import matplotlib.pyplot as plt
from dataclasses import dataclass
import sys
sys.setrecursionlimit(10000000)  # ← 必要に応じて（あくまで補助的）


# ベクトル演算
@dataclass
class Vec:
    x: float
    y: float
    z: float

    def __add__(self, b): return Vec(self.x + b.x, self.y + b.y, self.z + b.z)
    def __sub__(self, b): return Vec(self.x - b.x, self.y - b.y, self.z - b.z)
    def __mul__(self, b): return Vec(self.x * b, self.y * b, self.z * b) if isinstance(b, (int, float)) else Vec(self.x * b.x, self.y * b.y, self.z * b.z)
    def norm(self): return self * (1 / math.sqrt(self.x**2 + self.y**2 + self.z**2))
    def dot(self, b): return self.x * b.x + self.y * b.y + self.z * b.z
    def cross(self, b): return Vec(self.y * b.z - self.z * b.y, self.z * b.x - self.x * b.z, self.x * b.y - self.y * b.x)
    def clamp(self): return Vec(min(1, max(0, self.x)), min(1, max(0, self.y)), min(1, max(0, self.z)))
    def to_color(self): return [int(255 * self.clamp().x), int(255 * self.clamp().y), int(255 * self.clamp().z)]

@dataclass
class Ray:
    origin: Vec
    direction: Vec

# マテリアル定義
class Material:
    DIFFUSE = 0
    MIRROR = 1
    REFRACT = 2

@dataclass
class Sphere:
    radius: float
    position: Vec
    emission: Vec
    color: Vec
    material: int

    def intersect(self, ray: Ray):
        op = self.position - ray.origin
        b = op.dot(ray.direction)
        det = b * b - op.dot(op) + self.radius * self.radius
        if det < 0:
            return None
        det = math.sqrt(det)
        t1, t2 = b - det, b + det
        eps = 1e-4
        if t1 > eps:
            return t1
        if t2 > eps:
            return t2
        return None

# シーン構成
def create_scene():
    INF = 1e5
    return [
        # 球体3つ
        Sphere(1, Vec(-2, 1, -4), Vec(0, 0, 0), Vec(1, 0.2, 0.2), Material.DIFFUSE),
        Sphere(1, Vec(0, 1, -4), Vec(0, 0, 0), Vec(0.2, 1, 0.2), Material.MIRROR),
        Sphere(1, Vec(2, 1, -4), Vec(0, 0, 0), Vec(0.2, 0.2, 1), Material.DIFFUSE),

        # 屈折球体
        Sphere(1, Vec(0, 1, -6), Vec(0, 0, 0), Vec(1, 1, 1), Material.REFRACT),

        # 床（鏡面）
        Sphere(INF, Vec(0, -INF, 0), Vec(0, 0, 0), Vec(1, 1, 1), Material.MIRROR),

        # 左壁（鏡面）
        Sphere(INF, Vec(-INF, 0, 0), Vec(0, 0, 0), Vec(1, 1, 1), Material.MIRROR),

        # 右壁（拡散）
        Sphere(INF, Vec(INF, 0, 0), Vec(0, 0, 0), Vec(0.75, 0.75, 0.75), Material.DIFFUSE),

        # 奥壁（拡散）
        Sphere(INF, Vec(0, 0, -INF - 10), Vec(0, 0, 0), Vec(0.6, 0.6, 0.6), Material.DIFFUSE),
    ]

# 放射照度計算
def radiance(ray, depth, scene):
    t_hit = float('inf')
    hit_obj = None
    for obj in scene:
        t = obj.intersect(ray)
        if t and t < t_hit:
            t_hit = t
            hit_obj = obj
    if not hit_obj:
        return Vec(0, 0, 0)

    hit_point = ray.origin + ray.direction * t_hit
    normal = (hit_point - hit_obj.position).norm()
    nl = normal if normal.dot(ray.direction) < 0 else normal * -1
    color = hit_obj.color
    depth += 1

    if hit_obj.material == Material.DIFFUSE:
        # コサイン分布ランダム反射
        r1 = 2 * math.pi * np.random.rand()
        r2 = np.random.rand()
        r2s = math.sqrt(r2)
        w = nl
        u = (Vec(0.1, 1, 0).cross(w)).norm()
        v = w.cross(u)
        d = (u * math.cos(r1) * r2s + v * math.sin(r1) * r2s + w * math.sqrt(1 - r2)).norm()
        return hit_obj.emission + color * radiance(Ray(hit_point, d), depth, scene)
    elif hit_obj.material == Material.MIRROR:
        reflected = ray.direction - normal * 2 * normal.dot(ray.direction)
        return hit_obj.emission + color * radiance(Ray(hit_point, reflected), depth, scene)
    elif hit_obj.material == Material.REFRACT:
        refl_dir = ray.direction - normal * 2 * normal.dot(ray.direction)
        refl_ray = Ray(hit_point, refl_dir)
        into = normal.dot(nl) > 0
        nc, nt = 1, 1.5
        nnt = nc / nt if into else nt / nc
        ddn = ray.direction.dot(nl)
        cos2t = 1 - nnt * nnt * (1 - ddn * ddn)
        if cos2t < 0:
            return hit_obj.emission + color * radiance(refl_ray, depth, scene)
        tdir = (ray.direction * nnt - normal * (ddn * nnt + math.sqrt(cos2t))).norm()
        return hit_obj.emission + color * (
            radiance(refl_ray, depth, scene) * 0.5 +
            radiance(Ray(hit_point, tdir), depth, scene) * 0.5
        )

# 1行分のレンダリング
def render_line(args):
    y, width, height, fov, samples, scene = args
    img_row = np.zeros((width, 3))
    cx = Vec(width * fov / height, 0, 0)
    cy = (cx.cross(Vec(0, 0, -1))).norm() * fov
    cam = Ray(Vec(0, 1, 5), Vec(0, 0, -1).norm())

    for x in range(width):
        col = Vec(0, 0, 0)
        for s in range(samples):
            u = (x + np.random.rand()) / width
            v = (y + np.random.rand()) / height
            d = cx * (u - 0.5) + cy * (v - 0.5) + cam.direction
            col += radiance(Ray(cam.origin, d.norm()), 0, scene)
        col = col * (1.0 / samples)
        img_row[x] = [col.x, col.y, col.z]
    return y, img_row

# メイン関数
def main():
    width, height = 256, 192
    samples = 10
    fov = 0.5135
    scene = create_scene()
    image = np.zeros((height, width, 3))

    with mp.Pool(mp.cpu_count()) as pool:
        args = [(y, width, height, fov, samples, scene) for y in range(height)]
        for y, row in pool.imap_unordered(render_line, args):
            image[y] = row

    # 表示と保存
    plt.imshow(np.clip(image, 0, 1))
    plt.axis('off')
    plt.title("Ray Tracing Result")
    plt.savefig("rendered.png", dpi=300)
    plt.show()

if __name__ == '__main__':
    main()
