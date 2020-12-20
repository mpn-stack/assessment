from rest_framework import serializers
from .models import Customers
from django.utils import timezone
from .randomid import get_random_number
from django.core.cache import cache

class CustomersSerializer (serializers.ModelSerializer):
    
    class Meta:
        model = Customers
        fields = '__all__'
        read_only_fields =  ('tracking_code', 'created_date', 'update_date', 'status', )
    
    def create(self, validated_data):
        obj = super().create(validated_data)
        obj.created_date = timezone.now()
        obj.tracking_code = get_random_number()
        obj.status = 1
        obj.save()
        return obj


class CustomersUpdateSerializer (serializers.ModelSerializer):
    
    class Meta:
        model = Customers
        fields = '__all__'
        read_only_fields =  ('tracking_code', 'created_date', 'update_date', )

    def update(self, instance, validated_data):
        obj = super().update(instance, validated_data)
        obj.update_date = timezone.now()
        obj.save()
        if obj.status != 1 :
            cache.set(obj.tracking_code, obj)
        return obj        

class GetCustomersSerializer (serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = '__all__'
        read_only_fields =  ('first_name','last_name','national_code','created_date', 'update_date', 'status', ) 
            
    