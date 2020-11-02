from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyze(request):
    texts = request.POST.get('text', 'default')
    remove_punctuations = request.POST.get('removepunc', 'off')
    full_uppercase = request.POST.get('fulluppercase', 'off')
    newline_remover = request.POST.get('newlineremover', 'off')
    extraspace_remover = request.POST.get('extraspaceremover', 'off')
    char_count = request.POST.get('charcount', 'off')
    print(remove_punctuations)
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

    analyzed = ""
    if remove_punctuations == 'on':
        for char in texts:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Remove Punctuations', 'analyzed_text': analyzed}
    elif full_uppercase == 'on':
        for char in texts:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Lower to Upper Case', 'analyzed_text': analyzed}
    elif newline_remover == 'on':
        analyzed = ""
        for char in texts:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose': 'Remove NewLine', 'analyzed_text': analyzed}
    elif extraspace_remover == 'on':
        analyzed = ""
        for index, char in enumerate(texts):
            if texts[index] == " " and texts[index + 1] == " ":
                pass
            else:
                analyzed = analyzed + char
        params = {'purpose': 'Remove Extra space', 'analyzed_text': analyzed}
    elif char_count == 'on':
        analyzed = ""
        count = len(texts)
        params = {'purpose': 'No of Characters', 'analyzed_text': count}
    else:
        return HttpResponse("Error! Please choose from the options given")
    return render(request, 'analyze.html', params)

