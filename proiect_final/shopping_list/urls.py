from django.urls import path
from shopping_list import views
# from products import views

app_name = 'shopping_list'

urlpatterns = [
    path('', views.ShoppingListView.as_view(), name='lista_cumparaturi'),
    path('adaugare/', views.CreateShoppingListView.as_view(), name = 'adauga'),
    path('modificare/<int:pk>/', views.UpdateShoppingListView.as_view(), name='modifica'),
    path('sterge/<int:pk>/', views.deactivate_products, name='dezactiveaza'),
]