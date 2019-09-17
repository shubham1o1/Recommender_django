from django.urls import path
from . import views
# from .views import NewsDetailView

urlpatterns = [
   path('', views.home, name='news-home'),
   path('detail/<str:tags>/<str:username>/', views.detail, name='news-detail'),
   # path('login/', views.login, name='news-login'),
]