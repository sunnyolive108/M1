from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def contribution(request):
    contribution = request.GET['contribution']
    return render(request, 'contribution.html', {'contribution': contribution})

def thankyou(request):
    return render(request, 'thankyou.html')
