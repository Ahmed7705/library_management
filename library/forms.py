from django import forms
from .models import Book,Gategory

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Gategory
        fields = ['name'] 
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'})}
 
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'title', 'author', 'photo_book', 'photo_author', 'pages', 'price',
            'retal_price_day', 'retal_period', 'active', 'status', 'category'
        ]
        labels = {
            'title': 'عنوان الكتاب',
            'author': 'اسم المؤلف',
            'photo_book': 'صورة الكتاب',
            'photo_author': 'صورة المؤلف',
            'pages': 'عدد الصفحات',
            'price': 'السعر',
            'retal_price_day': 'سعر الإيجار اليومي',
            'retal_period': 'فترة الإيجار (بالأيام)',
            'active': 'نشط',
            'status': 'حالة الكتاب',
            'category': 'التصنيف'
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'photo_book': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'photo_author': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'pages': forms.NumberInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'retal_price_day': forms.NumberInput(attrs={'class': 'form-control'}),
            'retal_period': forms.NumberInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }
