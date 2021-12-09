import sympy

from .expr import Expr


class Equation:

    def __init__(self, left='', right=''):
        self.left_expr = Equation.make_expr(left)
        self.right_expr = Equation.make_expr(right, self.left_expr.var)

        self.text = self.left_expr.text + ' - (' + self.right_expr.text + ')'
        self.parsed = sympy.parse_expr(self.text)
        self.solved = sympy.solve(self.parsed)

    def check(self, answer):
        return self.solved[0] == sympy.parse_expr(answer)

    @staticmethod
    def make_expr(txt='', var=''):
        if txt:
            result = Expr()
            result.create_from_text(txt)
        else:
            result = Expr(var)
            result.make_expr()

        return result
