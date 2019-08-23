from django.shortcuts import render, redirect, get_object_or_404
from .models import Chemistry

def index(request):
    chemistry = Chemistry.objects.all()
    context = {
        'chemistry' : chemistry
    }
    return render(request ,'myapp/index.html',context)

def add(request):
    if request.method == 'POST':
        course = request.POST['course']
        course_number = request.POST['course_number']
        titile = request.POST['title']
        book_number = request.POST['book_number']
        experiment_number = request.POST['experiment_number']
        experiment_name = request.POST['experiment_name']
        chemical_name = request.POST['chemical_name']
        chemical_properties = request.POST['chemical_properties']
        ghs_sign = request.POST['ghs_sign']
        w1 = request.POST['w1']
        w2 = request.POST['w2']
        w3 = request.POST['w3']
        w4 = request.POST['w4']
        w5 = request.POST['w5']
        w6 = request.POST['w6']
        w7 = request.POST['w7']
        w = request.POST['w']
        reactions = request.POST['reactions']

        chemistry = Chemistry(course=course, course_number=course_number, titile=titile, book_number=book_number,
                            experiment_number=experiment_number, experiment_name=experiment_name,
                            chemical_name=chemical_name, chemical_properties=chemical_properties, ghs_sign=ghs_sign,
                            w1=w1, w2=w1, w3=w3, w4=w4, w5=w5, w6=w6, w7=w7, w=w, reactions=reactions)

        if chemistry:
           chemistry.save()
           return redirect('detail')
    return render(request ,'myapp/add.html')

def detail(request, chemistry_id):
    chem = Chemistry.objects.get(pk = chemistry_id)
    context = {
        'chemistry' : chem,
    }
    return render(request ,'myapp/detail.html',context)

def edit_form(request, chemistry_id):
    chemis = Chemistry.objects.get(pk = chemistry_id)
    context = {
        'chemistry' : chemis,
    }
    return render(request ,'myapp/edit.html',context)

def edit_save(request):
    if request.method == 'POST':
        course = request.POST['course']
        course_number = request.POST['course_number']
        titile = request.POST['title']
        book_number = request.POST['book_number']
        experiment_number = request.POST['experiment_number']
        experiment_name = request.POST['experiment_name']
        chemical_name = request.POST['chemical_name']
        chemical_properties = request.POST['chemical_properties']
        ghs_sign = request.POST['ghs_sign']
        w1 = request.POST['w1']
        w2 = request.POST['w2']
        w3 = request.POST['w3']
        w4 = request.POST['w4']
        w5 = request.POST['w5']
        w6 = request.POST['w6']
        w7 = request.POST['w7']
        w = request.POST['w']
        reactions = request.POST['reactions']

        chemistryid = request.POST['chemistryid']

        chemis = Chemistry.objects.get(pk = chemistryid)
        chemis.course = course
        chemis.course_number = course_number
        chemis.titile = titile
        chemis.book_number = book_number 
        chemis.experiment_number = experiment_number
        chemis.experiment_name = experiment_name
        chemis.chemical_name = chemical_name
        chemis.chemical_properties = chemical_properties
        chemis.ghs_sign = ghs_sign
        chemis.w1 = w1
        chemis.w2 = w2
        chemis.w3 = w3
        chemis.w4 = w4
        chemis.w5 = w5
        chemis.w6 = w6
        chemis.w7 = w7
        chemis.w = w
        chemis.reactions = reactions
        chemis.save()
    return redirect('detail')

def delete(request, chemistry_id):
    delete = get_object_or_404(Chemistry, pk=chemistry_id)
    delete.delete() 
    return redirect('index')