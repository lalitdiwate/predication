from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('predict_score/<int:num>/', views.score, name='score'),
    path('tfws_score/<int:num>/', views.tfws_score, name='tfws_score'),
    path('tfws_score/<int:num>/find_predict', views.find_predict, name='predict'),
    path('info/<int:num>/', views.score, name='info'),
    path('predict_score/<int:num>/find_predict', views.find_predict, name='predict'),
    path('pref_score',views.pref_score, name='pref_score'),
    path('tfws_list',views.tfws_list,name='tfws_list'),
    path('form',views.form,name='form'),
    path('inform',views.info),
    path('storeform',views.storeform,name='storeform'),
    path('store',views.store,name='store'),
    path('user',views.user,name='user'),
    path('collage',views.collage,name='collage'),
    path('pickle',views.getpic,name='getpic'),
    path('user_response',views.user_response, name='user_response'),
    path('graph/<int:num>/<str:cat>/<str:branch>/<str:year>/<int:num1>/<int:num2>/<int:num3>/<int:num4>/<int:num5>/',views.show_graph, name='show_graph'),


]
 