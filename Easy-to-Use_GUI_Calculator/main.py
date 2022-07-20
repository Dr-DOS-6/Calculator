import tkinter as tk
from tkinter import messagebox, END,ttk
import os
import textwrap as tw
import math
import re
#Thanks for Staycia930
mli = [0,0,0,0,0,0,0,0,0,0]
class func:
    def screenresetter(self,mode):
        self.style = ttk.Style()
        self.style.configure("stdButton.TButton",font=('Meiryo',20))
        self.style.configure("stdButton2.TButton",font=('Meiryo',15))
        self.style.configure("stdButton3.TButton",font=('Meiryo',12))
        self.style.configure("stdButton4.TButton",font=('Meiryo',10))
        self.style.configure("stdLabel.TLabel",font=('Meiryo',12))
        if mode == 1:
            if mli[3] == 1:
                text1 = '消去/出力'
                text1font = 15
                text2 = '終了/\nモード切替'
                text2font = 12
            else:
                text1 = '消去'
                text1font = 15
                text2 = '終了'
                text2font = 15   
            self.main_win.geometry(f'{self.winwid+(self.btnwid*2)}x{self.winhei}+{int((self.scrwid-self.winwid-self.btnwid*2)/2)}+{int((self.scrhei-self.winhei)/2)}')
            self.console.destroy()
            self.btn0.destroy()
            self.btn1.destroy()
            self.btn2.destroy()
            self.btn3.destroy()
            self.btn4.destroy()
            self.btn5.destroy()
            self.btn6.destroy()
            self.btn7.destroy()
            self.btn8.destroy()
            self.btn9.destroy()
            self.btnPe.destroy()
            self.btnPl.destroy()
            self.btnMin.destroy()
            self.btnAst.destroy()
            self.btnSl.destroy()
            self.btnEtr.destroy()
            self.btnFn.destroy()
            self.btnBksp.destroy()
            self.btnClr.destroy()
            self.btnExt.destroy()
            self.btn0 =    ttk.Button(self.main_win, text="0",style="stdButton.TButton",command=lambda: self.btnAdd('0'))
            self.btn1 =    ttk.Button(self.main_win, text="1",style="stdButton.TButton",command=lambda: self.btnAdd('1'))
            self.btn2 =    ttk.Button(self.main_win, text="2",style="stdButton.TButton",command=lambda: self.btnAdd('2'))
            self.btn3 =    ttk.Button(self.main_win, text="3",style="stdButton.TButton",command=lambda: self.btnAdd('3'))
            self.btn4 =    ttk.Button(self.main_win, text="4",style="stdButton.TButton",command=lambda: self.btnAdd('4'))
            self.btn5 =    ttk.Button(self.main_win, text="5",style="stdButton.TButton",command=lambda: self.btnAdd('5'))
            self.btn6 =    ttk.Button(self.main_win, text="6",style="stdButton.TButton",command=lambda: self.btnAdd('6'))
            self.btn7 =    ttk.Button(self.main_win, text="7",style="stdButton.TButton",command=lambda: self.btnAdd('7'))
            self.btn8 =    ttk.Button(self.main_win, text="8",style="stdButton.TButton",command=lambda: self.btnAdd('8'))
            self.btn9 =    ttk.Button(self.main_win, text="9",style="stdButton.TButton",command=lambda: self.btnAdd('9'))
            self.btnPe =   ttk.Button(self.main_win, text=".",style="stdButton.TButton",command=lambda: self.btnAdd('.'))
            self.btnPl =   ttk.Button(self.main_win, text="+",style="stdButton.TButton",command=lambda: self.btnAdd('+'))
            self.btnMin =  ttk.Button(self.main_win, text="-",style="stdButton.TButton",command=lambda: self.btnAdd('-'))
            self.btnAst =  ttk.Button(self.main_win, text="x",style="stdButton.TButton",command=lambda: self.btnAdd('*'))
            self.btnSl =   ttk.Button(self.main_win, text="÷",style="stdButton.TButton",command=lambda: self.btnAdd('/'))
            self.btnEtr =  ttk.Button(self.main_win, text="Enter",style="stdButton.TButton",command=lambda: self.btnEnter())
            self.btnFn =   ttk.Button(self.main_win, text="切替",style="stdButton.TButton",command=lambda: self.Fn())
            self.btnBksp = ttk.Button(self.main_win,text="←",style="stdButton.TButton", command=lambda: self.btnBackspace())
            self.btnClr =  ttk.Button(self.main_win,text="消去",style="stdButton.TButton",command=lambda: self.btnClear())
            self.btnExt =  ttk.Button(self.main_win,text='終了',style="stdButton.TButton",command=lambda: self.btnExit())
            self.console = ttk.Label(self.main_win,relief="sunken",style="stdLabel.TLabel",anchor=tk.NW,textvariable=self.textoutput)
            self.btnFcrl = ttk.Button(self.main_win,text="階乗",style="stdButton.TButton",command=lambda: self.btnFactorial())
            self.btnSqrt = ttk.Button(self.main_win,text="平方根",style="stdButton2.TButton",command=lambda: self.btnSquareroot())
            self.btnCil = ttk.Button(self.main_win,text="繰り上げ",style="stdButton2.TButton",command=lambda: self.btnCeil())
            self.btnFlr = ttk.Button(self.main_win,text="繰り下げ",style="stdButton2.TButton",command=lambda: self.btnFloor())
            self.btnCma = ttk.Button(self.main_win,text=",",style="stdButton.TButton",command=lambda: self.btnAdd(','))
            self.btnPct = ttk.Button(self.main_win,text='割り算\nの余り',style="stdButton3.TButton",command=lambda: self.btnAdd('%'))
            self.btnBrckL = ttk.Button(self.main_win,text="(",style="stdButton.TButton",command=lambda: self.btnAdd('('))
            self.btnBrckR = ttk.Button(self.main_win,text=")",style="stdButton.TButton",command=lambda: self.btnAdd(')'))
            self.btnGcd = ttk.Button(self.main_win,text="最大\n公約数",style="stdButton3.TButton",command=lambda: self.btnGcdfunc())
            self.btnExp = ttk.Button(self.main_win,text='eのx乗',style="stdButton2.TButton",command=lambda: self.btnExpfunc())
            self.btnLog = ttk.Button(self.main_win,text='xを底とする\nyの対数',style="stdButton3.TButton",command=lambda: self.btnLogfunc())
            self.btnSinx = ttk.Button(self.main_win,text='sinx',style="stdButton.TButton",command=lambda: self.btnSinxfunc())
            self.btnCosx = ttk.Button(self.main_win,text='cosx',style="stdButton.TButton",command=lambda: self.btnCosxfunc())
            self.btnTanx = ttk.Button(self.main_win,text='tanx',style="stdButton.TButton",command=lambda: self.btnTanxfunc())
            self.console.place(x=self.btnwid*2,y=0,width=self.btnwid*4,height=self.btnhei*2)
            self.btnFn.place(x=self.btnwid*2,y=self.btnhei*2,width=self.btnwid,height=self.btnhei)
            self.btnSl.place(x=self.btnwid*3,y=self.btnhei*2,width=self.btnwid,height=self.btnhei)
            self.btnAst.place(x=self.btnwid*4,y=self.btnhei*2,width=self.btnwid,height=self.btnhei)
            self.btnBksp.place(x=self.btnwid*5,y=self.btnhei*2,width=self.btnwid,height=self.btnhei)
            self.btn7.place(x=self.btnwid*2,y=self.btnhei*2+self.btnhei,width=self.btnwid,height=self.btnhei)
            self.btn8.place(x=self.btnwid*3,y=self.btnhei*2+self.btnhei,width=self.btnwid,height=self.btnhei)
            self.btn9.place(x=self.btnwid*4,y=self.btnhei*2+self.btnhei,width=self.btnwid,height=self.btnhei)
            self.btnEtr.place(x=self.btnwid*5,y=self.btnhei*2+self.btnhei,width=self.btnwid,height=self.btnhei)
            self.btn4.place(x=self.btnwid*2,y=self.btnhei*2+self.btnhei*2,width=self.btnwid,height=self.btnhei)
            self.btn5.place(x=self.btnwid*3,y=self.btnhei*2+self.btnhei*2,width=self.btnwid,height=self.btnhei)
            self.btn6.place(x=self.btnwid*4,y=self.btnhei*2+self.btnhei*2,width=self.btnwid,height=self.btnhei)
            self.btnPl.place(x=self.btnwid*5,y=self.btnhei*2+self.btnhei*2,width=self.btnwid,height=self.btnhei)
            self.btn1.place(x=self.btnwid*2,y=self.btnhei*2+self.btnhei*3,width=self.btnwid,height=self.btnhei)
            self.btn2.place(x=self.btnwid*3,y=self.btnhei*2+self.btnhei*3,width=self.btnwid,height=self.btnhei)
            self.btn3.place(x=self.btnwid*4,y=self.btnhei*2+self.btnhei*3,width=self.btnwid,height=self.btnhei)
            self.btnMin.place(x=self.btnwid*5,y=self.btnhei*2+self.btnhei*3,width=self.btnwid,height=self.btnhei)
            self.btnClr.place(x=self.btnwid*2,y=self.btnhei*2+self.btnhei*4,width=self.btnwid,height=self.btnhei)
            self.btn0.place(x=self.btnwid*3,y=self.btnhei*2+self.btnhei*4,width=self.btnwid,height=self.btnhei)
            self.btnPe.place(x=self.btnwid*4,y=self.btnhei*2+self.btnhei*4,width=self.btnwid,height=self.btnhei)
            self.btnExt.place(x=self.btnwid*5,y=self.btnhei*2+self.btnhei*4,width=self.btnwid,height=self.btnhei)
            self.btnFcrl.place(x=0,y=0,width=self.btnwid,height=self.btnhei)
            self.btnSqrt.place(x=self.btnwid,y=0,width=self.btnwid,height=self.btnhei)
            self.btnPct.place(x=self.btnwid,y=self.btnhei*5,width=self.btnwid,height=self.btnhei)
            self.btnCma.place(x=0,y=self.btnhei*5,width=self.btnwid,height=self.btnhei)
            self.btnCil.place(x=0,y=self.btnhei,width=self.btnwid,height=self.btnhei)
            self.btnFlr.place(x=self.btnwid,y=self.btnhei,width=self.btnwid,height=self.btnhei)
            self.btnGcd.place(x=0,y=self.btnhei*2,width=self.btnwid,height=self.btnhei)
            self.btnExp.place(x=self.btnwid,y=self.btnhei*2,width=self.btnwid,height=self.btnhei)
            self.btnLog.place(x=0,y=self.btnhei*3,width=self.btnwid,height=self.btnhei)
            self.btnSinx.place(x=self.btnwid,y=self.btnhei*3,width=self.btnwid,height=self.btnhei)
            self.btnCosx.place(x=0,y=self.btnhei*4,width=self.btnwid,height=self.btnhei)
            self.btnTanx.place(x=self.btnwid,y=self.btnhei*4,width=self.btnwid,height=self.btnhei)
            self.btnBrckL.place(x=0,y=self.btnhei*6,width=self.btnwid,height=self.btnhei)
            self.btnBrckR.place(x=self.btnwid,y=self.btnhei*6,width=self.btnwid,height=self.btnhei)
            self.mode2 = 1
        elif mode == 2:
            self.main_win.geometry(f'{self.winwid}x{self.winhei}+{int((self.scrwid-self.winwid)/2)}+{int((self.scrhei-self.winhei)/2)}')
            if self.mode2 == 1:
                self.btnFcrl.destroy()
                self.btnSqrt.destroy()
                self.btnBrckL.destroy()
                self.btnBrckR.destroy()
                self.btnCma.destroy()
                self.btnPct.destroy()
                self.btnFlr.destroy()
                self.btnCil.destroy()
                self.btnGcd.destroy()
                self.btnExp.destroy()
                self.btnLog.destroy()
                self.btnSinx.destroy()
                self.btnCosx.destroy()
                self.btnTanx.destroy()
            self.console.destroy()
            self.btn0.destroy()
            self.btn1.destroy()
            self.btn2.destroy()
            self.btn3.destroy()
            self.btn4.destroy()
            self.btn5.destroy()
            self.btn6.destroy()
            self.btn7.destroy()
            self.btn8.destroy()
            self.btn9.destroy()
            self.btnPe.destroy()
            self.btnPl.destroy()
            self.btnMin.destroy()
            self.btnAst.destroy()
            self.btnSl.destroy()
            self.btnEtr.destroy()
            self.btnFn.destroy()
            self.btnBksp.destroy()
            self.btnClr.destroy()
            self.btnExt.destroy()
            self.btn0 =    ttk.Button(self.main_win, text="0",style="stdButton.TButton",command=lambda: self.btnAdd('0'))
            self.btn1 =    ttk.Button(self.main_win, text="1",style="stdButton.TButton",command=lambda: self.btnAdd('1'))
            self.btn2 =    ttk.Button(self.main_win, text="2",style="stdButton.TButton",command=lambda: self.btnAdd('2'))
            self.btn3 =    ttk.Button(self.main_win, text="3",style="stdButton.TButton",command=lambda: self.btnAdd('3'))
            self.btn4 =    ttk.Button(self.main_win, text="4",style="stdButton.TButton",command=lambda: self.btnAdd('4'))
            self.btn5 =    ttk.Button(self.main_win, text="5",style="stdButton.TButton",command=lambda: self.btnAdd('5'))
            self.btn6 =    ttk.Button(self.main_win, text="6",style="stdButton.TButton",command=lambda: self.btnAdd('6'))
            self.btn7 =    ttk.Button(self.main_win, text="7",style="stdButton.TButton",command=lambda: self.btnAdd('7'))
            self.btn8 =    ttk.Button(self.main_win, text="8",style="stdButton.TButton",command=lambda: self.btnAdd('8'))
            self.btn9 =    ttk.Button(self.main_win, text="9",style="stdButton.TButton",command=lambda: self.btnAdd('9'))
            self.btnPe =   ttk.Button(self.main_win, text=".",style="stdButton.TButton",command=lambda: self.btnAdd('.'))
            self.btnPl =   ttk.Button(self.main_win, text="+",style="stdButton.TButton",command=lambda: self.btnAdd('+'))
            self.btnMin =  ttk.Button(self.main_win, text="-",style="stdButton.TButton",command=lambda: self.btnAdd('-'))
            self.btnAst =  ttk.Button(self.main_win, text="x",style="stdButton.TButton",command=lambda: self.btnAdd('*'))
            self.btnSl =   ttk.Button(self.main_win, text="÷",style="stdButton.TButton",command=lambda: self.btnAdd('/'))
            self.btnEtr =  ttk.Button(self.main_win, text="Enter",style="stdButton.TButton",command=lambda: self.btnEnter())
            self.btnFn =   ttk.Button(self.main_win, text="切替",style="stdButton.TButton",command=lambda: self.Fn())
            self.btnBksp = ttk.Button(self.main_win,text="←",style="stdButton.TButton", command=lambda: self.btnBackspace())
            self.btnClr =  ttk.Button(self.main_win,text="消去",style="stdButton.TButton",command=lambda: self.btnClear())
            self.btnExt =  ttk.Button(self.main_win,text='終了',style="stdButton.TButton",command=lambda: self.btnExit())
            self.console = ttk.Label(self.main_win,relief="sunken",style="stdLabel.TLabel",anchor=tk.NW,textvariable=self.textoutput)
            self.console.place(x=0,y=0,width=self.btnwid*4,height=self.btnhei*2)
            self.btnFn.place(x=0,y=self.btnhei*2,width=self.btnwid,height=self.btnhei)
            self.btnSl.place(x=self.btnwid,y=self.btnhei*2,width=self.btnwid,height=self.btnhei)
            self.btnAst.place(x=self.btnwid*2,y=self.btnhei*2,width=self.btnwid,height=self.btnhei)
            self.btnBksp.place(x=self.btnwid*3,y=self.btnhei*2,width=self.btnwid,height=self.btnhei)
            self.btn7.place(x=0,y=self.btnhei*2+self.btnhei,width=self.btnwid,height=self.btnhei)
            self.btn8.place(x=self.btnwid,y=self.btnhei*2+self.btnhei,width=self.btnwid,height=self.btnhei)
            self.btn9.place(x=self.btnwid*2,y=self.btnhei*2+self.btnhei,width=self.btnwid,height=self.btnhei)
            self.btnEtr.place(x=self.btnwid*3,y=self.btnhei*2+self.btnhei,width=self.btnwid,height=self.btnhei)
            self.btn4.place(x=0,y=self.btnhei*2+self.btnhei*2,width=self.btnwid,height=self.btnhei)
            self.btn5.place(x=self.btnwid,y=self.btnhei*2+self.btnhei*2,width=self.btnwid,height=self.btnhei)
            self.btn6.place(x=self.btnwid*2,y=self.btnhei*2+self.btnhei*2,width=self.btnwid,height=self.btnhei)
            self.btnPl.place(x=self.btnwid*3,y=self.btnhei*2+self.btnhei*2,width=self.btnwid,height=self.btnhei)
            self.btn1.place(x=0,y=self.btnhei*2+self.btnhei*3,width=self.btnwid,height=self.btnhei)
            self.btn2.place(x=self.btnwid,y=self.btnhei*2+self.btnhei*3,width=self.btnwid,height=self.btnhei)
            self.btn3.place(x=self.btnwid*2,y=self.btnhei*2+self.btnhei*3,width=self.btnwid,height=self.btnhei)
            self.btnMin.place(x=self.btnwid*3,y=self.btnhei*2+self.btnhei*3,width=self.btnwid,height=self.btnhei)
            self.btnClr.place(x=0,y=self.btnhei*2+self.btnhei*4,width=self.btnwid,height=self.btnhei)
            self.btn0.place(x=self.btnwid,y=self.btnhei*2+self.btnhei*4,width=self.btnwid,height=self.btnhei)
            self.btnPe.place(x=self.btnwid*2,y=self.btnhei*2+self.btnhei*4,width=self.btnwid,height=self.btnhei)
            self.btnExt.place(x=self.btnwid*3,y=self.btnhei*2+self.btnhei*4,width=self.btnwid,height=self.btnhei)
    def kbd_input(self,keyin1):
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
                #print(self.temp)
                self.textReplacer(self.temp)
    def inputreplacer(self,key_input: str) ->str:
        str(key_input)
        #print(key_input)
        if key_input == 'period':
            return '.'
        elif key_input == 'comma':
            return ','
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
        elif key_input == '+':
            return '+'
        elif key_input == '-':
            return '-'
        elif key_input == '*':
            return '*'
        elif key_input == '<':
            return '<'
        elif key_input == '>':
            return '>'
        elif key_input == '/':
            return '/'
        elif key_input == '.':
            return '.'
        elif key_input == ',':
            return ','
        elif key_input == '(':
            return '('
        elif key_input == ')':
            return ')'
        else:
            return 'ignore'
    def Fn(self):
        if self.btnExt.cget('text') == 'モード変更':
            self.btnClr.config(text= 'Clear')
            self.btnExt.config(text= '終了',style="stdButton.TButton")
        else:
            self.btnClr.config(text= 'Export')
            self.btnExt.config(text= 'モード変更',style="stdButton2.TButton")
    def textReplacer(self,_input):
        self._input = re.sub('Num_Lock|Tab|Control_R|Control_L|Shift_R|Shift_L|ignore','',tw.fill(_input,40))
        self.textoutput.set(f'{_input}')
    def btnAdd(self,_input):
        #print(mli[2])
        #print(mli[3])
        #print(mli[4])
        #print(_input)
        #print('-----ここで切り取り-----')
        try: 
            _intinput = int(_input)
        except ValueError:
            #print(_input)
            if _input == '+'or'-'or'*'or'<'or'>'or'/'or'.'or','or'('or')':
                pass
            else:
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
            #mli[4] = 1
            mli[8] = 1
        elif mli[3] == 1 and _input == '2':
            self.console.config(anchor=tk.NW)
            self.temp = str()
            self.textReplacer(self.temp)
            self.title = 'EUGC Ver.Dev 関数電卓モード'
            self.main_win.title(self.title)
            self.screenresetter(1)
            mli[3] = 0
            #mli[4] = 1
            mli[8] = 2
        elif mli[4] == 1:
            self.temp = str()
            self.textReplacer(self.temp)
            mli[4] = 0       
        else:
            self.console.config(anchor=tk.NW)
            self.temp += _input
            self.textReplacer(self.temp)
    def btnSinxfunc(self):
        self.temp += 'math.sin((math.pi/180)*'
        self.textReplacer(self.temp)
    def btnCosxfunc(self):
        self.temp += 'math.cos((math.pi/180)*'
        self.textReplacer(self.temp)
    def btnTanxfunc(self): 
        self.temp += 'math.tan((math.pi/180)*'
        self.textReplacer(self.temp)
    def btnLogfunc(self):
        self.temp += "math.log("
        self.textReplacer(self.temp)
    def btnExpfunc(self):
        self.temp += "math.exp("
        self.textReplacer(self.temp)
    def btnGcdfunc(self):
        self.temp += "math.gcd("
        self.textReplacer(self.temp)
    def btnCeil(self):
        self.temp += "math.ceil("
        self.textReplacer(self.temp)
    def btnFloor(self):
        self.temp += "math.floor("
        self.textReplacer(self.temp)
    def btnSquareroot(self):
        self.temp += "math.sqrt("
        self.textReplacer(self.temp)
    def btnFactorial(self):
        self.temp += "math.factorial("
        self.textReplacer(self.temp)
    def btnEnter(self):
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
    def btnClear(self):
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
    def btnBackspace(self):
        self.console.config(anchor=tk.NW)
        if self.temp[-23:] == 'math.sin((math.pi/180)*':
            self.temp = self.temp[:len(self.temp)-23]
        elif self.temp[-23:] == 'math.cos((math.pi/180)*':
            self.temp = self.temp[:len(self.temp)-23]
        elif self.temp[-23:] == 'math.tan((math.pi/180)*':
            self.temp = self.temp[:len(self.temp)-23]
        elif self.temp[-15:] == 'math.factorial(':
            #print(self.temp[-15:]+'\nこれは階乗です')
            self.temp = self.temp[:len(self.temp)-15]
        elif self.temp[-11:] == 'math.floor(':
            #print(self.temp[-11:]+'\nこれは繰り下げです')
            self.temp = self.temp[:len(self.temp)-11]
        elif self.temp[-10:] == 'math.sqrt(':
            #print(self.temp[-10:]+'\nこれは平方根です')
            self.temp = self.temp[:len(self.temp)-10]
        elif self.temp[-10:] == 'math.ceil(':
            #print(self.temp[-10:]+'\nこれは平方根です')
            self.temp = self.temp[:len(self.temp)-10]
        elif self.temp[-9:] == 'math.gcd(':
            self.temp = self.temp[:len(self.temp)-9]
        elif self.temp[-9:] == 'math.exp(':
            self.temp = self.temp[:len(self.temp)-9]
        elif self.temp[-9:] == 'math.log(':
            self.temp = self.temp[:len(self.temp)-9]
        else:
            self.temp = self.temp[:len(self.temp)-1]
        #print(self.temp)
        self.textReplacer(self.temp)
    def btnExit(self):
        if self.btnExt.cget('text') == 'モード変更':
            if self.title == 'EUGC Ver.Dev 電卓モード':
                self.title = 'EUGC Ver.Dev 関数電卓モード'
                self.main_win.title(self.title)
                self.screenresetter(1)
            elif self.title == 'EUGC Ver.Dev 関数電卓モード':
                self.title = 'EUGC Ver.Dev 電卓モード'
                self.main_win.title(self.title)
                self.screenresetter(2)
        else:
            Messagebox = tk.messagebox.askquestion('EUGC Ver.Dev 終了確認','終了してもよろしいですか？', icon='warning')
            if Messagebox == 'yes':
                self.main_win.destroy()
            else:
                pass
class main_win(func):
    def __init__(self):
        self.main_win = tk.Tk()
        self.style = ttk.Style()
        self.style.configure("stdButton.TButton",font=('Meiryo',20))
        self.style.configure("stdButton2.TButton",font=('Meiryo',15))
        self.style.configure("stdButton3.TButton",font=('Meiryo',12))
        self.style.configure("stdButton4.TButton",font=('Meiryo',10))
        self.style.configure("stdLabel.TLabel",font=('Meiryo',12))
        self.main_win.resizable(0,0)
        self.main_win.title('EUGC Ver.Dev')
        self.scrwid = self.main_win.winfo_screenwidth()
        self.scrhei = self.main_win.winfo_screenheight()
        self.winwid = 360
        self.winhei = 630
        self.btnwid = int(self.winwid/4)
        self.btnhei = int(self.winhei/7)
        self.winsize = f'{self.winwid}x{self.winhei}+{int((self.scrwid-self.winwid)/2)}+{int((self.scrhei-self.winhei)/2)}'
        self.main_win.geometry(self.winsize)
        self.main_win.bind("<KeyPress>",self.kbd_input)
        mli[7] = 0
        self.textoutput = tk.StringVar()
        mli[1] = 0
        self.temp = str()
        mli[2] = 0
        self.btn0 =    ttk.Button(self.main_win, text="0",style="stdButton.TButton",command=lambda: self.btnAdd('0'))
        self.btn1 =    ttk.Button(self.main_win, text="1",style="stdButton.TButton",command=lambda: self.btnAdd('1'))
        self.btn2 =    ttk.Button(self.main_win, text="2",style="stdButton.TButton",command=lambda: self.btnAdd('2'))
        self.btn3 =    ttk.Button(self.main_win, text="3",style="stdButton.TButton",command=lambda: self.btnAdd('3'))
        self.btn4 =    ttk.Button(self.main_win, text="4",style="stdButton.TButton",command=lambda: self.btnAdd('4'))
        self.btn5 =    ttk.Button(self.main_win, text="5",style="stdButton.TButton",command=lambda: self.btnAdd('5'))
        self.btn6 =    ttk.Button(self.main_win, text="6",style="stdButton.TButton",command=lambda: self.btnAdd('6'))
        self.btn7 =    ttk.Button(self.main_win, text="7",style="stdButton.TButton",command=lambda: self.btnAdd('7'))
        self.btn8 =    ttk.Button(self.main_win, text="8",style="stdButton.TButton",command=lambda: self.btnAdd('8'))
        self.btn9 =    ttk.Button(self.main_win, text="9",style="stdButton.TButton",command=lambda: self.btnAdd('9'))
        self.btnPe =   ttk.Button(self.main_win, text=".",style="stdButton.TButton",command=lambda: self.btnAdd('.'))
        self.btnPl =   ttk.Button(self.main_win, text="+",style="stdButton.TButton",command=lambda: self.btnAdd('+'))
        self.btnMin =  ttk.Button(self.main_win, text="-",style="stdButton.TButton",command=lambda: self.btnAdd('-'))
        self.btnAst =  ttk.Button(self.main_win, text="x",style="stdButton.TButton",command=lambda: self.btnAdd('*'))
        self.btnSl =   ttk.Button(self.main_win, text="÷",style="stdButton.TButton",command=lambda: self.btnAdd('/'))
        self.btnEtr =  ttk.Button(self.main_win, text="Enter",style="stdButton.TButton",command=lambda: self.btnEnter())
        self.btnFn =   ttk.Button(self.main_win, text="切替",style="stdButton.TButton",command=lambda: self.Fn())
        self.btnBksp = ttk.Button(self.main_win,text="←",style="stdButton.TButton", command=lambda: self.btnBackspace())
        self.btnClr =  ttk.Button(self.main_win,text="消去/\n出力",style="stdButton2.TButton",command=lambda: self.btnClear())
        self.btnExt =  ttk.Button(self.main_win,text='終了/\nモード切替',style="stdButton3.TButton",command=lambda: self.btnExit())
        self.console = ttk.Label(self.main_win,relief="sunken",style="stdLabel.TLabel",anchor=tk.NW,textvariable=self.textoutput)
        self.console.place(x=0,y=0,width=self.btnwid*4,height=self.btnhei*2)
        self.btnFn.place(x=0,y=self.btnhei*2,width=self.btnwid,height=self.btnhei)
        self.btnSl.place(x=self.btnwid,y=self.btnhei*2,width=self.btnwid,height=self.btnhei)
        self.btnAst.place(x=self.btnwid*2,y=self.btnhei*2,width=self.btnwid,height=self.btnhei)
        self.btnBksp.place(x=self.btnwid*3,y=self.btnhei*2,width=self.btnwid,height=self.btnhei)
        self.btn7.place(x=0,y=self.btnhei*2+self.btnhei,width=self.btnwid,height=self.btnhei)
        self.btn8.place(x=self.btnwid,y=self.btnhei*2+self.btnhei,width=self.btnwid,height=self.btnhei)
        self.btn9.place(x=self.btnwid*2,y=self.btnhei*2+self.btnhei,width=self.btnwid,height=self.btnhei)
        self.btnEtr.place(x=self.btnwid*3,y=self.btnhei*2+self.btnhei,width=self.btnwid,height=self.btnhei)
        self.btn4.place(x=0,y=self.btnhei*2+self.btnhei*2,width=self.btnwid,height=self.btnhei)
        self.btn5.place(x=self.btnwid,y=self.btnhei*2+self.btnhei*2,width=self.btnwid,height=self.btnhei)
        self.btn6.place(x=self.btnwid*2,y=self.btnhei*2+self.btnhei*2,width=self.btnwid,height=self.btnhei)
        self.btnPl.place(x=self.btnwid*3,y=self.btnhei*2+self.btnhei*2,width=self.btnwid,height=self.btnhei)
        self.btn1.place(x=0,y=self.btnhei*2+self.btnhei*3,width=self.btnwid,height=self.btnhei)
        self.btn2.place(x=self.btnwid,y=self.btnhei*2+self.btnhei*3,width=self.btnwid,height=self.btnhei)
        self.btn3.place(x=self.btnwid*2,y=self.btnhei*2+self.btnhei*3,width=self.btnwid,height=self.btnhei)
        self.btnMin.place(x=self.btnwid*3,y=self.btnhei*2+self.btnhei*3,width=self.btnwid,height=self.btnhei)
        self.btnClr.place(x=0,y=self.btnhei*2+self.btnhei*4,width=self.btnwid,height=self.btnhei)
        self.btn0.place(x=self.btnwid,y=self.btnhei*2+self.btnhei*4,width=self.btnwid,height=self.btnhei)
        self.btnPe.place(x=self.btnwid*2,y=self.btnhei*2+self.btnhei*4,width=self.btnwid,height=self.btnhei)
        self.btnExt.place(x=self.btnwid*3,y=self.btnhei*2+self.btnhei*4,width=self.btnwid,height=self.btnhei)
        self.console.config(anchor=tk.N)
        self.textoutput.set('Calculator GUI Version 1.0\n Dr.GLaDOS🄬 2022\n\nEnterキーを押して下さい...\nPress Enter key to continue...')
        self.main_win.mainloop()
if __name__ == '__main__':
    main_win()