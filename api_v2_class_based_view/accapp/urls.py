from django.contrib import admin
from django.urls import path,include,re_path
from rest_framework.urlpatterns import format_suffix_patterns
from accapp import views

urlpatterns = [
    
    path('accounts/', views.LoginAccountList.as_view(),name="all login accounts"),
    # path('logindetails/<int:pk>', views.LoginAccountDetail.as_view(),name="login details"),        

    path('profile/all', views.AccountList.as_view(),name="all profiles"),
    path('profile/<int:pk>', views.Profile.as_view(),name="profile details"),        
        
]

urlpatterns=format_suffix_patterns(urlpatterns)
