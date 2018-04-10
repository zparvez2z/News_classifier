from django.shortcuts import render
from django.http import HttpResponse
from . import natural_language_processing
import json


def index(request):
    context = {

    }
    return render(request,'index.html',context)

def classify(request):
    if request.method == 'POST':
        query = request.POST.get('news',None)
        print(type(query))
        print(query)
        result = natural_language_processing.predict_news(query)
        result = result[0]
        if result == 0:
            return HttpResponse("Other News")
        elif result == 1:
            return HttpResponse(" Sports news !!!")
    else:
        pass
