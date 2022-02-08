from asyncio.windows_events import NULL
import time
import sys
import math
import os
import datetime
import argparse
import platform as pf
import lists as li
parser = argparse.ArgumentParser()
parser.add_argument('debug',nargs="?")
args = parser.parse_args( )
argv = args.debug
if argv == None:
    argv = 'Normal'
pf_s = pf.system()
ver = pf.python_version()
date = datetime.datetime.today()
date_1 = date.strftime("%Y/%m/%d %H:%M:%S")
error = None
error_cnt = [0,0]
sysin = pf.system()
relin = pf.release()
verin = pf.version()
macin = pf.machine()
proin = pf.processor()
def sys_info():
    print ('System information for this computer:')
    print ('system          :', pf.system())
    print ('release         :', pf.release())
    print ('system_version  :', pf.version())
    print ('machine         :', pf.machine())
    print ('processor       :', pf.processor())
    print ('python_version  :',ver)
    print ('Software_version:',soft_ver)
    print ('Mode            : ',argv)
    with open('error.log', mode='a', encoding='UTF-8') as f:
        datalist = ['\n','System          : ',pf.system(),'\n','Release         : ',pf.release(),'\n','System_version  : ',pf.version(),'\n','Machine         : ',pf.machine(),'\n','Processor       : ',pf.processor(),'\n','Python_version  : ',ver,'\n','Generated_Date  : ',date_1,'\n','Software_version: ',soft_ver,'\n','Mode            : ',argv,'_mode'+'\n']
        f.writelines(datalist)
        f.close()
        print('An error log was output:',os.path.abspath('error.log'))
def output_1(input,formula,answer):
    #代数計算モード用
    with open('result.txt', mode = 'a', encoding = 'UTF-8') as f:
        datalist = ['\n','使用モード: 代数計算モード','\n','入力:',input,'\n',formula,answer,'\n','答え:',answer,'\n']
        f.writelines(datalist)
        f.close()
    print('An result was output:',os.path.abspath('result.txt'))
def output_2(input,formula,answer,unit):
    #幾何計算モード{面積/表面積}用
    with open('result.txt', mode = 'a', encoding = 'UTF-8') as f:
        datalist = ['\n','使用モード: 幾何計算モード/面積','\n','入力:',input,'\n',formula,answer,'\n','解:',answer,unit,'\n']
        f.writelines(datalist)
        f.close()
    print('An result was output:',os.path.abspath('result.txt'))
def output_3(input,formula,answer,unit):
    #幾何計算モード{体積}用
    with open('result.txt', mode = 'a', encoding = 'UTF-8') as f:
        datalist = ['\n','使用モード: 幾何計算モード/体積','\n','入力:',input,'\n',formula,answer,'\n','解:',answer,unit,'\n']
        f.writelines(datalist)
        f.close()
    print('An result was output:',os.path.abspath('result.txt'))
def output_4(input,formula,answer,unit,sel):
    #税計算モード用
    with open('result.txt', mode = 'a', encoding = 'UTF-8') as f:
        if sel == 0:
            datalist = ['\n','使用モード: 税計算モード','\n','入力:',input,'\n','式:',formula,'\n','答え:',unit,answer,'\n']
        elif sel == 1:
            datalist = ['\n','使用モード: 税計算モード','\n','入力:',input,'\n','式:',formula,'\n','答え:',answer,unit,'\n']
        f.writelines(datalist)
        f.close()
    print('An result was output:',os.path.abspath('result.txt'))
def output_5(input,answer):
    #直接計算モード用
    with open('result.txt', mode = 'a', encoding = 'UTF-8') as f:
        datalist = ['\n','使用モード: 直接計算モード','\n','入力:',input,'\n','答え:',answer,'\n']
        f.writelines(datalist)
        f.close()
    print('An result was output:',os.path.abspath('result.txt'))
def clear():
    if pf_s == 'Windows':
        os.system('cls')
    elif pf_s == 'Linux' or 'Darwin':
        os.system('clear')
    else:
        error_end_3()
def end():
    print('Finish the calculation.')
    sys.exit()
#エラー時再起動コード
def error_end(error_code,error):
    print('A serious error has occurred. Restarting the program.')
    print('Error code:',error_code)
    error_cnt[0] += 1
    if error_cnt[0] > 5:
        print('Multiple serious errors have occurred. Kill the program.')
        print('Error code: 0x000F')
        sys_info()
        os.system('PAUSE')
        sys.exit()
    if error == 'error':
        error_cnt[1] += 1
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
    sys_info()
    sys.exit()
error = 'A serious error has occurred. Restarting the program.'
def startup():
    print('Calculator')
    global soft_ver
    soft_ver = ('1.4.7.0_CUI_Dev_20220208')
    str(soft_ver)
    if argv == 'debug':
        soft_ver = ('1.4.7.0_CUI_Dev_20220208'+' '+'debug_mode')
    #Hallo 2022, Happy new year!!
    ver = 'Version'+' '+soft_ver
    #体積計算モード、表面積計算モードをモード2に統合
    #数値変換モードを復帰
    #モード1，2の名称変更
    #マルチプラットフォームへの対応
    #細部の修正
    #直接計算モード搭載
    #エラーログ出力機能の改修
    #代数計算モードに結果出力機能実装
    #選択コードの修正
    #デバッグ機能実装
    #任意コード実行防止機能改良
    #数値変換モード実装
    #可読性の向上
    #time.sleep()の全削除
    #税計算モード完成
    builder = 'Dr.DOS'
    year = '2021'
    built = builder+'/'+year
    Created_by_1 = 'Python 3.10.1'
    Created_by_2 = 'Visual Studio Code 1.62.3'
    Created_by = ('Created by'+' '+Created_by_1+' '+'and'+' '+Created_by_2)
    print(ver)
    print(built)
    print(Created_by)
    if pf_s == 'Windows' or 'Linux' or 'Darwin':
        if argv == 'debug':
            sysinfo_tst = input('Enter the name of the OS you want to test. :')
            if not sysinfo_tst == 'Windows' or 'Linux' or 'Darwin':
                print("I'm sorry. This calculator is available for Windows, Linux, Chrome OS, and MacOS. Please make sure that the OS you are using is supported. There is a possibility that it will not work properly.")
                error_end_3()
        return
    else:
        print("I'm sorry. This calculator is available for Windows, Linux, Chrome OS, and MacOS. Please make sure that the OS you are using is supported. There is a possibility that it will not work properly.")
        error_end_3()
    #if not pf_s == 'Linux':
    #    print("I'm sorry. This calculator is available for Windows, Linux, Chrome OS, and MacOS. Please make sure that the OS you are using is supported. There is a possibility that it will not work properly.")
startup()
#error_end_3()
# 代入コード1
def all_calc_code():
    if error_cnt[1] > 0:
        cal_mode = (input('使用するモードを選択してください。代数計算モードは1、幾何計算モードは2、数値変換モードは3、税計算モードは4です。現在、直接計算モードは利用できません。終了する場合は6を入力してください。'))
    else:    
        cal_mode = (input('使用するモードを選択してください。代数計算モードは1、幾何計算モードは2、数値変換モードは3、税計算モードは4、直接計算モードは5です。終了する場合は6を入力してください。'))
    if cal_mode == '1':
        clear()
        print('代数計算モードで起動します。')
        n = float(input('nに代入する数字を入力してください。'))
        def rep(n):
            error = 'A serious error has occurred. Restarting the program.'
            x = float(input('xに代入する数字を入力してください。'))
            print('nに代入された数字= ', n)
            print('xに代入された数字= ', x)
            input_pre_1 = str(n)
            input_pre_2 = str(x)
            input_ = str(' '+'n ='+' '+input_pre_1+' '+'x ='+' '+input_pre_2)
            input_str =str(input_)
            # 演算子の指定
            cal_mode_2 = (input('どの計算がしたいですか?加算は1、乗算は2、減算は3、除算は4、除算の商は5、除算の剰余は6、べき乗は7、平方根は8です。:'))
            # 計算
            if cal_mode_2 == '1':
                n_x_0 = n + x
                print('n + x =', n_x_0)
                n_x_8 = n_x_0
                formula = 'n + x = '
            elif cal_mode_2 == '2':
                n_x_1 = n * x
                print('n * x =', n_x_1)
                n_x_8 = n_x_1
                formula = 'n * x = '
            elif cal_mode_2 == '3':
                n_x_2 = n - x
                print('n - x =', n_x_2)
                n_x_8 = n_x_2
                formula = 'n - x = '
            elif cal_mode_2 == '4':
                if x == 0:
                    error_end('0x0001',None)
                n_x_3 = n / x
                print('n ÷ x =', n_x_3)
                n_x_8 = n_x_3
                formula = 'n ÷ x = '
            elif cal_mode_2 == '5':
                n_x_4 = n // x
                print('(余りがある場合、商のみ) n ÷ x =',n_x_4)
                n_x_8 = n_x_4
                formula = '(余りがある場合、商のみ) n ÷ x = '
            elif cal_mode_2 == '6':
                n_x_5 = n % x
                print('(余りがある場合、余りのみ) n ÷ x =',n_x_5)
                n_x_8 = n_x_5
                formula = '(余りがある場合、余りのみ) n ÷ x = '
            elif cal_mode_2 == '7':
                n_x_6 = n ** x
                print('n^x =',n_x_6)
                n_x_8 = n_x_6
                formula = 'n ^ x = '
            elif cal_mode_2 == '8':
                cal_mode_2_1 = (input('平方根を求めたい値はどちらですか?n/x or 1/2:'))
                if cal_mode_2_1 == '1' or 'n':
                    n_x_7 = math.sqrt(n)
                    print('√n =',n_x_7,'√',n)
                    n_x_8 = n_x_7
                    formula = '√n = '
                elif cal_mode_2_1 == '2' or 'x':
                    n_x_7 = math.sqrt(x)
                    print('√x =',n_x_7,'√',x)
                    n_x_8 = n_x_7
                    formula = '√x = '
                else:
                    error_end('0x0002',None)
            else:
                n_x_8 = n
                print(error)
                rep4 = (input('嘘です。計算をやり直しますか? y/n or 1/0:'))
                if rep4 == 'y' or '1':
                    rep4_2 = (input('nに代入した数を残しますか? y/n or 1/0:'))
                    if rep4_2 == 'y' or '1':
                        print('nの数字を引き継ぎます。')
                        print('引き継いだ数字:', n_x_8)
                        rep(n)
                    elif rep4_2 == 'n' or '0':
                        n = float(input('nに代入する数字を入力してください。:'))
                    else:
                        error_end('0x0003',None)
                    rep(n)
                elif rep4 == 'n' or '0':
                    end()
                else:
                    error_end('0x0001',None)
            answer = str(n_x_8)
            output_1(input_str,formula,answer)
            # 再計算するかの確認
            rep2 = (input('もう一回計算したいですか? y/n or 1/0:'))
            if rep2 == 'y' or '1':
                # 計算結果の引継ぎの確認
                rep3 = (input('計算結果を引継ぎますか? y/n or 1/0:'))
                if rep3 == 'y' or '1':
                    clear()
                    n = n_x_8
                    print('nに結果を引き継ぎます。引き継いだ結果:', n_x_8)
                    rep(n)
                elif rep3 == 'n' or '0':
                    # 再代入
                    n = float(input('nに代入する数字を入力してください。:'))
                    rep(n)
                else:
                    error_end('0x0003',None)
            elif rep2 == 'n' or '0':
                end()
            else:
                error_end('0x0004',None)
        rep(n)
    elif cal_mode == '2':
        clear()
        print('幾何計算モードで起動します。')
        cal_mode_int = (input('使用したいモードを選択してください。1:面積計算モード 2:体積計算モード 3:表面積計算モード :'))
        if cal_mode_int == '1':
            unit = input('使用する単位を入力して下さい。:')
            cal_mode_3 = (input('面積を計算したい図形を入力してください。1:三角形、2:四角形、3:五角形、4:円 :'))
            if cal_mode_3 == '1':
                cal_mode_3_1 = (input('どちらの計算方法を利用しますか?3辺の長さ:1/y 底辺の長さと高さ:0/n :'))
                if cal_mode_3_1 == '1' or 'y':
                    cal_mode_3_1_1 =(input('面積を計算したい三角形の種類を選択してください。正三角形:1/y それ以外:0/n:'))
                    if cal_mode_3_1_1 == '1' or 'y':
                        cal_mode_3_1_1_val = float(input('1辺の長さを入力してください。:'))
                        cal_n_1 = float(cal_mode_3_1_1_val)
                        area = cal_n_1 * cal_n_1 /4
                        area_2 = ((cal_n_1 * cal_n_1)*(math.sqrt(3)))/4
                        area = (str(area)+'√3')
                        input_1 = str(cal_mode_3_1_1_val)
                        formula_1 = '1辺の長さ^2*√3÷4'
                        answer_1 = str(area),'/',str(area_2)
                        print('面積:','1辺の長さ*3',area,'/',area_2,unit)
                        end()
                    elif cal_mode_3_1_1 =='0' or 'n':
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
                        error_end('0x0004',None)
                elif cal_mode_3_1 == '0' or 'n':
                    cal_mode_3_1_2_val_1 = float(input('底辺の長さを入力してください。:'))
                    cal_mode_3_1_2_val_2 = float(input('高さを入力してください。:'))
                    cal_n_1_1 = cal_mode_3_1_2_val_1
                    cal_n_1_2 = cal_mode_3_1_2_val_2
                    cal_n_2 = float((cal_n_1_1 * cal_n_1_2)/2)
                    area = str(cal_n_2)
                    print('面積:',area)
                    end()
                else:
                    error_end('0x0004',None)
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
                            area = area_all
                        elif cal_n_5 == '1':
                            cal_n_5_1 = float(input('対角線の長さを入力してください。:'))
                            cal_n_6 = float((cal_n_4 + cal_n_1 + cal_n_5_1)/float(2))
                            area_1 = float(math.sqrt(cal_n_6*(cal_n_6 - cal_n_4)*(cal_n_6 - cal_n_1)*(cal_n_6 - cal_n_5_1)))
                            cal_n_7 = float((cal_n_2 + cal_n_3 + cal_n_5_1)/float(2))
                            area_2 = float(math.sqrt(cal_n_7*(cal_n_7 - cal_n_2)*(cal_n_7 - cal_n_3)*(cal_n_7 - cal_n_5_1)))
                            area_all = str(area_1 + area_2)
                            area = area_all
                        else:
                            error_end('0x0004',None)
                        print('面積:',area)
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
                            error_end('0x0004',None)
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
                            error_end('0x0004',None)
                        s = ((cal_n_1+cal_n_2+cal_n_3+cal_n_4)/2)
                        area_all = (math.sqrt((s-cal_n_1)*(s-cal_n_2)*(s-cal_n_3)*(s-cal_n_4)-cal_n_1*cal_n_2*cal_n_3*cal_n_4*((1+cal_n_7)/2)))
                        area = area_all
                        print('面積:',area)
                        end()
                    else:
                        error_end('0x0004',None)
            elif cal_mode_3 == '3':
                cal_mode_3_2 = input('面積を求めたい五角形の種類を指定してください。正五角形:1 五角形:2')
                if cal_mode_3_2 == '1':
                    cal_n_1 = float(input('一辺の長さを入力してください。:'))
                    cal_n_2 = float(input('中心までの距離を入力してください。:'))
                    area_pre = ((cal_n_1*cal_n_2)/2)
                    area = area_pre*5
                elif cal_mode_3_2 == '2':
                    print('五角形を5つの三角形に分け、上から時計周りに入力してください。「底辺」は、五角形にした時に一番外側に来る辺のことを言います。')
                    cal_n_1 = float(input('1つ目の三角形の底辺の長さを入力してください。'))
                    cal_n_2 = float(input('1つ目の三角形の頂点までの距離を入力してください。'))
                    cal_n_3 = float(input('2つ目の三角形の底辺の長さを入力してください。'))
                    cal_n_4 = float(input('2つ目の三角形の頂点までの距離を入力してください。'))
                    cal_n_5 = float(input('3つ目の三角形の底辺の長さを入力してください。'))
                    cal_n_6 = float(input('3つ目の三角形の頂点までの距離を入力してください。'))
                    cal_n_7 = float(input('4つ目の三角形の底辺の長さを入力してください。'))
                    cal_n_8 = float(input('4つ目の三角形の頂点までの距離を入力してください。'))
                    cal_n_9 = float(input('5つ目の三角形の底辺の長さを入力してください。'))
                    cal_n_10 = float(input('5つ目の三角形の頂点までの距離を入力してください。'))
                    area_1 = ((cal_n_1*cal_n_2)/2)
                    area_2 = ((cal_n_3*cal_n_4)/2)
                    area_3 = ((cal_n_5*cal_n_6)/2)
                    area_4 = ((cal_n_7*cal_n_8)/2)
                    area_5 = ((cal_n_9*cal_n_10)/2)
                    area_all = area_1+area_2+area_3+area_4+area_5
                    area = area_all
                else:
                    error_end('0x0004',None)
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
                    error_end('0x0004',None)
        elif cal_mode_int == '2':
            error_end_2('0x1001')
        elif cal_mode_int == '3':
            error_end_2('0x1001')
        else:
            error_end_2('0x1002')
    elif cal_mode == '3':
        clear()
        print('数値変換モードで起動します。')
        sel = int(input('使用するモードを選択してください。 角度→三角比変換モード:0 三角比→角度変換モード:1 '))
        if sel == 0:
            tri = int(input('角度から変換する先を選択してください。sin:0 cos:1 tan:2 '))
            if tri == 0:
                tri = li.sintheta
                ans_2 = 'sin'
            elif tri == 1:
                tri = li.costheta
                ans_2 = 'cos'
            elif  tri == 2:
                tri = li.tantheta
                ans_2 = 'tan'
            else:
                error_end('0x0001',None)
            deg_sel_1 = int(input('角度を入力してください。'))
            deg_sel_2 = li.deg.index(deg_sel_1)
            if not 0 <= deg_sel_2 < len(li.deg):
                error_end('0x0001',None)
            ans = tri[deg_sel_2]
            ans_3 = str(deg_sel_1)
        elif sel == 1:
            print('現在開発中につき、利用できません。')
            error_end_2('0x1001')
        print(ans_2+ans_3+'°','=',ans)
        end()
    elif cal_mode == '4':
        clear()
        print('税計算モードで起動します。')
        cal = float(input('どの値を求めますか? 1:税込み金額、2:税抜き金額、3:税率、4:税額 :'))
        if cal == 1:
            tax_free_price = float(input('税抜き価格:'))
            unit = str(input('単位を入力してください。:'))
            tax_percent = float(input('税率(%):'))
            tax_free_price_str = str(tax_free_price)
            tax_percent_str = str(tax_percent)
            input_ = tax_free_price_str+','+tax_percent_str 
            tax_include_price = str((tax_free_price+(tax_free_price*(tax_percent*0.01))))
            formula = '税抜き価格+(税抜き価格*税率(%))'
            print(unit+tax_include_price)
            output_4(input_,formula,tax_include_price,unit,0)
        elif cal == 2:
            tax_include_price = float(input('税込み価格:'))
            unit = str(input('単位を入力してください。:'))
            tax_percent = float(input('税率(%):'))
            tax_include_price_str = str(tax_include_price)
            tax_percent_str = str(tax_percent)
            input_ = tax_include_price_str+','+tax_percent_str
            tax_free_price = str(int(tax_include_price-(tax_include_price/(((tax_percent*0.01)+1)*100)*tax_percent)))
            formula = '税込み価格-(税込み価格÷(((税率+1)*100)*税率))'
            print(unit+tax_free_price)
            output_4(input_,formula,tax_free_price,unit,0)
        elif cal == 3:
            tax_include_price = float(input('税込み価格:'))
            tax_free_price = float(input('税抜き価格:'))
            tax_include_price_str = str(tax_include_price)
            tax_free_price_str = str(tax_free_price)
            input_ = tax_include_price_str+','+tax_free_price_str 
            tax_percent = str(int(((tax_include_price/tax_free_price)-1)*100))
            formula = '((税込み価格÷税抜き価格)-1)*100'
            print(tax_percent+'%')
            output_4(input_,formula,tax_percent,'%',1)
        elif cal == 4:
            tax_include_price = float(input('税込みの価格:'))
            tax_free_price = float(input('税抜き価格:'))
            unit = str(input('単位を入力してください。:'))
            tax_include_price_str = str(tax_include_price)
            tax_free_price_str = str(tax_free_price)
            input_ = tax_include_price_str+','+tax_free_price_str 
            tax_price = str(int(tax_include_price-tax_free_price))
            formula = '税込み価格-税抜き価格'
            print(unit+tax_price)
            output_4(input_,formula,tax_price,unit,0)
        else:
            error_end('0x0004',None)
        end()
    elif cal_mode == '5' and error_cnt[1] == 1:
        print('直接計算モードは現在利用できません。計算機を再起動してください。')
        error_end_2('0x1001')
    elif cal_mode == '5':
        clear()
        cal = None
        cal_int = None
        cal_error = 0
        print('直接計算モードで起動します。')
        cal = (input('計算を行いたい式を入力してください。'))
        cal_str = str(cal)
        for i in range (0,25):
            if li.block_cap[i] in cal_str:
                cal_error += 1
        for i in range (0,25):
            if li.block_low[i] in cal_str:
                cal_error += 1
        for i in range (0,14):
            if li.block_sym[i] in cal_str:
                cal_error += 1
        if cal_error > 0:
            error_end('input_is_not_calculation_formula','error')
        cal_int = str(eval(cal))
        print('結果:',cal_int)
        output_5(cal_str,cal_int)
        end()
    elif cal_mode == '2022':
        error_end('Happy new year!',None)
    elif cal_mode == '6':
        end()
    else:
        error_end('0x0004',None)
all_calc_code()