from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from polls.grupoService import GrupoService
from polls.grupo import Grupo, User
from polls.cancion import Cancion
from polls.recomendacion import Recommender as rc
from polls.grupo import GrupoEncoder
import json
from json import JSONEncoder
from polls.recomendacion import clases as cs

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def getGrupo(resquest):
    grupoService = GrupoService()
    id = resquest.GET['id']
    #'636744ad08412a018708d4d00f0dc02fa4b884ee'
    grupo = grupoService.getGrupoByUsuario(User(id))

    jsonStr = json.dumps(grupo, indent=4 ,cls=GrupoEncoder)
    return HttpResponse(grupo)

def getCanciones(resquest):
    grupoService = GrupoService()
    resp = grupoService.getCanciones()
    return HttpResponse(resp)

def getTestRecomendacion(request):
    df=rc.Recommender(1000,60)
    recomendacion=df.EvalAlgorithm(10,"a820d2d4f16bbd53be9e41e0417dfb234bfdfba8")
    jsonStr = json.dumps(recomendacion, indent=4 ,cls=cs.RecomendacionEncoder)
    return HttpResponse(jsonStr)


