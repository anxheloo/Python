# Create your views here.

from django.http import HttpResponse
# We import render so instead of returning a HTTP Response we use render
from django.shortcuts import render

# We need to import the Photo model in order to use it
from .models import Photo
# We need to import loader to load this template we created
from django.template import loader
# We need to import this error to handle it
from django.http import Http404


def index(request):

    # This line connect to DB and extract all the objects
    all_photos = Photo.objects.all()

    # This line gets the path where template is located
    # After using render we also dont need to use the template loader
    # template = loader.get_template('photoapp/index.html')

    context = {
        'all_photos': all_photos
    }

    # render function is more efficent than HttpResponse & you dont have to load the template, we just pass the request,path and context
    return render(request, 'photoapp/index.html', context)

    # We comment this so we can use render instead of HTTPResponse
    # return HttpResponse(template.render(context, request))

    '''
    WE HAVE TO DELETE THIS IN ORDER TO USE TEMPLATES for frontend

    all_photos = Photo.objects.all()

    html = ''

    for x in all_photos:

        # we build the link
        url = '/photos/' + str(x.id) + '/'

        # here we return an html response thats an anchor tag
        html += '<a href = "' + url + '">' + str(x.name) + '</a><br>'

        print(url)  # just for myself to check the output
        print(html)  # just for myself to check the output

        return HttpResponse(html)
    '''


def detail(request, photo_id):
    # We delete this so we handle the DB elements, and raise error if the id we are searching doesnt exist
    # return HttpResponse('<h2>This is the page for Photo: ' + str(photo_id) + '</h2>')

    # 1-Try to get the data from DB
    try:
        # 2-Get photo by id
        photoById = Photo.objects.get(id=photo_id)
    # 3-If it doesnt exist raise 404 error
    except Photo.DoesNotExist:
        raise Http404('Photo not found')

    return render(request, 'photoapp/detail.html', {'photoById': photoById})
