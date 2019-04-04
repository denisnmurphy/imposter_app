from django.shortcuts import render
from django.http import HttpResponse
from .forms import QuestionOneForm, QuestionTwoForm, QuestionThreeForm
# Create your views here.

def question_one_detail(request):

    if request.method == 'POST':
        form = QuestionOneForm(request.POST)
        if form.is_valid():
            form.save()


    form = QuestionOneForm()
    return render(request, 'form.html', {'form': form})


def question_two_detail(request):

    if request.method == 'POST':
        form = QuestionTwoForm(request.POST)
        if form.is_valid():
            form.save()


    form = QuestionTwoForm()
    return render(request, 'secondform.html', {'form': form})

def question_three_detail(request):

    if request.method == 'POST':
        form = QuestionThreeForm(request.POST)
        if form.is_valid():
            form.save()


    form = QuestionThreeForm()
    return render(request, 'finalform.html', {'form': form})
