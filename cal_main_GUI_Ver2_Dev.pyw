import tkinter as tk
from tkinter import StringVar, ttk
import os
import textwrap as tw
import multiprocessing as ml
from mgmtlist import mlist as mli
mli[0] = 0
class Keypad:
    def __init__(self):
        self.main_win = tk.Tk()
        self.main_win.resizable(0,0)
        self.main_win.title('Calculator Ver.Dev')
        self.scrwid = self.main_win.winfo_screenwidth()
        self.scrhei = self.main_win.winfo_screenheight()
        self.winwid = 330
        self.winhei = 560
        self.winsize = f'330x560+{int((self.scrwid-self.winwid)/2)}+{int((self.scrhei-self.winhei)/2)}'
        self.main_win.geometry(self.winsize)
        self.main_frm = ttk.Frame(self.main_win)
        self.textoutput = tk.StringVar()
        mli[1] = 0
        self.temp = str()
        mli[2] = 0
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
        self.btnEtr =  tk.Button(self.main_frm, text="Enter", height=4, width=10,command=lambda: self.btnEnter())
        self.btnFn =   tk.Button(self.main_frm, text="Fn", height=4, width=10, command=lambda: self.Fn())
        self.btnBksp = tk.Button(self.main_frm,text="Bksp",height=4,width=10, command=lambda: self.btnBackspace())
        self.btnClr =  tk.Button(self.main_frm,text="Clear/\nExport",height=4,width=10,command=lambda: self.btnClear())
        self.btnExt = tk.Button(self.main_frm,text='Exit',height=4,width=10,command=lambda: self.btnExit())
        self.console = tk.Label(self.main_frm,height=9,width=38,borderwidth=3,relief="sunken",font=('Meiryo',10),anchor=tk.NW,textvariable=self.textoutput)
        self.console.grid(column=0,row=0,columnspan=4,rowspan=2)
        self.btnFn.grid(column=0,row=2)
        self.btnSl.grid(column=1,row=2)
        self.btnAst.grid(column=2,row=2)
        self.btnMin.grid(column=3,row=5)
        self.btn7.grid(column=0,row=3)
        self.btn8.grid(column=1,row=3)
        self.btn9.grid(column=2,row=3)
        self.btnPl.grid(column=3,row=4)
        self.btn4.grid(column=0,row=4)
        self.btn5.grid(column=1,row=4)
        self.btn6.grid(column=2,row=4)
        self.btnEtr.grid(column=3,row=3)
        self.btn1.grid(column=0,row=5)
        self.btn2.grid(column=1,row=5)
        self.btn3.grid(column=2,row=5)
        self.btnPe.grid(column=2,row=6)
        self.btn0.grid(column=1,row=6)
        self.btnClr.grid(column=0,row=6)
        self.btnBksp.grid(column=3,row=2)
        self.btnExt.grid(column=3,row=6)
        self.console.config(anchor=tk.N)
        self.textoutput.set('Calculator GUI Version 1.0\n Dr.GLaDOS🄬 2022\n\n何かキーを押して下さい...\nPress any key to continue...')
        self.main = self.main_win.mainloop()
    def Fn(self):
        if self.btnFn.config('relief')[-1] == 'sunken':
            self.btnFn.config(relief="raised")
            #self.btn2.config(text= '2')
            #self.btn4.config(text= '4')
            #self.btn6.config(text= '6')
            #self.btn8.config(text= '8')
            self.btnClr.config(text= 'Clear')
        else:
            self.btnFn.config(relief="sunken")
            #self.btn2.config(text='↓')
            #self.btn4.config(text= '←')
            #self.btn6.config(text= '→')
            #self.btn8.config(text= '↑')
            self.btnClr.config(text= 'Export')
    def textReplacer(self,_input):
        _input = tw.fill(_input,40)
        self.textoutput.set(f'{_input}')
    def btnAdd(self,_input):
        self.console.config(anchor=tk.NW)
        #if mli[1] == 0:
        #    self.textoutput.set('言語を選択してください。\nPlease select a Language.\n日本語:1\nEnglish:2')
        #    self.console.config(anchor=tk.NW)
        #    mli[1] += 1
        if mli[2] == 1:
            self.temp = str()
            self.textReplacer(self.temp)
            mli[2] = 0
        else:
            self.temp += _input
            self.textReplacer(self.temp)
    def btnEnter(self):
        self.console.config(anchor=tk.NW)
        #if mli[1] == 0:
        #    self.textoutput.set('言語を選択してください。\nPlease select a Language.\n日本語:1\nEnglish:2')
        #    self.console.config(anchor=tk.NW)
        #    mli[1] += 1
        if mli[2] == 1:
            self.temp = str()
            self.textReplacer(self.temp)
            mli[2] = 0
        else:
            try :
                self.temp = str(eval(self.temp))
            except SyntaxError:
                pass
                self.temp += '入力された式は使用できません。もう一度式を入力してください。'
                self.textReplacer(self.temp)
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
        self.temp = self.temp[:-1]
        self.textReplacer(self.temp)
    def btnExit(self):
        self.exit_win = tk.Toplevel()
        self.exit_win.resizable(0,0)
        self.scrwid = self.exit_win.winfo_screenwidth()
        self.scrhei = self.exit_win.winfo_screenheight()
        self.winwid = 150
        self.winhei = 100
        self.winsize = f'150x100+{int((self.scrwid-self.winwid)/2)}+{int((self.scrhei-self.winhei)/2)}'
        #print(self.winsize)
        self.exit_win.geometry(self.winsize)
        self.exit_win.title("終了確認")
        self.exit_win.grab_set()
        self.exit_win.focus_set()
        self.exit_win.transient(self.main_win)
        self.exit_label =tk.Label(self.exit_win,text="終了しますか？")
        self.confirm_btn = tk.Button(self.exit_win,text="はい",command=lambda: self.exit_win.quit())
        self.deny_btn = tk.Button(self.exit_win,text="いいえ",command=lambda: self.exit_win.destroy())
        self.exit_label.pack()
        self.confirm_btn.pack()
        self.deny_btn.pack()
exit_win = None
def sub_window():
    sub_win = tk.Tk()
    sub_win.title('Calculator Ver.Dev')
    sub_win.geometry('150x50')
    textoutput2 = tk.StringVar()
    sub_win_msg = tk.Label(sub_win,font=('Meiryo',10),textvariable=textoutput2)
    sub_win_msg.grid(column=0,row=0)
    main = sub_win.mainloop()
if __name__ == '__main__':
    mwin = ml.Process(target=Keypad)
    swin = ml.Process(target=sub_window,daemon=True)
    mwin.start()
    swin.start()
if mli[0] == 1:
    swin.kill()
mli[0] = 1