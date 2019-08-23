from django.shortcuts import render
from .models import Category

def index(request):
    face_and_eyes = Category.objects.filter(cat_type = 0)
    hand = Category.objects.filter(cat_type = 1)
    crown = Category.objects.filter(cat_type = 2)
    foot = Category.objects.filter(cat_type = 3)
    suit = Category.objects.filter(cat_type = 4)
    respiratory_tract = Category.objects.filter(cat_type = 5)

    context = {
        'face_and_eyes' : face_and_eyes,
        'hand' : hand,
        'crown' : crown,
        'foot' : foot,
        'suit' : suit,
        'respiratory_tract' : respiratory_tract,
    }
    return render(request ,'category/index.html',context)