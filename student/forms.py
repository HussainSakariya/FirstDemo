from django import forms
from .models import student

class student_form(forms.ModelForm):
    no=forms.IntegerField(widget=forms.NumberInput(),required=True)
    name=forms.CharField(widget=forms.TextInput(),required=True,max_length=10)
    age=forms.IntegerField(widget=forms.NumberInput(),required=True)

    class Meta():
        model=student
        fields=["no","name","age"]

        # excludes=[] which field you dont want to use ..........its vice versa......... fields
