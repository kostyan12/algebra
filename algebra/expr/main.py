#from algebra.models import Expressions
#from expr import Expr
from equation import Equation

# class Tutor:
#     def __init__(self):
#         self.expr_type = 0
#
#     @staticmethod
#     def print_menu():
#         print("1. Уравнение")
#         print("2. Выражение")
#
#     def start(self):
#         self.print_menu()
#         while True:
#             try:
#                 self.expr_type = int(input())
#             except:
#                 self.expr_type = 0
#             if not (1 <= self.expr_type <= 2):
#                 print("Неверный ввод")
#             else:
#                 break
#         print("Выбор:", self.expr_type)
#
#         expr = Expr(var="")
#         expr.make_expr()
#         print(expr.text)
#
#         expr.get_answer()
#         if expr.check_answer():
#             print("Верно!")
#         else:
#             print("Неверно! Правильно:")
#             expr.print_expr(expr.parsed)


e = Equation()
print(e.text)
print(e.parsed)
print(e.solved)
res = input()
rr = e.check(res)
print(e.check(res))

#t = Tutor()

#t.start()

# expr = Expressions.expr_view()
#
# for e in expr:
#     print(e.get_absolute_url())
