import tkinter as tk
from tkinter import ttk
import platform as pf
class Keypad:
    def __init__(self):
        self.main_win = tk.Tk()
        self.main_win.title('Calculator GUI Lite')
        self.main_win.geometry('330x560')
        self.main_frm = ttk.Frame(self.main_win)
        self.textoutput = tk.StringVar()
        self.textoutput.set('Calculator GUI Lite Version 1.0\n  Dr.GLaDOS🄬 2022')
        self.temp = str()
        self.outputbkup = 'Calculator GUI Lite Version 1.0\n  Dr.GLaDOS🄬 2022'
        self.main_frm.grid(column=0, row=0, sticky=tk.NSEW, padx=5, pady=10)
        self.btn0 =    tk.Button(self.main_frm, text="0", height=4, width=10,command=lambda: self.btnAdd('0'))
        self.btn1 =    tk.Button(self.main_frm, text="1", height=4, width=10,command=lambda: self.btnAdd('1'))
        self.btn2 =    tk.Button(self.main_frm, text="2", height=4, width=10,command=lambda: self.btnAdd('2'))
        self.btn3 =    tk.Button(self.main_frm, text="3", height=4, width=10,command=lambda: self.btnAdd('3'))
        self.btn4 =    tk.Button(self.main_frm, text="4", height=4, width=10,command=lambda: self.btnAdd('4'))
        self.btn5 =    tk.Button(self.main_frm, text="5", height=4, width=10,command=lambda: self.btnAdd('5'))
        self.btn6 =    tk.Button(self.main_frm, text="6", height=4, width=10,command=lambda: self.btnAdd('6'))
        self.btn7 =    tk.Button(self.main_frm, text="7", height=4, width=10,command=lambda: self.btnAdd('7'))
        self.btn8 =    tk.Button(self.main_frm, text="8", height=4, width=10,command=lambda: self.btnAdd('8'))
        self.btn9 =    tk.Button(self.main_frm, text="9", height=4, width=10,command=lambda: self.btnAdd('9'))
        self.btnPe =   tk.Button(self.main_frm, text=".", height=4, width=10,command=lambda: self.btnAdd('.'))
        self.btnPl =   tk.Button(self.main_frm, text="+", height=4, width=10,command=lambda: self.btnAdd('+'))
        self.btnMin =  tk.Button(self.main_frm, text="-", height=4, width=10,command=lambda: self.btnAdd('-'))
        self.btnAst =  tk.Button(self.main_frm, text="*", height=4, width=10,command=lambda: self.btnAdd('*'))
        self.btnSl =   tk.Button(self.main_frm, text="/", height=4, width=10,command=lambda: self.btnAdd('/'))
        self.btnEtr =  tk.Button(self.main_frm, text="Enter", height=9, width=10,command=lambda: self.btnEnter())
        self.btnFn =   tk.Button(self.main_frm, text="Fn", height=4, width=10, command=lambda: self.Fn())
        self.btnBksp = tk.Button(self.main_frm,text="Bksp",height=4,width=10, command=lambda: self.btnBackspace())
        self.btnClr =  tk.Button(self.main_frm,text="Clear",height=4,width=10,command=lambda: self.btnClear())
        self.console = tk.Label(self.main_frm,height=9,width=38,borderwidth=3,relief="sunken",font=('Meiryo',10),anchor=tk.NW,textvariable=self.textoutput)
        self.console.grid(column=0,row=0,columnspan=4,rowspan=2)
        self.btnFn.grid(column=0,row=2)
        self.btnSl.grid(column=1,row=2)
        self.btnAst.grid(column=2,row=2)
        self.btnMin.grid(column=3,row=3)
        self.btn7.grid(column=0,row=3)
        self.btn8.grid(column=1,row=3)
        self.btn9.grid(column=2,row=3)
        self.btnPl.grid(column=3,row=4)
        self.btn4.grid(column=0,row=4)
        self.btn5.grid(column=1,row=4)
        self.btn6.grid(column=2,row=4)
        self.btnEtr.grid(column=3,row=5,rowspan=2)
        self.btn1.grid(column=0,row=5)
        self.btn2.grid(column=1,row=5)
        self.btn3.grid(column=2,row=5)
        self.btnPe.grid(column=2,row=6)
        self.btn0.grid(column=1,row=6)
        self.btnClr.grid(column=0,row=6)
        self.btnBksp.grid(column=3,row=2)
        self.main = self.main_win.mainloop()
    def Fn(self):
        if self.btnFn.config('relief')[-1] == 'sunken':
            self.btnFn.config(relief="raised")
            #self.btn2.config(text= '2')
            #self.btn4.config(text= '4')
            #self.btn6.config(text= '6')
            #self.btn8.config(text= '8')
        else:
            self.btnFn.config(relief="sunken")
            #self.btn2.config(text='↓')
            #self.btn4.config(text= '←')
            #self.btn6.config(text= '→')
            #self.btn8.config(text= '↑')
    def textReplacer(self,test):
        self.textoutput.set(f'{test}')
    def btnAdd(self,_input):
        self.temp += _input
        self.outputbkup += self.temp
        self.textReplacer(self.temp)
    def btnEnter(self):
        try :
            self.outputbkup = self.temp = str(eval(self.temp))
        except SyntaxError:
            pass
        self.textReplacer(self.temp)
    def btnClear(self):
        self.temp = str()
        self.textReplacer(self.temp)
    def btnBackspace(self):
        self.temp = self.temp[:-1]
        self.textReplacer(self.temp)
app = Keypad()
