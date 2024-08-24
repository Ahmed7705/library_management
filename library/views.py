from django.shortcuts import render


def books(request):
    return render(request, 'pages/index.html')

def author_detail(request):
    return render(request, 'pages/books.html')
