from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import generic
from django.template import loader
from django.shortcuts import render, redirect

from .models import Book

class IndexView(generic.ListView):
    template_name = 'manbooks/index.html'
    context_object_name = 'all_book_list'

    def get_queryset(self):
        return Book.objects.all()

class DetailView(generic.DetailView):
    model = Book
    template_name = 'manbooks/detail.html'

def newbook(request):
    # return HttpResponseRedirect(reverse('manbooks:newbook'))
    return render(request, 'manbooks/newbook.html')

def addnew(request):
    abook = Book(book_name = request.POST['bookname'],
        author_name=request.POST['authorname'],
        link_addr=request.POST['linkaddr'],
        pub_year=request.POST['pubyear'])
    abook.save()
    return HttpResponseRedirect('/manbooks')

def delbook(request, book_id):
    book=Book.objects.get(pk=book_id)
    book.delete()
    return HttpResponseRedirect('/manbooks')