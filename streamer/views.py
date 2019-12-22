from django.shortcuts import render, redirect
from .models import Streamer
import uuid
import requests

# Create your views here.

def signup(request):
    signup = request.GET.get('connect')
    if signup == "bot":
        scope = "chat:edit+chat:read+channel:moderate+channel_editor+user_read"
        request.session['streamer_signup'] = False
        return redirect('https://id.twitch.tv/oauth2/authorize?client_id=9k1gvkbdahrasual41n1cq6bvzpgkw&redirect_uri=http://localhost:5000/bot/oauth2/&response_type=token&scope=' + scope)
    elif signup == "streamer":
        scope = "chat:edit+user_read+channel_check_subscription+channel_commercial+channel_editor+channel_subscriptions"
        request.session['streamer_signup'] = True
        return redirect('https://id.twitch.tv/oauth2/authorize?client_id=9k1gvkbdahrasual41n1cq6bvzpgkw&redirect_uri=http://localhost:5000/bot/oauth2/&response_type=token&scope=' + scope)
    else:
        return render(request, 'signup.html')


def oauth(request):
    return render(request, 'oauth.html')

def oauth_redir(request):
    step = request.GET.get('step')
    if step == "1":
        bot_token = request.POST.get("bot_token")
        headers = {'Authorization': 'Bearer ' + bot_token}
        print("headers: ", headers)
        r = requests.get('https://api.twitch.tv/helix/users', headers=headers)
        resp = r.json()
        print("response: ", resp)
        bot = Streamer.objects.create(bot_key=bot_token, bot_name=resp['data'][0]['display_name'])
        bot.save()
        request.session['streamer_id'] = bot.id
        scope = "chat:edit+user_read+channel_check_subscription+channel_commercial+channel_editor+channel_subscriptions"
        return redirect(
            'https://id.twitch.tv/oauth2/authorize?client_id=9k1gvkbdahrasual41n1cq6bvzpgkw&redirect_uri=http://localhost:5000/bot/oauth2/step-2/&response_type=token&scope=' + scope + '&force_verify=true')
    else:
        streamer_token = request.POST.get("streamer_token")
        headers = {'Authorization': 'Bearer ' + streamer_token}
        r = requests.get('https://api.twitch.tv/helix/users', headers=headers)
        resp = r.json()
        streamer = Streamer.objects.get(pk=request.session['streamer_id'])
        streamer.streamer_key = streamer_token
        streamer.streamer_name = resp['data'][0]['display_name']
        streamer.save()
        return redirect('oauth_step3')

def oauth_step2(request):
    return render(request, 'oauth_step2.html')


def oauth_step3(request):
    streamer = Streamer.objects.get(pk=request.session['streamer_id'])
    cobraKey = uuid.uuid4().hex
    streamer.cobra_key = cobraKey
    streamer.save()
    return render(request, 'oauth_step3.html', {'cobra': cobraKey, 'bot': streamer.bot_key, 'streamer': streamer.streamer_key})