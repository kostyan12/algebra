from django.contrib import admin

from algebra.models import ExprTypes, Expressions, SolvedExpressions

# Register your models here.

admin.site.register(ExprTypes)


@admin.register(Expressions)
class ExprTypesAdmin(admin.ModelAdmin):
    list_display = ('text', 'text_r', 'result', 'expr_type')
    list_filter = ('expr_type',)

    fieldsets = (
        (None, {
            'fields': ('text', 'text_r', 'result')
        }),
        ('Expression type', {
            'fields': ('expr_type', )
        }),
    )


# admin.site.register(Expressions)


#  admin.site.register(SolvedExpressions)
@admin.register(SolvedExpressions)
class SolvedExpressionsAdmin(admin.ModelAdmin):
    list_display = ('expr', 'user', 'solv_date', 'result', 'trys')
    list_filter = ('user', 'expr__expr_type')

    fieldsets = (
        (None, {
            'fields': ('expr', 'result', 'trys')
        }),
        ('Solved', {
            'fields': ('user', 'expr__expr_type')
        }),
    )
