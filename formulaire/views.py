#-*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    """ Exemple de page HTML, non valide pour que l'exemple soit concis """
    titrePrincipal = """<h1><b>Visites du GeePs</h1></b>"""
    titreFormulaire = """<h2><b>Information visiteur :</b><h2>"""
    texteFooter = """<h2><b>Protection des informations nominatives</b></h2>
    					"""
    text = titrePrincipal + titreFormulaire
    return HttpResponse(text)