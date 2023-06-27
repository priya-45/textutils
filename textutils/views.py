from django.http import HttpResponse
from django.shortcuts import render


# def index(request):
#     params = {"name":"priya", "from" :"up"}
#     print(request.GET.get('text','default'))
#     return render(request, "index.html",params)

#     return HttpResponse("Home")

# def removepunc(request):
#     return HttpResponse("remove punc")

# def capfirst(request):
#     print(request.GET.get('text','default'))
#     return HttpResponse("capitalize first")

# def newlineremove(request):
#     return HttpResponse("newline remove first")


# def spaceremove(request):
#     return HttpResponse("space remover back")

# def charcount(request):
#     return HttpResponse("charcount ")


# def analyze(request):
    
#     # Get the text
#     djtext = request.GET.get('text', 'default')
#     analyzed=djtext
#     params = {'purpose': "Removing Punctuations", 'analyzed_text': analyzed}
#     return render(request,'analyze.html',params)



def index(reques):
    return render(reques, 'index.html')

def analyze(request):
    # Get the text
    djtext = request.GET.get('text', 'default')
    removepunc=request.GET.get('removepunc','off')
    caps=request.GET.get('caps','off')
    newline=request.GET.get('newlineremove','off')
    space=request.GET.get('spaceremove','off')
    count=request.GET.get('count','off')

    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        # return render(request, 'analyze.html', params)
        djtext = analyzed
        print(djtext)
    
    if caps=="on":
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params = {'purpose': 'IN UPPER CASE ', 'analyzed_text': analyzed}
        # return render(request, 'analyze.html', params)
        djtext = analyzed
    if newline=="on":
        analyzed=""    
        for char in djtext:
            if char!="/n":
                analyzed=analyzed+char
        params = {'purpose': 'New line remove', 'analyzed_text': analyzed}
        # return render(request, 'analyze.html', params)
        djtext=analyzed
    if space=="on":
        analyzed = ""
        for index,char in enumerate(djtext):
            if not (djtext[index]==" " and djtext[index+1]==" "):
                analyzed = analyzed + char
        params = {'purpose': 'Removed Extra space', 'analyzed_text': analyzed}
        # return render(request, 'analyze.html', params)
        djtext=analyzed
    if count=="on":
        analyzed=len(djtext)
        params = {'purpose': 'count charachters', 'analyzed_text': analyzed}
        djtext=analyzed
    if removepunc != "on" and caps != "on" and newline != "on" and space != "on" and count != "on":
        return HttpResponse("Eroor! You didn't select any opration so that's why you got Error")

    return render(request, 'analyze.html', params)



    