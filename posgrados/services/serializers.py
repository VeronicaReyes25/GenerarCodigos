from django.contrib.auth.models import User, Group, Permission, PermissionsMixin
from rest_framework import serializers


from .models import  Noticia, Aspirante,Image, Validacion


class RolUsuariosSerializer(serializers.HyperlinkedModelSerializer):

    users_list = serializers.SerializerMethodField()
    def get_users_list(self, instance):
        users=[]
        u=instance.users.get_queryset()
        for i in u:
            users.append(i.desc)
        return users

    class Meta:
        model = Group
        fields =('users_list', )




class PermisionsMixinSerializer(serializers.ModelSerializer):
    class Meta:
        model = PermissionsMixin
        fields = '__all__'


class PermisionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = '__all__'


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name')
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class User1Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name')


    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class NoticiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Noticia
        fields = '__all__'


class AspiranteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aspirante
        fields = '__all__'


class ImgSerializer(serializers.ModelSerializer):
    img = serializers.ImageField(max_length=None, use_url=True)

    class Meta:
        model= Image
        fields= '__all__'

class CodigoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Validacion
        fields = '__all__'