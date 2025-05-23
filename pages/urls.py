from django.urls import path , include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('job/', views.job, name='job'),
    path('report/', views.report, name='report'),
    path('product_info/', views.product_info, name='product_info'),
    path('labaratory/', views.labaratory, name='labaratory'),
    path('General/', views.General, name='General'),
    path('cephalosporins/', views.cephalosporins, name='cephalosporins'),
    path('benicillins/', views.benicillins, name='benicillins'),
]
