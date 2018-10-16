from rest_framework import serializers
from .models import Employee,Category

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields='__all__'

class CategorySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    cat_name=serializers.CharField(max_length=50)
    cat_des=serializers.CharField(max_length=50)
    cat_id=serializers.IntegerField()
    class Meta:
        model=Category
        fields='__all__'
    
    def create(self, validated_data):
        return Category.objects.create(**validated_data)

    def update(self, instance, validated_data):
        cat_name=validated_data.get('cat_name',instance.cat_name)
        cat_des=validated_data.get('cat_des',instance.cat_des)
        cat_id=validated_data.get('cat_id',instance.cat_id)
        instance.save()
        return instance


