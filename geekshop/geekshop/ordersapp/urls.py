import ordersapp.views as ordersapp
from django.urls import path

app_name="ordersapp"

urlpatterns = [
    path('', ordersapp.OrderList.as_view(), name='list'),
    path('forming/complete/<pk>', ordersapp.forming_complete, name='forming_complete'),
    path('create/', ordersapp.OrderItemsCreate.as_view(), name='create'),
    path('read/<pk>/', ordersapp.OrderRead.as_view(), name='read'),
    path('update/<pk>/', ordersapp.OrderItemsUpdate.as_view(), name='update'),
    path('delete/<pk>/', ordersapp.OrderDelete.as_view(), name='delete'),
    path('product/<int:pk>/price/', ordersapp.get_product_price),

]
