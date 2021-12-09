from django import forms


class ExprSolveForm(forms.Form):
    solved = forms.CharField(label="Enter your answer")

    def clean_solved(self):
        data = self.cleaned_data['solved']
        return data

