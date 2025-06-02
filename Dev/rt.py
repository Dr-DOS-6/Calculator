import sys
import subprocess
import importlib

# 必要モジュールのインストール
required_modules = ['numpy', 'Pillow', 'matplotlib']
for module in required_modules:
    try:
        importlib.import_module(module)
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", module])

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import time

# シーンの設定
WIDTH, HEIGHT = 200, 200
CAMERA_POS = np.array([0, 0, -1])
SPHERE_CENTER = np.array([0, 0, 3])
SPHERE_RADIUS = 1
LIGHT_POS = np.array([5, 5, -10])
BACKGROUND_COLOR = np.array([0, 0, 0])
SPHERE_COLOR = np.array([200, 50, 50])

def normalize(v):
    return v / np.linalg.norm(v)

def intersect_ray_sphere(ray_origin, ray_dir, sphere_center, sphere_radius):
    oc = ray_origin - sphere_center
    a = np.dot(ray_dir, ray_dir)
    b = 2.0 * np.dot(oc, ray_dir)
    c = np.dot(oc, oc) - sphere_radius ** 2
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        return None
    else:
        t = (-b - np.sqrt(discriminant)) / (2 * a)
        return t if t > 0 else None

def render(step_visualize=False, save_steps=False):
    image = np.zeros((HEIGHT, WIDTH, 3), dtype=np.uint8)

    for y in range(HEIGHT):
        for x in range(WIDTH):
            # スクリーン座標をワールド座標に変換
            px = (x - WIDTH / 2) / WIDTH
            py = -(y - HEIGHT / 2) / HEIGHT
            ray_dir = normalize(np.array([px, py, 1]))
            t = intersect_ray_sphere(CAMERA_POS, ray_dir, SPHERE_CENTER, SPHERE_RADIUS)

            if t is not None:
                hit_point = CAMERA_POS + t * ray_dir
                normal = normalize(hit_point - SPHERE_CENTER)
                to_light = normalize(LIGHT_POS - hit_point)
                brightness = np.clip(np.dot(normal, to_light), 0, 1)
                color = SPHERE_COLOR * brightness
                image[y, x] = color
            else:
                image[y, x] = BACKGROUND_COLOR

        if step_visualize:
            plt.imshow(image)
            plt.title(f"Rendering... row {y+1}/{HEIGHT}")
            plt.pause(0.001)

    img = Image.fromarray(image)
    img.save("output.png")
    print("画像保存完了: output.png")
    if not step_visualize:
        plt.imshow(image)
        plt.title("Ray Tracing Result")
        plt.axis('off')
        plt.show()

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="シンプルなレイトレーサー")
    parser.add_argument('--step', action='store_true', help="過程を1行ずつ描画")
    args = parser.parse_args()

    start = time.time()
    render(step_visualize=args.step)
    print(f"完了: {(time.time() - start):.2f} 秒")
