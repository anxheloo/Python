from .models import Task
from rest_framework import serializers
from django.contrib.auth import get_user_model


class UserSrializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = get_user_model().objects.create(
            username = validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


    class Meta:
        model = get_user_model()
        fields = ('username', 'password')

#We create class Serializer for Task (to convert the Task DATAS to JSON format)
class TaskSerializer(serializers.ModelSerializer):

    image = serializers.ImageField(max_length = 1000, use_url=True)

    #we need to provide the infos from model class, name of model and fields we want to display in JSON format
    class Meta:
        model = Task
        fields = ('id','task_name','task_desc','completed','date_created','image')