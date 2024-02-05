from django.http import HttpResponse, JsonResponse
import google.generativeai as genai
from django.conf import settings

# Create your views here.


genai.configure(api_key=settings.API_KEY)


def index(request):
    request
    model = genai.GenerativeModel('gemini-pro')
    chat = model.start_chat(history=[
        {
            'role': 'user',
            'parts': ['i am hungry'],
        },
        {
            'role': 'model',
            'parts': ['so what?'],
        }
    ])
    response = chat.send_message("suggest me a receipe?")
    return JsonResponse({
        "success": True,
        "message": response.text,
    })
