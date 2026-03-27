from django.shortcuts import render

def index(request):
    # Render toma el request y el archivo HTML que queremos mostrar
    return render(request, 'home/index.html')

    # Vista para la pagina de contacto
def contacto(request):
    return render(request, 'home/contacto.html')
