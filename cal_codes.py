import cal_main
import time
import sys
import math
def end():
    time.sleep(1)
    print('Finish the calculation.')
    time.sleep(1)
    sys.exit()
#エラー時再起動コード
def error_end():
    error = 'A serious error has occurred. Restart the program.'
    print(error)
    time.sleep(1)
    cal_main.all_calc_code()
def Bret_formula():
    cal_n_1 = float(input('1つ目の辺の長さを入力してください。:'))
    cal_n_2 = float(input('2つ目の辺の長さを入力してください。:'))
    cal_n_3 = float(input('3つ目の辺の長さを入力してください。:'))
    cal_n_4 = float(input('4つ目の辺の長さを入力してください。:'))
    cal_n_5 = input('1つ目の角の大きさを指定してください。15°:0 30°:1 45°:2 60°:3 75°:4 90°:5:')
    cal_n_6 = input('2つ目の角の大きさを指定してください。15°:0 30°:1 45°:2 60°:3 75°:4 90°:5:')
    #cal_n_7の値と整数の一覧:30°:0 45°:1 60°:2 75°:3 90°:4 105°:5 120°:6 135°:7 150°:8 165°:9 180°:10
    #90°を超える場合、角度をθとした場合、(sin or cos)90° + (sin or cos)θ-90°
    if cal_n_5 == '0' and cal_n_6 == '0':
        cal_n_7 = '0'
    elif {cal_n_5 == '0' and cal_n_6 == '1'} or {cal_n_5 == '1' and cal_n_6 == '0'}:
        cal_n_7 = '1'
    elif {cal_n_5 == '0' and cal_n_6 == '2'} or {cal_n_5 == '1' and cal_n_6 == '1'} or {cal_n_5 == '2' and cal_n_6 == '0'}:
        cal_n_7 = '2'
    elif {cal_n_5 == '0' and cal_n_6 == '3'} or {cal_n_5 == '1' and cal_n_6 == '2'} or {cal_n_5 == '2' and cal_n_6 == '1'} or {cal_n_5 == '3' and cal_n_6 == '0'}:
        cal_n_7 = '3'
    elif {cal_n_5 == '0' and cal_n_6 == '4'} or {cal_n_5 == '1' and cal_n_6 == '3'} or {cal_n_5 == '2' and cal_n_6 == '2'} or {cal_n_5 == '3' and cal_n_6 == '1'} or {cal_n_5 == '4' and cal_n_6 == '0'}:
        cal_n_7 = '4'
    elif {cal_n_5 == '0' and cal_n_6 == '5'} or {cal_n_5 == '1' and cal_n_6 == '4'} or {cal_n_5 == '2' and cal_n_6 == '3'} or {cal_n_5 == '3' and cal_n_6 == '2'} or {cal_n_5 == '4' and cal_n_6 == '1'} or {cal_n_5 == '5' and cal_n_6 == '0'}:
        cal_n_7 = '5'
    elif {cal_n_5 == '1' and cal_n_6 == '5'} or {cal_n_5 == '2' and cal_n_6 == '4'} or {cal_n_5 == '3' and cal_n_6 == '3'} or {cal_n_5 == '4' and cal_n_6 == '2'} or {cal_n_5 == '5' and cal_n_6 == '1'}:
        cal_n_7 = '6'
    elif {cal_n_5 == '2' and cal_n_6 == '5'} or {cal_n_5 == '3' and cal_n_6 == '4'} or {cal_n_5 == '4' and cal_n_6 == '3'} or {cal_n_5 == '5' and cal_n_6 == '2'}:
        cal_n_7 = '7'
    elif {cal_n_5 == '3' and cal_n_6 == '5'} or {cal_n_5 == '4' and cal_n_6 == '4'} or {cal_n_5 == '5' and cal_n_6 == '3'}:
        cal_n_7 = '8'
    elif {cal_n_5 == '4' and cal_n_6 == '5'} or {cal_n_5 == '5' and cal_n_6 == '4'}:
        cal_n_7 = '9'
    elif cal_n_5 == '5' and cal_n_6 == '5':
        cal_n_7 = '10'
    if cal_n_7 == '0' or cal_n_7 == '8':
        cal_n_7 = 1/2
    elif cal_n_7 == '1' or cal_n_7 == '7':
        cal_n_7 = 0
    elif cal_n_7 == '2' or cal_n_7 == '6':
        cal_n_7 = -1/2
    elif cal_n_7 == '3' or cal_n_7 == '5':
        cal_n_7 = (-1*(math.sqrt(3)/2))
    elif cal_n_7 == '4':
        cal_n_7 = -1
    elif cal_n_7 == '9':
        cal_n_7 = (math.sqrt(3)/2)
    elif cal_n_7 == '10':
        cal_n_7 = 1
    else:
        error_end()
    s = ((cal_n_1 + cal_n_2 + cal_n_3 + cal_n_4)/2)
    area_all = (math.sqrt((s-cal_n_1)*(s-cal_n_2)*(s-cal_n_3)*(s-cal_n_4)-cal_n_1*cal_n_2*cal_n_3*cal_n_4*((1+cal_n_7)/2)))
    print('面積:',area_all)
    end()