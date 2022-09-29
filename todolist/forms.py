from django import forms
from django import forms
from todolist.models import task

class taskform(forms.ModelForm):
    class Meta:
        model = task
        fields = {"title", "description"}