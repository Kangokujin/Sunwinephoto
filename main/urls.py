from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='main'),
    path('about-me', views.about, name='about'),
    path('single', views.single, name='single'),
    path('services', views.services, name='services'),
    path('contact', views.contact, name='contact'),
    path('category/<str:category>/', views.CategoryListView.as_view())
]
