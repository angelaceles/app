from django.http import HttpResponse

def index(request):
    return HttpResponse("Hola Mundo")

def inicio(request):
    return HttpResponse("Bienvenido")

def about(request):
    return HttpResponse("Sobre que trata")

