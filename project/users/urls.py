from django.urls import path
from . import views



urlpatterns = [
    path('', views.UserList.as_view(), name='user-list'),
    path('<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
    path('register/', views.RegisterView.as_view(), name='user-register'),
    
]