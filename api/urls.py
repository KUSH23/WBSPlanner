from django.urls import path
from . import views

urlpatterns = [
    path('', views.mgroup_list),
    path('restapi/', views.MGroupList.as_view()),
    path('restapi/<int:pk>/', views.MGroupDetail.as_view()),
    path('restapi/sub/', views.MSGroupList.as_view()),
]