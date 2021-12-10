from . import views
from django.urls import include, re_path

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^new/(?P<et>(\w|-)+)/$', views.new, name='new'),
    re_path(r'^expr/$', views.ExprListView.as_view(), name='expr'),
    re_path(r'^eq/$', views.EquationListView.as_view(), name='eq'),
    re_path(r'^expr/(?P<pk>(\w|-)+)/$', views.expr_solve_view, name='expr_solve'),
]
