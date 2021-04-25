from django import forms

class CommandForm(forms.Form):
    body = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "Введите новую команду!"
        })
    )  