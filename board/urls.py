from django.urls import path
from . import views   # 현재폴더의 view가져오기

urlpatterns = [
    path('detail/<int:pk>/', views.board_detail),
    path('list/', views.board_list),
    path('write/', views.board_write),
]

# views.py의 resgister함수랑 연
