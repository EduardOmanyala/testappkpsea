from django.urls import path
from storepage import views as order_views

urlpatterns = [
    path('create/order', order_views.createOrder, name='order_create'),
    path('update/order/<int:id>/', order_views.OrderUpdate, name='order_update'),
    path('order/details/<int:id>/', order_views.OrderDetail, name='order_detail'),
    path('mainpage', order_views.mainpage, name='mainpage'),
   
]