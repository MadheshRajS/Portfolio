from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def GiveResponse(request):
    return render(request, 'WebDevApp/RajCards.html')
