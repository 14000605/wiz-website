from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import requests

from app.utils import *
# Create your views here.
def index(request):
    return render(request, 'index.html')

def get_wizards(request):
    x_email = "khalili@sfu.ca"
    api_Token = "Nf7zvG9vaYOW6cx1ZXXT0_9DPr1srXzZ7phJ3il7"
    content_type = "application/json"

    headers = {
        'Content-Type' : content_type,
         'x-email' : x_email,
         'x-api-token' : api_Token
    }

    params = request.GET
    query_str = construct_query_from_dict(params)

    get_wizards_url = BASE_ENDPOINT_URL + "wizards?" + query_str
    res = requests.get(get_wizards_url, headers = headers)

    return JsonResponse(res.json())
