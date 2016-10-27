#coding: utf-8
from django.http import JsonResponse
from django.shortcuts import render
from core.models import Table, Client, ClientSerializer
from rest_framework import generics, permissions


def table(request):
    return render(request, "table.html", {})


def crud(request):
    return render(request, "crud.html", {})


def get_table(request):
    table = Table.objects.first()
    if table:
        return JsonResponse({'table': table.to_dict_json()})
    else:
        raise NoTableException('Não existem tabelas salvas no banco')


class NoTableException(Exception):
    pass


class ClientList(generics.ListCreateAPIView):
    model = Client
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [
        permissions.AllowAny
    ]


class ClientDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Client
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [
        permissions.AllowAny
    ]
