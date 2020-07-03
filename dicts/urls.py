from django.urls import path
from . import views


urlpatterns = [
    path('categories/', views.CategoryModelView.as_view({'get': 'list'}), name='categories'),
    path('brands/', views.BrandModelView.as_view({'get': 'list'}), name='brands'),
]
