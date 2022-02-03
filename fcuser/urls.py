from django.urls import path
from . import views   # 현재폴더의 view가져오기

urlpatterns = [
    path('register/', views.register),
    path('login/', views.login),
    path('logout/', views.logout)
]

# views.py의 resgister함수랑 연
