#2022/06/13開発開始

class Settings():
    settings = [0,0]
    ques = str()
    def lang_select(self):
        self.settings[0] = input('言語を選択してください。/Please select the language. 日本語:1 English:2 :')
    def mode_select(self):
        if self.settings[0] == 1:
            self.settings[1] = input('使用するモードを選択してください。:')
        elif self.settings[0] == 2:
            self.settings[1] = input('Please select the mode. :')
app = Settings()
app.lang_select()