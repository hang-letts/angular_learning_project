from rest_framework import serializers
from django.db.models import fields
from .models import LoginModel, ProfileModel

class LoginModelSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    # email=serializers.CharField(max_length=100)
    email=serializers.EmailField(max_length=100)
    psswrd=serializers.CharField(max_length=100,style={'input_type': 'password'})
    class Meta:
        model=LoginModel
        fields='__all__'
    
    def create(self, validated_data):
        return LoginModel.objects.create(**validated_data)

    def update(self, instance, validated_data):
        email=validated_data.get('email',instance.email)
        psswrd=validated_data.get('psswrd',instance.psswrd)
        instance.save()
        return instance

#Profile
class ProfileModelSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    first_name=serializers.CharField(max_length=100)
    last_name=serializers.CharField(max_length=100)
    # email=serializers.CharField(max_length=100)
    email=serializers.EmailField(max_length=100)
    phone_no=serializers.CharField(max_length=10)
    class Meta:
        model=ProfileModel
        fields='__all__'
    
    def create(self, validated_data):
        return ProfileModel.objects.create(**validated_data)

    def update(self, instance, validated_data):
        first_name=validated_data.get('first_name',instance.first_name)
        last_name=validated_data.get('last_name',instance.last_name)
        email=validated_data.get('email',instance.email)
        phone_no=validated_data.get('phone', instance.phone_no)
        instance.save()
        return instance
