import time
import sys
import math
import os
import datetime
import platform as pf
pf_s = pf.system()
ver = pf.python_version()
date = datetime.datetime.today()
date_1 = date.strftime("%Y/%m/%d %H:%M:%S")
def sys_info():
    print ('System information for this computer:')
    print ('system   :', pf.system())
    print ('release  :', pf.release())
    print ('system_version  :', pf.version())
    print ('machine  :', pf.machine())
    print ('processor:', pf.processor())
    print ('python_version:',ver)
    print ('Software_version:',soft_ver)
    with open('error.log', mode='a', encoding='UTF-8') as f:
        datalist = ['\n','System: ',pf.system()+'\n','Release: ',pf.release()+'\n','System_version: ',pf.version()+'\n','Machine: ',pf.machine()+'\n','Processor: ',pf.processor()+'\n','Python_version: ',ver+'\n','Generated_Date: ',date_1+'\n','Software_version: ',soft_ver+'\n']
        f.writelines(datalist)
        f.close()
        print('An error log was output:',os.path.abspath('error.log'))
def clear():
    if pf_s == 'Windows':
        os.system('cls')
    elif pf_s == 'Linux' or 'Darwin':
        os.system('clear')
    else:
        error_end_3()
def end():
    time.sleep(1)
    print('Finish the calculation.')
    time.sleep(1)
    clear()
    sys.exit()
#エラー時再起動コード
def error_end(error_code):
    print('A serious error has occurred. Restarting the program.')
    print('Error code:',error_code)
    error_cnt[0] += 1
    if error_cnt[0] > 5:
        print('Multiple serious errors have occurred. Kill the program.')
        print('Error code: 0x000F')
        sys_info()
        os.system('PAUSE')
        sys.exit()
    os.system('PAUSE')
    clear()
    startup()
    all_calc_code()
def error_end_2(error_code):
    print('This feature is currently not implemented and cannot be activated. Restarting the program.')
    print('Error code:',error_code)
    error_cnt[0] += 1
    if error_cnt[0] > 5:
        print('Multiple serious errors have occurred. Kill the program.')
        print('Error code: 0x000F')
        sys_info()
        os.system('PAUSE')
        sys.exit()
    os.system('PAUSE')
    clear()
    startup()
    all_calc_code()
def error_end_3():
    print('This program will not run on this computer.')
    print('Error code: 0x000E')
    time.sleep(1)
    sys_info()
    sys.exit()
error = 'A serious error has occurred. Restarting the program.'
def startup():
    print('Calculator')
    global soft_ver
    soft_ver = '1.4.4.2_CUI_Dev_20220105'
    #Hallo 2022, Happy new year!!
    ver = 'Version'+' '+soft_ver
    #体積計算モード、表面積計算モードをモード2に統合
    #数値変換モードを復帰
    #モード1，2の名称変更
    #マルチプラットフォームへの対応
    #細部の修正
    #直接計算モード搭載
    #エラーログ出力機能の改修
    builder = 'Dr.DOS'
    year = '2021'
    built = builder+'/'+year
    Created_by_1 = 'Python 3.9.9'
    Created_by_2 = 'Visual Studio Code 1.62.3'
    Created_by = ('Created by'+' '+Created_by_1+' '+'and'+' '+Created_by_2)
    time.sleep(0.3)
    print(ver)
    time.sleep(0.3)
    print(built)
    time.sleep(0.3)
    print(Created_by)
    time.sleep(1)
    if pf_s == 'Windows' or pf_s == 'Linux' or pf_s == 'Darwin':
        return
    else:
        print("I'm sorry. This calculator is available for Windows, Linux, Chrome OS, and MacOS. Please make sure that your OS is supported.")
    #if not pf_s == 'Linux':
    #    print("I'm sorry. This calculator is available for Windows. Please make sure that your OS is supported.")
        time.sleep(0.5)
        error_end_3()
startup()
#error_end_3()
# 代入コード1
error_cnt = [0]
def all_calc_code():
    cal_mode = (input('使用するモードを選択してください。代数計算モードは1、幾何計算モードは2、数値変換モードは3、税計算モードは4、直接計算モードは5です。'))
    if cal_mode == '1':
        clear()
        print('代数計算モードで起動します。')
        time.sleep(1)
        n = float(input('nに代入する数字を入力してください。'))
        def rep(n):
            error = 'A serious error has occurred. Restarting the program.'
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
                if x == 0:
                    error_end('0x0001')
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
                cal_mode_2_1 = (input('平方根を求めたい値はどちらですか？n/x or 1/2:'))
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
                    error_end('0x0002')
            else:
                n_x_8 = n
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
                        error_end('0x0003')
                    rep(n)
                elif rep4 == 'n':
                    end()
                else:
                    error_end()
            # 再計算するかの確認
            rep2 = (input('もう一回計算したいですか？ y/n or 1/0:'))
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
                    clear()
                    n = n_x_8
                    print('nに結果を引き継ぎます。引き継いだ結果:', n_x_8)
                    rep(n)
                elif rep3 == 'n':
                    # 再代入
                    n = float(input('nに代入する数字を入力してください。:'))
                    rep(n)
                else:
                    error_end('0x0003')
            elif rep2 == ('n'):
                end()
            else:
                error_end('0x0004')
        rep(n)
    elif cal_mode == '2':
        clear()
        print('幾何計算モードで起動します。')
        time.sleep(1)
        cal_mode_int = (input('使用したいモードを選択してください。1:面積計算モード 2:体積計算モード 3:表面積計算モード :'))
        if cal_mode_int == '1':
            cal_mode_3 = (input('面積を計算したい図形を入力してください。1:三角形、2:四角形、3:五角形、4:円 :'))
            if cal_mode_3 == '1':
                cal_mode_3_1 = (input('どちらの計算方法を利用しますか？3辺の長さ:1/y 底辺の長さと高さ:0/n :'))
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
                        cal_mode_3_1_1_val = float(input('1辺の長さを入力してください。:'))
                        cal_n_1 = float(cal_mode_3_1_1_val)
                        cal_n_2 = float((cal_n_1 * 3)/2)
                        cal_n_3 = float(math.sqrt(cal_n_2*(float(3)(cal_n_2 - cal_n_1))))
                        cal_n_3_1 = str(cal_n_3)
                        area = cal_n_3_1
                        print('面積:',area)
                        end()
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
                        end()
                    else:
                        error_end('0x0004')
                elif cal_mode_3_1 == '0':
                    cal_mode_3_1_2_val_1 = float(input('底辺の長さを入力してください。:'))
                    cal_mode_3_1_2_val_2 = float(input('高さを入力してください。:'))
                    cal_n_1_1 = cal_mode_3_1_2_val_1
                    cal_n_1_2 = cal_mode_3_1_2_val_2
                    cal_n_2 = float((cal_n_1_1 * cal_n_1_2)/2)
                    area = str(cal_n_2)
                    print('面積:',area)
                    end()
                else:
                    error_end('0x0004')
            if cal_mode_3 == '2':
                cal_mode_3_2 = (input('面積を計算したい四角形の種類を入力してください。1:正方形 2:長方形 3:平行四辺形 4:台形 5:菱形 6:それ以外の四角形:'))
                if cal_mode_3_2 == '1':
                    cal_mode_3_2_1 = float(input('1辺の長さを入力してください。:'))
                    cal_n_1 = cal_mode_3_2_1
                    cal_n_2 = cal_n_1 ** 2
                    area = str(cal_n_2)
                    print('面積:',area)
                    end()
                elif cal_mode_3_2 == '2':
                    cal_mode_3_2_1 = float(input('高さを入力してください。:'))
                    cal_mode_3_2_2 = float(input('横幅を入力してください。:'))
                    cal_n_1 = cal_mode_3_2_1
                    cal_n_2 = cal_mode_3_2_2 
                    cal_n_3 = cal_n_1 * cal_n_2
                    area = cal_n_3
                    print('面積:',area)
                    end()
                elif cal_mode_3_2 == '3':
                    cal_mode_3_2_1 = float(input('高さを入力してください。:'))
                    cal_mode_3_2_2 = float(input('上底/下底どちらかの長さを入力してください。'))
                    cal_n_1 = cal_mode_3_2_1
                    cal_n_2 = cal_mode_3_2_2 
                    cal_n_3 = cal_n_1 * cal_n_2
                    area = cal_n_3
                    print('面積:',area)
                    end()
                elif cal_mode_3_2 == '4':
                    cal_mode_3_2_1 = float(input('高さを入力してください。'))
                    cal_mode_3_2_2 = float(input('上底の長さを入力してください。'))
                    cal_mode_3_2_3 = float(input('下底の長さを入力してください。'))
                    cal_n_1 = cal_mode_3_2_1
                    cal_n_2 = cal_mode_3_2_2
                    cal_n_3 = cal_mode_3_2_3
                    cal_n_4 = ((cal_n_2 + cal_n_3)*cal_n_1)/2
                    area = cal_n_4
                    print('面積:',area)
                    end()
                elif cal_mode_3_2 == '5':
                    cal_mode_3_2_1 = float(input('縦の対角線の長さを入力してください。:'))
                    cal_mode_3_2_2 = float(input('横の対角線の長さを入力してください。:'))
                    cal_n_1 = cal_mode_3_2_1
                    cal_n_2 = cal_mode_3_2_2
                    cal_n_3 = (cal_n_1 * cal_n_2)/2
                    area = cal_n_3
                    print('面積:',area)
                    end()
                elif cal_mode_3_2 == '6':
                    cal_mode_3_2_1 = (input('使用したい計算方法を入力してください。1:4つの辺と対角線の長さ 2:2本の対角線の長さとその交わる角度 3:ブレートシュナイダーの公式:'))
                    if cal_mode_3_2_1 == '1':
                        print('辺の長さは、上→右→下→左の順に入力してください。')
                        cal_n_1 = float(input('1つ目の辺の長さを入力してください。:'))
                        cal_n_2 = float(input('2つ目の辺の長さを入力してください。:'))
                        cal_n_3 = float(input('3つ目の辺の長さを入力してください。:'))
                        cal_n_4 = float(input('4つ目の辺の長さを入力してください。:'))
                        cal_n_5 = (input('対角線の向きを入力してください。左上から右下:0 右上から左下:1 :'))
                        if cal_n_5 == '0':
                            cal_n_5_1 = float(input('対角線の長さを入力してください。:'))
                            cal_n_6 = float((cal_n_1 + cal_n_2 + cal_n_5_1)/float(2))
                            area_1 = float(math.sqrt(cal_n_6*(cal_n_6 - cal_n_1)*(cal_n_6 - cal_n_2)*(cal_n_6 - cal_n_5_1)))
                            cal_n_7 = float((cal_n_3 + cal_n_4 + cal_n_5_1)/float(2))
                            area_2 = float(math.sqrt(cal_n_7*(cal_n_7 - cal_n_3)*(cal_n_7 - cal_n_4)*(cal_n_7 - cal_n_5_1)))
                            area_all = str(area_1 + area_2)
                        elif cal_n_5 == '1':
                            cal_n_5_1 = float(input('対角線の長さを入力してください。:'))
                            cal_n_6 = float((cal_n_4 + cal_n_1 + cal_n_5_1)/float(2))
                            area_1 = float(math.sqrt(cal_n_6*(cal_n_6 - cal_n_4)*(cal_n_6 - cal_n_1)*(cal_n_6 - cal_n_5_1)))
                            cal_n_7 = float((cal_n_2 + cal_n_3 + cal_n_5_1)/float(2))
                            area_2 = float(math.sqrt(cal_n_7*(cal_n_7 - cal_n_2)*(cal_n_7 - cal_n_3)*(cal_n_7 - cal_n_5_1)))
                            area_all = str(area_1 + area_2)
                        else:
                            error_end('0x0004')
                        print('面積:',area_all)
                        end()
                    elif cal_mode_3_2_1 == '2':
                        cal_n_1 = float(input('1つ目の対角線の長さを入力してください。:'))
                        cal_n_2 = float(input('2つ目の対角線の長さを入力してください。:'))
                        cal_n_3 = input('θの大きさを選んでください。15°:0 30°:1 45°:2 60°:3 75°:4 90°:5 :')
                        cal_n_4 = (cal_n_1*cal_n_2)
                        if cal_n_3 == '0':
                            area = float(0.5*cal_n_4*(((math.sqrt(6))-(math.sqrt(2)))/4))
                        elif cal_n_3 == '1':
                            area = float(0.5*cal_n_4*0.5)
                        elif cal_n_3 == '2':
                            area = float(0.5*cal_n_4*(math.sqrt(2)/2))
                        elif cal_n_3 == '3':
                            area = float(0.5*cal_n_4*(math.sqrt(3)/2))
                        elif cal_n_3 == '4':
                            area = float(0.5*cal_n_4*(((math.sqrt(2))+(math.sqrt(6)))/4))
                        elif cal_n_3 == '5':
                            area = float(0.5*cal_n_4)
                        else:
                            error_end('0x0004')
                        print('面積:',area)
                        end()
                    elif cal_mode_3_2_1 == '3':
                        cal_n_1 = float(input('1つ目の辺の長さを入力してください。:'))
                        cal_n_2 = float(input('2つ目の辺の長さを入力してください。:'))
                        cal_n_3 = float(input('3つ目の辺の長さを入力してください。:'))
                        cal_n_4 = float(input('4つ目の辺の長さを入力してください。:'))
                        cal_n_5 = float(input('1つ目の角の大きさを指定してください。15°:0 30°:1 45°:2 60°:3 75°:4 90°:5:'))
                        cal_n_6 = float(input('2つ目の角の大きさを指定してください。15°:0 30°:1 45°:2 60°:3 75°:4 90°:5:'))
                        #cal_n_7の値と整数の一覧:30°:0 45°:1 60°:2 75°:3 90°:4 105°:5 120°:6 135°:7 150°:8 165°:9 180°:10
                        #90°を超える場合、角度をθとした場合、(sin or cos)90° + (sin or cos)θ-90°
                        cal_n_7 = cal_n_5 + cal_n_6 
                        if cal_n_7 == 0 or cal_n_7 == 8:
                            cal_n_7 = 1/2
                        elif cal_n_7 == 1 or cal_n_7 == 7:
                            cal_n_7 = 0
                        elif cal_n_7 == 2 or cal_n_7 == 6:
                            cal_n_7 = -1/2
                        elif cal_n_7 == 3 or cal_n_7 == 5:
                            cal_n_7 = (-1*(math.sqrt(3)/2))
                        elif cal_n_7 == 4:
                            cal_n_7 = -1
                        elif cal_n_7 == 9:
                            cal_n_7 = (math.sqrt(3)/2)
                        elif cal_n_7 == '10':
                            cal_n_7 = 1
                        else:
                            error_end('0x0004')
                        s = ((cal_n_1+cal_n_2+cal_n_3+cal_n_4)/2)
                        area_all = (math.sqrt((s-cal_n_1)*(s-cal_n_2)*(s-cal_n_3)*(s-cal_n_4)-cal_n_1*cal_n_2*cal_n_3*cal_n_4*((1+cal_n_7)/2)))
                        print('面積:',area_all)
                        end()
                    else:
                        error_end('0x0004')
            elif cal_mode_3 == '3':
                cal_mode_3_2 = input('面積を求めたい五角形の種類を指定してください。正五角形:1 五角形:2')
                if cal_mode_3_2 == '1':
                    cal_n_1 = float(input('一辺の長さを入力してください。:'))
                    cal_n_2 = float(input('中心までの距離を入力してください。:'))
                    area_pre = ((cal_n_1*cal_n_2)/2)
                    area = area_pre*5
                elif cal_mode_3_2 == '2':
                    print('五角形を5つの三角形に分け、上から時計周りに入力してください。')
                    cal_n_1 = float(input('1つ目の三角形の一辺の長さを入力してください。'))
                    cal_n_2 = float(input('1つ目の三角形の頂点までの距離を入力してください。'))
                    cal_n_3 = float(input('2つ目の三角形の一辺の長さを入力してください。'))
                    cal_n_4 = float(input('2つ目の三角形の頂点までの距離を入力してください。'))
                    cal_n_5 = float(input('3つ目の三角形の一辺の長さを入力してください。'))
                    cal_n_6 = float(input('3つ目の三角形の頂点までの距離を入力してください。'))
                    cal_n_7 = float(input('4つ目の三角形の一辺の長さを入力してください。'))
                    cal_n_8 = float(input('4つ目の三角形の頂点までの距離を入力してください。'))
                    cal_n_9 = float(input('5つ目の三角形の一辺の長さを入力してください。'))
                    cal_n_10 = float(input('5つ目の三角形の頂点までの距離を入力してください。'))
                    area_1 = ((cal_n_1*cal_n_2)/2)
                    area_2 = ((cal_n_3*cal_n_4)/2)
                    area_3 = ((cal_n_5*cal_n_6)/2)
                    area_4 = ((cal_n_7*cal_n_8)/2)
                    area_5 = ((cal_n_9*cal_n_10)/2)
                    area_all = area_1+area_2+area_3+area_4+area_5
                else:
                    error_end('0x0004')
                print('面積:',area)
                end()
            elif cal_mode_3 == '4':
                cal_mode_3_2 = input('面積の求め方を指定してください。半径と円周率:1 半径と円周:2')
                if cal_mode_3_2 == '1':
                    cal_n_1 = float(input('半径の長さを入力してください。'))
                    area = math.pi*(cal_n_1*cal_n_1)
                    print('面積:',area)
                    end()
                elif cal_mode_3_2 == '2':
                    cal_n_1 = float(input('半径の長さを入力してください。'))
                    cal_n_2 = float(input('円周の長さを入力してください。'))
                    area_pre = cal_n_2/math.pi/2
                    area = area_pre*area_pre*math.pi
                    print('面積:',area)
                    end()
                else:
                    error_end('0x0004')
        elif cal_mode_int == '2':
            error_end_2('0x1001')
        elif cal_mode_int == '3':
            error_end_2('0x1001')
        else:
            error_end_2('0x1002')
    elif cal_mode == '3':
        clear()
        print('数値変換モードで起動します。')
        error_end_2('0x1001')
    elif cal_mode == '4':
        clear()
        print('税計算モードで起動します。')
        cal = float(input('どの値を求めますか？ 1:税込み金額、2:税抜き金額、3:税率、4:税額 :'))
        if cal == 1:
            tax_free_price = float(input('原価(円):'))
            tax_percent = float(input('税率(%):'))
            tax_include_price = str((tax_free_price+(tax_free_price*(tax_percent*0.01))))
            print('¥'+tax_include_price)
        elif cal == 2:
            tax_include_price = float(input('税込みの値段(円):'))
            tax_percent = float(input('税率(%):'))
            tax_free_price = str(int(tax_include_price-(tax_include_price/(((tax_percent*0.01)+1)*100)*tax_percent)))
            print('¥'+tax_free_price)
        elif cal == 3:
            tax_include_price = float(input('税込みの値段:'))
            tax_free_price = float(input('原価:'))
            tax_percent = str(int(((tax_include_price/tax_free_price)-1)*100))
            print(tax_percent+'%')
        elif cal == 4:
            tax_include_price = float(input('税込みの値段:'))
            tax_free_price = float(input('原価:'))
            tax_price = str(int(tax_include_price-tax_free_price))
            print('¥'+tax_price)
        else:
            error_end('0x0004')
        end()
    elif cal_mode == '5':
        clear()
        print('直接計算モードで起動します。')
        cal = (input('計算を行いたい式を入力してください。'))
        cal_int = eval(cal)
        print('結果:',cal_int)
    elif cal_mode == '2022':
        error_end('Happy new year!')
    else:
        error_end('0x0004')
all_calc_code()