from typing import Counter
from django.shortcuts import render
from mywatchlist.models import Film
from django.http import HttpResponse
from django.core import serializers

def show_status(request):
    data_film = Film.objects.all()
    counter=0
    for data in data_film:
        if data.watched == True:
            counter+=1
    
    if counter >= len(data_film)-counter:
        return "Selamat, kamu sudah banyak menonton!"
    else:
        return "Wah, kamu masih sedikit menonton!"

def show_film(request):
    data_film = Film.objects.all()

    context = {
        'list_film' : data_film,
        'nama' : 'Abby Marvel',
        'id' : '2106751796',
        'status' : show_status(request),
    }
    return render(request, "mywatchlist.html", context)

def show_xml(request):
    data = Film.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Film.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Film.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Film.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
