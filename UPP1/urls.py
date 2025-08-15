"""
URL configuration for UPP1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from users.views import login_view, logout_view, register_view, quick_login, role_redirect, dashboard_basic, dashboard_admin

urlpatterns = [
    path('admin/', admin.site.urls),

    # User Authentication URLs
    path('login/', login_view, name='login'),               # Login URL
    path('logout/', logout_view, name='logout'),            # Logout URL
    path('register/', register_view, name='register'),      # Registration URL
    path('redirector/', role_redirect, name='role_redirect'),
    path('dashboard/basic/', dashboard_basic, name='dashboard_basic'),
    path('dashboard/admin/', dashboard_admin, name='dashboard_admin'),


    path('quick-login/<str:role>/', quick_login, name='quick_login'),       # Quick Login URL (For Testing Purposes)

]