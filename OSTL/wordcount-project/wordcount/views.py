from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def count(request):
    fulltext = request.GET['fulltext']
    word_list = fulltext.split()
    max_count = 0
    max_word = ''
    #number of occurences of a word in the list
    for word in  word_list:
        count = 1
        for other_word in word_list[word_list.index(word)+1:]:
            if word.lower() == other_word.lower():
                count += 1
                if count >= max_count:
                    max_word = word
                    max_count = count
    return render(request, 'count.html', {'fulltext': fulltext, 'count': len(word_list), 'max_word': max_word, 'max_count': max_count })