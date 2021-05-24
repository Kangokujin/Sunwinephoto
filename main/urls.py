from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='main'),
    path('about-me', views.about, name='about'),
    path('gallery', views.gallery, name='gallery'),
    path('services', views.services, name='services'),
    path('contact', views.ContactView.as_view(), name='contact'),
    path('category/<str:category>/', views.CategoryListView.as_view())
]
