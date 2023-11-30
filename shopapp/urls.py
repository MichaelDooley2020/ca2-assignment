from django.urls import path
from . import views

app_name = 'shopapp'

urlpatterns = [
    path('', views.prod_list, name='all_products'),
    path('<uuid:category_id>/', views.prod_list, name='products_by_category'),
]
