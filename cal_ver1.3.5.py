import time
import sys
import math
print('Calculator')
ver = '1.3.6:1.3.1_Dev'
builder = 'Aya0_Mi5on0'
year = '2021'
month = 'Oct'
day = '16'
print('Version', ver)
print(builder,'/',month,day,year)

# 代入コード1
def all_calc_code():
    cal_mode = (input('使用するモードを選択してください。通常計算モードは1、面積計算モードは2、体積計算モードは3、表面積計算モードは4です。'))
    if cal_mode == '1':
        print('通常計算モードで起動します。')
        time.sleep(1)
        n = float(input('nに代入する数字を入力してください。'))
        def rep(n):
            x = float(input('xに代入する数字を入力してください。'))
            print('nに代入された数字= ', n)
            print('xに代入された数字= ', x)
            # 演算子の指定
            cal_mode_2 = (input('どの計算がしたいですか？加算は1、乗算は2、減算は3、除算は4、除算の商は5、除算の剰余は6、べき乗は7、平方根は8です。:'))
            # 計算
            if cal_mode_2 == '1':
                n_x_0 = n + x
                print('n + x =', n_x_0)
                n_x_8 = n_x_0
            elif cal_mode_2 == '2':
                n_x_1 = n * x
                print('n * x =', n_x_1)
                n_x_8 = n_x_1
            elif cal_mode_2 == '3':
                n_x_2 = n - x
                print('n - x =', n_x_2)
                n_x_8 = n_x_2
            elif cal_mode_2 == '4':
                n_x_3 = n / x
                print('n / x =', n_x_3)
                n_x_8 = n_x_3
            elif cal_mode_2 == '5':
                n_x_4 = n // x
                print('n // x =',n_x_4)
                n_x_8 = n_x_4
            elif cal_mode_2 == '6':
                n_x_5 = n % x
                print('n % x =',n_x_5)
                n_x_8 = n_x_5
            elif cal_mode_2 == '7':
                n_x_6 = n ** x
                print('n^x =',n_x_6)
                n_x_8 = n_x_6
            elif cal_mode_2 == '8':
                cal_mode_2_1 = (input('平方根を求めたい値はどちらですか？n/x or 0/1:'))
                if cal_mode_2_1 == 'n':
                    cal_mode_2_1 = '1'
                if cal_mode_2_1 == 'x':
                    cal_mode_2_1 = '2'
                if cal_mode_2_1 == '1':
                    n_x_7 = math.sqrt(n)
                    print('√n =',n_x_7,'√',n)
                    n_x_8 = n_x_7
                elif cal_mode_2_1 == '2':
                    n_x_7 = math.sqrt(x)
                    print('√x =',n_x_7,'√',x)
                    n_x_8 = n_x_7
                else:
                    print('深刻なエラーが発生しました。プログラムを再起動します。')
                    time.sleep(1)
                    all_calc_code()
            else:
                n_x_8 = n
                error = '深刻なエラーが発生しました。計算を強制終了します。'
                time.sleep(1)
                print(error)
                time.sleep(3)
                rep4 = (input('嘘です。計算をやり直しますか？ y/n or 1/0:'))
                if rep4 == '1':
                    rep4 = 'y'
                elif rep4 == '0':
                    rep4 = 'n'
                if rep4 == 'y':
                    rep4_2 = (input('nに代入した数を残しますか？ y/n or 1/0:'))
                    if rep4_2 == '1':
                        rep4_2 = 'y'
                    elif rep4_2 == '0':
                        rep4_2 = 'n'
                    if rep4_2 == 'y':
                        print('nの数字を引き継ぎます。')
                        print('引き継いだ数字:', n_x_8)
                        rep(n)
                    elif rep4_2 == 'n':
                        n = float(input('nに代入する数字を入力してください。:'))
                    else:
                        print('深刻なエラーが発生しました。プログラムを再起動します。')
                        time.sleep(1)
                        all_calc_code()
                    rep(n)
                elif rep4 == 'n':
                    time.sleep(1)
                    print('計算を終了します。')
                    time.sleep(1)
                    sys.exit()
                else:
                    print('深刻なエラーが発生しました。プログラムを再起動します。')
                    time.sleep(1)
                    all_calc_code()
            # 再計算するかの確認
            rep2 = (input('もう一回計算したいですか？　y/n or 1/0:'))
            if rep2 == "1":
                rep2 = 'y'
            elif rep2 == "0":
                rep2 = 'n'
            if rep2 == 'y':
                # 計算結果の引継ぎの確認
                rep3 = (input('計算結果を引継ぎますか？ y/n or 1/0:'))
                if rep3 == "1":
                    rep3 = 'y'
                elif rep3 == "0":
                    rep3 = 'n'
                if rep3 == 'y':
                    n = n_x_8
                    print('nに結果を引き継ぎます。引き継いだ結果:', n_x_8)
                    rep(n)
                elif rep3 == 'n':
                    # 再代入
                    n = float(input('nに代入する数字を入力してください。:'))
                    rep(n)
                else:
                    print('深刻なエラーが発生しました。プログラムを再起動します。')
                    time.sleep(1)
                    all_calc_code()
            elif rep2 == ('n'):
                # 終了メッセージ
                time.sleep(1)
                print('計算を終了します。')
                time.sleep(1)
                sys.exit()
            else:
                print('深刻なエラーが発生しました。プログラムを再起動します。')
                time.sleep(1)
                all_calc_code()
        rep(n)
    elif cal_mode == '2':
        print('面積計算モードで起動します。')
        time.sleep(1)
        cal_mode_3 = (input('面積を計算したい図形を入力してください。1は三角形、2は四角形、3は五角形、4は六角形、5は任意の角数の図形、6は円、7は楕円です。:'))
        if cal_mode_3 == '1':
            cal_mode_3_1 = (input('どちらの計算方法を利用しますか？3辺の長さを利用する場合:1/y 底辺の長さと高さを利用する場合:0/n:'))
            if cal_mode_3_1 == 'y':
                cal_mode_3_1 = '1'
            if cal_mode_3_1 == 'n':
                cal_mode_3_1 = '0'
            if cal_mode_3_1 == '1':
                cal_mode_3_1_1 =(input('面積を計算したい三角形の種類を選択してください。正三角形:1/y それ以外:0/n:'))
                if cal_mode_3_1_1 == 'y':
                    cal_mode_3_1_1 ='1'
                if cal_mode_3_1_1 == 'n':
                    cal_mode_3_1_1 = '0'
                if cal_mode_3_1_1 == '1':
                    cal_mode_3_1_1_val = (input('1辺の長さを入力してください。:'))
                    cal_n_1 = float(cal_mode_3_1_1_val)
                    cal_n_2 = float((cal_n_1 * 3)/2)
                    cal_n_3 = float(math.sqrt(cal_n_2*(float(3)(cal_n_2 - cal_n_1))))
                    area = str(cal_n_3)
                    print('面積:',area)
                    time.sleep(1)
                    print('計算を終了します。')
                    time.sleep(1)
                    sys.exit()
                elif cal_mode_3_1_1 =='0':
                    cal_mode_3_1_1_val_1 = float(input('1つ目の辺の長さを入力してください。:'))
                    cal_mode_3_1_1_val_2 = float(input('2つ目の辺の長さを入力してください。:'))
                    cal_mode_3_1_1_val_3 = float(input('3つ目の辺の長さを入力してください。:'))
                    cal_n_1_1 = cal_mode_3_1_1_val_1
                    cal_n_1_2 = cal_mode_3_1_1_val_2
                    cal_n_1_3 = cal_mode_3_1_1_val_3
                    cal_n_2 = float((cal_n_1_1 + cal_n_1_2 + cal_n_1_3)/2)
                    cal_n_3 = float(math.sqrt(cal_n_2*(cal_n_2 - cal_n_1_1)*(cal_n_2 - cal_n_1_2)*(cal_n_2 - cal_n_1_3)))
                    area = str(cal_n_3)
                    print('面積',area)
                    time.sleep(1)
                    print('計算を終了します。')
                    time.sleep(1)
                    sys.exit()
                else:
                    print('深刻なエラーが発生しました。プログラムを再起動します。')
                    time.sleep(1)
                    all_calc_code()
            elif cal_mode_3_1 == '0':
                cal_mode_3_1_2_val_1 = float(input('底辺の長さを入力してください。:'))
                cal_mode_3_1_2_val_2 = float(input('高さを入力してください。:'))
                cal_n_1_1 = cal_mode_3_1_2_val_1
                cal_n_1_2 = cal_mode_3_1_2_val_2
                cal_n_2 = float((cal_n_1_1 * cal_n_1_2)/2)
                area = str(cal_n_2)
                print('面積:',area)
                time.sleep(1)
                print('計算を終了します。')
                time.sleep(1)
                sys.exit()
            else:
                print('深刻なエラーが発生しました。プログラムを再起動します。')
                time.sleep(1)
                all_calc_code()
all_calc_code()
