from django.contrib import admin
from django.urls import path,include,re_path
from rest_framework.urlpatterns import format_suffix_patterns
from accapp import views

urlpatterns = [
    
    path('accounts/', views.LoginList.as_view(),name="all login accounts"),
    path('loginlist/', views.login_list,name="all login accounts"),
    path('logindetails/<int:pk>', views.login_detail,name="login details"),        

    path('profile/all', views.AccountList.as_view(),name="all accounts"),
    path('accountlist/', views.account_list,name="all login accounts"),
    path('profile/<int:pk>', views.profile_detail,name="profile details"),        
        
]

urlpatterns=format_suffix_patterns(urlpatterns)
