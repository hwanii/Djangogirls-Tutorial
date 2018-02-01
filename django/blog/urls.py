from django.urls import path, re_path
from . import views
import re

urlpatterns = [
    path('', views.post_list, name='post-list'),  # 함수 자체를 전달. 응답을 전달하면 다시 실행할 수 없음
    # re_path(r'(?P<pk>\d+)/$', views.post_detail),
    path('<int:pk>/', views.post_detail, name='post-detail'),
    # localhost:8000/add 에 접근
    path('add/', views.post_add, name='post-add'),
]
