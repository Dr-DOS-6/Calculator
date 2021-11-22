import time
import sys
import math
import menu
class menu():
    def cal_mode_2():
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
    cal_mode_2()