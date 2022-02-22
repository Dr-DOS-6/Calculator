import os
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
def output_6(input,answer):
    #数値変換モード用
    with open('result.txt',mode='a',encoding='UTF-8') as f:
        datalist = ['\n','使用モード: 数値変換モード','\n','入力:',input,'\n','結果:',answer,'\n']
        f.writelines(datalist)
        f.close()
    print('An result was output:',os.path.abspath('result.txt'))