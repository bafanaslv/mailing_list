from django.contrib.auth.mixins import LoginRequiredMixin
from mailing.forms import ClientForm, MessageForm, MailingForm
from mailing.models import Client, MailingAttempt, Mailing, Message
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


class MailingListView(ListView):
    model = Mailing

    def get_queryset(self):
        user = self.request.user
        if not user.is_authenticated:
            user = None
        queryset = Mailing.objects.filter(owner=user)
        return queryset


class MailingCreateView(CreateView):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy("mailing:list")

    def form_valid(self, form):
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.owner = self.request.user
            new_post.save()
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


class MailingUpdateView(UpdateView):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy("mailing:list")

    def form_valid(self, form):
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.save()
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


class MailingDetailView(DetailView):
    model = Mailing

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.save()
        return self.object


class MailingDeleteView(DeleteView):
    model = Mailing
    template_name = 'mailing/confirm_delete.html'
    success_url = reverse_lazy("mailing:list")


class ClientListView(ListView):
    model = Client
    template_name = "client_list.html"

    def get_queryset(self):
        user = self.request.user
        if not user.is_authenticated:
            user = None
        queryset = Client.objects.filter(owner=user)
        return queryset


class ClientCreateView(CreateView, LoginRequiredMixin):
    model = Client
    form_class = ClientForm
    template_name = "client_form.html"
    success_url = reverse_lazy("mailing:client_list")

    def form_valid(self, form):
        if form.is_valid():
            client = form.save()
            client.owner = self.request.user
            client.save()
        return super().form_valid(form)


class ClientUpdateView(UpdateView):
    model = Client
    form_class = ClientForm
    template_name = "client_form.html"
    success_url = reverse_lazy("mailing:client_list")


class ClientDeleteView(DeleteView):
    model = Client
    template_name = 'client_confirm_delete.html'
    success_url = reverse_lazy("mailing:client_list")


class MessageListView(ListView):
    model = Message
    template_name = "message_list.html"

    def get_queryset(self):
        user = self.request.user
        if not user.is_authenticated:
            user = None
        queryset = Message.objects.filter(owner=user)
        return queryset


class MessageCreateView(CreateView):
    model = Message
    form_class = MessageForm
    template_name = "message_form.html"
    success_url = reverse_lazy("mailing:message_list")

    def form_valid(self, form):
        if form.is_valid():
            message = form.save()
            message.owner = self.request.user
            message.save()
        return super().form_valid(form)


class MessageUpdateView(UpdateView):
    model = Message
    form_class = MessageForm
    template_name = "message_form.html"
    success_url = reverse_lazy("mailing:message_list")


class MessageDeleteView(DeleteView):
    model = Message
    template_name = 'message_confirm_delete.html'
    success_url = reverse_lazy("mailing:message_list")


class AttemptListView(ListView):
    model = MailingAttempt
    template_name = "attempt_list.html"


class MainView(ListView):
    model = Mailing
    template_name = "main.html"
