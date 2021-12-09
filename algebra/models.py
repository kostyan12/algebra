import uuid

from django.db import models

# Create your models here.
from django.urls import reverse
from django.contrib.auth.models import User
from algebra.expr.expr import Expr
from algebra.expr.equation import Equation


class ExprTypes(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(verbose_name='Type of expression', max_length=50)

    def __str__(self):
        return f'{self.name}'


class Expressions(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    text = models.CharField(max_length=255)
    text_r = models.CharField(max_length=255, null=True, blank=True)
    result = models.CharField(max_length=255, null=True, blank=True)
    expr_type = models.ForeignKey('ExprTypes', on_delete=models.CASCADE)
    cr_date = models.DateTimeField(auto_now=True)

    expr_key = "3d8e6484-0551-43b7-a721-4d9a3039a275"
    eq_key = "b57df554-143e-4686-90cd-1bcf9b8eda2b"
    expr_txt = 'expression'
    eq_txt = 'equation'

    class Meta:
        permissions = (("can_add_new_expr", "Can add new expression"),
                       ("can_add_new_eq", "Can add new equation"),)
        ordering = ['-cr_date']

    def __str__(self):
        res = self.text
        if self.text_r:
            res += f' = {self.text_r}'
        # res += f' ({self.expr_type})'
        return res

    def get_absolute_url(self):
        return reverse('expr_solve', args=[str(self.id)])

    @staticmethod
    def expr_view():
        return Expressions.objects.filter(expr_type=Expressions.expr_key)

    @staticmethod
    def eq_view():
        return Expressions.objects.filter(expr_type=Expressions.eq_key)

    def check_expr(self, answer):
        if str(self.expr_type.id) == Expressions.expr_key:
            expr = Expr()
            expr.create_from_text(self.text)
            expr.print_expr(expr.parsed)
            expr.get_answer(answer=answer)
            return expr.check_answer()
        elif str(self.expr_type.id) == Expressions.eq_key:
            expr = Equation(left=self.text, right=self.text_r)
            return expr.check(answer=answer)

    def create_new(self, expr_type):
        # print(str(expr_type.id) == Expressions.expr_key)
        if str(expr_type.id) == Expressions.expr_key:
            expr = Expr()
            expr.make_expr()
            self.text = expr.text
            self.result = expr.parsed
        elif str(expr_type.id) == Expressions.eq_key:
            equation = Equation()
            self.text = equation.left_expr.text
            self.text_r = equation.right_expr.text
            self.result = equation.solved

        self.expr_type = expr_type
        self.save()
        return self.id


class SolvedExpressions(models.Model):
    expr = models.ForeignKey(Expressions, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    solv_date = models.DateTimeField(auto_now=True)
    result = models.CharField(max_length=255, null=True, blank=True)
    trys = models.IntegerField(verbose_name="Number of trys", default=0)
