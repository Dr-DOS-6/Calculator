#coding: UTF-8
import tkinter as tk
from tkinter import messagebox,END,ttk
import os
import textwrap as tw
import math
import re
import multiprocessing
import time
#Thanks for Staycia930
#Version  Dev
mli = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
#                   0            1              2           3      4      5     6       7         8          9            10          11          12            13                          14      15      16            17                       18                                                          19                                                      20                   21                                     22              23            24       25         26                      27      28           29    30
#     langJa = ['消去/出力','消去/\n出力','終了/\nモード切替','消去','終了','切替','階乗','平方根','繰り上げ','繰り下げ','割り算\nの余り','最大\n公約数','eのx乗','yを底とする\nxの対数\n(log(x,y))','関数','絶対値','電卓モード','関数電卓モード','使用するモードを選んでください。\n電卓モード:1 関数電卓モード:2','入力された式は使用できません。もう一度式を入力してください。','が選択されました。','数値が大きすぎます。一回表示を消去してください。','結果の出力先:','デバッグ','EUGC Ver.Dev ','終了確認','終了してもよろしいですか？','確認','モード\n変更','出力','JA-Jp']
#                     0                 1                2           3      4       5          6             7          8          9                     10             11    12        13                    14              15                  16                   17                    18                                                                                          19                                              20                                         21                                                         22                  23           24             25                                  26        27     28        29              30                                                                       
#     langEn = ['Erase/\nExport','Erase/\nExport','Exit/\nSwitch','Erase','Exit','Switch','Factorial','Square\nroot','Carry','Carry\nforward','Remainder\nof division','G.C.D','exp','Logarithm\n(log(x,y))','Function','Absolute\nValue','Calculator Mode','Functions Calculator Mode','Please select the mode that you want to use.\nCalculator Mode:1 \nFunctions Calculator Mode:2',"has selected.","The inputted formula can't be calculated.\nPlease re-input the formula.",'The value is too large.Please erase the display once.','An result was output at:','Debug','EUGC Ver.Dev ','Confirm Exit','Are you sure you want to exit?','Confirm','Switch','Export','US-En']
#langset = []

# mliのインデックスを定数として定義
MLI_LANGUAGE_SELECTED = 1
MLI_DISPLAY_CLEAR = 2
MLI_MODE_SELECTION = 3
MLI_DISPLAY_CLEARED = 4
MLI_INITIALIZED = 7
MLI_CURRENT_MODE = 8
MLI_LANGUAGE_IN_PROGRESS = 11
MLI_FUNC_SCREEN_RESETTER = 12
MLI_FUNC_BTN_ADD = 13
MLI_FUNC_BTN_ENTER = 14
MLI_FUNC_BTN_CLEAR = 15
MLI_FUNC_BTN_EXIT = 16

class func:
    def screenresetter(self,mode):
        self.style = ttk.Style()
        if self.langset[-1] == 'JA-Jp':
            self.style.configure("stdButton.TButton",font=('Meiryo',20))
            self.style.configure("stdButton2.TButton",font=('Meiryo',18))
            self.style.configure("stdButton3.TButton",font=('Meiryo',14))
            self.style.configure("stdButton4.TButton",font=('Meiryo',10))
            self.style.configure("stdLabel.TLabel",font=('Meiryo',15))
        elif self.langset[-1] == 'US-En':
            self.style.configure("stdButton.TButton",font=('Meiryo',20))
            self.style.configure("stdButton2.TButton",font=('Meiryo',18))
            self.style.configure("stdButton3.TButton",font=('Meiryo',14))
            self.style.configure("stdButton4.TButton",font=('Meiryo',12))
            self.style.configure("stdLabel.TLabel",font=('Meiryo',15))
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
            if self.langset[-1] == 'US-En': 
                self.btnFcrl = ttk.Button(self.main_win,text=f"{self.langset[6]}",style="stdButton3.TButton",command=lambda: self.btnFactorial())
                self.btnSqrt = ttk.Button(self.main_win,text=f"{self.langset[7]}",style="stdButton3.TButton",command=lambda: self.btnSquareroot())
                self.btnCil = ttk.Button(self.main_win,text=f"{self.langset[8]}",style="stdButton.TButton",command=lambda: self.btnCeil())
                self.btnFn = ttk.Button(self.main_win, text=f"{self.langset[5]}",style="stdButton2.TButton",command=lambda: self.Fn())
                self.btnGcd = ttk.Button(self.main_win,text=f"{self.langset[11]}",style="stdButton.TButton",command=lambda: self.btnGcdfunc())
                self.btnExp = ttk.Button(self.main_win,text=f'{self.langset[12]}',style="stdButton.TButton",command=lambda: self.btnExpfunc())               
            elif self.langset[-1] == 'JA-Jp':
                self.btnFcrl = ttk.Button(self.main_win,text=f"{self.langset[6]}",style="stdButton.TButton",command=lambda: self.btnFactorial())
                self.btnSqrt = ttk.Button(self.main_win,text=f"{self.langset[7]}",style="stdButton.TButton",command=lambda: self.btnSquareroot())
                self.btnCil = ttk.Button(self.main_win,text=f"{self.langset[8]}",style="stdButton3.TButton",command=lambda: self.btnCeil())                
                self.btnFn = ttk.Button(self.main_win, text=f"{self.langset[5]}",style="stdButton.TButton",command=lambda: self.Fn())       
                self.btnGcd = ttk.Button(self.main_win,text=f"{self.langset[11]}",style="stdButton3.TButton",command=lambda: self.btnGcdfunc())
                self.btnExp = ttk.Button(self.main_win,text=f'{self.langset[12]}',style="stdButton3.TButton",command=lambda: self.btnExpfunc())
            self.btnLog = ttk.Button(self.main_win,text=f'{self.langset[13]}',style="stdButton4.TButton",command=lambda: self.btnLogfunc())
            self.btnPct = ttk.Button(self.main_win,text=f'{self.langset[10]}',style="stdButton3.TButton",command=lambda: self.btnAdd('%'))   
            self.btnFlr = ttk.Button(self.main_win,text=f"{self.langset[9]}",style="stdButton3.TButton",command=lambda: self.btnFloor())
            self.console = ttk.Label(self.main_win,relief="sunken",style="stdLabel.TLabel",anchor=tk.NW,textvariable=self.textoutput)
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
            self.btnBksp = ttk.Button(self.main_win,text="←",style="stdButton.TButton", command=lambda: self.btnBackspace())
            self.btnClr =  ttk.Button(self.main_win,text=f"{self.langset[3]}",style="stdButton.TButton",command=lambda: self.btnClear())
            self.btnExt =  ttk.Button(self.main_win,text=f'{self.langset[4]}',style="stdButton.TButton",command=lambda: self.btnExit())    
            self.btnCma = ttk.Button(self.main_win,text=",",style="stdButton.TButton",command=lambda: self.btnAdd(','))
            self.btnBrckL = ttk.Button(self.main_win,text="(",style="stdButton.TButton",command=lambda: self.btnAdd('('))
            self.btnBrckR = ttk.Button(self.main_win,text=")",style="stdButton.TButton",command=lambda: self.btnAdd(')'))
            self.btnSint = ttk.Button(self.main_win,text='sin',style="stdButton.TButton",command=lambda: self.btnSintfunc())
            self.btnCost = ttk.Button(self.main_win,text='cos',style="stdButton.TButton",command=lambda: self.btnCostfunc())
            self.btnTant = ttk.Button(self.main_win,text='tan',style="stdButton.TButton",command=lambda: self.btnTantfunc())
            self.console.place(x=self.btnwid*2,y=0,width=self.btnwid*4,height=self.btnhei*2)
            self.btnFn.place(x=self.btnwid*2,y=self.btnhei*2,width=self.btnwid,height=self.btnhei)
            self.btnSl.place(x=self.btnwid*3,y=self.btnhei*2,width=self.btnwid,height=self.btnhei)
            self.btnAst.place(x=self.btnwid*4,y=self.btnhei*2,width=self.btnwid,height=self.btnhei)
            self.btnBksp.place(x=self.btnwid*5,y=self.btnhei*2,width=self.btnwid,height=self.btnhei)
            self.btn7.place(x=self.btnwid*2,y=self.btnhei*2+self.btnhei,width=self.btnwid,height=self.btnhei)
            self.btn8.place(x=self.btnwid*3, y=self.btnhei*3, width=self.btnwid, height=self.btnhei)
            self.btn9.place(x=self.btnwid*4, y=self.btnhei*3, width=self.btnwid, height=self.btnhei)
            self.btnEtr.place(x=self.btnwid*5, y=self.btnhei*3, width=self.btnwid, height=self.btnhei)
            
            self.btn4.place(x=self.btnwid*2, y=self.btnhei*4, width=self.btnwid, height=self.btnhei)
            self.btn5.place(x=self.btnwid*3, y=self.btnhei*4, width=self.btnwid, height=self.btnhei)
            self.btn6.place(x=self.btnwid*4, y=self.btnhei*4, width=self.btnwid, height=self.btnhei)
            self.btnPl.place(x=self.btnwid*5, y=self.btnhei*4, width=self.btnwid, height=self.btnhei)
            
            self.btn1.place(x=self.btnwid*2, y=self.btnhei*5, width=self.btnwid, height=self.btnhei)
            self.btn2.place(x=self.btnwid*3, y=self.btnhei*5, width=self.btnwid, height=self.btnhei)
            self.btn3.place(x=self.btnwid*4, y=self.btnhei*5, width=self.btnwid, height=self.btnhei)
            self.btnMin.place(x=self.btnwid*5, y=self.btnhei*5, width=self.btnwid, height=self.btnhei)
            
            self.btnClr.place(x=self.btnwid*2, y=self.btnhei*6, width=self.btnwid, height=self.btnhei)
            self.btn0.place(x=self.btnwid*3, y=self.btnhei*6, width=self.btnwid, height=self.btnhei)
            self.btnPe.place(x=self.btnwid*4, y=self.btnhei*6, width=self.btnwid, height=self.btnhei)
            self.btnExt.place(x=self.btnwid*5, y=self.btnhei*6, width=self.btnwid, height=self.btnhei)
            
            self.btnFcrl.place(x=0, y=0, width=self.btnwid, height=self.btnhei)
            self.btnSqrt.place(x=self.btnwid, y=0, width=self.btnwid, height=self.btnhei)
            self.btnPct.place(x=self.btnwid, y=self.btnhei*5, width=self.btnwid, height=self.btnhei)
            self.btnCma.place(x=0, y=self.btnhei*5, width=self.btnwid, height=self.btnhei)
            self.btnCil.place(x=0, y=self.btnhei, width=self.btnwid, height=self.btnhei)
            self.btnFlr.place(x=self.btnwid, y=self.btnhei, width=self.btnwid, height=self.btnhei)
            
            self.btnGcd.place(x=0, y=self.btnhei*2, width=self.btnwid, height=self.btnhei)
            self.btnExp.place(x=self.btnwid, y=self.btnhei*2, width=self.btnwid, height=self.btnhei)
            self.btnLog.place(x=0, y=self.btnhei*3, width=self.btnwid, height=self.btnhei)
            self.btnSint.place(x=self.btnwid, y=self.btnhei*3, width=self.btnwid, height=self.btnhei)
            self.btnCost.place(x=0, y=self.btnhei*4, width=self.btnwid, height=self.btnhei)
            self.btnTant.place(x=self.btnwid, y=self.btnhei*4, width=self.btnwid, height=self.btnhei)
            
            self.btnBrckL.place(x=0, y=self.btnhei*6, width=self.btnwid, height=self.btnhei)
            self.btnBrckR.place(x=self.btnwid, y=self.btnhei*6, width=self.btnwid, height=self.btnhei)

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
            if self.langset[-1] == 'US-En': 
                self.btnFn =  ttk.Button(self.main_win, text=f"{self.langset[5]}",style="stdButton2.TButton",command=lambda: self.Fn())         
            elif self.langset[-1] == 'JA-Jp':          
                self.btnFn =   ttk.Button(self.main_win, text=f"{self.langset[5]}",style="stdButton.TButton",command=lambda: self.Fn())
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
            self.btnBksp = ttk.Button(self.main_win,text="←",style="stdButton.TButton", command=lambda: self.btnBackspace())
            self.btnClr =  ttk.Button(self.main_win,text=f"{self.langset[3]}",style="stdButton.TButton",command=lambda: self.btnClear())
            self.btnExt =  ttk.Button(self.main_win,text=f'{self.langset[4]}',style="stdButton.TButton",command=lambda: self.btnExit())
            self.console = ttk.Label(self.main_win,relief="sunken",style="stdLabel.TLabel",anchor=tk.NW,textvariable=self.textoutput)
            self.console.place(x=0,y=0,width=self.btnwid*4,height=self.btnhei*2)
            self.btnFn.place(x=0, y=self.btnhei*2, width=self.btnwid, height=self.btnhei)
            self.btnSl.place(x=self.btnwid, y=self.btnhei*2, width=self.btnwid, height=self.btnhei)
            self.btnAst.place(x=self.btnwid*2, y=self.btnhei*2, width=self.btnwid, height=self.btnhei)
            self.btnBksp.place(x=self.btnwid*3, y=self.btnhei*2, width=self.btnwid, height=self.btnhei)
            
            self.btn7.place(x=0, y=self.btnhei*3, width=self.btnwid, height=self.btnhei)
            self.btn8.place(x=self.btnwid, y=self.btnhei*3, width=self.btnwid, height=self.btnhei)
            self.btn9.place(x=self.btnwid*2, y=self.btnhei*3, width=self.btnwid, height=self.btnhei)
            self.btnEtr.place(x=self.btnwid*3, y=self.btnhei*3, width=self.btnwid, height=self.btnhei)
            
            self.btn4.place(x=0, y=self.btnhei*4, width=self.btnwid, height=self.btnhei)
            self.btn5.place(x=self.btnwid, y=self.btnhei*4, width=self.btnwid, height=self.btnhei)
            self.btn6.place(x=self.btnwid*2, y=self.btnhei*4, width=self.btnwid, height=self.btnhei)
            self.btnPl.place(x=self.btnwid*3, y=self.btnhei*4, width=self.btnwid, height=self.btnhei)
            
            self.btn1.place(x=0, y=self.btnhei*5, width=self.btnwid, height=self.btnhei)
            self.btn2.place(x=self.btnwid, y=self.btnhei*5, width=self.btnwid, height=self.btnhei)
            self.btn3.place(x=self.btnwid*2, y=self.btnhei*5, width=self.btnwid, height=self.btnhei)
            self.btnMin.place(x=self.btnwid*3, y=self.btnhei*5, width=self.btnwid, height=self.btnhei)
            
            self.btnClr.place(x=0, y=self.btnhei*6, width=self.btnwid, height=self.btnhei)
            self.btn0.place(x=self.btnwid, y=self.btnhei*6, width=self.btnwid, height=self.btnhei)
            self.btnPe.place(x=self.btnwid*2, y=self.btnhei*6, width=self.btnwid, height=self.btnhei)
            self.btnExt.place(x=self.btnwid*3, y=self.btnhei*6, width=self.btnwid, height=self.btnhei)
        mli[MLI_FUNC_SCREEN_RESETTER] = 1  # screenresetterが実行されたことを記録
        self.update_mli_state()  # mliの状態を更新
        self.log_mli_transition("screenresetter executed")

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
                self.btnChgwinsize()
            else:
                self.temp += self.keyin2
                self.textReplacer(self.temp)
    def inputreplacer(self,key_input: str) ->str:
        str(key_input)
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
            self.btnExt.config(text= f'{self.langset[4]}',style="stdButton.TButton")
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
                self.btnClr.config(text=f'{self.langset[29]}',style="stdButton3.TButton")
            else:
                self.btnClr.config(text= f'{self.langset[29]}')
            self.btnExt.config(text= f'{self.langset[28]}',style="stdButton2.TButton")
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
    def textReplacer(self,_input):
        self._input = re.sub('Num_Lock|Tab|Control_R|Control_L|Shift_R|Shift_L|ignore','',tw.fill(_input,40))
        self.textoutput.set(f'{_input}')
    def btnAdd(self,_input):
        try: 
            _intinput = int(_input)
        except ValueError:
            if _input == '+'or'-'or'*'or'<'or'>'or'/'or'.'or','or'('or')':
                pass
            else:
                _input = self.inputreplacer(_input)
        if mli[MLI_DISPLAY_CLEAR] == 1:
            self.console.config(anchor=tk.NW)
            mli[MLI_LANGUAGE_SELECTED] += 1
            self.update_mli_state()
            self.log_mli_transition("Added input after display clear")
        elif mli[MLI_DISPLAY_CLEAR] == 1:
            self.temp = str()
            self.textReplacer(self.temp)
            mli[MLI_DISPLAY_CLEAR] = 0
            self.update_mli_state()
            self.log_mli_transition("Cleared display")
        if mli[10] == 0 and mli[MLI_LANGUAGE_IN_PROGRESS] == 1 and _input == '1':
            self.langset = ['消去/出力','消去/\n出力','終了/\nモード切替','消去','終了','切替','階乗','平方根','繰り上げ','繰り下げ','割り算\nの余り','最大\n公約数','eのx乗','yを底とする\nxの対数\n(log(x,y))','関数','絶対値','電卓モード','関数電卓モード','使用するモードを選んでください。\n電卓モード:1 関数電卓モード:2','入力された式は使用できません。もう一度式を入力してください。','が選択されました。','数値が大きすぎます。一回表示を消去してください。','結果の出力先:','デバッグ','EUGC Ver.Dev ','終了確認','終了してもよろしいですか？','確認','モード\n変更','出力','JA-Jp']
            self.textoutput.set('日本語が選択されました。\nEnterキーを押してください。')
            mli[10] = 1
            mli[MLI_LANGUAGE_IN_PROGRESS] = 0
            self.update_mli_state()
            self.log_mli_transition("Japanese language selected")
        elif mli[10] == 0 and mli[MLI_LANGUAGE_IN_PROGRESS] == 1 and _input == '2':
            self.langset = ['Erase/\nExport','Erase/\nExport','Exit/\nSwitch','Erase','Exit','Switch','Factorial','Square\nroot','Carry','Carry\nforward','Remain\nof divid','G.C.D','exp','Logarithm\n(log(x,y))','Function','Absolute\nValue','Calculator Mode','Functions Calculator Mode','Please select the mode that you want to use.\nCalculator Mode:1 \nFunctions Calculator Mode:2',"has selected.","The inputted formula can't be calculated.\nPlease re-input the formula.",'The value is too large.Please erase the display once.','An result was output at:','Debug','EUGC Ver.Dev ','Confirm Exit','Are you sure you want to exit?','Confirm','Switch','Export','US-En']
            self.textoutput.set('English has selected.\nPress Enter to proceed.')
            mli[10] = 1
            mli[MLI_LANGUAGE_IN_PROGRESS] = 0
            self.update_mli_state()
            self.log_mli_transition("English language selected")
        elif  mli[MLI_MODE_SELECTION] == 1 and _input == '1':
            self.console.config(anchor=tk.NW)
            self.temp = str()
            self.textReplacer(self.temp)
            self.title = f'{self.langset[24]+self.langset[16]}'
            self.main_win.title(self.title)
            self.screenresetter(2)
            mli[MLI_MODE_SELECTION] = 0
            mli[MLI_CURRENT_MODE] = 1
            self.update_mli_state()
            self.log_mli_transition("Switched to basic mode")
        elif mli[MLI_MODE_SELECTION] == 1 and _input == '2':
            self.console.config(anchor=tk.NW)
            self.temp = str()
            self.textReplacer(self.temp)
            self.title = f'{self.langset[24]+self.langset[17]}'
            self.main_win.title(self.title)
            self.screenresetter(1)
            mli[MLI_MODE_SELECTION] = 0
            mli[MLI_CURRENT_MODE] = 2
            self.update_mli_state()
            self.log_mli_transition("Switched to advanced mode")
        elif mli[MLI_MODE_SELECTION] == 1 and _input == '3':
            self.temp = f'{self.langset[30]}'
        elif mli[MLI_DISPLAY_CLEARED] == 1:
            self.temp = str()
            self.textReplacer(self.temp)
            mli[MLI_DISPLAY_CLEARED] = 0
            self.update_mli_state()
            self.log_mli_transition("Cleared display")
        else:
            if self.stat == 0:
                self.stat = 1
            else:
                self.console.config(anchor=tk.NW)
                self.temp += _input
                self.textReplacer(self.temp)
        self.show_debug_instructions()  # デバッグ指示を更新
        mli[MLI_FUNC_BTN_ADD] = 1  # btnAddが実行されたことを記録
        self.update_mli_state()  # mliの状態を更新
        self.log_mli_transition("btnAdd executed")

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
        self.textReplacer(self.temp)
    def btnCostfunc(self):
        if self.btnCost.cget('text') == 'cos':
            self.temp += 'self.cos('
        elif self.btnCost.cget('text') == 'arc\ncos':
            self.temp += 'self.acos('
        self.textReplacer(self.temp)
    def btnTantfunc(self): 
        if self.btnTant.cget('text') == 'tan':
            self.temp += 'self.tan('
        elif self.btnTant.cget('text') == 'arc\ntan':
            self.temp += 'self.atan('
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
        if self.btnFcrl.cget('text') == f'{self.langset[6]}':
            self.temp += "self.factorial("
        elif self.btnFcrl.cget('text') == f'{self.langset[15]}':
            self.temp += "self.fabs("
        self.textReplacer(self.temp)
    def btnEnter(self):
        self.console.config(anchor=tk.NW)
        if mli[MLI_LANGUAGE_SELECTED] == 0:
            if mli[10] == 0:
                self.progress_queue.put("__CLOSE__")
                self.textoutput.set('言語を選んでください。\nPlease select a language.\n日本語:1 English:2')
                mli[MLI_LANGUAGE_IN_PROGRESS] = 1
                self.update_mli_state()
                self.log_mli_transition("Prompted language selection")
            elif mli[10] == 1:
                self.textoutput.set(f'{self.langset[18]}')
                self.console.config(anchor=tk.NW)
                mli[MLI_LANGUAGE_SELECTED] = 1
                mli[MLI_MODE_SELECTION] = 1
                self.update_mli_state()
                self.log_mli_transition("Language selected")
        elif mli[MLI_DISPLAY_CLEAR] == 1:
            self.temp = str()
            self.textReplacer(self.temp)
            mli[MLI_DISPLAY_CLEAR] = 0
            self.update_mli_state()
            self.log_mli_transition("Cleared display after Enter")
        elif mli[MLI_CURRENT_MODE] == 0:
            pass
        else:
            try :
                self.temp = str(eval(self.temp))
                self.textReplacer(self.temp)
                self.log_mli_transition("Performed calculation")
            except SyntaxError:
                if mli[MLI_LANGUAGE_SELECTED] == 0 or mli[6] == 1:
                    pass
                    END
                elif f'{self.langset[19]}' or f'{self.langset[16]+self.langset[20]}' or f'{self.langset[17]+self.langset[20]}' in self.temp:
                    self.btnClear()
                else:
                    pass
                    self.temp += f'{self.langset[19]}'
                    self.textReplacer(self.temp)
            except ZeroDivisionError:
                pass
            except OverflowError:
                self.temp = f'{self.langset[21]}'
                self.textReplacer(self.temp)
                self.log_mli_transition("Overflow error during calculation")
        self.show_debug_instructions()  # デバッグ指示を更新
        mli[MLI_FUNC_BTN_ENTER] = 1  # btnEnterが実行されたことを記録
        self.update_mli_state()  # mliの状態を更新
        self.log_mli_transition("btnEnter executed")

    def btnClear(self):
        self.console.config(anchor=tk.NW)
        if self.btnClr.cget('text') == 'Export':
            with open('result.txt', mode = 'a', encoding = 'UTF-8') as f:
                f.write(self.temp)
            self.path = os.path.abspath('result.txt')
            self.temp = f'An result was output at:\n{self.path}'
            self.textReplacer(self.temp)
            mli[MLI_DISPLAY_CLEAR] = 1
            self.update_mli_state()
            self.log_mli_transition("Exported result")
        else:
            self.temp = str()
            self.textReplacer(self.temp)
            self.log_mli_transition("Cleared display")
        self.show_debug_instructions()  # デバッグ指示を更新
        mli[MLI_FUNC_BTN_CLEAR] = 1  # btnClearが実行されたことを記録
        self.update_mli_state()  # mliの状態を更新
        self.log_mli_transition("btnClear executed")

    def btnBackspace(self):
        self.console.config(anchor=tk.NW)
        if self.temp[-15:] == 'math.factorial(':
            self.temp = self.temp[:len(self.temp)-15]
        elif self.temp[-11:] == 'math.floor(':
            self.temp = self.temp[:len(self.temp)-11]
        elif self.temp[-10:] == 'math.sqrt(':
            self.temp = self.temp[:len(self.temp)-10]
        elif self.temp[-10:] == 'math.ceil(':
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
        self.textReplacer(self.temp)
    def btnExit(self):
        if self.btnExt.cget('text') == f'{self.langset[28]}':
            if self.title == f'{self.langset[24]+self.langset[16]}':
                self.title = f'{self.langset[24]+self.langset[17]}'
                self.main_win.title(self.title)
                self.screenresetter(1)
                self.log_mli_transition("Switched to advanced mode")
            elif self.title == f'{self.langset[24]+self.langset[17]}':
                self.title = f'{self.langset[24]+self.langset[16]}'
                self.main_win.title(self.title)
                self.screenresetter(2)
                self.log_mli_transition("Switched to basic mode")
        else:
            Messagebox = tk.messagebox.askquestion(f'{self.langset[24]+self.langset[25]}',f'{self.langset[26]}', icon='warning')
            if Messagebox == 'yes':
                self.main_win.destroy()
                self.log_mli_transition("Exited application")
            else:
                self.log_mli_transition("Exit canceled")
        self.show_debug_instructions()  # デバッグ指示を更新
        mli[MLI_FUNC_BTN_EXIT] = 1  # btnExitが実行されたことを記録
        self.update_mli_state()  # mliの状態を更新
        self.log_mli_transition("btnExit executed")

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
            self.btnressel = tk.Button(self.sub_win,text=f'{self.langset[27]}',style='stdButton.TButton')
            self.resinput.pack()
            self.subwin.mainloop()
    def log_mli_transition(self, action_description):
        """mliの遷移ログを記録"""
        log_entry = f"Action: {action_description}\n"
        log_entry += "mli state:\n"
        for i, value in enumerate(mli):
            description = self.mli_descriptions[i] if i < len(self.mli_descriptions) else "No description available"
            log_entry += f"  {i}: {value} ({description})\n"
        log_entry += "-" * 40 + "\n"
        with open("mli_transition_log.txt", "a", encoding="utf-8") as log_file:
            log_file.write(log_entry)

    def show_debug_instructions(self):
        """現在のmliの状態に基づいて次に実行すべき操作を表示"""
        instructions = "Next action:\n"
        if mli[MLI_LANGUAGE_SELECTED] == 0:
            instructions += "- Select a language (1: Japanese, 2: English).\n"
        elif mli[MLI_MODE_SELECTION] == 1:
            instructions += "- Select a mode (1: Basic, 2: Advanced).\n"
        elif mli[MLI_DISPLAY_CLEAR] == 1:
            instructions += "- Clear the display or perform a calculation.\n"
        elif mli[MLI_FUNC_SCREEN_RESETTER] == 0:
            instructions += "- Execute screenresetter function.\n"
        elif mli[MLI_FUNC_BTN_ADD] == 0:
            instructions += "- Execute btnAdd function.\n"
        elif mli[MLI_FUNC_BTN_ENTER] == 0:
            instructions += "- Execute btnEnter function.\n"
        elif mli[MLI_FUNC_BTN_CLEAR] == 0:
            instructions += "- Execute btnClear function.\n"
        elif mli[MLI_FUNC_BTN_EXIT] == 0:
            instructions += "- Execute btnExit function.\n"
        else:
            instructions += "- Continue using the calculator or exit the application.\n"

        # デバッグ用ウィンドウに表示
        if self.debug_window is None or not self.debug_window.winfo_exists():
            self.debug_window = tk.Toplevel(self.main_win)
            self.debug_window.title("Debug Instructions")
            self.debug_window.geometry("400x200")
            self.debug_text = tk.Text(self.debug_window, wrap=tk.WORD)
            self.debug_text.pack(expand=True, fill=tk.BOTH)
        self.debug_text.config(state=tk.NORMAL)
        self.debug_text.delete(1.0, tk.END)
        self.debug_text.insert(tk.END, instructions)
        self.debug_text.config(state=tk.DISABLED)

class ProgressWindow:
    """進捗状況を表示するウィンドウ"""
    def __init__(self, queue):
        self.queue = queue
        self.root = tk.Tk()
        self.root.title("Startup Progress")
        self.root.geometry("400x200")
        self.progress_label = tk.Label(self.root, text="Initializing...", font=("Arial", 14))
        self.progress_label.pack(expand=True, fill=tk.BOTH)
        self.root.protocol("WM_DELETE_WINDOW", self.disable_close)  # 閉じるボタンを無効化
        self.update_progress()

    def update_progress(self):
        """キューから進捗メッセージを取得して表示"""
        try:
            while not self.queue.empty():
                message = self.queue.get_nowait()
                if message == "__CLOSE__":
                    self.close()
                    return  # 閉じた後に再スケジュールしないように抜ける
                self.progress_label.config(text=message)
        except Exception:
            pass
        self.root.after(100, self.update_progress)

    def close(self):
        """ウィンドウを閉じる"""
        self.root.destroy()

    def disable_close(self):
        """閉じるボタンを無効化"""
        pass

def start_progress_window(queue):
    """進捗ウィンドウを別プロセスで起動"""
    progress_window = ProgressWindow(queue)
    progress_window.root.mainloop()


class main_win(func):
    def __init__(self):
        # 進捗表示用のキューとプロセスを作成
        self.progress_queue = multiprocessing.Queue()
        self.progress_process = multiprocessing.Process(target=start_progress_window, args=(self.progress_queue,))
        self.progress_process.start()
        self.progress_queue.put("Initializing main window...")
        # メインウィンドウの初期化
        self.main_win = tk.Tk()
        self.style = ttk.Style()
        self.style.configure("stdButton.TButton", font=('Meiryo', 20))
        self.style.configure("stdButton2.TButton", font=('Meiryo', 15))
        self.style.configure("stdButton3.TButton", font=('Meiryo', 12))
        self.style.configure("stdButton4.TButton", font=('Meiryo', 10))
        self.style.configure("stdLabel.TLabel", font=('Meiryo', 12))
        self.main_win.resizable(0, 0)
        self.main_win.title('EUGC Ver.Dev')
        self.scrwid = self.main_win.winfo_screenwidth()
        self.scrhei = self.main_win.winfo_screenheight()
        self.winwid = 360
        self.winhei = 630
        self.fulwinwid = self.scrwid
        self.fulwinhei = self.scrhei
        self.fulbtnwid = int(self.fulwinwid/4)
        self.fulbtnhei = int(self.fulwinhei/7)

        self.btnwid = int(self.winwid / 4)
        self.btnhei = int(self.winhei / 7)
        self.winsize = f'{self.winwid}x{self.winhei}+{int((self.scrwid - self.winwid) / 2)}+{int((self.scrhei - self.winhei) / 2)}'
        self.main_win.geometry(self.winsize)
        self.main_win.bind("<KeyPress>", self.kbd_input)

        # 進捗状況を更新
        self.progress_queue.put("Initializing variables...")
        #time.sleep(0.5)  # シミュレーション用の遅延

        # mliの初期化
        mli[MLI_INITIALIZED] = 0
        self.textoutput = tk.StringVar()
        mli[MLI_LANGUAGE_SELECTED] = 0
        self.temp = str()
        mli[MLI_DISPLAY_CLEAR] = 0

        # 進捗状況を更新
        self.progress_queue.put("Creating buttons...")
        #time.sleep(0.5)  # シミュレーション用の遅延

        # ボタンの作成
        self.btn0 = ttk.Button(self.main_win, text="0", style="stdButton.TButton")
        self.btn1 = ttk.Button(self.main_win, text="1", style="stdButton.TButton", command=lambda: self.btnAdd('1'))
        self.btn2 = ttk.Button(self.main_win, text="2", style="stdButton.TButton", command=lambda: self.btnAdd('2'))
        self.btn3 = ttk.Button(self.main_win, text="3", style="stdButton.TButton", command=lambda: self.btnAdd('3'))
        self.btn4 = ttk.Button(self.main_win, text="4", style="stdButton.TButton", command=lambda: self.btnAdd('4'))
        self.btn5 = ttk.Button(self.main_win, text="5", style="stdButton.TButton", command=lambda: self.btnAdd('5'))
        self.btn6 = ttk.Button(self.main_win, text="6", style="stdButton.TButton", command=lambda: self.btnAdd('6'))
        self.btn7 = ttk.Button(self.main_win, text="7", style="stdButton.TButton", command=lambda: self.btnAdd('7'))
        self.btn8 = ttk.Button(self.main_win, text="8", style="stdButton.TButton", command=lambda: self.btnAdd('8'))
        self.btn9 = ttk.Button(self.main_win, text="9", style="stdButton.TButton", command=lambda: self.btnAdd('9'))
        self.btnPe = ttk.Button(self.main_win, text=".", style="stdButton.TButton", command=lambda: self.btnAdd('.'))
        self.btnPl = ttk.Button(self.main_win, text="+", style="stdButton.TButton", command=lambda: self.btnAdd('+'))
        self.btnMin = ttk.Button(self.main_win, text="-", style="stdButton.TButton", command=lambda: self.btnAdd('-'))
        self.btnAst = ttk.Button(self.main_win, text="x", style="stdButton.TButton", command=lambda: self.btnAdd('*'))
        self.btnSl = ttk.Button(self.main_win, text="÷", style="stdButton.TButton", command=lambda: self.btnAdd('/'))
        self.btnEtr = ttk.Button(self.main_win, text="Enter", style="stdButton.TButton", command=lambda: self.btnEnter())
        self.btnFn = ttk.Button(self.main_win, text=f"切替", style="stdButton.TButton")
        self.btnBksp = ttk.Button(self.main_win, text="←", style="stdButton.TButton", command=lambda: self.btnBackspace())
        self.btnClr = ttk.Button(self.main_win, text=f"消去/\n出力", style="stdButton2.TButton", command=lambda: self.btnClear())
        self.btnExt = ttk.Button(self.main_win, text=f'終了/\nモード切替', style="stdButton3.TButton", command=lambda: self.btnExit())

        # 進捗状況を更新
        self.progress_queue.put("Creating Console...")
        #time.sleep(0.5)  # シミュレーション用の遅延

        # コンソールの作成
        self.console = ttk.Label(self.main_win, relief="sunken", style="stdLabel.TLabel", anchor=tk.NW, textvariable=self.textoutput)
        self.console.place(x=0, y=0, width=self.btnwid * 4, height=self.btnhei * 2)
        self.btnFn.place(x=0, y=self.btnhei * 2, width=self.btnwid, height=self.btnhei)
        self.btnSl.place(x=self.btnwid, y=self.btnhei * 2, width=self.btnwid, height=self.btnhei)
        self.btnAst.place(x=self.btnwid * 2, y=self.btnhei * 2, width=self.btnwid, height=self.btnhei)
        self.btnBksp.place(x=self.btnwid * 3, y=self.btnhei * 2, width=self.btnwid, height=self.btnhei)
        self.btn7.place(x=0, y=self.btnhei * 3, width=self.btnwid, height=self.btnhei)
        self.btn8.place(x=self.btnwid, y=self.btnhei * 3, width=self.btnwid, height=self.btnhei)
        self.btn9.place(x=self.btnwid * 2, y=self.btnhei * 3, width=self.btnwid, height=self.btnhei)
        self.btnEtr.place(x=self.btnwid * 3, y=self.btnhei * 3, width=self.btnwid, height=self.btnhei)
        self.btn4.place(x=0, y=self.btnhei * 4, width=self.btnwid, height=self.btnhei)
        self.btn5.place(x=self.btnwid, y=self.btnhei * 4, width=self.btnwid, height=self.btnhei)
        self.btn6.place(x=self.btnwid * 2, y=self.btnhei * 4, width=self.btnwid, height=self.btnhei)
        self.btnPl.place(x=self.btnwid * 3, y=self.btnhei * 4, width=self.btnwid, height=self.btnhei)
        self.btn1.place(x=0, y=self.btnhei * 5, width=self.btnwid, height=self.btnhei)
        self.btn2.place(x=self.btnwid, y=self.btnhei * 5, width=self.btnwid, height=self.btnhei)
        self.btn3.place(x=self.btnwid * 2, y=self.btnhei * 5, width=self.btnwid, height=self.btnhei)
        self.btnMin.place(x=self.btnwid * 3, y=self.btnhei * 5, width=self.btnwid, height=self.btnhei)
        self.btnClr.place(x=0, y=self.btnhei * 6, width=self.btnwid, height=self.btnhei)
        self.btn0.place(x=self.btnwid, y=self.btnhei * 6, width=self.btnwid, height=self.btnhei)
        self.btnPe.place(x=self.btnwid * 2, y=self.btnhei * 6, width=self.btnwid, height=self.btnhei)
        self.btnExt.place(x=self.btnwid * 3, y=self.btnhei * 6, width=self.btnwid, height=self.btnhei)

        # 進捗状況を更新
        self.progress_queue.put("Initializing Complete!")
        self.progress_queue.put("Finalizing...")

        # メインウィンドウの起動
        self.console.config(anchor=tk.N)
        self.textoutput.set('Calculator GUI Version Dev\n Dr.GLaDOS🄬 2022\n\nEnterキーを押して下さい...\nPress Enter key to continue...')
        self.stat = 0
        self.mli_descriptions = [
            "0: Placeholder for future use",
            "1: Tracks whether the language selection is complete",
            "2: Tracks whether the display needs to be cleared",
            "3: Tracks the current mode selection state",
            "4: Tracks whether the display was cleared",
            "5: Placeholder for future use",
            "6: Placeholder for future use",
            "7: Tracks initialization state",
            "8: Tracks the current calculator mode (1: Basic, 2: Advanced)",
            "9: Placeholder for future use",
            "10: Tracks whether a language is selected",
            "11: Tracks whether language selection is in progress",
            "12: Tracks whether screenresetter function is executed",
            "13: Tracks whether btnAdd function is executed",
            "14: Tracks whether btnEnter function is executed",
            "15: Tracks whether btnClear function is executed",
            "16: Tracks whether btnExit function is executed"
        ]
        self.mli_window = None  # ウィンドウの参照を保持
        self.show_mli_state()  # 起動直後にmliの状態を表示するウィンドウを呼び出す
        self.debug_window = None  # デバッグ指示ウィンドウの参照を保持
        self.show_debug_instructions()  # 起動時にデバッグ指示を表示
        self.log_mli_transition("Application started")
        mli[MLI_FUNC_SCREEN_RESETTER] = 0  # screenresetter未実行
        mli[MLI_FUNC_BTN_ADD] = 0  # btnAdd未実行
        mli[MLI_FUNC_BTN_ENTER] = 0  # btnEnter未実行
        mli[MLI_FUNC_BTN_CLEAR] = 0  # btnClear未実行
        mli[MLI_FUNC_BTN_EXIT] = 0  # btnExit未実行
        self.progress_queue.put("Starting main loop...")
        self.main_win.mainloop()

    def show_mli_state(self):
        """mliの状態を表示するウィンドウを作成または更新"""
        if self.mli_window is None or not self.mli_window.winfo_exists():
            self.mli_window = tk.Toplevel(self.main_win)
            self.mli_window.title("mli State")
            self.mli_window.geometry("400x300")
            self.mli_text = tk.Text(self.mli_window, wrap=tk.WORD)
            self.mli_text.pack(expand=True, fill=tk.BOTH)
        self.update_mli_state()

    def update_mli_state(self):
        """mliの状態をウィンドウに反映"""
        if self.mli_window and self.mli_window.winfo_exists():
            self.mli_text.config(state=tk.NORMAL)
            self.mli_text.delete(1.0, tk.END)
            self.mli_text.insert(tk.END, "mli state:\n")
            for i, value in enumerate(mli):
                description = self.mli_descriptions[i] if i < len(self.mli_descriptions) else "No description available"
                self.mli_text.insert(tk.END, f"{i}: {value} ({description})\n")
            self.mli_text.config(state=tk.DISABLED)
if __name__ == "__main__":
    # プロセスを開始して進捗ウィンドウを表示
#    queue = multiprocessing.Queue()
#    progress_process = multiprocessing.Process(target=start_progress_window, args=(queue,))
#    progress_process.start()

    # メインウィンドウを起動
    main_win()