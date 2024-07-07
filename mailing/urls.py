from django.urls import path
from mailing.apps import MailingConfig
from mailing import views

app_name = MailingConfig.name

urlpatterns = [
    path('', views.MailingListView.as_view(), name='list'),
    path('create/', views.MailingCreateView.as_view(), name='create'),
    path('<int:pk>/detail/', views.MailingDetailView.as_view(), name='detail'),
    path('<int:pk>/update/', views.MailingUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', views.MailingDeleteView.as_view(), name='conform_delete'),
]
