from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list), # 함수 자체를 전달. 응답을 전달하면 다시 실행할 수 없음
]