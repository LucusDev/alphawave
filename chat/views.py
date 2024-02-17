from django.http import HttpResponse, JsonResponse, HttpRequest
import google.generativeai as genai
from django.conf import settings
import json


genai.configure(api_key=settings.API_KEY)


def index(request: HttpRequest):
    try:
        if request.method == 'POST':
            req_body = json.loads(request.body)
            if (req_body['message'] != None):
                model = genai.GenerativeModel('gemini-pro')
                chat = model.start_chat(history=[
                    # {
                    #     'role': 'user',
                    #     'parts': ['i am hungry'],
                    # },
                    # {
                    #     'role': 'model',
                    #     'parts': ['so what?'],
                    # }
                ])
                response = chat.send_message(req_body['message'])
                return JsonResponse({
                    "success": True,
                    "message": response.text,
                })
        raise Exception
    except:
        return JsonResponse({
            "success": False,
            "message": "Server error!",
        })
