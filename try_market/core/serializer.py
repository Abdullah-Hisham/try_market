from rest_framework import serializers
from .models import *

class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = seller
        fields = '__all__'
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = product
        fields = '__all__'
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = order
        fields = '__all__'

class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = reviews
        fields = '__all__'
class Product_info_Serializers(serializers.ModelSerializer):
    class Meta :
        model = product
        fields = ['seller_name']


