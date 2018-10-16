from django.contrib import admin
from django.urls import path,include,re_path
from rest_framework.urlpatterns import format_suffix_patterns
from webapp import views

urlpatterns = [
    
    path('employees/', views.EmployeeList.as_view(),name="all employees"),
    path('category_list/', views.CategoryList.as_view(),name="all categories"),
    path('categories/', views.category_list),
    path('categories/<int:pk>', views.category_detail),
]

urlpatterns=format_suffix_patterns(urlpatterns)

