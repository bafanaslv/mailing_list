from mailing.models import Client, MailingAttempt, Mailing, Message
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse


class MailingListView(ListView):
    model = Mailing


class MailingCreateView(CreateView):
    model = Mailing
    fields = ("message", "client", "begin_time", "end_time", "end_time", "periodicity", "status")
    success_url = reverse_lazy("mailing:list")

    def form_valid(self, form):
        if form.is_valid():
            new_post = form.save(commit=False)
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


class ClientCreateView(CreateView):
    model = Client
    fields = ("name", "email")
    template_name = "client_form.html"
    success_url = reverse_lazy("mailing:client_list")


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


class MessageUpdateView(UpdateView):
    model = Message
    fields = ("title", "body")
    template_name = "message_form.html"
    success_url = reverse_lazy("mailing:message_list")


class MessageDeleteView(DeleteView):
    model = Message
    template_name = 'message_confirm_delete.html'
    success_url = reverse_lazy("mailing:message_list")
