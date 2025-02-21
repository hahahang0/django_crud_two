from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import Books
from .forms import BooksForm

# Create your views here.

def getBooks(request):
    books = Books.objects.all()
    return render(request,'books/books_list.html',{'books':books})

def createBooks(request):
    if request.method == "POST":
        form = BooksForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('books_list')
        
    else : 
        form = BooksForm()
    return render(request,'books/create.html',{'form' : form})


def updateBooks(request,pk):
    books = get_object_or_404(Books,book_id= pk)
    if request.method == "POST": 
        form = BooksForm(request.POST,request.FILES,instance=books)
        form.save()
        return redirect('books_list')
    else : 
        form = BooksForm(instance=books)
        return render(request,'books/update.html',{'form' : form})
    
def deleteBooks(request,pk):
    book = get_object_or_404(Books,book_id=pk)
    if request.method == "POST" : 
        book.delete()
    return redirect('books_list')
    
