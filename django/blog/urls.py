from django.urls import path, re_path
from . import views
import re
urlpatterns = [
    path('', views.post_list), # 함수 자체를 전달. 응답을 전달하면 다시 실행할 수 없음
    # path('detail/', views.post_detail),


    re_path(r'(?P<pk>\d+)/$', views.post_detail),
]