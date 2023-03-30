
''' -> We Comment everything in order to use Generic views

from django.shortcuts import render

# Create your views here.

#1-We need to display something to the User. In order to Respond to the Request
from django.http import HttpResponse
from .models import book                    #-> we need to import the book model in order to use it
from django.template import loader          #-> we import loader which is going to load our template
from django.shortcuts import render
from django.http import Http404

def index(request):

    #We import the book class from models & save datas from our database in a variable
    all_books = book.objects.all()

    #template = loader.get_template('books/index.html')
    context = {
        'all_books':all_books
    }

    #print(all_books) -> trying for myself

    #return HttpResponse(template.render(context,request))
    return render(request,'books/index.html',context)


def detail(request,book_id):
    try:
        #we get here the book object by id
        get_book_by_id = book.objects.get(id=book_id)

        #we pass here the book class
    except book.DoesNotExist:
        raise Http404('THis book does not exist')

    #print(get_book_by_id)
    #print(get_book_by_id.name)
    #print(get_book_by_id.type)      -> THis all works
    #print(get_book_by_id.author)

    return render(request, 'books/detail.html', {'get_book_by_id':get_book_by_id})
    #return HttpResponse("<h2>Details for Book ID:" + str(book_id) + "</h2>")
'''

from django.views import generic
from .models import book
from django.views.generic.edit import CreateView

#View we display on index file
class IndexView(generic.ListView):
    template_name = 'books/index.html'

    def get_queryset(self):
        return book.objects.all()



#For Add Book
class DetailView(generic.DetailView):
    model = book
    template_name = 'books/detail.html'



class BookCreate(CreateView):
    model = book
    fields = ['name','author','price','type','book_image']