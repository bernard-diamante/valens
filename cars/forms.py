from django import forms
from .models import *

class add_CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = [
            "name",
            "color",
            "position"
            ]

class update_CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = [
            "name",
            "color",
            "position"
            ]

class delete_CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = [
            "name",
            ]