from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')
    # render는 3개의 인자를 받을 수 있고 마지막 인자는 사전형태

def about(request):
    return render(request, 'about.html')

def result(request):
    text = request.GET['fulltext']
    words = text.split()
    word_dictionary = {}

    for word in words:
        if word in word_dictionary:
            #increase
            word_dictionary[word]+=1
        else:
            #add tp dictionary
            word_dictionary[word]=1

    return render(request, 'result.html', {'full':text, 'total':len(words), 'dictionary':word_dictionary.items()})