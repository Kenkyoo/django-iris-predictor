# predictor/forms.py
from django import forms

class IrisForm(forms.Form):
    sepal_length = forms.FloatField(widget=forms.NumberInput(attrs={"class": "input", "placeholder": "e.g. 5.1"}))
    sepal_width  = forms.FloatField(widget=forms.NumberInput(attrs={"class": "input", "placeholder": "e.g. 3.5"}))
    petal_length = forms.FloatField(widget=forms.NumberInput(attrs={"class": "input", "placeholder": "e.g. 1.4"}))
    petal_width  = forms.FloatField(widget=forms.NumberInput(attrs={"class": "input", "placeholder": "e.g. 0.2"}))