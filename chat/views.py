import json
from django.views.generic.base import TemplateView
from django.views.generic import View
from django.http import JsonResponse
from chatterbot import ChatBot
from chatterbot.ext.django_chatterbot import settings
from rest_framework import generics
from django.views.decorators.csrf import csrf_exempt



class ChatterBotAppView(TemplateView):
    template_name = 'app.html'

@csrf_exempt
def chatterbot_api(request):
    """
    Provide an API endpoint to interact with ChatterBot.
    """

    chatterbot = ChatBot(**settings.CHATTERBOT)
    if request.method == 'GET':
        """
        Return data corresponding to the current conversation.
        """
        return JsonResponse({
            'name': chatterbot.name
        })
    
    if request.method == 'POST':
        """
        Post text to chatbot
        * The JSON data should contain a 'text' attribute.
        """
        # this is info to a user
        # print(request.body.decode('utf-8'))
        # input_data = json.loads(request.body.decode('utf-8'))
        # print(input_data["mssg"])

        try:
            input_data = json.loads(request.body.decode('utf-8'))
            print(input_data['mssg'])
            if 'mssg' not in input_data:
                return JsonResponse(
                        'The attribute "text" is required.'
                    
                , status=400)

            # this is the reponse from the chatbot
            response = chatterbot.get_response(input_data["mssg"])

            response_data = response.serialize()
        except:
            raise


        return JsonResponse(response_data, safe=False,status=200)
        
        



# # Create your views here.
# class ChatSessionTemplateView(TemplateView):
#     template_name='chatume.html'

# #list comments
# class ChatSessionListView(ListView):
#     model = Message
#     template_name= 'message_list.html'

# #creates api endpont to interact with chatterbot
# class ChatSessionCreateView(CreateView):
#     form_class = ChatMessageForm
#     template_name = 'chat_form.html'

# class ChatSessionDetailView(DetailView):
#     model = Message

# class ChatSessionDeleteView(DeleteView):
#     model = Message
#     success_url = reverse_lazy('message_list')

# class ChatSessionUpdateView(UpdateView):
#     model = Message
#     fields = ["text", "bot"]


