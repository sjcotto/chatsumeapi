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
class ChatSession(models.Model):
    title = models.TextField(null=True)

#model handles messege information
class Message(models.Model):
    bot = models.BooleanField()
    text = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    chat_session = models.ForeignKey(ChatSession, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return f' {self.text}, {self.bot}'

    def get_absolute_url(self):
        return reverse_lazy("chatume_detail", args=[str(self.id)])



