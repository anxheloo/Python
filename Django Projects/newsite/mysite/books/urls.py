from django.contrib import admin
from django.urls import path, re_path
from . import views          #we import the views class in order to use the function



#We can use 're_path' with regular expressions cuz 'path' doesnt allow regular expressions

# urlpatterns = [
#    re_path(r'^$', views.index, name='index'),
#    #/books/2/
#    re_path(r'^(?P<book_id>[0-9]+)/$', views.detail, name='detail'),
# ]


#Or we can use path this way without regular expressions

# urlpatterns = [
#    path('', views.index, name='index'),
#    path('<int:book_id>/', views.detail, name="detail"),
# ]


# #For Generic Views we replace these 2 attributes:
urlpatterns = [
   re_path(r'^$', views.IndexView.as_view(), name='index'),
   #/books/2/
   re_path(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
   re_path(r'books/add/$', views.BookCreate.as_view(), name='books-add'),
]



