from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic.list import ListView

from . import models


class Pagar(View):
    pass
    
class FecharPedido(View):
    def get(self,*args, **kwargs):
        return HttpResponse('FecharPedido')

class Detalhe(View):
    def get(self,*args, **kwargs):
        return HttpResponse('Detalhe')

class Logout(View):
    def get(self,*args, **kwargs):
        return HttpResponse('Logout')            
