
from django.http import HttpResponse
from django.shortcuts import render


# def homeMethodXXX(request):
# 	return HttpResponse('hello motherfuckas')

# def jayNepal(request):
# 	return HttpResponse('<h1>THuikka maobadi mug gu kha</h1>')

def homepage(request):
	return render(request, 'homepage.html')
	
def count(request):
	fulltext = request.GET['fulltext']
	worddict = fulltext.split()
	d = {}
	for word in worddict:
		if word in d:
			d[word] += 1
		else:
			d[word] = 1

	d = sorted(d.items(), key=lambda x: x[1], reverse=True)

	return render(request, 'count.html',{'fulltext':fulltext,'count':len(worddict), 'wordcount':d})

def about(request):
	return render(request, 'about.html')