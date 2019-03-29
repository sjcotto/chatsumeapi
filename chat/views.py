from django.views.generic import TemplateView ,CreateView, ListView, DetailView, DeleteView, UpdateView
from chatterbot.ext.django_chatterbot import settings
from django.http import JsonResponse, HttpResponse
from django.db.models.signals import post_save
from chat.models import Message, ChatSession
from chat.form.forms import ChatMessageForm
from django.urls import reverse_lazy
from django.core import serializers
from django.shortcuts import render
from chatterbot import ChatBot
import requests
import json


def get_next_message(request):
    # Get previous messeg from api call
    if(request.method == "GET"):
        latest_entry = Message.objects.latest('created_at')
        # print('bot')
        chatterbot = ChatBot(**settings.CHATTERBOT)
        new_message = Message.objects.create( text = chatterbot.get_response(latest_entry.text), bot = True )
        return JsonResponse(serializers.serialize("JSON", new_message), safe = False)
    return HttpResponse("DONT PLAY WITH ME, PLAY WIT YO BITCH....RICH NIGGA ON SOME MULTI MILLION DOLLAR SHIT")
    # Todo return JSON from new message
    

    
def enter_message(request):
    if(request.method == "POST"):
        new_entry = Message.objects.create(
            bot = False,
            text = request.POST.get("text")
        )
        return JsonResponse(serializers.serialize("JSON", new_entry), safe = False)
    return HttpResponse("FOUND OUT YO BIG BROTHER SNITCH SO I CALL HIM YO BIG SISTER")
    #todo return if succesful POST

# Create your views here.
class ChatSessionTemplateView(TemplateView):
    template_name='chatume.html'

#list comments
class ChatSessionListView(ListView):
    model = Message
    template_name= 'chatume_messages.html'

#creates api endpont to interact with chatterbot
class ChatSessionCreateView(CreateView):
    form_class = ChatMessageForm
    template_name = 'chat_form.html'

class ChatSessionDetailView(DetailView):
    model = Message

class ChatSessionDeleteView(DeleteView):
    model = Message
    success_url = reverse_lazy('chatume_messages')

class ChatSessionUpdateView(UpdateView):
    model = Message
    fields = ["text", "bot"]


