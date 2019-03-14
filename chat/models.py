from django.db import models
from django.urls import reverse_lazy
from django.db.models.signals import post_save
from django.shortcuts import redirect,render
import requests
import json
from chatterbot.ext.django_chatterbot import settings
from chatterbot import ChatBot

# Create your models here.

#model handles name of chat session

#model handles messege information
class Message(models.Model):
    bot = models.BooleanField()
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def create_bot(self):
        #print('bot')
        chatterbot = ChatBot(**settings.CHATTERBOT)
        if(self.bot == False):
            new_message = Message.objects.create( text = chatterbot.get_response(self.text), bot = True )
            return new_message
    
    def __str__(self):
        return f' {self.text}, {self.bot}'

    def get_absolute_url(self):
        return reverse_lazy("chatume_detail", args=[str(self.id)])



class ChatSession(models.Model):
    name = models.CharField(max_length=40, unique=True)
    chat_session = models.ForeignKey(Message, on_delete=models.SET_NULL, null=True)

    def create_bot(sender, instance, **kwargs):
        instance.create_bot()

    post_save.connect(create_bot, sender=Message)
