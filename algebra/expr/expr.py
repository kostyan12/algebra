import random
import string
import sympy


from .base_item import BaseItem


class Expr:
    max_len = 3

    def __init__(self, var="x"):
        random.seed()
        self.var = (var if var else Expr.get_var()).lower()
        self.length = random.randint(2, Expr.max_len)
        self.items = []
        self.text = ""
        self.parsed = sympy.simplify(0)
        self.answer = ""
        self.parsed_answer = sympy.simplify(0)

    def create_from_text(self, text):
        self.text = text
        self.parsed = self.parse_expr(self.text)

    def make_expr(self):
        for i in range(0, self.length):
            item = ExprItem(self.var)
            item.make_item()
            self.items.append(item)
            self.text += item.get_text(i)
            item.debug_log(f'{i}, {item.get_text(i)}, is_positive = {item.is_positive}')
        self.parsed = self.parse_expr(self.text)

    def parse_expr(self, expr_txt):
        if not self.text:
            self.make_expr()

        return sympy.parse_expr(expr_txt)

    def get_answer(self, answer=""):
        self.answer = str(input("Введите ответ:")) if not answer else answer
        self.parsed_answer = self.parse_expr(expr_txt=self.answer)

    @staticmethod
    def print_expr(expr):
        print(expr)

    def check_answer(self):
        return sympy.simplify(self.parsed - self.parsed_answer) == 0

    @staticmethod
    def get_var():
        return random.choice(string.ascii_letters)


class ExprItem(BaseItem):
    def __init__(self, var, length=0):
        super().__init__()
        random.seed()
        self.length = random.randint(1, 3) if not length else length
        self.debug_log(f'self.length = {self.length}')
        self.first_item = Term(var)
        self.second_item = 0
        self.coefficient = 0
        self.first_item.make_term()
        if self.length < 2:
            self.is_positive = self.first_item.is_positive
            return

        self.second_item = Term(var)
        if self.first_item.is_var:
            self.second_item.is_var = False
        else:
            self.second_item.is_var = True

        self.second_item.make_term()

        self.coefficient = Coefficient(var)

        if self.length < 3:
            self.coefficient.numerator = 1
            self.coefficient.is_int = True

        self.coefficient.make_term()
        self.is_positive = self.coefficient.is_positive

    def make_item(self):
        self.text = self.first_item.get_text()

        if self.length > 1:
            self.text += self.second_item.get_text(1)

        if self.length > 1:
            self.text = self.parenthesize()

        if self.coefficient and self.coefficient.divider != 1:
            self.text = self.coefficient.get_text(1) + "*" + self.text


class Term(BaseItem):
    def __init__(self, var):
        super().__init__()
        random.seed()

        self.divider = 0
        self.numerator = 0
        self.is_var = BaseItem.randbool()
        self.is_int = BaseItem.randbool()
        self.var = var

        self.sign = '+' if self.is_positive else '-'

    def make_term(self):
        if self.is_int:
            self.numerator = random.randint(1, 99)
            self.divider = 1
        else:
            self.divider = random.randint(2, 9)
            self.numerator = random.randint(1, self.divider - 1)
        if self.numerator > 1:
            self.text = str(self.numerator)
        if len(self.text) and self.is_var:
            self.text += '*' + self.var
        elif self.is_var:
            self.text = self.var
        if not self.text:
            self.text = '1'
        if not self.is_int:
            self.text += '/' + str(self.divider)


class Coefficient(Term):
    def __init__(self, var):
        super().__init__(var)
        self.is_var = False

    def get_text(self, index=0):
        return self.text
