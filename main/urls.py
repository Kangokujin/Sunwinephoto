from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='main'),
    path('about-me', views.about, name='about'),
    path('portfolio', views.portfolio, name='portfolio'),
    path('blog', views.blog, name='blog'),
    path('category/<str:category>/', views.CategoryListView.as_view())
]
