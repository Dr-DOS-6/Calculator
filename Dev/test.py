import tkinter as tk
from tkinter import ttk 
import re
import textwrap as tw
global textoutput
global elmwid
global elmhei
class methods():
    elements_common = [
        ["scrn","none","none","none"],
        ["none","none","none","none"],
        ["func","divd","mltp","bksp"],
        ["7","8","9","Entr"],
        ["4","5","6","addt"],
        ["1","2","3","subt"],
        ["clr","0","prid","swch"]
    ]
    elements_advanced = [
        ["exp","root","fctr","expn"],
        ["flor","ceil","rond","trnc"],
        ["gcd","lcm","pfac","mod"],
        ["logn","loge","log10","log2"],
        ["sin","cos","tan","deg"],
        ["asin","acos","atan","rad"],
        ["coma","brkl","brkr","setg"]
    ]
    elements_settingwindow = [
    ["jp_btn", "en_btn"]
]
    test = ["test"]
    kbd_dict = {
        "period":".",
        "comma":",",
        "less":"<",
        "greater":">", 
        "slash":"/",
        "exclam":"!",
        "root":"√",
        "percent":"%",
        "asciicircum":"^",
        "asterisk":"*",
        "parenleft":"(",
        "parenright":")",
        "minus":"-",
        "plus":"+",
        "equal":"=",
        "Return":"Return",
        "BackSpace":"BackSpace",
        "Escape":"Escape",
        "Shift_R":"Shift_R",
        "Shift_L":"Shift_L",
        "Control_R":"Control_R",
        "Control_L":"Control_L",
        "Tab":"Tab",
        "NumLock":"NumLock",
        "*":"+",
        "-":"-",
        "*":"*",
        "<":"<",
        ">":">",
        "/":"/",
        ".":".",
        ",":",",
        "(":"(",
        ")":")",
        "ignore":"ignore"
    }
    def kbd_input(self,keyin1):
        try:
            self.keyin2i = int(keyin1.keysym)
            self.btnAdd(str(self.keyin2i))
        except:
            self.keyin2 = self.kbd_dict[keyin1.keysym]
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
                self.textReplacer(self.temp)
    def textReplacer(self,_input):
        self._input = re.sub('Num_Lock|Tab|Control_R|Control_L|Shift_R|Shift_L|ignore','',tw.fill(_input,40))
        self.textoutput.set(f'{_input}')
    locales =locales = {
    0: {
        "clr_default": '消去/\n出力',
        "swch": '終了/\nモード切替',
        "clr_clr": '消去',
        "swch_exit": '終了',
        "func": '切替',
        "fctr": '階乗',
        "root": '平方根',
        "ceil": '繰り上げ',
        "flor": '繰り下げ',
        "mod": '割り算\nの余り',
        "gcd": '最大\n公約数',
        "exp": 'eのx乗',
        "logn": 'yを底とする\nxの対数\n(log(x,y))',
        "setg": '関数',
        "abs": '絶対値',
        "mode_calc": '電卓モード',
        "mode_adv": '多機能電卓モード',
        "selectmode": '使用するモードを選んでください。\n電卓モード:1 多機能電卓モード:2',
        "inputerr": '入力された式は使用できません。もう一度式を入力してください。',
        "overflow": '数値が大きすぎます。一回表示を消去してください。',
        "outputdest": '結果の出力先:',
        "debug": 'デバッグ',
        "version": 'EUGC Ver1.2 ',
        "exitconfirm": '終了確認',
        "exitprompt": '終了してもよろしいですか？',
        "confirm": '確認',
        "mode_change": 'モード\n変更',
        "export": '出力'
    },
    1: {
        "clr_default": 'Erase/\nExport',
        "swch": 'Exit/\nSwitch',
        "clr_clr": 'Erase',
        "swch_exit": 'Exit',
        "func": 'Switch',
        "fctr": 'Factorial',
        "root": 'Square\nroot',
        "ceil": 'Ceil',
        "flor": 'Floor',
        "mod": 'Modulus',
        "gcd": 'G.C.D',
        "exp": 'exp',
        "logn": 'Logarithm\n(log(x,y))',
        "setg": 'Function',
        "abs": 'Absolute\nValue',
        "mode_calc": 'Calculator Mode',
        "mode_adv": 'Multifunction Calculator Mode',
        "selectmode": 'Please select the mode that you want to use.\nCalculator Mode:1 \nMultifunction Calculator Mode:2',
        "inputerr": "The inputted formula can't be calculated.\nPlease re-input the formula.",
        "overflow": 'The value is too large.\nPlease erase the display once.',
        "outputdest": 'An result was output at:',
        "debug": 'Debug',
        "version": 'EUGC Ver1.2 ',
        "exitconfirm": 'Confirm Exit',
        "exitprompt": 'Are you sure you want to exit?',
        "confirm": 'Confirm',
        "mode_change": 'Mode\nSwitch',
        "export": 'Export'
    }
}
    def switch_mode(self):
        self.advanced = not getattr(self, "advanced", False)  # True ⇔ False
        self.root.destroy()
        main(self.lang, self.advanced)
    def bksp(self):
        None
    def btnAdd(self,_input):
        self.buffer += _input
        self.textReplacer(self.buffer)
    def elements_definition(self,elmwid,elmhei,used_keys=None): 
        full_def = {
        "jp_btn": ["Button", {"text": "日本語", "style": "stdBtn.TButton", "command": lambda: self.select_lang(0)}, {"relwidth": 0.5, "relheight": 1}],
        "en_btn": ["Button", {"text": "English", "style": "stdBtn.TButton", "command": lambda: self.select_lang(1)}, {"relwidth": 0.5, "relheight": 1}],
        "test": ["Button",{"text":"test","style":"stdBtn.TButton","command": lambda: self.btnAdd("test")},{"relwidth":elmwid,"relheight":elmhei}],
        "scrn": ["Label",{"relief":"sunken","style":"stdLbl.TLabel","anchor":tk.NW,"textvariable":self.textoutput},{"relwidth":elmwid*4,"relheight":elmhei*2}],
        "none": ["Blank",{},{}],
        "0":    ["Button",{"text":"0","style":"stdBtn.TButton","command": lambda: self.btnAdd('0')},{"relwidth":elmwid,"relheight":elmhei}],
        "1":    ["Button",{"text":"1","style":"stdBtn.TButton","command": lambda: self.btnAdd('1')},{"relwidth":elmwid,"relheight":elmhei}],
        "2":    ["Button",{"text":"2","style":"stdBtn.TButton","command": lambda: self.btnAdd('2')},{"relwidth":elmwid,"relheight":elmhei}],
        "3":    ["Button",{"text":"3","style":"stdBtn.TButton","command": lambda: self.btnAdd('3')},{"relwidth":elmwid,"relheight":elmhei}],
        "4":    ["Button",{"text":"4","style":"stdBtn.TButton","command": lambda: self.btnAdd('4')},{"relwidth":elmwid,"relheight":elmhei}],
        "5":    ["Button",{"text":"5","style":"stdBtn.TButton","command": lambda: self.btnAdd('5')},{"relwidth":elmwid,"relheight":elmhei}],
        "6":    ["Button",{"text":"6","style":"stdBtn.TButton","command": lambda: self.btnAdd('6')},{"relwidth":elmwid,"relheight":elmhei}],
        "7":    ["Button",{"text":"7","style":"stdBtn.TButton","command": lambda: self.btnAdd('7')},{"relwidth":elmwid,"relheight":elmhei}],
        "8":    ["Button",{"text":"8","style":"stdBtn.TButton","command": lambda: self.btnAdd('8')},{"relwidth":elmwid,"relheight":elmhei}],
        "9":    ["Button",{"text":"9","style":"stdBtn.TButton","command": lambda: self.btnAdd('9')},{"relwidth":elmwid,"relheight":elmhei}],
        "func": ["Button",{"text": self.locales[self.lang]["func"],"style": "stdBtn.TButton","command": self.switch_mode},{"relwidth": elmwid, "relheight": elmhei}],
        "divd": ["Button",{"text": "÷","style":"stdBtn.TButton","command": lambda: self.btnAdd("/")},{"relwidth":elmwid,"relheight":elmhei}],
        "mltp": ["Button",{"text":"×","style":"stdBtn.TButton","command": lambda: self.btnAdd("*")},{"relwidth":elmwid,"relheight":elmhei}],
        "addt": ["Button",{"text":"+","style":"stdBtn.TButton","command": lambda: self.btnAdd("+")},{"relwidth":elmwid,"relheight":elmhei}],
        "bksp": ["Button",{"text":"←","style":"stdBtn.TButton","command": self.bksp},{"relwidth":elmwid,"relheight":elmhei}],
        "Entr": ["Button",{"text":"Enter","style":"stdBtn.TButton","command": lambda: self.btnEnter()},{"relwidth":elmwid,"relheight":elmhei}],
        "subt": ["Button",{"text":"-","style":"stdBtn.TButton","command": lambda: self.btnAdd("-")},{"relwidth":elmwid,"relheight":elmhei}],
        "clr":  ["Button",{"text": self.locales[self.lang]["clr_default"],"style":"stdBtn.TButton","command": lambda: self.btnClear()},{"relwidth":elmwid,"relheight":elmhei}],
        "prid": ["Button",{"text":".","style":"stdBtn.TButton","command": lambda: self.btnAdd(".")},{"relwidth":elmwid,"relheight":elmhei}],
        "swch": ["Button",{"text": self.locales[self.lang]["swch"],"style":"stdBtn.TButton","command": lambda: self.btnSwitch()},{"relwidth":elmwid,"relheight":elmhei}],
        "exp":  ["Button",{"text":"exp","style":"stdBtn.TButton","command": lambda: self.btnAdd("exp")},{"relwidth":elmwid,"relheight":elmhei}],
        "root": ["Button",{"text": self.locales[self.lang]["root"],"style":"stdBtn.TButton","command": lambda: self.btnAdd("√")},{"relwidth":elmwid,"relheight":elmhei}],
        "fctr": ["Button",{"text": self.locales[self.lang]["fctr"],"style":"stdBtn.TButton","command": lambda: self.btnAdd("!")},{"relwidth":elmwid,"relheight":elmhei}],
        "expn": ["Button",{"text":"^","style":"stdBtn.TButton","command": lambda: self.btnAdd("^")},{"relwidth":elmwid,"relheight":elmhei}],
        "flor": ["Button",{"text": self.locales[self.lang]["flor"],"style":"stdBtn.TButton","command": lambda: self.btnAdd("floor")},{"relwidth":elmwid,"relheight":elmhei}],
        "ceil": ["Button",{"text": self.locales[self.lang]["ceil"],"style":"stdBtn.TButton","command": lambda: self.btnAdd("ceil")},{"relwidth":elmwid,"relheight":elmhei}],
        "rond": ["Button",{"text":"rnd","style":"stdBtn.TButton","command": lambda: self.btnAdd("round")},{"relwidth":elmwid,"relheight":elmhei}],
        "trnc": ["Button",{"text":"trunc","style":"stdBtn.TButton","command": lambda: self.btnAdd("trunc")},{"relwidth":elmwid,"relheight":elmhei}],
        "gcd":  ["Button",{"text": self.locales[self.lang]["gcd"],"style":"stdBtn.TButton","command": lambda: self.btnAdd("gcd")},{"relwidth":elmwid,"relheight":elmhei}],
        "lcm":  ["Button",{"text":"lcm","style":"stdBtn.TButton","command": lambda: self.btnAdd("lcm")},{"relwidth":elmwid,"relheight":elmhei}],
        "pfac": ["Button",{"text":"pfac","style":"stdBtn.TButton","command": lambda: self.btnAdd("pfac")},{"relwidth":elmwid,"relheight":elmhei}],
        "mod":  ["Button",{"text": self.locales[self.lang]["mod"],"style":"stdBtn.TButton","command": lambda: self.btnAdd("%")},{"relwidth":elmwid,"relheight":elmhei}],
        "logn": ["Button",{"text": self.locales[self.lang]["logn"],"style":"stdBtn.TButton","command": lambda: self.btnAdd("log")},{"relwidth":elmwid,"relheight":elmhei}],
        "loge": ["Button",{"text":"loge","style":"stdBtn.TButton","command": lambda: self.btnAdd("loge")},{"relwidth":elmwid,"relheight":elmhei}],
        "log10":["Button",{"text":"log10","style":"stdBtn.TButton","command": lambda: self.btnAdd("log10")},{"relwidth":elmwid,"relheight":elmhei}],
        "log2": ["Button",{"text":"log2","style":"stdBtn.TButton","command": lambda: self.btnAdd("log2")},{"relwidth":elmwid,"relheight":elmhei}],
        "sin":  ["Button",{"text":"sin","style":"stdBtn.TButton","command": lambda: self.btnAdd("sin")},{"relwidth":elmwid,"relheight":elmhei}],
        "cos":  ["Button",{"text":"cos","style":"stdBtn.TButton","command": lambda: self.btnAdd("cos")},{"relwidth":elmwid,"relheight":elmhei}],
        "tan":  ["Button",{"text":"tan","style":"stdBtn.TButton","command": lambda: self.btnAdd("tan")},{"relwidth":elmwid,"relheight":elmhei}],
        "deg":  ["Button",{"text":"deg","style":"stdBtn.TButton","command": lambda: self.btnAdd("deg")},{"relwidth":elmwid,"relheight":elmhei}],
        "asin": ["Button",{"text":"asin","style":"stdBtn.TButton","command": lambda: self.btnAdd("asin")},{"relwidth":elmwid,"relheight":elmhei}],
        "acos": ["Button",{"text":"acos","style":"stdBtn.TButton","command": lambda: self.btnAdd("acos")},{"relwidth":elmwid,"relheight":elmhei}],
        "atan": ["Button",{"text":"atan","style":"stdBtn.TButton","command": lambda: self.btnAdd("atan")},{"relwidth":elmwid,"relheight":elmhei}],
        "rad":  ["Button",{"text":"rad","style":"stdBtn.TButton","command": lambda: self.btnAdd("rad")},{"relwidth":elmwid,"relheight":elmhei}],
        "coma": ["Button",{"text":",","style":"stdBtn.TButton","command": lambda: self.btnAdd(",")},{"relwidth":elmwid,"relheight":elmhei}],
        "brkl": ["Button",{"text":"(","style":"stdBtn.TButton","command": lambda: self.btnAdd("(")},{"relwidth":elmwid,"relheight":elmhei}],
        "brkr": ["Button",{"text":")","style":"stdBtn.TButton","command": lambda: self.btnAdd(")")},{"relwidth":elmwid,"relheight":elmhei}],
        "setg": ["Button",{"text": self.locales[self.lang]["setg"],"style":"stdBtn.TButton","command": lambda: self.btnSetg()},{"relwidth":elmwid,"relheight":elmhei}]
    }   
        if used_keys is not None:
            return {key: full_def[key] for key in used_keys if key in full_def}
        else:
            return full_def
    def windowgenerator(self,root,name,layout,size,location,resizability):
        root.resizable(resizability[0],resizability[1])
        root.title(name)
        root.geometry(f"{size[0]}x{size[1]}+{location[0]}+{location[1]}")
        elmwid = 1/len(layout[0])
        elmhei = 1/len(layout)
        used_keys = {elem for row in layout for elem in row if elem != "none"}
        elem_def = self.elements_definition(elmwid, elmhei, used_keys)
        #print(elem_def)
        for i,row in enumerate(layout):
            for j,line in enumerate(row):
                if line == "none":
                    continue
                else:
                    elm_type = elem_def[line][0]
                    elm_args = elem_def[line][1]
                    dims = elem_def[line][2]
                    widget = getattr(ttk,elm_type)(root,**elm_args)
                    x = j*elmwid   
                    y = i*elmhei
                    widget.place(relx=x,rely=y,**dims,anchor=tk.NW)
class settingwindow(methods):
    def __init__(self):
        self.lang = 1
        self.textoutput = None
        self.root = tk.Tk()
        style = ttk.Style()
        style.configure("stdBtn.TButton", font=("Meiryo", 20))
        self.windowgenerator(self.root, "Language Setting", self.elements_settingwindow, (300, 100), (100, 100), [0, 0])
        self.root.mainloop()

    def select_lang(self, lang_code):
        self.lang = lang_code
        self.root.destroy()
class main(methods):
    def __init__(self,lang=0):
        self.buffer = str()
        self.lang = lang
        root = tk.Tk()
        self.textoutput = tk.StringVar()
        style = ttk.Style()
        root.bind("<KeyPress>",self.kbd_input)
        scrwid = root.winfo_screenwidth()
        scrhei = root.winfo_screenheight()
        winwid = 360
        winhei = 640
        style.configure("stdBtn.TButton",font=("Meiryo",20))#普通のボタン
        style.configure("lngBtn1.TButton",font=('Meiryo',15))#名前の長いボタン1
        style.configure("lngBtn2.TButton",font=('Meiryo',12))#名前の長いボタン2
        style.configure("stdLbl.TLabel",font=("Meiryo",20))#普通のラベル
        self.windowgenerator(root,"Calculator",self.elements_common,(winwid,winhei),(int((scrwid-winwid)/2),int((scrhei-winhei)/2)),[1,1])
        root.mainloop()

if __name__ == "__main__":
    setting = settingwindow()
    lang = setting.lang if setting.lang is not None else 0
    main(lang)