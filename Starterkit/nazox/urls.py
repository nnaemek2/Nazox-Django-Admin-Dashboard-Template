from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from nazox import views
from django.urls import include
from django.contrib.auth.decorators import login_required
from nazox.views import MyPasswordChangeView,MyPasswordSetView


urlpatterns = [
    # Menu    
    path('',views.DashboardView.as_view(),name='dashboard'),# Dashboard
   
    # Apps 
    path('layouts/',include('layouts.urls')),# Layout
    path('pages/',include('utility.urls')),# Utility
    
    path('admin/', admin.site.urls),# Admin
    
    path(
        "accounts/password/change/",
        login_required(MyPasswordChangeView.as_view()),
        name="account_change_password",
    ),
    path(
        "accounts/password/set/",
        login_required(MyPasswordSetView.as_view()),
        name="account_set_password",
    ),

    path('account/', include('allauth.urls')),
]
