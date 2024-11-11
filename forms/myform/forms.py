from django import forms

class Form1(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    mobile_number = forms.CharField(label='Mobile Number', max_length=15)
    hobbies = forms.CharField(label='Hobbies', widget=forms.Textarea)

class Form2(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    subject_marks = forms.IntegerField(label='Subject Marks')
