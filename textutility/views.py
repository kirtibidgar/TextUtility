#I have create this file
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


# def EXercise2(request):
def analyze(request):
    #get the text value
    djtext = request.POST.get('text', 'defaulttext')

    #get the checkbox value
    removePunc = request.POST.get('removePunc', 'off')
    fullCaps = request.POST.get('fullCaps', 'off')
    newLineRemover = request.POST.get('newLineRemover', 'off')
    spaceRemover = request.POST.get('spaceRemover', 'off')
    extraSpaceRemover = request.POST.get('extraSpaceRemover', 'off')
    charCount = request.POST.get('charCount', 'off')

    analayzed=''
    purposeTitle=''
    #check coonditions
    if removePunc  == 'on':
        purposeTitle= purposeTitle + 'Removed Punctuations' + ', '
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~`'''
        for char in djtext :
            if char not in punctuations:
                analayzed =  analayzed+ char
        djtext = analayzed


    if fullCaps == 'on':
        analayzed=''
        purposeTitle =purposeTitle + 'Changed to Uppercase' + ', '
        # analayzed=djtext.upper()
        for char in djtext :
            analayzed=analayzed + char.upper()
        djtext = analayzed


    if newLineRemover == 'on':
        analayzed = ''
        purposeTitle = purposeTitle + 'Removed NewLines' + ', '
        for char in djtext :
            # if char != '/n':
            if char != "\n" and char != "\r":
                analayzed = analayzed + char
        djtext = analayzed


    if spaceRemover == 'on':
        analayzed = ''
        purposeTitle = purposeTitle + 'Removed Space' +', '
        for char in djtext :
            if char != ' ':
                analayzed = analayzed + char
        djtext = analayzed

    if extraSpaceRemover == 'on':
        analayzed = ''
        purposeTitle = purposeTitle + 'Removed Extra Space' +', '
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analayzed = analayzed + char
        djtext = analayzed


    # if charCount == 'on':
    #     # analyzed = len(djtext)
    #     purposeTitle = purposeTitle + 'Number of Characters' +', '
    #     i=0;
    #     for char in djtext:
    #         i = i + 1
    #     analayzed = i

    if(removePunc != "on" and newLineRemover!="on" and extraSpaceRemover!="on" and fullCaps!="on"):
        return HttpResponse("please select any operation and try again")


    params = {'purpose': purposeTitle, 'analyze_ext': analayzed}
    return render(request, 'analyze.html', params)