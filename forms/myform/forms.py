from django import forms
from .models import Form1Submission, Form2Submission  # Import your models

class Form1(forms.ModelForm):
    class Meta:
        model = Form1Submission  # Link to the Form1Submission model
        fields = ['name', 'mobile_number', 'hobbies']

class Form2(forms.ModelForm):
    class Meta:
        model = Form2Submission  # Link to the Form2Submission model
        fields = ['name', 'subject_marks']
