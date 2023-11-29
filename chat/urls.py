from django.urls import path
from . import views

urlpatterns = [
    path('group/<int:group_id>/', views.group_chat, name='group_chat'),
    path('private/<int:recipient_id>/', views.private_chat, name='private_chat'),
    path('group/send_message/', views.send_group_message, name='send_group_message'),
    path('private/send_message/', views.send_private_message, name='send_private_message'),
    path('create_group/', views.create_group, name='create_group'),
    path('join_group/', views.join_group, name='join_group'),
    path('communities/', views.communities, name='communities'),
    path('create_group/', views.create_group, name='create_group'),
    path('view_group/<int:group_id>/', views.view_group, name='view_group'),
    path('update_group/<int:group_id>/', views.update_group, name='update_group'),
    path('delete_group/<int:group_id>/', views.delete_group, name='delete_group'),
    path('messages/', views.messages, name='messages'),
    path('unchatted_users/', views.unchatted_users, name='unchatted_users'),
]

