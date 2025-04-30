import tkinter as tk
from tkinter import ttk
global textoutput
global elmwid
global elmhei
textoutput = tk.StringVar()
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
    def elements_definition(self,elmwid,elmhei): 
        return{
        "scrn": ["Label",{"relief":"sunken","style":"stdLbl.TLabel","anchor":tk.NW,"textvariable":"textoutput"},{"width":elmwid*4,"height":elmhei*2}],
        "none": ["Blank",{},{}],
        "0":    {"Button",{},{}},
        "1":    {"Button",{},{}},
        "2":    {"Button",{},{}},
        "3":    {"Button",{},{}}, 
        "4":    {"Button",{},{}},
        "5":    {"Button",{},{}},
        "6":    {"Button",{},{}},
        "7":    {"Button",{},{}},
        "8":    {"Button",{},{}},
        "9":    {"Button",{},{}},
        "func": {"Button",{},{}},  
        "divd": {"Button",{},{}},
        "mltp": {"Button",{},{}},
        "bksp": {"Button",{},{}},
        "Entr": {"Button",{},{}},
        "addt": {"Button",{},{}},
        "subt": {"Button",{},{}},
        "clr":  {"Button",{},{}},
        "prid": {"Button",{},{}},
        "swch": {"Button",{},{}},
        "exp":  {"Button",{},{}},
        "root": {"Button",{},{}},
        "fctr": {"Button",{},{}},
        "expn": {"Button",{},{}},
        "flor": {"Button",{},{}},
        "ceil": {"Button",{},{}},
        "rond": {"Button",{},{}},
        "trnc": {"Button",{},{}},
        "gcd":  {"Button",{},{}},
        "lcm":  {"Button",{},{}},
        "pfac": {"Button",{},{}},
        "mod":  {"Button",{},{}},
        "logn": {"Button",{},{}},
        "loge": {"Button",{},{}},
        "log10":{"Button",{},{}},
        "log2": {"Button",{},{}},
        "sin":  {"Button",{},{}},
        "cos":  {"Button",{},{}},
        "tan":  {"Button",{},{}},
        "deg":  {"Button",{},{}},
        "asin": {"Button",{},{}},
        "acos": {"Button",{},{}},
        "atan": {"Button",{},{}},
        "rad":  {"Button",{},{}},
        "coma": {"Button",{},{}},
        "brkl": {"Button",{},{}},
        "brkr": {"Button",{},{}},
        "setg": {"Button",{},{}},

    }   
    def windowgenerator(self,root,name,layout,size,location,resizability):
        root.resizable(resizability[0],resizability[1])
        root.title(name)
        root.geometry(f"{size[0]}x{size[1]}+{location[0]}+{location[1]}")
        elmwid = 1/len(layout[0])
        elmhei = 1/len(layout)
        elem_def = self.elements_definition(elmwid,elmhei) 
        for row in layout:
            for line in row:
                if line == "none":
                    continue
                
                


class main(methods):
    root = tk.Tk()
    style = ttk.Style()
    scrwid = root.winfo_screenwidth()
    scrhei = root.winfo_screenheight()
    winwid = 360
    winhei = 640
    style.configure("stdBtn1.TButton",font=("Meiryo",20))
    style.configure("stdBtn2.TButton",font=('Meiryo',15))
    style.configure("stdBtn3.TButton",font=('Meiryo',12))
    style.configure("stdBtn4.TButton",font=('Meiryo',10))
    style.configure("stdLbl.TLabel",font=('Meiryo',12))
    methods.windowgenerator(root,"Calculator",methods.elements_common,{360,640},{scrwid//2-180,scrhei//2-320},[1,1])
