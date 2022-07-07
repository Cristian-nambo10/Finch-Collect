from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
    return render(request, 'about.html')


class Finch:
    def __init__(self, name, family, age, description):
        self.name = name
        self.family = family
        self.order = age
        self.description = description

finch = [
    Finch('Test', 'hi', 'tall', 'Small and cute'),
    Finch('test2', 'no', 'short', "Small but fierce"),
    Finch('test3', 'lin', 'average', 'Big and scared'),
]

def finch_index(request):
    # finches = Finch.objects.all()
    return render(request, 'finches/index.html', {'finch': finch})