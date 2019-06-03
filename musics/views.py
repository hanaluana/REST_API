from django.shortcuts import render, get_object_or_404
from .models import Music
from .serializers import MusicSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['GET', 'POST']) #허용할 http method를 적어줌
def music_list(request):
    if request.method=="GET":
        musics = Music.objects.all()
        serializer = MusicSerializer(musics, many=True)
        return Response(serializer.data)
    else:
        # CREATE
        music = request.data
        # Create an article from the above data
        serializer = MusicSerializer(data=music)
        if serializer.is_valid(raise_exception=True):
            music_saved = serializer.save()
        return Response(music_saved.data)
    
@api_view(['GET','PUT','DELETE'])
def music_detail(request, music_id):
    if request.method=="GET":
        music = get_object_or_404(Music, id=music_id)
        serializer = MusicSerializer(music, many=False)
        return Response(serializer.data)
    elif request.method=="PUT":
        saved_music = get_object_or_404(Music.objects.all(), pk=music_id)
        music = request.data
        serializer = MusicSerializer(instance=saved_music, data=music, partial=True)
        if serializer.is_valid(raise_exception=True):
            music_saved = serializer.save()
        return Response(music_saved)
    else:
        music = get_object_or_404(Music.objects.all(), pk=music_id)
        music.delete()
        return Response(status=204)
