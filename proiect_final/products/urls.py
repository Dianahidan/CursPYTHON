from django.urls import path
from products import views

app_name = 'products'

urlpatterns = [
    path('', views.ProductsView.as_view(), name='lista_produse'),
    path('adaugare/', views.CreateProductView.as_view(), name = 'adauga'),
    path('modifica/<int:pk>/', views.UpdateProductView.as_view(), name='modifica'),
    path('modifica_necesar/<int:pk>', views.modifica_necesar , name='modifica_necesar'),
    path('cumpara/<int:pk>/', views.cumpara, name='cumpara'),
    path('sterge/<int:pk>/', views.deactivate_products, name='dezactiveaza'),
]