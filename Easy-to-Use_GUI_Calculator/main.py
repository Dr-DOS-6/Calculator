import tkinter as tk
from tkinter import messagebox, END
import os
import textwrap as tw
import multiprocessing as ml
from mgmtlist import mlist as mli
from mgmtlist import allow as al
import math
import re
#Thanks for Staycia930
class func:
    def kbd_input(self,keyin1,calledfrom):
        try:
            self.keyin2i = int(keyin1.keysym)
            self.keyin2 = str(self.keyin2)
            self.btnAdd(str(self.keyin2i))
        except:
            replacer = self.inputreplacer(keyin1.keysym)
            self.keyin2 = replacer
            if self.keyin2 == 'ignore':
                self.keyin2 = str()
            elif self.keyin2 == "Return":
                self.btnEnter()
                self.keyin2 == str()
            elif self.keyin2 == "BackSpace":
                self.btnBackspace()
            else:
                self.temp += self.keyin2
                self.textReplacer(self.temp)
    def inputreplacer(self,key_input: str,calledfrom) ->str:
        str(key_input)
        #print(key_input)
        if key_input == 'period':
            return '.'
        elif key_input == 'less':
            return '<'
        elif key_input == 'greater':
            return '>'
        elif key_input == 'slash':
            return '/'
        elif key_input == 'exclam':
            return 'math.factorial('
        elif key_input == 'root':
            return 'math.sqrt('
        elif key_input == 'percent':
            return '%'
        elif key_input == 'asciicircum':
            return '**'
        elif key_input == 'asterisk':
            return '*'
        elif key_input == 'parenleft':
            return '('
        elif key_input == 'parenright':
            return ')'
        elif key_input == 'minus':
            return '-'
        elif key_input == 'plus':
            return '+'
        elif key_input == 'equal':
            return '='
        elif key_input == 'Return':
            return 'Return'
        elif key_input == 'BackSpace':
            return 'BackSpace'
        elif key_input == 'Shift_R'or'Shift_L'or'Control_R'or'Control_L'or'Tab'or'NumLock':
            return 'ignore'
    def Fn(self,calledfrom):
        if self.btnFn.config('relief')[-1] == 'sunken':
            self.btnFn.config(relief="raised")
            self.btnClr.config(text= 'Clear')
            self.btnExt.config(text= '終了',font=('Meiryo',20))
        else:
            self.btnFn.config(relief="sunken")
            self.btnClr.config(text= 'Export')
            self.btnExt.config(text= 'モード変更',font=('Meiryo',10))
    def textReplacer(self,_input,calledfrom):
        self._input = re.sub('Num_Lock|Tab|Control_R|Control_L|Shift_R|Shift_L|ignore','',tw.fill(_input,40))
        self.textoutput.set(f'{_input}')
    def btnAdd(self,_input,calledfrom):
        try: 
            _intinput = int(_input)
        except ValueError:
            _input = self.inputreplacer(_input)
        if mli[2] == 1:
            self.console.config(anchor=tk.NW)
            mli[1] += 1
        elif mli[2] == 1:
            self.temp = str()
            self.textReplacer(self.temp)
            mli[2] = 0
        if  mli[3] == 1 and _input == '1':
            self.console.config(anchor=tk.NW)
            self.temp = str()
            self.textReplacer(self.temp)
            self.title = 'EUGC Ver.Dev 電卓モード'
            self.main_win.title(self.title)
            mli[3] = 0
            mli[4] = 1
            mli[8] = 1
            END
        if mli[3] == 1 and _input == '2':
            self.console.config(anchor=tk.NW)
            self.temp = str()
            self.textReplacer(self.temp)
            self.title = 'EUGC Ver.Dev 関数電卓モード'
            self.main_win.title(self.title)
            mli[3] = 0
            mli[4] = 1
            mli[8] = 2
            END
        if mli[4] == 1 and mli[8] == 2:
            self.subwin = ml.Process(target=sub_win,daemon=True)
            self.subwin.start()
            mli[4] = 0
            mli[8] = 0 
        elif mli[4] == 1:
            self.temp = str()
            self.textReplacer(self.temp)
            mli[4] = 0       
        else:
            try:
                self.console.config(anchor=tk.NW)
            except AttributeError:
                main_win.console.config(anchor=tk.NW)
            self.temp += _input
            self.textReplacer(self.temp)
    def btnEnter(self,calledfrom):
        self.console.config(anchor=tk.NW)
        if mli[1] == 0:
            self.textoutput.set('使用するモードを選んでください。\n電卓モード:1 関数電卓モード:2 ')
            self.console.config(anchor=tk.NW)
            mli[1] = 1
            mli[3] = 1
        elif mli[2] == 1:
            self.temp = str()
            self.textReplacer(self.temp)
            mli[2] = 0
        elif mli[4] == 1:
            self.btnAdd(1)
        else:
            try :
                self.temp = str(eval(self.temp))
                self.textReplacer(self.temp)
            except SyntaxError:
                if mli[1] == 0 or mli[6] == 1:
                    pass
                    END
                elif '入力された式は使用できません。もう一度式を入力してください。' or '電卓モードが選択されました。' or '関数電卓モードが選択されました。' in self.temp:
                    self.btnClear()
                else:
                    pass
                    self.temp += '入力された式は使用できません。もう一度式を入力してください。'
                    self.textReplacer(self.temp)
            except ZeroDivisionError:
                pass
            except OverflowError:
                self.temp = '数値が大きすぎます。一回表示を消去してください。'
                self.textReplacer(self.temp)
    def btnClear(self,calledfrom):
        self.console.config(anchor=tk.NW)
        if self.btnClr.cget('text') == 'Export':
            with open('result.txt', mode = 'a', encoding = 'UTF-8') as f:
                f.write(self.temp)
            self.path = os.path.abspath('result.txt')
            self.temp = f'An result was output at:\n{self.path}'
            self.textReplacer(self.temp)
            mli[2] = 1
        else:
            self.temp = str()
            self.textReplacer(self.temp)
    def btnBackspace(self,calledfrom):
        self.console.config(anchor=tk.NW)
        self.temp = self.temp[:-1]
        self.textReplacer(self.temp)
    def btnExit(self,calledfrom):
        if self.btnExt.cget('text') == 'モード変更':
            if self.title == 'EUGC Ver.Dev 電卓モード':
                self.title = 'EUGC Ver.Dev 関数電卓モード'
                self.main_win.title(self.title)
                self.subwin = ml.Process(target=sub_win,daemon=True)
                self.subwin.start()
            elif self.title == 'EUGC Ver.Dev 関数電卓モード':
                self.title = 'EUGC Ver.Dev 電卓モード'
                self.main_win.title(self.title)
                self.subwin.terminate()
        else:
            Messagebox = tk.messagebox.askquestion('EUGC Ver.Dev 終了確認','終了してもよろしいですか？', icon='warning')
            if Messagebox == 'yes':
                self.main_win.destroy()
            else:
                pass
class main_win(func):
    def __init__(self):
        self.main_win = tk.Tk()
        self.main_win.resizable(0,0)
        self.main_win.title('EUGC Ver.Dev')
        self.scrwid = self.main_win.winfo_screenwidth()
        self.scrhei = self.main_win.winfo_screenheight()
        self.winwid = 360
        self.winhei = 640
        self.consolehei = int(self.winwid/2)
        self.btnwid = int(self.winwid/4)
        self.btnhei = int((self.winhei-self.consolehei)/5)
        self.winsize = f'{self.winwid}x{self.winhei}+{int((self.scrwid-self.winwid)/2)}+{int((self.scrhei-self.winhei)/2)}'
        self.main_win.geometry(self.winsize)
        self.main_win.bind("<KeyPress>",self.kbd_input)
        mli[7] = 0
        self.textoutput = tk.StringVar()
        mli[1] = 0
        self.temp = str()
        mli[2] = 0
        self.btn0 =    tk.Button(self.main_win, text="0",font=('Meiryo',20),command=lambda: self.btnAdd('0','main_win'))
        self.btn1 =    tk.Button(self.main_win, text="1",font=('Meiryo',20),command=lambda: self.btnAdd('1','main_win'))
        self.btn2 =    tk.Button(self.main_win, text="2",font=('Meiryo',20),command=lambda: self.btnAdd('2','main_win'))
        self.btn3 =    tk.Button(self.main_win, text="3",font=('Meiryo',20),command=lambda: self.btnAdd('3','main_win'))
        self.btn4 =    tk.Button(self.main_win, text="4",font=('Meiryo',20),command=lambda: self.btnAdd('4','main_win'))
        self.btn5 =    tk.Button(self.main_win, text="5",font=('Meiryo',20),command=lambda: self.btnAdd('5','main_win'))
        self.btn6 =    tk.Button(self.main_win, text="6",font=('Meiryo',20),command=lambda: self.btnAdd('6','main_win'))
        self.btn7 =    tk.Button(self.main_win, text="7",font=('Meiryo',20),command=lambda: self.btnAdd('7','main_win'))
        self.btn8 =    tk.Button(self.main_win, text="8",font=('Meiryo',20),command=lambda: self.btnAdd('8','main_win'))
        self.btn9 =    tk.Button(self.main_win, text="9",font=('Meiryo',20),command=lambda: self.btnAdd('9','main_win'))
        self.btnPe =   tk.Button(self.main_win, text=".",font=('Meiryo',20),command=lambda: self.btnAdd('.','main_win'))
        self.btnPl =   tk.Button(self.main_win, text="+",font=('Meiryo',20),command=lambda: self.btnAdd('+','main_win'))
        self.btnMin =  tk.Button(self.main_win, text="-",font=('Meiryo',20),command=lambda: self.btnAdd('-','main_win'))
        self.btnAst =  tk.Button(self.main_win, text="x",font=('Meiryo',20),command=lambda: self.btnAdd('*','main_win'))
        self.btnSl =   tk.Button(self.main_win, text="÷",font=('Meiryo',20),command=lambda: self.btnAdd('/','main_win'))
        self.btnEtr =  tk.Button(self.main_win, text="Enter",font=('Meiryo',20),command=lambda: self.btnEnter('main_win'))
        self.btnFn =   tk.Button(self.main_win, text="切替",font=('Meiryo',20),command=lambda: self.Fn('main_win'))
        self.btnBksp = tk.Button(self.main_win,text="←",font=('Meiryo',20), command=lambda: self.btnBackspace('main_win'))
        self.btnClr =  tk.Button(self.main_win,text="消去/\n出力",font=('Meiryo',15),command=lambda: self.btnClear('main_win'))
        self.btnExt =  tk.Button(self.main_win,text='終了/\nモード切替',font=('Meiryo',12),command=lambda: self.btnExit('main_win'))
        self.console = tk.Label(self.main_win,relief="sunken",font=('Meiryo',10),height=self.consolehei,anchor=tk.NW,textvariable=self.textoutput)
        self.console.place(x=0,y=0,width=self.winwid,height=self.consolehei)
        self.btnFn.place(x=0,y=self.consolehei,width=self.btnwid,height=self.btnhei)
        self.btnSl.place(x=self.btnwid,y=self.consolehei,width=self.btnwid,height=self.btnhei)
        self.btnAst.place(x=self.btnwid*2,y=self.consolehei,width=self.btnwid,height=self.btnhei)
        self.btnBksp.place(x=self.btnwid*3,y=self.consolehei,width=self.btnwid,height=self.btnhei)
        self.btn7.place(x=0,y=self.consolehei+self.btnhei,width=self.btnwid,height=self.btnhei)
        self.btn8.place(x=self.btnwid,y=self.consolehei+self.btnhei,width=self.btnwid,height=self.btnhei)
        self.btn9.place(x=self.btnwid*2,y=self.consolehei+self.btnhei,width=self.btnwid,height=self.btnhei)
        self.btnEtr.place(x=self.btnwid*3,y=self.consolehei+self.btnhei,width=self.btnwid,height=self.btnhei)
        self.btn4.place(x=0,y=self.consolehei+self.btnhei*2,width=self.btnwid,height=self.btnhei)
        self.btn5.place(x=self.btnwid,y=self.consolehei+self.btnhei*2,width=self.btnwid,height=self.btnhei)
        self.btn6.place(x=self.btnwid*2,y=self.consolehei+self.btnhei*2,width=self.btnwid,height=self.btnhei)
        self.btnPl.place(x=self.btnwid*3,y=self.consolehei+self.btnhei*2,width=self.btnwid,height=self.btnhei)
        self.btn1.place(x=0,y=self.consolehei+self.btnhei*3,width=self.btnwid,height=self.btnhei)
        self.btn2.place(x=self.btnwid,y=self.consolehei+self.btnhei*3,width=self.btnwid,height=self.btnhei)
        self.btn3.place(x=self.btnwid*2,y=self.consolehei+self.btnhei*3,width=self.btnwid,height=self.btnhei)
        self.btnMin.place(x=self.btnwid*3,y=self.consolehei+self.btnhei*3,width=self.btnwid,height=self.btnhei)
        self.btnClr.place(x=0,y=self.consolehei+self.btnhei*4,width=self.btnwid,height=self.btnhei)
        self.btn0.place(x=self.btnwid,y=self.consolehei+self.btnhei*4,width=self.btnwid,height=self.btnhei)
        self.btnPe.place(x=self.btnwid*2,y=self.consolehei+self.btnhei*4,width=self.btnwid,height=self.btnhei)
        self.btnExt.place(x=self.btnwid*3,y=self.consolehei+self.btnhei*4,width=self.btnwid,height=self.btnhei)
        self.console.config(anchor=tk.N)
        self.textoutput.set('Calculator GUI Version 1.0\n Dr.GLaDOS🄬 2022\n\nEnterキーを押して下さい...\nPress Enter key to continue...')
        self.main_win.mainloop()
class sub_win(main_win,func):
    def __init__(self):
        mli[4] = 0
        self.sub_win = tk.Tk()
        self.sub_win.resizable(0,0)
        self.sub_win.title('EUGC Ver.Dev')
        self.scrwid = self.sub_win.winfo_screenwidth()
        self.scrhei = self.sub_win.winfo_screenheight()
        self.winwid = 200
        self.winhei = 640
        self.btnwid = int(self.winwid/2)
        self.btnhei = int(self.winhei/8)
        self.winlocwid = int((self.scrwid-360)/2)-self.winwid
        self.winlochei = int((self.scrhei-self.winhei)/2)
        self.winsize = f'{self.winwid}x{self.winhei}+{self.winlocwid}+{self.winlochei}'
        self.sub_win.geometry(self.winsize)
        self.btnfactrial = tk.Button(self.sub_win,text="階乗",font=('Meiryo',20),command=lambda: self.btnAdd('excram','sub_win'))
        self.btnsqroot = tk.Button(self.sub_win,text="平方根",font=('Meiryo',20),command=lambda: self.btnAdd('root','sub_win'))
        self.btnpower = tk.Button(self.sub_win,text="累乗",font=('Meiryo',20),command=lambda: self.btnAdd('**','sub_win'))
        self.btnfactrial.place(x=0,y=0,width=self.btnwid,height=self.btnhei)
        self.btnsqroot.place(x=self.btnwid,y=0,width=self.btnwid,height=self.btnhei)
        self.btnpower.place(x=0,y=self.btnhei,width=self.btnwid,height=self.btnhei)
        self.sub_win.mainloop()
if __name__ == '__main__':
    mainwin = ml.Process(target=main_win)
    mainwin.start()