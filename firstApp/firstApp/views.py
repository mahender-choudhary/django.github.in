from django.http import  HttpResponse
from django.shortcuts import render
def index(request):
    return render(request, 'index.html')


def analyze(request):
    var1 = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremove = request.POST.get('newlineremove', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')

    if removepunc == 'on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in var1:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Remove Punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif(fullcaps == 'on'):
        analyzed = ""
        for char in var1:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Change to Uppercase', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif(newlineremove == 'on'):
        analyzed = ""
        for char in var1:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose': 'Remove New Line', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif(extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(var1):
            if not (var1[index] == " " and var1[index + 1] == " "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}

        # Analyze the text
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse("Error")