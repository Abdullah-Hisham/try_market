from django.urls import path,include
from .views import *
from core import views

urlpatterns = [
    path('product_list',product_list.as_view()),
    path('seller_product/<int:pk>/',views.seller_product),
    path('try/',views.tryy),
    path('order/',order_list.as_view()),
    path('reviews/',views.review_list.as_view()),
    path('product_reviews/<int:pk>/',views.product_reviews),
    path('product_info/<int:pk>/',views.product_info),
    path('auth/',auth.as_view()),
    path('make_order/<int:pk>',views.make_order),


]
