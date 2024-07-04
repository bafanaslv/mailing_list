from django.urls import path
from mailing.apps import MailingConfig

app_name = MailingConfig.name

urlpatterns = [
    # path('', views.ProductListView.as_view(), name='products_list'),
]
