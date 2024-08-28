# example/urls.py
from django.urls import path

from example import views


urlpatterns = [
    path('', views.login_view, name='login'),
    path('quiz/<int:id>/', views.quiz_view, name='quiz'),
    path('quiz_submit/<int:id>/', views.quiz_submit, name='quiz_submit'),
    path('saudacao',views.saudacao,name='saudacao'),
    path('mario',views.mario,name='mario'),
    path('premio',views.premio,name='premio'),
]