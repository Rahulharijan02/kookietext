
from this import d
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
   
    return render(request, 'index.html')


def analyze(request):
    
    djtext = request.POST.get('text', 'default')
    removepunc=request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    spaceremover = request.POST.get('spaceremover', 'off')
   

    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif(fullcaps== "on"):
        analyzed=" "
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Change to Uppercase', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)    
    elif newlineremover=="on":
        analyzed=""
        for char in djtext:    
             if char!="\n" and char!="r":
                 analyzed=analyzed+char
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}


        return render(request, 'analyze.html', params)           
    elif(spaceremover== "on"):
        analyzed = " "
        for index, char in enumerate(djtext):
            if not(djtext[index]== " " and djtext[index+1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'Extra Space Remover', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params) 
                 
    else:
        return HttpResponse('Error') 


