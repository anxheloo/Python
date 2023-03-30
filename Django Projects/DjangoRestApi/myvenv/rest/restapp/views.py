from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TaskSerializer, UserSrializer
from .models import Task
import django_filters.rest_framework
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated,AllowAny
from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView

# Create your views here.

class TaskViewSet(viewsets.ModelViewSet):

    # Views cannot be accessed unless users are logged in | We also need to build a user model(serializers.py)
    permission_classes = (IsAuthenticated,)

    queryset = Task.objects.all().order_by("date_created")
    serializer_class = TaskSerializer

    #This allows us to define different types of filters available
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ('completed',) #we filter by completed -> http://127.0.0.1:8000/task/?completed=True
    ordering = ('date_created',)
    search_fields = ('task_name',)  #we search(filter) by image -> http://127.0.0.1:8000/task/?search=image


class CreateUserView(CreateAPIView):
    model = get_user_model()
    permission_classes = (AllowAny,)
    serializer_class = UserSrializer

''' We commented these cuz now we are going to use filters 
class DueTaskViewSet(viewsets.ModelViewSet):

    #List out those tasks that are not completed
    queryset = Task.objects.all().order_by("date_created").filter(completed = False)
    serializer_class = TaskSerializer

    # List out those tasks that are completed
class CompletedTaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by("date_created").filter(completed = True)
    serializer_class = TaskSerializer

'''


