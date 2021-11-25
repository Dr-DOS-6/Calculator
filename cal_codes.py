import cal_main
import time
import sys
import math

def cal_mode_3_2_1_1():
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
        cal_main.error_end()
    print('面積:',area_all)
    cal_main.end()

def cal_mode_3_2_1_2():
    cal_n_1 = float(input('1つ目の対角線の長さを入力してください。:'))
    cal_n_2 = float(input('2つ目の対角線の長さを入力してください。:'))
    cal_n_4 = input('θの大きさを選んでください。15°:0 30°:1 45°:2 60°:3 75°:4 90°:5 :')
    if cal_n_4 == '0':
        area = float(0.5*cal_n_1*cal_n_2*(((math.sqrt(6))-(math.sqrt(2)))/4))
    elif cal_n_4 == '1':
        area = float(0.5*cal_n_1*cal_n_2*0.5)
    elif cal_n_4 == '2':
        area = float(0.5*cal_n_1*cal_n_2*(math.sqrt(2)/2))
    elif cal_n_4 == '3':
        area = float(0.5*cal_n_1*cal_n_2*(math.sqrt(3)/2))
    elif cal_n_4 == '4':
        area = float(0.5*cal_n_1*cal_n_2*(((math.sqrt(2))+(math.sqrt(6)))/4))
    elif cal_n_4 == '5':
        area = float(0.5*cal_n_1*cal_n_2)
    else:
        cal_main.error_end()
    print('面積:',area)
    cal_main.end()

def cal_mode_3_2_1_3():
    cal_n_1 = float(input('1つ目の辺の長さを入力してください。:'))
    cal_n_2 = float(input('2つ目の辺の長さを入力してください。:'))
    cal_n_3 = float(input('3つ目の辺の長さを入力してください。:'))
    cal_n_4 = float(input('4つ目の辺の長さを入力してください。:'))
    cal_n_5 = float(input('1つ目の角の大きさを指定してください。15°:0 30°:1 45°:2 60°:3 75°:4 90°:5:'))
    cal_n_6 = float(input('2つ目の角の大きさを指定してください。15°:0 30°:1 45°:2 60°:3 75°:4 90°:5:'))
    #cal_n_7の値と整数の一覧:30°:0 45°:1 60°:2 75°:3 90°:4 105°:5 120°:6 135°:7 150°:8 165°:9 180°:10
    #90°を超える場合、角度をθとした場合、(sin or cos)90° + (sin or cos)θ-90°
    cal_n_7 = cal_n_5 + cal_n_6 
    str(cal_n_7)
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
        cal_main.error_end()
    s = ((cal_n_1 + cal_n_2 + cal_n_3 + cal_n_4)/2)
    area_all = (math.sqrt((s-cal_n_1)*(s-cal_n_2)*(s-cal_n_3)*(s-cal_n_4)-cal_n_1*cal_n_2*cal_n_3*cal_n_4*((1+cal_n_7)/2)))
    print('面積:',area_all)
    cal_main.end()