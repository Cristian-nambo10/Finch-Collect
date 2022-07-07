from django.shortcuts import render
from django.http import HttpResponse
from main_app.models import Finch

# Create your views here.
def home(request):
    return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
    return render(request, 'about.html')


# class Finch:
#     def __init__(self, name, family, age, description):
#         self.name = name
#         self.family = family
#         self.age = age
#         self.description = description

# finch = [
#     Finch('Test', 'hi', 7, 'Small and cute'),
#     Finch('test2', 'no', 5, "Small but fierce"),
#     Finch('test3', 'lin', 3, 'Big and scared'),
# ]

def finch_index(request):
    finch = Finch.objects.all()
    return render(request, 'finches/index.html', {'finch': finch})

def finch_detail(request, finch_id):
    finch = Finch.objects.get(id=finch_id)
    return render(request, 'finches/detail.html', { 'finch': finch })