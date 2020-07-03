from django.urls import path

from . import views


urlpatterns = [
    path('properties/', views.PropertyModelView.as_view({'get': 'list'}), name='properties'),
    path('products/', views.ProductModelView.as_view({'get': 'list'}), name='products'),
    path('products/<int:pk>/', views.ProductModelView.as_view({'get': 'retrieve'}), name='product'),
]
