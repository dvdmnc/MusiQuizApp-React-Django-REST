from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Singers,Songs
from django.forms.models import model_to_dict
from rest_framework.response import Response

@api_view(['GET'])
def getData(request):
    singers = [model_to_dict(x) for x in Singers.objects.all()] #Turn the QuerySet into a dict
    singers_names_faces = {}
    for dict in singers:
        singers_names_faces[dict["name"]] = request.build_absolute_uri(dict["face"].url)
    songssingers = [model_to_dict(x) for x in Songs.objects.all()]
    songs = []
    songs_singers = {}
    songs_samples = {}
    for dict in songssingers:
        songs.append(dict["name"])
        songs_samples[dict["name"]] = dict["sample"]
        for dict2 in singers:
            if dict["singer"] == dict2["id"]:
                try: 
                    songs_singers[dict2["name"]].append(dict["name"])
                except KeyError:
                    songs_singers[dict2["name"]] = [dict["name"]]
    response = [songs, singers_names_faces, songs_singers, songs_samples]
    return Response(response)
