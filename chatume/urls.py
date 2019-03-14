"""chatume URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from chat import views

urlpatterns = [
    path('admin/', admin.site.urls),


    path('chatume/', views.ChatSessionCreateView.as_view(), name= 'chatume'),
    path('', views.ChatSessionListView.as_view(), name= 'chatume_messages'),
    
    path('chatume/delete/<int:pk>', views.ChatSessionDeleteView.as_view(), name = "chatume_delete"),
    path('chatume/detail/<int:pk>', views.ChatSessionDetailView.as_view(), name = "chatume_detail"),
    path('chatume/update/<int:pk>', views.ChatSessionUpdateView.as_view()),
]

