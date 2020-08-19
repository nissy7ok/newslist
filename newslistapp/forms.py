from django import forms

class StockForm(forms.Form):
    created_at = forms.CharField()
    title = forms.CharField()
    name = forms.CharField()
    url = forms.CharField()