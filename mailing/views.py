from django.contrib.auth.mixins import LoginRequiredMixin
from mailing.forms import ClientForm
from mailing.models import Client, MailingAttempt, Mailing, Message
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


class MailingListView(ListView):
    model = Mailing


class MailingCreateView(CreateView):
    model = Mailing
    fields = ("message", "client", "begin_time", "end_time", "end_time", "periodicity", "status")
    success_url = reverse_lazy("mailing:list")

    def form_valid(self, form):
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.owner = self.request.user
            new_post.save()
        return super().form_valid(form)


class MailingUpdateView(UpdateView):
    model = Mailing
    fields = ("message", "client", "begin_time", "end_time", "end_time", "periodicity", "status")
    success_url = reverse_lazy("mailing:list")

    def form_valid(self, form):
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.save()
        return super().form_valid(form)


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


class ClientCreateView(CreateView, LoginRequiredMixin):
    model = Client
    form_class = ClientForm
    template_name = "client_form.html"
    success_url = reverse_lazy("mailing:client_list")

    def form_invalid(self, form):
        client = form.save()
        client.owner = self.request.user
        print(client.owner)
        client.save()

    def form_valid(self, form):
        if form.is_valid():
            client = form.save()
            client.owner = self.request.user
            print(client.owner)
            client.save()
        return super().form_valid(form)


class ClientUpdateView(UpdateView):
    model = Client
    fields = ("name", "email")
    template_name = "client_form.html"
    success_url = reverse_lazy("mailing:client_list")


class ClientDeleteView(DeleteView):
    model = Client
    template_name = 'client_confirm_delete.html'
    success_url = reverse_lazy("mailing:client_list")


class MessageListView(ListView):
    model = Message
    template_name = "message_list.html"


class MessageCreateView(CreateView):
    model = Message
    fields = ("title", "body")
    template_name = "message_form.html"
    success_url = reverse_lazy("mailing:message_list")

    def form_valid(self, form):
        message = form.save()
        message.owner = self.request.user
        message.save()
        return super().form_valid(form)


class MessageUpdateView(UpdateView):
    model = Message
    fields = ("title", "body")
    template_name = "message_form.html"
    success_url = reverse_lazy("mailing:message_list")


class MessageDeleteView(DeleteView):
    model = Message
    template_name = 'message_confirm_delete.html'
    success_url = reverse_lazy("mailing:message_list")


class AttemptListView(ListView):
    model = MailingAttempt
    template_name = "attempt_list.html"
