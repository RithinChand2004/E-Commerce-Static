from django.shortcuts import render, redirect, get_object_or_404
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

def form1_list(request):
    submissions = Form1Submission.objects.all()  # Retrieve all Form1 submissions
    return render(request, 'form1_list.html', {'submissions': submissions})

def form2_list(request):
    submissions = Form2Submission.objects.all()  # Retrieve all Form2 submissions
    return render(request, 'form2_list.html', {'submissions': submissions})

# Edit form1 submission
def edit_form1(request, id):
    submission = get_object_or_404(Form1Submission, id=id)
    if request.method == 'POST':
        form = Form1(request.POST, instance=submission)
        if form.is_valid():
            form.save()
            return redirect('form1_list')
    else:
        form = Form1(instance=submission)
    return render(request, 'edit_form1.html', {'form': form})

# Delete form1 submission
def delete_form1(request, id):
    submission = get_object_or_404(Form1Submission, id=id)
    if request.method == 'POST':
        submission.delete()
        return redirect('form1_list')
    return render(request, 'delete_confirmation.html', {'submission': submission})

# Similarly for form2
def edit_form2(request, id):
    submission = get_object_or_404(Form2Submission, id=id)
    if request.method == 'POST':
        form = Form2(request.POST, instance=submission)
        if form.is_valid():
            form.save()
            return redirect('form2_list')
    else:
        form = Form2(instance=submission)
    return render(request, 'edit_form2.html', {'form': form})

def delete_form2(request, id):
    submission = get_object_or_404(Form2Submission, id=id)
    if request.method == 'POST':
        submission.delete()
        return redirect('form2_list')
    return render(request, 'delete_confirmation.html', {'submission': submission})
