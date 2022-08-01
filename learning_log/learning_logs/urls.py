from django.urls import path
from . import views

app_name = 'learning_logs'
urlpatterns = [
    path('', views.index, name='index'),
    path('topics/', views.topics, name='topics'),
    # Detail page for a single topic. 
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    path('new_topic/', views.new_topic, name='new_topic'),
    path('new_entry/', views.new_entry, name='new_entry'),
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry')
]