from django.shortcuts import render ,redirect,get_object_or_404
from .forms import BookForm ,CategoryForm
from .models import *

def index(request):
    
    form = BookForm()

    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid(): 
            form.save()  
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()

        else:
         form = CategoryForm()
    
    context = {
        'Gategory': Gategory.objects.all(),
        'books': Book.objects.all(),
        'forms': form ,
        'catform' : CategoryForm(),
        'allbooks' :Book.objects.filter(active=True).count,
        'statussold' :Book.objects.filter(status='sold').count,
        'statusrental' :Book.objects.filter(status='rental').count,
        'statusavailble' :Book.objects.filter(status='availble').count,

    }
    
    
    
    return render(request, 'pages/index.html', context)

def books(request):

    context = {
        'Gategory': Gategory.objects.all(),
        'books': Book.objects.all(),
    }
    return render(request, 'pages/books.html', context)

def update(request,id):
    book_id=Book.objects.get(id=id)
    if request.method == 'POST':
        book_update = BookForm(request.POST, request.FILES,instance=book_id)
        if book_update.is_valid():
         book_update.save()
         return redirect('/')  

    else:
         book_update=BookForm(instance=book_id)
         
    context = {
        'book_update' : book_update,
        'Gategory': Gategory.objects.all(),
    }
    return render(request, 'pages/update.html', context)

def delete(request,id):
    book_id_delete=get_object_or_404(Book ,id=id)
    if request.method == 'POST':
        book_id_delete.delete()
        return redirect('/')  

    context = {
        'Gategory': Gategory.objects.all(),
    }
    return render(request, 'pages/delete.html', context)
