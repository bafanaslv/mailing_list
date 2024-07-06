from django.shortcuts import render
from mailing.models import Client, MailingAttempt, MailingList, Message
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy, reverse


class MailingListView(ListView):
    model = MailingList
