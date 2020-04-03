import json
from django.views.generic.base import TemplateView
from django.views.generic import View
from django.http import JsonResponse
from chatterbot import ChatBot
from chatterbot.ext.django_chatterbot import settings
from django.views.decorators.csrf import csrf_exempt

class ChatterBotAppView(TemplateView):
    template_name = 'app.html'

@csrf_exempt 
class ChatterBotApiView(View):
    """
    Provide an API endpoint to interact with ChatterBot.
    """

    chatterbot = ChatBot(**settings.CHATTERBOT)

    def post(self, request, *args, **kwargs):
        """
        Return a response to the statement in the posted data.
        * The JSON data should contain a 'text' attribute.
        """
        input_data = json.loads(request.body.decode('utf-8'))

        if 'text' not in input_data:
            return JsonResponse({
                'text': [
                    'The attribute "text" is required.'
                ]
            }, status=400)

        response = self.chatterbot.get_response(input_data)

        response_data = response.serialize()

        return JsonResponse(response_data, status=200)

    def get(self, request, *args, **kwargs):
        """
        Return data corresponding to the current conversation.
        """
        return JsonResponse({
            'name': self.chatterbot.name
        })

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


