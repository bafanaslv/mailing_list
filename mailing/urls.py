from django.urls import path
from mailing.apps import MailingConfig
from mailing import views

app_name = MailingConfig.name

urlpatterns = [
    path('', views.MainListView.as_view(), name='main'),
    path('client/', views.ClientListView.as_view(), name='client_list'),
    path('mailing/', views.MailingListView.as_view(), name='list'),
    path('create/', views.MailingCreateView.as_view(), name='create'),
    path('<int:pk>/detail/', views.MailingDetailView.as_view(), name='detail'),
    path('<int:pk>/update/', views.MailingUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', views.MailingDeleteView.as_view(), name='confirm_delete'),
    path('client/create/', views.ClientCreateView.as_view(), name='client_form'),
    path('<int:pk>/client_update/', views.ClientUpdateView.as_view(), name='client_form'),
    path('<int:pk>/client_delete/', views.ClientDeleteView.as_view(), name='client_confirm_delete'),
    path('message/', views.MessageListView.as_view(), name='message_list'),
    path('message/create/', views.MessageCreateView.as_view(), name='message_form'),
    path('<int:pk>/message_update/', views.MessageUpdateView.as_view(), name='message_form'),
    path('<int:pk>/message_delete/', views.MessageDeleteView.as_view(), name='message_confirm_delete'),
    path('attempt/', views.AttemptListView.as_view(), name='attempt_list'),
]
