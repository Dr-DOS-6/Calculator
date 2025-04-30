#coding: UTF-8
import tkinter as tk
from tkinter import messagebox, ttk
import os
import textwrap as tw
import math
import re
import platform

# Windows の場合、DPI スケーリングを有効化
if platform.system() == "Windows":
    try:
        import ctypes
        ctypes.windll.shcore.SetProcessDpiAwareness(1)  # プロセス全体で DPI スケーリングを有効化
    except Exception:
        pass  # Windows 以外やエラー時は無視

# グローバル状態（元のコードの mli をそのまま使用）
mli = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

class func:
    def setup_window(self, mode):
        """ウィンドウサイズと位置を設定"""
        # ウィンドウが初期化された後に画面サイズを取得
        self.main_win.update()  # ウィンドウ状態を更新
        self.scrwid = self.main_win.winfo_screenwidth()
        self.scrhei = self.main_win.winfo_screenheight()

        # サイズを大きく調整
        self.winwid = 480  # 基本モードの幅を 480px に
        self.winhei = 840  # 高さを 840px に
        self.btnwid = int(self.winwid / 4)  # ボタンの幅（480/4 = 120px）
        self.btnhei = int(self.winhei / 7)  # ボタンの高さ（840/7 = 120px）
        if mode == 'advanced':
            self.winwid += self.btnwid * 2  # 多機能モードでは幅を拡張（480 + 120*2 = 720px）

        # オリジナルの self.winsize 計算を流用
        self.winsize = f'{self.winwid}x{self.winhei}+{int((self.scrwid-self.winwid)/2)}+{int((self.scrhei-self.winhei)/2)}'
        self.main_win.geometry(self.winsize)
        self.main_win.title(f'{self.langset[24]}{self.langset[16 if mode == "basic" else 17]}')

    def setup_styles(self):
        """言語に応じたスタイルを設定"""
        font_sizes = {
            'JA-Jp': {'stdButton': 24, 'stdButton2': 22, 'stdButton3': 18, 'stdButton4': 14, 'stdLabel': 20},
            'US-En': {'stdButton': 24, 'stdButton2': 22, 'stdButton3': 18, 'stdButton4': 16, 'stdLabel': 20}
        }
        sizes = font_sizes[self.langset[-1]]
        self.style.configure("stdButton.TButton", font=('Meiryo', sizes['stdButton']))
        self.style.configure("stdButton2.TButton", font=('Meiryo', sizes['stdButton2']))
        self.style.configure("stdButton3.TButton", font=('Meiryo', sizes['stdButton3']))
        self.style.configure("stdButton4.TButton", font=('Meiryo', sizes['stdButton4']))
        self.style.configure("stdLabel.TLabel", font=('Meiryo', sizes['stdLabel']))

    def clear_widgets(self):
        """既存のウィジェットをクリア"""
        for widget in self.main_win.winfo_children():
            widget.destroy()
        self.buttons = {}  # ボタン参照をリセット

    def screenresetter(self, mode_num):
        """モードに応じて画面を再構築（1: 多機能, 2: 基本）"""
        mode = 'advanced' if mode_num == 1 else 'basic'
        self.mode = mode
        mli[8] = mode_num

        # ウィジェットをクリア
        self.clear_widgets()

        # ウィンドウとスタイルを設定
        self.setup_window(mode)
        self.setup_styles()

        # ボタン定義
        common_buttons = {
            '0': {'text': '0', 'style': 'stdButton.TButton', 'command': lambda: self.handle_input(input_char='0')},
            '1': {'text': '1', 'style': 'stdButton.TButton', 'command': lambda: self.handle_input(input_char='1')},
            '2': {'text': '2', 'style': 'stdButton.TButton', 'command': lambda: self.handle_input(input_char='2')},
            '3': {'text': '3', 'style': 'stdButton.TButton', 'command': lambda: self.handle_input(input_char='3')},
            '4': {'text': '4', 'style': 'stdButton.TButton', 'command': lambda: self.handle_input(input_char='4')},
            '5': {'text': '5', 'style': 'stdButton.TButton', 'command': lambda: self.handle_input(input_char='5')},
            '6': {'text': '6', 'style': 'stdButton.TButton', 'command': lambda: self.handle_input(input_char='6')},
            '7': {'text': '7', 'style': 'stdButton.TButton', 'command': lambda: self.handle_input(input_char='7')},
            '8': {'text': '8', 'style': 'stdButton.TButton', 'command': lambda: self.handle_input(input_char='8')},
            '9': {'text': '9', 'style': 'stdButton.TButton', 'command': lambda: self.handle_input(input_char='9')},
            'Pe': {'text': '.', 'style': 'stdButton.TButton', 'command': lambda: self.handle_input(input_char='.')},
            'Pl': {'text': '+', 'style': 'stdButton.TButton', 'command': lambda: self.handle_input(input_char='+')},
            'Min': {'text': '-', 'style': 'stdButton.TButton', 'command': lambda: self.handle_input(input_char='-')},
            'Ast': {'text': 'x', 'style': 'stdButton.TButton', 'command': lambda: self.handle_input(input_char='*')},
            'Sl': {'text': '÷', 'style': 'stdButton.TButton', 'command': lambda: self.handle_input(input_char='/')},
            'Etr': {'text': 'Enter', 'style': 'stdButton.TButton', 'command': lambda: self.handle_input(input_char='enter')},
            'Bksp': {'text': '←', 'style': 'stdButton.TButton', 'command': lambda: self.handle_input(input_char='backspace')},
            'Clr': {'text': self.langset[3], 'style': 'stdButton.TButton', 'command': lambda: self.handle_input(input_char='clear')},
            'Ext': {'text': self.langset[4], 'style': 'stdButton.TButton', 'command': lambda: self.handle_input(input_char='exit')},
            'Fn': {'text': self.langset[5], 'style': 'stdButton.TButton' if self.langset[-1] == 'JA-Jp' else 'stdButton2.TButton', 'command': lambda: self.handle_input(input_char='fn')}
        }

        advanced_buttons = {
            'Fcrl': {'text': self.langset[6], 'style': 'stdButton.TButton' if self.langset[-1] == 'JA-Jp' else 'stdButton3.TButton', 'command': lambda: self.handle_input(input_char='self.factorial(' if not self.fn_mode else 'self.fabs(')},
            'Sqrt': {'text': self.langset[7], 'style': 'stdButton.TButton', 'command': lambda: self.handle_input(input_char='math.sqrt(')},
            'Cil': {'text': self.langset[8], 'style': 'stdButton3.TButton' if self.langset[-1] == 'JA-Jp' else 'stdButton.TButton', 'command': lambda: self.handle_input(input_char='math.ceil(')},
            'Flr': {'text': self.langset[9], 'style': 'stdButton3.TButton', 'command': lambda: self.handle_input(input_char='math.floor(')},
            'Pct': {'text': self.langset[10], 'style': 'stdButton3.TButton', 'command': lambda: self.handle_input(input_char='%')},
            'Gcd': {'text': self.langset[11], 'style': 'stdButton3.TButton' if self.langset[-1] == 'JA-Jp' else 'stdButton.TButton', 'command': lambda: self.handle_input(input_char='math.gcd(')},
            'Exp': {'text': self.langset[12], 'style': 'stdButton3.TButton' if self.langset[-1] == 'JA-Jp' else 'stdButton.TButton', 'command': lambda: self.handle_input(input_char='math.exp(')},
            'Log': {'text': self.langset[13], 'style': 'stdButton4.TButton', 'command': lambda: self.handle_input(input_char='math.log(')},
            'Sint': {'text': 'sin', 'style': 'stdButton.TButton', 'command': lambda: self.handle_input(input_char='self.sin(' if not self.fn_mode else 'self.asin(')},
            'Cost': {'text': 'cos', 'style': 'stdButton.TButton', 'command': lambda: self.handle_input(input_char='self.cos(' if not self.fn_mode else 'self.acos(')},
            'Tant': {'text': 'tan', 'style': 'stdButton.TButton', 'command': lambda: self.handle_input(input_char='self.tan(' if not self.fn_mode else 'self.atan(')},
            'Cma': {'text': ',', 'style': 'stdButton.TButton', 'command': lambda: self.handle_input(input_char=',')},
            'BrckL': {'text': '(', 'style': 'stdButton.TButton', 'command': lambda: self.handle_input(input_char='(')},
            'BrckR': {'text': ')', 'style': 'stdButton.TButton', 'command': lambda: self.handle_input(input_char=')')}
        }

        # モードに応じたボタンリスト
        buttons = common_buttons if mode == 'basic' else {**common_buttons, **advanced_buttons}

        # レイアウト定義（x, y はボタンの位置、単位は btnwid, btnhei）
        layout_basic = {
            'console': {'x': 0, 'y': 0, 'width': 4, 'height': 2},
            'Fn': {'x': 0, 'y': 2, 'width': 1, 'height': 1},
            'Sl': {'x': 1, 'y': 2, 'width': 1, 'height': 1},
            'Ast': {'x': 2, 'y': 2, 'width': 1, 'height': 1},
            'Bksp': {'x': 3, 'y': 2, 'width': 1, 'height': 1},
            '7': {'x': 0, 'y': 3, 'width': 1, 'height': 1},
            '8': {'x': 1, 'y': 3, 'width': 1, 'height': 1},
            '9': {'x': 2, 'y': 3, 'width': 1, 'height': 1},
            'Etr': {'x': 3, 'y': 3, 'width': 1, 'height': 1},
            '4': {'x': 0, 'y': 4, 'width': 1, 'height': 1},
            '5': {'x': 1, 'y': 4, 'width': 1, 'height': 1},
            '6': {'x': 2, 'y': 4, 'width': 1, 'height': 1},
            'Pl': {'x': 3, 'y': 4, 'width': 1, 'height': 1},
            '1': {'x': 0, 'y': 5, 'width': 1, 'height': 1},
            '2': {'x': 1, 'y': 5, 'width': 1, 'height': 1},
            '3': {'x': 2, 'y': 5, 'width': 1, 'height': 1},
            'Min': {'x': 3, 'y': 5, 'width': 1, 'height': 1},
            'Clr': {'x': 0, 'y': 6, 'width': 1, 'height': 1},
            '0': {'x': 1, 'y': 6, 'width': 1, 'height': 1},
            'Pe': {'x': 2, 'y': 6, 'width': 1, 'height': 1},
            'Ext': {'x': 3, 'y': 6, 'width': 1, 'height': 1}
        }

        layout_advanced = {
            'console': {'x': 2, 'y': 0, 'width': 4, 'height': 2},
            'Fn': {'x': 2, 'y': 2, 'width': 1, 'height': 1},
            'Sl': {'x': 3, 'y': 2, 'width': 1, 'height': 1},
            'Ast': {'x': 4, 'y': 2, 'width': 1, 'height': 1},
            'Bksp': {'x': 5, 'y': 2, 'width': 1, 'height': 1},
            '7': {'x': 2, 'y': 3, 'width': 1, 'height': 1},
            '8': {'x': 3, 'y': 3, 'width': 1, 'height': 1},
            '9': {'x': 4, 'y': 3, 'width': 1, 'height': 1},
            'Etr': {'x': 5, 'y': 3, 'width': 1, 'height': 1},
            '4': {'x': 2, 'y': 4, 'width': 1, 'height': 1},
            '5': {'x': 3, 'y': 4, 'width': 1, 'height': 1},
            '6': {'x': 4, 'y': 4, 'width': 1, 'height': 1},
            'Pl': {'x': 5, 'y': 4, 'width': 1, 'height': 1},
            '1': {'x': 2, 'y': 5, 'width': 1, 'height': 1},
            '2': {'x': 3, 'y': 5, 'width': 1, 'height': 1},
            '3': {'x': 4, 'y': 5, 'width': 1, 'height': 1},
            'Min': {'x': 5, 'y': 5, 'width': 1, 'height': 1},
            'Clr': {'x': 2, 'y': 6, 'width': 1, 'height': 1},
            '0': {'x': 3, 'y': 6, 'width': 1, 'height': 1},
            'Pe': {'x': 4, 'y': 6, 'width': 1, 'height': 1},
            'Ext': {'x': 5, 'y': 6, 'width': 1, 'height': 1},
            'Fcrl': {'x': 0, 'y': 0, 'width': 1, 'height': 1},
            'Sqrt': {'x': 1, 'y': 0, 'width': 1, 'height': 1},
            'Cil': {'x': 0, 'y': 1, 'width': 1, 'height': 1},
            'Flr': {'x': 1, 'y': 1, 'width': 1, 'height': 1},
            'Gcd': {'x': 0, 'y': 2, 'width': 1, 'height': 1},
            'Exp': {'x': 1, 'y': 2, 'width': 1, 'height': 1},
            'Log': {'x': 0, 'y': 3, 'width': 1, 'height': 1},
            'Sint': {'x': 1, 'y': 3, 'width': 1, 'height': 1},
            'Cost': {'x': 0, 'y': 4, 'width': 1, 'height': 1},
            'Tant': {'x': 1, 'y': 4, 'width': 1, 'height': 1},
            'Cma': {'x': 0, 'y': 5, 'width': 1, 'height': 1},
            'Pct': {'x': 1, 'y': 5, 'width': 1, 'height': 1},
            'BrckL': {'x': 0, 'y': 6, 'width': 1, 'height': 1},
            'BrckR': {'x': 1, 'y': 6, 'width': 1, 'height': 1}
        }

        layout = layout_basic if mode == 'basic' else layout_advanced

        # コンソール（表示領域）の作成
        self.console = ttk.Label(self.main_win, relief="sunken", style="stdLabel.TLabel", anchor=tk.NW, textvariable=self.textoutput)
        console_layout = layout.pop('console')
        self.console.place(
            x=console_layout['x'] * self.btnwid,
            y=console_layout['y'] * self.btnhei,
            width=console_layout['width'] * self.btnwid,
            height=console_layout['height'] * self.btnhei
        )

        # ボタンの作成と配置
        for btn_key, btn_layout in layout.items():
            btn_def = buttons[btn_key]
            btn = ttk.Button(
                self.main_win,
                text=btn_def['text'],
                style=btn_def['style'],
                command=btn_def['command']
            )
            btn.place(
                x=btn_layout['x'] * self.btnwid,
                y=btn_layout['y'] * self.btnhei,
                width=btn_layout['width'] * self.btnwid,
                height=btn_layout['height'] * self.btnhei
            )
            self.buttons[btn_key] = btn  # ボタンを保存（Fn などで参照）

        # Fn モードの初期化
        if mode == 'advanced' and self.fn_mode:
            self.handle_input(input_char='fn')  # Fn モードを反映

    # 数学関数（元のコードから変更なし）
    def sin(self, _input):
        return math.sin(math.radians(_input))

    def asin(self, _input):
        return math.asin(_input)

    def cos(self, _input):
        return math.cos(math.radians(_input))

    def acos(self, _input):
        return math.acos(_input)

    def tan(self, _input):
        return math.tan(math.radians(_input))

    def atan(self, _input):
        return math.atan(_input)

    def factorial(self, _input):
        return math.factorial(_input)

    def fabs(self, _input):
        return math.fabs(_input)

    def update_display(self):
        """ディスプレイの更新"""
        self.textoutput.set(tw.fill(self.temp, 40))

    def handle_input(self, event=None, input_char=None):
        """キーボードまたはボタンからの入力を一元的に処理"""
        if event:
            key = event.keysym
            key_mappings = {
                'period': '.', 'comma': ',', 'slash': '/', 'asterisk': '*',
                'minus': '-', 'plus': '+', 'parenleft': '(', 'parenright': ')',
                'exclam': 'self.factorial(' if not self.fn_mode else 'self.fabs(',
                'root': 'math.sqrt(', 'percent': '%', 'asciicircum': '**',
                'Return': 'enter', 'BackSpace': 'backspace', 'Escape': 'exit',
                'equal': '='
            }
            if key in key_mappings:
                input_char = key_mappings[key]
            elif key.isdigit():
                input_char = key
            elif key in ('Shift_R', 'Shift_L', 'Control_R', 'Control_L', 'Tab', 'NumLock'):
                return
            else:
                input_char = key
        else:
            # ボタン入力の場合、input_char は直接渡される
            pass

        # 初期設定（言語選択、モード選択）の処理
        if (mli[10] == 0 and mli[11] == 1) or (mli[1] == 1 and mli[3] == 1):
            if self.handle_initial_setup(input_char):
                return

        # 通常の入力処理
        if input_char == 'enter':
            if mli[2] == 1:
                self.temp = ''
                mli[2] = 0
                self.update_display()
            elif mli[8] == 0:
                return
            else:
                try:
                    self.temp = str(eval(self.temp))
                    self.update_display()
                except SyntaxError:
                    if mli[1] == 0 or mli[6] == 1:
                        pass
                    elif self.langset[19] in self.temp or (self.langset[16]+self.langset[20]) in self.temp or (self.langset[17]+self.langset[20]) in self.temp:
                        self.temp = ''
                    else:
                        self.temp = self.langset[19]
                    self.update_display()
                except ZeroDivisionError:
                    pass
                except OverflowError:
                    self.temp = self.langset[21]
                    self.update_display()

        elif input_char == 'clear':
            if self.buttons['Clr'].cget('text') == self.langset[29]:  # Export
                with open('result.txt', mode='a', encoding='UTF-8') as f:
                    f.write(self.temp)
                self.path = os.path.abspath('result.txt')
                self.temp = f'{self.langset[22]}\n{self.path}'
                mli[2] = 1
            else:
                self.temp = ''
            self.update_display()

        elif input_char == 'backspace':
            if self.temp[-15:] == 'self.factorial(':
                self.temp = self.temp[:-15]
            elif self.temp[-11:] == 'math.floor(':
                self.temp = self.temp[:-11]
            elif self.temp[-10:] == 'math.sqrt(':
                self.temp = self.temp[:-10]
            elif self.temp[-10:] == 'math.ceil(':
                self.temp = self.temp[:-10]
            elif self.temp[-9:] == 'math.gcd(':
                self.temp = self.temp[:-9]
            elif self.temp[-9:] == 'math.exp(':
                self.temp = self.temp[:-9]
            elif self.temp[-9:] == 'math.log(':
                self.temp = self.temp[:-9]
            elif self.temp[-9:] == 'self.sin(':
                self.temp = self.temp[:-9]
            elif self.temp[-10:] == 'self.asin(':
                self.temp = self.temp[:-10]
            elif self.temp[-9:] == 'self.cos(':
                self.temp = self.temp[:-9]
            elif self.temp[-10:] == 'self.acos(':
                self.temp = self.temp[:-10]
            elif self.temp[-9:] == 'self.tan(':
                self.temp = self.temp[:-9]
            elif self.temp[-10:] == 'self.atan(':
                self.temp = self.temp[:-10]
            else:
                self.temp = self.temp[:-1]
            self.update_display()

        elif input_char == 'exit':
            if self.buttons['Ext'].cget('text') == self.langset[28]:
                if self.mode == 'basic':
                    self.screenresetter(1)
                else:
                    self.screenresetter(2)
            else:
                if messagebox.askyesno(f'{self.langset[24]+self.langset[25]}', f'{self.langset[26]}'):
                    self.main_win.destroy()
                return

        elif input_char == 'fn':
            self.fn_mode = not self.fn_mode
            if self.buttons['Ext'].cget('text') == self.langset[28]:
                self.buttons['Clr'].config(text=self.langset[3])
                self.buttons['Ext'].config(text=self.langset[4], style="stdButton.TButton")
                if self.mode == 'advanced':
                    self.buttons['Sint'].config(text='sin')
                    self.buttons['Cost'].config(text='cos')
                    self.buttons['Tant'].config(text='tan')
                    self.buttons['Fcrl'].config(text=self.langset[6])
            else:
                self.buttons['Clr'].config(text=self.langset[29], style="stdButton3.TButton" if self.langset[-1] == 'US-En' else 'stdButton.TButton')
                self.buttons['Ext'].config(text=self.langset[28], style="stdButton2.TButton")
                if self.mode == 'advanced':
                    self.buttons['Sint'].config(text='arc\nsin')
                    self.buttons['Cost'].config(text='arc\ncos')
                    self.buttons['Tant'].config(text='arc\ntan')
                    self.buttons['Fcrl'].config(text=self.langset[15])
            return

        else:
            # 入力状態のリセットと検証
            if mli[2] == 1:
                self.temp = ''
                mli[2] = 0
            elif mli[4] == 1:
                self.temp = ''
                mli[4] = 0
            # 最初の入力でも確実に追加
            self.stat = 1
            # 連続する演算子の防止
            if input_char in ('+', '-', '*', '/', '%') and self.temp and self.temp[-1] in ('+', '-', '*', '/', '%'):
                return
            self.temp += input_char
            self.update_display()

    def handle_initial_setup(self, input_char):
        """言語選択とモード選択を処理"""
        if mli[10] == 0 and mli[11] == 1:  # 言語選択
            if input_char == '1':
                self.langset = ['消去/出力','消去/\n出力','終了/\nモード切替','消去','終了','切替','階乗','平方根','繰り上げ','繰り下げ','割り算\nの余り','最大\n公約数','eのx乗','yを底とする\nxの対数\n(log(x,y))','関数','絶対値','電卓モード','多機能電卓モード','使用するモードを選んでください。\n電卓モード:1 多機能電卓モード:2','入力された式は使用できません。もう一度式を入力してください。','が選択されました。','数値が大きすぎます。一回表示を消去してください。','結果の出力先:','デバッグ','EUGC Ver1.2 ','終了確認','終了してもよろしいですか？','確認','モード\n変更','出力','JA-Jp']
                self.temp = '日本語が選択されました。\nEnterキーを押してください。'
                mli[10] = 1
                mli[11] = 0
                mli[1] = 1
                mli[3] = 1  # モード選択へ
            elif input_char == '2':
                self.langset = ['Erase/\nExport','Erase/\nExport','Exit/\nSwitch','Erase','Exit','Switch','Factorial','Square\nroot','Carry','Carry\nforward','Remain\nof divid','G.C.D','exp','Logarithm\n(log(x,y))','Function','Absolute\nValue','Calculator Mode','Multifunction Calculator Mode','Please select the mode that you want to use.\nCalculator Mode:1 \nMultifunction Calculator Mode:2',"has selected.","The inputted formula can't be calculated.\nPlease re-input the formula.",'The value is too large.Please erase the display once.','An result was output at:','Debug','EUGC Ver1.2 ','Confirm Exit','Are you sure you want to exit?','Confirm','Mode\nSwitch','Export','US-En']
                self.temp = 'English has selected.\nPress Enter to proceed.'
                mli[10] = 1
                mli[11] = 0
                mli[1] = 1
                mli[3] = 1  # モード選択へ
            self.update_display()
            return True

        if mli[1] == 1 and mli[3] == 1:  # モード選択
            if input_char == '1':
                self.temp = ''
                self.screenresetter(2)
                mli[3] = 0
                mli[8] = 1
                mli[1] = 0  # 入力状態をリセット
                self.stat = 0  # 入力開始フラグをリセット
            elif input_char == '2':
                self.temp = ''
                self.screenresetter(1)
                mli[3] = 0
                mli[8] = 2
                mli[1] = 0  # 入力状態をリセット
                self.stat = 0  # 入力開始フラグをリセット
            else:
                self.temp = self.langset[18]  # モード選択のプロンプトを再表示
                self.update_display()
                return True
            self.update_display()
            return True

        return False

class main_win(func):
    def __init__(self):
        self.main_win = tk.Tk()
        self.style = ttk.Style()
        self.main_win.resizable(0, 0)
        self.main_win.title('EUGC Ver1.2')

        # 初期ウィンドウサイズと位置を設定（基本モードのサイズに合わせる）
        self.main_win.update()  # ウィンドウ状態を更新
        scrwid = self.main_win.winfo_screenwidth()
        scrhei = self.main_win.winfo_screenheight()
        winwid = 480  # 基本モードの幅
        winhei = 840  # 基本モードの高さ
        winsize = f'{winwid}x{winhei}+{int((scrwid-winwid)/2)}+{int((scrhei-winhei)/2)}'
        self.main_win.geometry(winsize)

        self.buttons = {}  # ボタン参照を保持
        self.fn_mode = False  # 関数モード（sin/arcsin 切り替え）
        self.mode = None  # 現在のモード（basic または advanced）
        self.textoutput = tk.StringVar()
        self.temp = ''
        self.stat = 0
        mli[1] = 0
        mli[2] = 0
        mli[7] = 0
        self.main_win.bind("<KeyPress>", self.handle_input)

        # 初期コンソールのスタイルを設定
        self.style.configure("stdLabel.TLabel", font=('Meiryo', 20))
        self.console = ttk.Label(self.main_win, relief="sunken", style="stdLabel.TLabel", anchor=tk.NW, textvariable=self.textoutput)
        self.console.place(x=0, y=0, width=480, height=240)  # 初期コンソールサイズ
        self.textoutput.set('Calculator GUI Version 1.2\n Dr.GLaDOS© 2022\n\nEnterキーを押して下さい...\nPress Enter key to continue...')
        mli[11] = 1  # 言語選択画面へ
        self.main_win.mainloop()

main_win()