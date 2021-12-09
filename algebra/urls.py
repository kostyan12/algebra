from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^new/(?P<et>(\w|-)+)/$', views.new, name='new'),
    url(r'^expr/$', views.ExprListView.as_view(), name='expr'),
    url(r'^eq/$', views.EquationListView.as_view(), name='eq'),
    url(r'^expr/(?P<pk>(\w|-)+)/$', views.expr_solve_view, name='expr_solve'),
]
