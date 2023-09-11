from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect


# Create your views here.

def redirect_view(request):
    response = redirect('')
    return response
def inpu(request):
    if request.method == "POST":
        data = request.POST
        with open("word.txt", 'a', encoding='utf-8') as file:
            fword = data['fword']
            sword = data['sword']
            fword = fword.strip()
            sword = sword.strip()
            file.write(fword + " " + sword +"\n")
            return HttpResponseRedirect('/')
    else:
        return render(request,'dictionary/add.html')


def outpu(request):
    ln = []
    with open("word.txt", 'r', encoding='utf-8') as file:
        for line in file:
            ln.append(line.rstrip())
            if not line:
                break
    context = {'lines': ln}
    return render(request, 'dictionary/index.html', context)
