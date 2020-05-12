from django.db import models
from django.urls import reverse_lazy
from django.db.models.signals import post_save
from django.shortcuts import redirect,render
import requests
import json
from chatterbot.ext.django_chatterbot import settings
from chatterbot import ChatBot


# when you meet with your teamate, morning afternoon, evening, night, needs no meet selsction.

# Create your models here.
"""
Conversation model:
Tracks text between agents.
conversation can be: 
    bot - bot
    bot - user
    user - user

MVP will be user send, bot response
I will use django rest framework to communicate over api
i could just use a flask app.
saving text allows me to train in the future models, 
but my model will rely on pretrained vectors, or yml
so saving data may be trash. 

it could be to perform analysis on responses and text submission
i mean i want to send data from django to react app. 
"""

class ChatSession(models.Model):
    title = models.TextField(null=True)

#model handles messege information
class Message(models.Model):
    send_to = models.CharField(default="", max_length=25)
    text = models.TextField(null=True)