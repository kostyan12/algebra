import random


class BaseItem:
    @staticmethod
    def randbool():
        return random.randint(0, 1) == 1

    def __init__(self):
        self.text = ""
        self.is_positive = BaseItem.randbool()
        self.sign = ""
        self.debug = False
        self.length = 1

    def debug_log(self, text):
        if self.debug:
            print(f'debug=>{self}', text)

    def get_text(self, index=0):
        res = self.text

        # if index == 0 and not self.is_positive:
        #     res = self.get_sign() + res
        # elif index > 0:
        #     res = f'{self.get_sign()} {res}'
        # return res
        if (index > 0 or index == 0 and not self.is_positive) and not res[0] == '-':
            res = f'{self.get_sign()} {res}'
            self.debug_log(text=f'index = {index}; {res}')

        return res

    def get_sign(self):
        if self.is_positive:
            return '+'
        else:
            return '-'

    def parenthesize(self):
        if self.text:
            return "( " + self.text + " )"
