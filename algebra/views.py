from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from .models import Expressions, SolvedExpressions, ExprTypes
from .forms import ExprSolveForm
from django.contrib import messages


# Create your views here.


def index(request):
    num_expr = Expressions.expr_view().count()
    num_eq = Expressions.eq_view().count()
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    if request.user.is_authenticated:
        se = SolvedExpressions.objects.filter(user=request.user).filter(expr__expr_type=Expressions.expr_key)
        num_expr_solved = se.count()
        se = SolvedExpressions.objects.filter(user=request.user).filter(expr__expr_type=Expressions.eq_key)
        num_eq_solved = se.count()
    else:
        num_expr_solved = num_eq_solved = 0

    return render(request, 'algebra/index.html',
                  context={"num_expr": num_expr, "num_eq": num_eq, 'num_visits': num_visits,
                           "num_expr_solved": num_expr_solved, "num_eq_solved": num_eq_solved})


def new(request, et):
    expr_type = None
    try:
        expr_type = ExprTypes.objects.get(id=et)
    except ObjectDoesNotExist:
        pass

    if expr_type:
        expr = Expressions()
        expr.create_new(expr_type=expr_type)
        return HttpResponseRedirect(expr.get_absolute_url())
    else:
        return HttpResponseRedirect('index')


class ExprListView(generic.ListView):
    model = Expressions
    template_name = 'algebra/expr_list.html'
    queryset = Expressions.expr_view()
    context_object_name = "expr_list"
    paginate_by = 10

    def __init__(self):
        super(ExprListView, self).__init__()
        self.expr_type = ExprTypes.objects.get(id=Expressions.expr_key)

    def get_context_data(self, **kwargs):
        context = super(ExprListView, self).get_context_data(**kwargs)
        context['expr_type'] = self.expr_type
        return context


class EquationListView(ExprListView):
    queryset = Expressions.eq_view()

    def __init__(self):
        super(EquationListView, self).__init__()
        self.expr_type = ExprTypes.objects.get(id=Expressions.eq_key)


def expr_solve_view(request, pk):
    expr_b = get_object_or_404(Expressions, pk=pk)

    if request.method == 'POST':

        form = ExprSolveForm(request.POST)

        if form.is_valid():
            res = form.cleaned_data['solved']

            if expr_b.check_expr(res):

                if request.user.is_authenticated:
                    try:
                        es = SolvedExpressions.objects.get(expr=expr_b, user=request.user)
                    except ObjectDoesNotExist:
                        es = SolvedExpressions()
                        es.expr = expr_b
                        es.user = request.user

                    es.trys += 1
                    es.result = res
                    es.save()

                return HttpResponseRedirect(reverse('expr'))
            else:
                messages.error(request, "Invalid answer")

    else:
        form = ExprSolveForm()

    return render(request, 'algebra/expr_solve.html', {'form': form, 'expr': expr_b})
