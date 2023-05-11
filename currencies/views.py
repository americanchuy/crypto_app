from django.shortcuts import render, redirect
from django.http import HttpResponse
from .update_models import update_currency
import json
from .call_api import selected_coins_api_call, landing_page_api, latest_news_page
from django.contrib.auth import authenticate, login

# Create your views here.

def main(request):
    return render(request, 'currencies/main.html')

def login_view(request):
    if request.method == "POST /account/login/ HTTP/1.1":
        print('POST METHOD')
        return HttpResponse('It works?')

def latest_news(request):
    all_stories = latest_news_page()
    return render(request, 'currencies/latest_news.html', {'all_stories': all_stories})
def top_performers(request):
    coins_list = landing_page_api()
    return render(request, 'currencies/currencies.html', {'coins': coins_list})

def render_stats(request):
    coin = request.POST.get('selected-coin')
    json_data = selected_coins_api_call(coin)
    if json_data != '[]':
        update_currency(json_data)
        return render(request, 'currencies/selected_currencies.html', {'json_data': json.loads(json_data)})
    else:
        return HttpResponse('Invalid coin')

    