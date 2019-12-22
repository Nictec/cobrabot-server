from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from streamer.models import Streamer, Command
from rest_framework.views import Response
from rest_framework.decorators import api_view
from .serializers import StreamerSerializer, CommandSerializer

# Create your views here.
@api_view(['GET'])
def verify(request):
    try:
        auth = request.headers['Authentication']
    except KeyError:
        return HttpResponse('Unauthorized', status=401)
    streamer = get_object_or_404(Streamer, cobra_key=auth)
    serializer = StreamerSerializer(streamer)
    print(serializer.data)
    return Response(serializer.data)

@api_view(['GET', 'POST'])
def commands(request):
    try:
        auth = request.headers['Authentication']
    except KeyError:
        return HttpResponse('Unauthorized', status=401)
    streamer = get_object_or_404(Streamer, cobra_key=auth)
    commands = Command.objects.filter(streamer=streamer)
    serializer = CommandSerializer(commands)
    return Response(serializer.data)