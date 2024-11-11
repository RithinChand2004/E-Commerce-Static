from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import Form1, Form2
from .models import Form1Submission, Form2Submission

def home(request):
    return render(request, 'home.html')

def form1_view(request):
    if request.method == 'POST':
        form = Form1(request.POST)
        if form.is_valid():
            # Save form data to the database
            Form1Submission.objects.create(
                name=form.cleaned_data['name'],
                mobile_number=form.cleaned_data['mobile_number'],
                hobbies=form.cleaned_data['hobbies']
            )
            return HttpResponse("Form 1 Submitted")
    else:
        form = Form1()
    return render(request, 'form1.html', {'form': form})

def form2_view(request):
    if request.method == 'POST':
        form = Form2(request.POST)
        if form.is_valid():
            # Save form data to the database
            Form2Submission.objects.create(
                name=form.cleaned_data['name'],
                subject_marks=form.cleaned_data['subject_marks']
            )
            return HttpResponse("Form 2 Submitted")
    else:
        form = Form2()
    return render(request, 'form2.html', {'form': form})
