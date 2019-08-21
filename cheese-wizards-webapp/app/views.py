import requests
from requests.exceptions import HTTPError
from json.decoder import JSONDecodeError

from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

from app.utils import *

x_email = "khalili@sfu.ca"
api_Token = "Nf7zvG9vaYOW6cx1ZXXT0_9DPr1srXzZ7phJ3il7"
content_type = "application/json"

headers = {
    'Content-Type' : content_type,
    'x-email' : x_email,
    'x-api-token' : api_Token
}
# Create your views here.
def index(request):
    return render(request, 'index.html')

def get_wizards(request):
    params = request.GET.dict()
    res = requests.get(
            BASE_ENDPOINT_URL_WIZARD,
            headers=headers,
            params=params,
    )
    try:
        res.raise_for_status()
        response = res.json()
    except (HTTPError, JSONDecodeError):
        response = {'error': 'bad API call'}

    return JsonResponse(response)


def get_wizards_by_id(request, id):
    get_wizards_url = BASE_ENDPOINT_URL_WIZARD + "/" + str(id)
    res = requests.get(get_wizards_url, headers = headers)
    try:
        res.raise_for_status()
        response = res.json()
        response = {'wizards' : [response]}
    except (HTTPError, JSONDecodeError):
        response = {'error': 'bad API call'}

    return JsonResponse(response)
    
