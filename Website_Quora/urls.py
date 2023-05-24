"""
URL configuration for Website_Quora project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path,re_path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user_registration/',user_registration,name='user_registration'),
    path('ListOfQuestions/',ListOfQuestions.as_view(),name='ListOfQuestions'),
    path('login_user/',login_user,name='login_user'),
    path('logout_user/',logout_user,name='logout_user'),
    path('post_questions/',post_questions,name='post_questions'),
    path('answer_question/',answer_question,name='answer_question'),
    path('likes/',likes,name='likes'),
    re_path('(?P<pk>\d+)/',DetailQuestions.as_view(),name='detail'),
    
]
