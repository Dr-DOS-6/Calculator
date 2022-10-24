#coding: UTF-8
import tkinter as tk
from tkinter import messagebox,END
import os
import textwrap as tw
import math
import re
#Thanks for Staycia930
#Version dev
mli = [0,0,0,0,0,0,0,0,0,0,0,0]
#                   0            1              2           3      4      5     6       7         8          9            10          11          12            13                          14      15      16            17                       18                                                          19                                                      20                   21                                     22              23            24       25         26                      27      28           29    30
#     langJa = ['消去/出力','消去/\n出力','終了/\nモード切替','消去','終了','切替','階乗','平方根','繰り上げ','繰り下げ','割り算\nの余り','最大\n公約数','eのx乗','yを底とする\nxの対数\n(log(x,y))','関数','絶対値','電卓モード','関数電卓モード','使用するモードを選んでください。\n電卓モード:1 関数電卓モード:2','入力された式は使用できません。もう一度式を入力してください。','が選択されました。','数値が大きすぎます。一回表示を消去してください。','結果の出力先:','デバッグ','EUGC Ver.Dev ','終了確認','終了してもよろしいですか？','確認','モード\n変更','出力','JA-Jp']
#                     0                 1                2           3      4       5          6             7          8          9                     10             11    12        13                    14              15                  16                   17                    18                                                                                          19                                              20                                         21                                                         22                  23           24             25                                  26        27     28        29              30                                                                       
#     langEn = ['Erase/\nExport','Erase/\nExport','Exit/\nSwitch','Erase','Exit','Switch','Factorial','Square\nroot','Carry','Carry\nforward','Remainder\nof division','G.C.D','exp','Logarithm\n(log(x,y))','Function','Absolute\nValue','Calculator Mode','Functions Calculator Mode','Please select the mode that you want to use.\nCalculator Mode:1 \nFunctions Calculator Mode:2',"has selected.","The inputted formula can't be calculated.\nPlease re-input the formula.",'The value is too large.Please erase the display once.','An result was output at:','Debug','EUGC Ver.Dev ','Confirm Exit','Are you sure you want to exit?','Confirm','Mode\nSwitch','Export','US-En']
#langset = []
class func:
    def screenresetter(self,mode):
        #self.style = tk.Style()
        #if self.langset[-1] == 'JA-Jp':
            #self.style.configure("stdButton.TButton",font=('Meiryo',20))
            #self.style.configure("stdButton2.TButton",font=('Meiryo',18))
            #self.style.configure("stdButton3.TButton",font=('Meiryo',14))
            #self.style.configure("stdButton4.TButton",font=('Meiryo',10))
            #self.style.configure("stdLabel.TLabel",font=('Meiryo',15))
        #elif self.langset[-1] == 'US-En':
            #self.style.configure("stdButton.TButton",font=('Meiryo',20))
            #self.style.configure("stdButton2.TButton",font=('Meiryo',18))
            #self.style.configure("stdButton3.TButton",font=('Meiryo',14))
            #self.style.configure("stdButton4.TButton",font=('Meiryo',12))
            #self.style.configure("stdLabel.TLabel",font=('Meiryo',15))
        if mode == 1:
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
            self.conframe.destroy()
            if self.langset[-1] == 'US-En': 
                self.btnFcrl = tk.Button(self.main_win,text=f"{self.langset[6]}",command=lambda: self.btnFactorial())
                self.btnSqrt = tk.Button(self.main_win,text=f"{self.langset[7]}",command=lambda: self.btnSquareroot())
                self.btnCil = tk.Button(self.main_win,text=f"{self.langset[8]}",command=lambda: self.btnCeil())
                self.btnFn =  tk.Button(self.main_win, text=f"{self.langset[5]}",command=lambda: self.Fn())
                self.btnGcd = tk.Button(self.main_win,text=f"{self.langset[11]}",command=lambda: self.btnGcdfunc())
                self.btnExp = tk.Button(self.main_win,text=f'{self.langset[12]}',command=lambda: self.btnExpfunc())               
            elif self.langset[-1] == 'JA-Jp':
                self.btnFcrl = tk.Button(self.main_win,text=f"{self.langset[6]}",command=lambda: self.btnFactorial())
                self.btnSqrt = tk.Button(self.main_win,text=f"{self.langset[7]}",command=lambda: self.btnSquareroot())
                self.btnCil = tk.Button(self.main_win,text=f"{self.langset[8]}",command=lambda: self.btnCeil())                
                self.btnFn =   tk.Button(self.main_win, text=f"{self.langset[5]}",command=lambda: self.Fn())       
                self.btnGcd = tk.Button(self.main_win,text=f"{self.langset[11]}",command=lambda: self.btnGcdfunc())
                self.btnExp = tk.Button(self.main_win,text=f'{self.langset[12]}',command=lambda: self.btnExpfunc())
            self.conframe = tk.Frame(self.main_win, width=self.btnwid*4,height=self.btnhei*2)
            self.btnLog = tk.Button(self.main_win,text=f'{self.langset[13]}',command=lambda: self.btnLogfunc())
            self.btnPct = tk.Button(self.main_win,text=f'{self.langset[10]}',command=lambda: self.btnAdd('%'))   
            self.btnFlr = tk.Button(self.main_win,text=f"{self.langset[9]}",command=lambda: self.btnFloor())
            self.console = tk.Label(self.conframe,relief="sunken",anchor=tk.NW,textvariable=self.textoutput)
            self.btn0 =    tk.Button(self.main_win, text="0",command=lambda: self.btnAdd('0'))
            self.btn1 =    tk.Button(self.main_win, text="1",command=lambda: self.btnAdd('1'))
            self.btn2 =    tk.Button(self.main_win, text="2",command=lambda: self.btnAdd('2'))
            self.btn3 =    tk.Button(self.main_win, text="3",command=lambda: self.btnAdd('3'))
            self.btn4 =    tk.Button(self.main_win, text="4",command=lambda: self.btnAdd('4'))
            self.btn5 =    tk.Button(self.main_win, text="5",command=lambda: self.btnAdd('5'))
            self.btn6 =    tk.Button(self.main_win, text="6",command=lambda: self.btnAdd('6'))
            self.btn7 =    tk.Button(self.main_win, text="7",command=lambda: self.btnAdd('7'))
            self.btn8 =    tk.Button(self.main_win, text="8",command=lambda: self.btnAdd('8'))
            self.btn9 =    tk.Button(self.main_win, text="9",command=lambda: self.btnAdd('9'))
            self.btnPe =   tk.Button(self.main_win, text=".",command=lambda: self.btnAdd('.'))
            self.btnPl =   tk.Button(self.main_win, text="+",command=lambda: self.btnAdd('+'))
            self.btnMin =  tk.Button(self.main_win, text="-",command=lambda: self.btnAdd('-'))
            self.btnAst =  tk.Button(self.main_win, text="x",command=lambda: self.btnAdd('*'))
            self.btnSl =   tk.Button(self.main_win, text="÷",command=lambda: self.btnAdd('/'))
            self.btnEtr =  tk.Button(self.main_win, text="Enter",command=lambda: self.btnEnter())                         
            self.btnBksp = tk.Button(self.main_win,text="←", command=lambda: self.btnBackspace())
            self.btnClr =  tk.Button(self.main_win,text=f"{self.langset[3]}",command=lambda: self.btnClear())
            self.btnExt =  tk.Button(self.main_win,text=f'{self.langset[4]}',command=lambda: self.btnExit())    
            self.btnCma = tk.Button(self.main_win,text=",",command=lambda: self.btnAdd(','))
            self.btnBrckL = tk.Button(self.main_win,text="(",command=lambda: self.btnAdd('('))
            self.btnBrckR = tk.Button(self.main_win,text=")",command=lambda: self.btnAdd(')'))
            self.btnSint = tk.Button(self.main_win,text='sin',command=lambda: self.btnSintfunc())
            self.btnCost = tk.Button(self.main_win,text='cos',command=lambda: self.btnCostfunc())
            self.btnTant = tk.Button(self.main_win,text='tan',command=lambda: self.btnTantfunc())
            self.console.pack(expand=1,fill=tk.BOTH)#lace(x=self.btnwid*2,y=0,width=self.btnwid*4,height=self.btnhei*2)
            self.conframe.pack()#fill=tk.BOTH,side='left',expand=1)
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
            self.btnSint.place(x=self.btnwid,y=self.btnhei*3,width=self.btnwid,height=self.btnhei)
            self.btnCost.place(x=0,y=self.btnhei*4,width=self.btnwid,height=self.btnhei)
            self.btnTant.place(x=self.btnwid,y=self.btnhei*4,width=self.btnwid,height=self.btnhei)
            self.btnBrckL.place(x=0,y=self.btnhei*6,width=self.btnwid,height=self.btnhei)
            self.btnBrckR.place(x=self.btnwid,y=self.btnhei*6,width=self.btnwid,height=self.btnhei)
            self.mode2 = 1
        elif mode == 2:
            self.main_win.geometry(f'{self.winwid}x{self.winhei}+{int((self.scrwid-self.winwid)/2)}+{int((self.scrhei-self.winhei)/2)}')
            try:
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
                self.btnSint.destroy()
                self.btnCost.destroy()
                self.btnTant.destroy()
            except AttributeError:
                None
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
            self.conframe.destroy()
            self.btnframe1.destroy()
            self.btnframe2.destroy()
            self.btnframe3.destroy()
            self.btnframe4.destroy()
            self.btnframe5.destroy()
            
            
            self.conframe =  tk.Frame(self.main_win,relief=tk.RAISED,bd=2,bg='green',width=self.btnwid*4,height=self.btnhei*4)
            self.btnframe1 = tk.Frame(self.main_win,relief=tk.RAISED,bd=2,bg='red', width=self.btnwid*4,height=self.btnhei)
            self.btnframe2 = tk.Frame(self.main_win,relief=tk.RAISED,bd=2,bg='blue', width=self.btnwid*4,height=self.btnhei)
            self.btnframe3 = tk.Frame(self.main_win,relief=tk.RAISED,bd=2,bg='yellow', width=self.btnwid*4,height=self.btnhei)
            self.btnframe4 = tk.Frame(self.main_win,relief=tk.RAISED,bd=2,bg='black', width=self.btnwid*4,height=self.btnhei)
            self.btnframe5 = tk.Frame(self.main_win,relief=tk.RAISED,bd=2,bg='orange', width=self.btnwid*4,height=self.btnhei)

            self.console =   tk.Label(self.conframe,relief="sunken",anchor=tk.NW,textvariable=self.textoutput)

            self.btnAst =   tk.Button(self.btnframe1,width=self.btnwid,height=self.btnhei, text="x",command=lambda: self.btnAdd('*'))
            self.btnSl =    tk.Button(self.btnframe1,width=self.btnwid,height=self.btnhei, text="÷",command=lambda: self.btnAdd('/'))
            if self.langset[-1] == 'US-En': 
                self.btnFn =  tk.Button(self.btnframe1,width=self.btnwid,height=self.btnhei, text=f"{self.langset[5]}",command=lambda: self.Fn())         
            elif self.langset[-1] == 'JA-Jp':          
                self.btnFn =   tk.Button(self.btnframe1,width=self.btnwid,height=self.btnhei, text=f"{self.langset[5]}",command=lambda: self.Fn())   
            self.btnBksp =  tk.Button(self.btnframe1,width=self.btnwid,height=self.btnhei,text="←", command=lambda: self.btnBackspace())

            self.btn7 =    tk.Button(self.btnframe2,width=self.btnwid,height=self.btnhei, text="7",command=lambda: self.btnAdd('7'))
            self.btn8 =    tk.Button(self.btnframe2,width=self.btnwid,height=self.btnhei, text="8",command=lambda: self.btnAdd('8'))
            self.btn9 =    tk.Button(self.btnframe2,width=self.btnwid,height=self.btnhei, text="9",command=lambda: self.btnAdd('9'))
            self.btnEtr =  tk.Button(self.btnframe2,width=self.btnwid,height=self.btnhei, text="Enter",command=lambda: self.btnEnter())

            self.btn4 =    tk.Button(self.btnframe3,width=self.btnwid,height=self.btnhei, text="4",command=lambda: self.btnAdd('4'))
            self.btn5 =    tk.Button(self.btnframe3,width=self.btnwid,height=self.btnhei, text="5",command=lambda: self.btnAdd('5'))
            self.btn6 =    tk.Button(self.btnframe3,width=self.btnwid,height=self.btnhei, text="6",command=lambda: self.btnAdd('6'))
            self.btnPl =   tk.Button(self.btnframe3,width=self.btnwid,height=self.btnhei, text="+",command=lambda: self.btnAdd('+'))

            self.btn1 =    tk.Button(self.btnframe4,width=self.btnwid,height=self.btnhei, text="1",command=lambda: self.btnAdd('1'))
            self.btn2 =    tk.Button(self.btnframe4,width=self.btnwid,height=self.btnhei, text="2",command=lambda: self.btnAdd('2'))
            self.btn3 =    tk.Button(self.btnframe4,width=self.btnwid,height=self.btnhei, text="3",command=lambda: self.btnAdd('3'))
            self.btnMin =  tk.Button(self.btnframe4,width=self.btnwid,height=self.btnhei, text="-",command=lambda: self.btnAdd('-'))

            self.btnClr =  tk.Button(self.btnframe5,width=self.btnwid,height=self.btnhei,text=f"{self.langset[3]}",command=lambda: self.btnClear())
            self.btn0 =    tk.Button(self.btnframe5,width=self.btnwid,height=self.btnhei, text="0",command=lambda: self.btnAdd('0'))
            self.btnPe =   tk.Button(self.btnframe5,width=self.btnwid,height=self.btnhei, text=".",command=lambda: self.btnAdd('.'))
            self.btnExt =  tk.Button(self.btnframe5,width=self.btnwid,height=self.btnhei,text=f'{self.langset[4]}',command=lambda: self.btnExit())

            self.conframe.pack(fill='x')
            self.btnframe1.pack(fill='x')
            self.btnframe2.pack(fill='x')
            self.btnframe3.pack(fill='x')
            self.btnframe4.pack(fill='x')
            self.btnframe5.pack(fill='x')

            self.console.grid(column=0,row=0)

            self.btnFn.grid(column=0,row=0)
            self.btnSl.grid(column=1,row=0)
            self.btnAst.grid(column=2,row=0)
            self.btnBksp.grid(column=3,row=0)

            self.btn7.grid(column=0,row=0)
            self.btn8.grid(column=1,row=0)
            self.btn9.grid(column=2,row=0)
            self.btnEtr.grid(column=3,row=0)

            self.btn4.grid(column=0,row=0)
            self.btn5.grid(column=1,row=0)
            self.btn6.grid(column=2,row=0)
            self.btnPl.grid(column=3,row=0)

            self.btn1.grid(column=0,row=0)
            self.btn2.grid(column=1,row=0)
            self.btn3.grid(column=2,row=0)
            self.btnMin.grid(column=3,row=0)

            self.btnClr.grid(column=0,row=0)
            self.btn0.grid(column=1,row=0)
            self.btnPe.grid(column=2,row=0)
            self.btnExt.grid(column=3,row=0)
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
            elif self.keyin2 == "Escape":
                self.btnExit()
            else:
                self.temp += self.keyin2
                #print(self.temp
                self.textReplacer(self.temp,'kbd_input')
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
        elif key_input == "Escape":
            return "Escape"
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
        if self.btnExt.cget('text') == f'{self.langset[28]}':
            self.btnClr.config(text= f'{self.langset[3]}')
            self.btnExt.config(text= f'{self.langset[4]}')
            if not f'{self.langset[14]}' in self.title:
                None
            else:
                try:
                    self.btnSint.config(text='sin')
                    self.btnCost.config(text='cos')
                    self.btnTant.config(text='tan')
                    self.btnFcrl.config(text=f'{self.langset[6]}')
                except AttributeError:
                    None
        elif self.btnExt.cget('text') == f'{self.langset[4]}':
            if self.langset[-1] == 'US-En': 
                self.btnClr.config(text=f'{self.langset[29]}')
            else:
                self.btnClr.config(text= f'{self.langset[29]}')
            self.btnExt.config(text= f'{self.langset[28]}')
            if not f'{self.langset[14]}' in self.title:
                None
            else:
                try:
                    self.btnSint.config(text='arc\nsin')
                    self.btnCost.config(text='arc\ncos')
                    self.btnTant.config(text='arc\ntan')
                    self.btnFcrl.config(text=f'{self.langset[15]}')
                except AttributeError:
                    None
    def textReplacer(self,_input,caller):
        self._input = re.sub('Num_Lock|Tab|Control_R|Control_L|Shift_R|Shift_L|ignore','',tw.fill(_input,40))
        #if caller == 'btnEnter':
        #    self._input = re.sub('sin[0-9]{,10}','self.sin',)
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
            self.textReplacer(self.temp,'btnAdd')
            mli[2] = 0
        if mli[10] == 0 and mli[11] == 1 and _input == '1':
            self.langset = ['消去/出力','消去/\n出力','終了/\nモード切替','消去','終了','切替','階乗','平方根','繰り上げ','繰り下げ','割り算\nの余り','最大\n公約数','eのx乗','yを底とする\nxの対数\n(log(x,y))','関数','絶対値','電卓モード','関数電卓モード','使用するモードを選んでください。\n電卓モード:1 関数電卓モード:2','入力された式は使用できません。もう一度式を入力してください。','が選択されました。','数値が大きすぎます。一回表示を消去してください。','結果の出力先:','デバッグ','EUGC Verdev ','終了確認','終了してもよろしいですか？','確認','モード\n変更','出力','JA-Jp']
            self.textoutput.set('日本語が選択されました。\nEnterキーを押してください。')
            mli[10] = 1
            mli[11] = 0
        elif mli[10] == 0 and mli[11] == 1 and _input == '2':
            #self.langset = ['ID0','ID1','ID2','ID3','ID4','ID5','ID6','ID7','ID8','ID9','ID10','ID11','ID12','ID13','ID14','ID15','ID16','ID17','ID18','ID19','ID20','ID21','ID22','ID23','ID24','ID25','ID26','ID27','ID28','ID29','US-En']
            self.langset = ['Erase/\nExport','Erase/\nExport','Exit/\nSwitch','Erase','Exit','Switch','Factorial','Square\nroot','Carry','Carry\nforward','Remain\nof divid','G.C.D','exp','Logarithm\n(log(x,y))','Function','Absolute\nValue','Calculator Mode','Functions Calculator Mode','Please select the mode that you want to use.\nCalculator Mode:1 \nFunctions Calculator Mode:2',"has selected.","The inputted formula can't be calculated.\nPlease re-input the formula.",'The value is too large.Please erase the display once.','An result was output at:','Debug','EUGC Verdev ','Confirm Exit','Are you sure you want to exit?','Confirm','Mode\nSwitch','Export','US-En']
            self.textoutput.set('English has selected.\nPress Enter to proceed.')
            mli[10] = 1
            mli[11] = 0
        elif  mli[3] == 1 and _input == '1':
            self.console.config(anchor=tk.NW)
            self.temp = str()
            self.textReplacer(self.temp,'btnAdd')
            self.title = f'{self.langset[24]+self.langset[16]}'
            self.main_win.title(self.title)
            self.screenresetter(2)
            mli[3] = 0
            #mli[4] = 1
            mli[8] = 1
        elif mli[3] == 1 and _input == '2':
            self.console.config(anchor=tk.NW)
            self.temp = str()
            self.textReplacer(self.temp,'btnAdd')
            self.title = f'{self.langset[24]+self.langset[17]}'
            self.main_win.title(self.title)
            self.screenresetter(1)
            mli[3] = 0
            #mli[4] = 1
            mli[8] = 2
        elif mli[3] == 1 and _input == '3':
            self.temp = f'{self.langset[30]}'
        elif mli[4] == 1:
            self.temp = str()
            self.textReplacer(self.temp,'btnAdd')
            mli[4] = 0       
        else:
            if self.stat == 0:
                self.stat = 1
            else:
                self.console.config(anchor=tk.NW)
                self.temp += _input
                self.textReplacer(self.temp,'btnAdd')
    def sin(self,_input):
        return math.sin(math.radians(_input))
    def asin(self,_input):
        return math.asin(_input)
    def cos(self,_input):
        return math.cos(math.radians(_input))
    def acos(self,_input):
        return math.acos(_input)
    def tan(self,_input):
        return math.tan(math.radians(_input))
    def atan(self,_input):
        return math.atan(_input)
    def factorial(self,_input):
        return math.factorial(_input)
    def fabs(self,_input):
        return math.fabs(_input)
    def btnSintfunc(self):
        if self.btnSint.cget('text') == 'sin':
            self.temp += 'self.sin('
        elif self.btnSint.cget('text') == 'arc\nsin':
            self.temp += 'self.asin('
        self.textReplacer(self.temp,'btnSintfunc')
    def btnCostfunc(self):
        if self.btnCost.cget('text') == 'cos':
            self.temp += 'self.cos('
        elif self.btnCost.cget('text') == 'arc\ncos':
            self.temp += 'self.acos('
        self.textReplacer(self.temp,'btnCostfunc')
    def btnTantfunc(self): 
        if self.btnTant.cget('text') == 'tan':
            self.temp += 'self.tan('
        elif self.btnTant.cget('text') == 'arc\ntan':
            self.temp += 'self.atan('
        self.textReplacer(self.temp,'btnTantfunc')
    def btnLogfunc(self):
        self.temp += "math.log("
        self.textReplacer(self.temp,'btnLogfunc')
    def btnExpfunc(self):
        self.temp += "math.exp("
        self.textReplacer(self.temp,'btnExpfunc')
    def btnGcdfunc(self):
        self.temp += "math.gcd("
        self.textReplacer(self.temp,'btnGcdfunc')
    def btnCeil(self):
        self.temp += "math.ceil("
        self.textReplacer(self.temp,'btnCeil')
    def btnFloor(self):
        self.temp += "math.floor("
        self.textReplacer(self.temp,'btnFloor')
    def btnSquareroot(self):
        self.temp += "math.sqrt("
        self.textReplacer(self.temp,'btnSqrt')
    def btnFactorial(self):
        if self.btnFcrl.cget('text') == f'{self.langset[6]}':
            self.temp += "self.factorial("
        elif self.btnFcrl.cget('text') == f'{self.langset[15]}':
            self.temp += "self.fabs("
        self.textReplacer(self.temp,'btnFactorial')
    def btnEnter(self):
        self.console.config(anchor=tk.NW)
        if mli[1] == 0:
            if mli[10] == 0:
                self.textoutput.set('言語を選んでください。\nPlease select a language.\n日本語:1 English:2')
                mli[11] = 1
            elif mli[10] == 1:
                self.textoutput.set(f'{self.langset[18]}')
                self.console.config(anchor=tk.NW)
                mli[1] = 1
                mli[3] = 1
        elif mli[2] == 1:
            self.temp = str()
            self.textReplacer(self.temp,'btnEnter2')
            mli[2] = 0
        elif mli[8] == 0:
            pass
        else:
            try :
                self.temp = str(eval(self.temp))
                self.textReplacer(self.temp,'btnEnter')
            except SyntaxError:
                if mli[1] == 0 or mli[6] == 1:
                    pass
                    END
                elif f'{self.langset[19]}' or f'{self.langset[16]+self.langset[20]}' or f'{self.langset[17]+self.langset[20]}' in self.temp:
                    self.btnClear()
                else:
                    pass
                    self.temp += f'{self.langset[19]}'
                    self.textReplacer(self.temp,'btnEnter2')
            except ZeroDivisionError:
                pass
            except OverflowError:
                self.temp = f'{self.langset[21]}'
                self.textReplacer(self.temp,'btnEnter2')
    def btnClear(self):
        self.console.config(anchor=tk.NW)
        if self.btnClr.cget('text') == 'Export':
            with open('result.txt', mode = 'a', encoding = 'UTF-8') as f:
                f.write(self.temp)
            self.path = os.path.abspath('result.txt')
            self.temp = f'An result was output at:\n{self.path}'
            self.textReplacer(self.temp,'btnClear')
            mli[2] = 1
        else:
            self.temp = str()
            self.textReplacer(self.temp,'btnClear')
    def btnBackspace(self):
        self.console.config(anchor=tk.NW)
        if self.temp[-15:] == 'math.factorial(':
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
        elif self.temp[-4:] == 'asin(':
            self.temp = self.temp[:len(self.temp)-4]
        elif self.temp[-4:] == 'acos(':
            self.temp = self.temp[:len(self.temp)-4]
        elif self.temp[-4:] == 'atan(':
            self.temp = self.temp[:len(self.temp)-4]
        elif self.temp[-3:] == 'sin(':
            self.temp = self.temp[:len(self.temp)-3]
        elif self.temp[-3:] == 'cos(':
            self.temp = self.temp[:len(self.temp)-3]
        elif self.temp[-3:] == 'tan(':
            self.temp = self.temp[:len(self.temp)-3]
        else:
            self.temp = self.temp[:len(self.temp)-1]
        #print(self.temp)
        self.textReplacer(self.temp,'btnBackspace')
    def btnExit(self):
        if self.btnExt.cget('text') == f'{self.langset[28]}':
            if self.title == f'{self.langset[24]+self.langset[16]}':
                self.title = f'{self.langset[24]+self.langset[17]}'
                self.main_win.title(self.title)
                self.screenresetter(1)
            #elif self.title == '{self.langset[24]} 電卓デバッグモード':
            #    self.title = '{self.langset[24]} 関数電卓デバッグモード'
            #    self.main_win.title(self.title)
            #    self.screenresetter(4)
            elif self.title == f'{self.langset[24]+self.langset[17]}':
                self.title = f'{self.langset[24]+self.langset[16]}'
                self.main_win.title(self.title)
                self.screenresetter(2)
            #elif self.title == '{self.langset[24]} 関数電卓デバッグモード':
            #    self.title = '{self.langset[24]} 電卓デバッグモード'
            #    self.main_win.title(self.title)
            #    self.screenresetter(3)
        else:
            Messagebox = tk.messagebox.askquestion(f'{self.langset[24]+self.langset[25]}',f'{self.langset[26]}', icon='warning')
            if Messagebox == 'yes':
                self.main_win.destroy()
            else:
                pass
    def btnChgwinsize(self):
        if self.subwin.winfo_exists == True:
            pass
        else:
            self.subwin = tk.Toplevel()
            self.winhei2 = self.main_win.winfo_height()
            self.winwid2 = self.main_win.winfo_width()
            self.scrhei2 = self.main_win.winfo_screenheight()
            self.scrwid2 = self.main_win.winfo_screenwidth()
            self.winsize = f'{int(self.winwid2/2)}x{int(self.winhei2/2)}+{int((self.scrwid2-self.winwid2)/2)-int(self.winwid2/2)}+{int((self.scrhei2-self.winhei2)/2)}'
            self.subwin.geometry(self.winsize)
            self.resinput = tk.Entry(self.subwin,width=20)
            self.btnressel = tk.Button(self.sub_win,text=f'{self.langset[27]}')
            self.resinput.pack()
            self.subwin.mainloop()
class main_win(func):
    def __init__(self):
        self.main_win = tk.Tk()
        #self.style = tk.Style()
        #self.style.configure("stdButton.TButton",font=('Meiryo',20))
        #self.style.configure("stdButton2.TButton",font=('Meiryo',15))
        #self.style.configure("stdButton3.TButton",font=('Meiryo',12))
        #self.style.configure("stdButton4.TButton",font=('Meiryo',10))
        #self.style.configure("stdLabel.TLabel",font=('Meiryo',12))
        self.main_win.title('EUGC Verdev')
        self.scrwid = self.main_win.winfo_screenwidth()
        self.scrhei = self.main_win.winfo_screenheight()
        self.fulwinwid = self.scrwid
        self.fulwinhei = self.scrhei
        self.fulbtnwid = int(self.fulwinwid/4)
        self.fulbtnhei = int(self.fulwinhei/7)
        self.winwid = 360
        self.winhei = 630
        self.btnwid = int((self.winwid/4)/10)
        self.btnhei = int(((self.winhei/7)/2)/10)
        self.winsize = f'{self.winwid}x{self.winhei}+{int((self.scrwid-self.winwid)/2)}+{int((self.scrhei-self.winhei)/2)}'
        self.main_win.geometry(self.winsize)
        self.main_win.bind("<KeyPress>",self.kbd_input)
        mli[7] = 0
        self.textoutput = tk.StringVar()
        mli[1] = 0
        self.temp = str()
        mli[2] = 0
        self.conframe =  tk.Frame(self.main_win,relief=tk.RAISED,bd=2,bg='green',width=self.btnwid*4,height=self.btnhei*4)
        self.btnframe1 = tk.Frame(self.main_win,relief=tk.RAISED,bd=2,bg='red', width=self.btnwid*4,height=self.btnhei)
        self.btnframe2 = tk.Frame(self.main_win,relief=tk.RAISED,bd=2,bg='blue', width=self.btnwid*4,height=self.btnhei)
        self.btnframe3 = tk.Frame(self.main_win,relief=tk.RAISED,bd=2,bg='yellow', width=self.btnwid*4,height=self.btnhei)
        self.btnframe4 = tk.Frame(self.main_win,relief=tk.RAISED,bd=2,bg='black', width=self.btnwid*4,height=self.btnhei)
        self.btnframe5 = tk.Frame(self.main_win,relief=tk.RAISED,bd=2,bg='orange', width=self.btnwid*4,height=self.btnhei)

        self.console =   tk.Label(self.conframe,relief="sunken",anchor=tk.NW,textvariable=self.textoutput)

        self.btnAst =   tk.Button(self.btnframe1,width=self.btnwid,height=self.btnhei,text="x")
        self.btnSl =    tk.Button(self.btnframe1,width=self.btnwid,height=self.btnhei,text="÷")
        self.btnFn =    tk.Button(self.btnframe1,width=self.btnwid,height=self.btnhei,text=f"切替")   
        self.btnBksp =  tk.Button(self.btnframe1,width=self.btnwid,height=self.btnhei,text="←")

        self.btn7 =     tk.Button(self.btnframe2,width=self.btnwid,height=self.btnhei, text="7")
        self.btn8 =     tk.Button(self.btnframe2,width=self.btnwid,height=self.btnhei, text="8")
        self.btn9 =     tk.Button(self.btnframe2,width=self.btnwid,height=self.btnhei, text="9")
        self.btnEtr =   tk.Button(self.btnframe2,width=self.btnwid,height=self.btnhei, text="Enter",command=lambda: self.btnEnter())

        self.btn4 =     tk.Button(self.btnframe3,width=self.btnwid,height=self.btnhei, text="4")
        self.btn5 =     tk.Button(self.btnframe3,width=self.btnwid,height=self.btnhei, text="5")
        self.btn6 =     tk.Button(self.btnframe3,width=self.btnwid,height=self.btnhei, text="6")
        self.btnPl =    tk.Button(self.btnframe3,width=self.btnwid,height=self.btnhei, text="+")

        self.btn1 =     tk.Button(self.btnframe4,width=self.btnwid,height=self.btnhei, text="1",command=lambda: self.btnAdd('1'))
        self.btn2 =     tk.Button(self.btnframe4,width=self.btnwid,height=self.btnhei, text="2",command=lambda: self.btnAdd('2'))
        self.btn3 =     tk.Button(self.btnframe4,width=self.btnwid,height=self.btnhei, text="3")
        self.btnMin =   tk.Button(self.btnframe4,width=self.btnwid,height=self.btnhei, text="-")

        self.btnClr =   tk.Button(self.btnframe5,width=self.btnwid,height=self.btnhei,text=f"消去/\n出力")
        self.btn0 =     tk.Button(self.btnframe5,width=self.btnwid,height=self.btnhei, text="0")
        self.btnPe =    tk.Button(self.btnframe5,width=self.btnwid,height=self.btnhei, text=".")
        self.btnExt =   tk.Button(self.btnframe5,width=self.btnwid,height=self.btnhei,text=f'終了/\nモード切替',command=lambda: self.btnExit())

        self.conframe.pack(fill='x')
        self.btnframe1.pack(fill='x')
        self.btnframe2.pack(fill='x')
        self.btnframe3.pack(fill='x')
        self.btnframe4.pack(fill='x')
        self.btnframe5.pack(fill='x')

        self.console.grid(column=0,row=0)

        self.btnFn.grid(column=0,row=0)
        self.btnSl.grid(column=1,row=0)
        self.btnAst.grid(column=2,row=0)
        self.btnBksp.grid(column=3,row=0)
        
        self.btn7.grid(column=0,row=0)
        self.btn8.grid(column=1,row=0)
        self.btn9.grid(column=2,row=0)
        self.btnEtr.grid(column=3,row=0)

        self.btn4.grid(column=0,row=0)
        self.btn5.grid(column=1,row=0)
        self.btn6.grid(column=2,row=0)
        self.btnPl.grid(column=3,row=0)

        self.btn1.grid(column=0,row=0)
        self.btn2.grid(column=1,row=0)
        self.btn3.grid(column=2,row=0)
        self.btnMin.grid(column=3,row=0)

        self.btnClr.grid(column=0,row=0)
        self.btn0.grid(column=1,row=0)
        self.btnPe.grid(column=2,row=0)
        self.btnExt.grid(column=3,row=0)

        self.console.config(anchor=tk.N)
        self.textoutput.set('Calculator GUI Version dev\n Dr.GLaDOS© 2022\n\nEnterキーを押して下さい...\nPress Enter key to continue...')
        self.stat = 0
        self.main_win.mainloop()
main_win()