"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from web_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
	path('', views.login_view),
	path('home', views.home),
	path('read', views.read_messages),
	path('delete_request/<str:id_request>/<str:fecha>/', views.delete_request, name = 'delete_request'),
	path('login', views.login_view, name='login'),
	path('logout', views.logout_view),
	path('device_token/<str:device_token>/', views.get_device_token, name = 'device_token'),
	path('firebase-messaging-sw.js', views.showFirebaseJS,name="show_firebase_js"),
	path('delete_unread/<str:id_request>/', views.delete_unread, name = 'delete_unread'),
]
