from multiprocessing import context
from django.shortcuts import render ,redirect
from .models import equipos
from .forms import equiposform
from .models import estadios
from .forms import estadiosform
from .models import jugadores
from .forms import jugadoresform





# Create your views here.
def index(request):
    return render(request,"home/index.html",{})


def list(request):
    context ={
        "list_equipos": equipos.objects.all,
        
    }
    return render(request, "home/list.html",context)



def create(request):
    form = equiposform(request.POST or None)
    if request.user.is_authenticated:
            error = "User Logged"
            if form.is_valid():
                form.save()
                return redirect('list')
    else:
        error = "User Mis Be Logged"
    context ={
        "form" : form,
        "message": error


    }
    return render(request,"home/create.html",context)


def detail(request , id):
    queryset = equipos.objects.get(pk = id)
    context = {
        "object": queryset
    }
    return render(request,"home/detail.html",context)


def update(request , id):
    queryset = equipos.objects.get(pk = id)
    if request.method == "POST":
        form = equiposform(request.POST, instance = queryset )
        if  form.is_valid():
            form.save()
            return redirect('list')

    else :
         form = equiposform(instance= queryset)
   
    return render(request,"home/update.html", {'form' :form} )
    
def delete(request , id):
    queryset = equipos.objects.get(pk = id)

    if queryset:
        queryset.delete()
    
        return redirect('list')
def list_estadios(request):
    context ={
        "list_estadios": estadios.objects.all,
        
    }
    return render(request, "home/list_estadios.html",context)

def create_estadio(request):
    form = estadiosform(request.POST or None)
    if request.user.is_authenticated:
            error = "User Logged"
            if form.is_valid():
                form.save()
                return redirect('list_estadios')
    else:
        error = "User Mis Be Logged"
    context ={
        "form" : form,
        "message": error


    }
    return render(request,"home/create.html",context)


def detail_estadio(request , id):
    queryset = estadios.objects.get(pk = id)
    context = {
        "object": queryset
    }
    return render(request,"home/detail_estadios.html",context)


def update_estadio(request , id):
    queryset = estadios.objects.get(pk = id)
    if request.method == "POST":
        form = estadiosform(request.POST, instance = queryset )
        if  form.is_valid():
            form.save()
            return redirect('list_estadios')

    else :
         form = estadiosform(instance= queryset)
   
    return render(request,"home/update.html", {'form' :form} )
    
def delete_estadio(request , id):
    queryset = estadios.objects.get(pk = id)

    if queryset:
        queryset.delete()
    
        return redirect('list_estadios')

   
def list_jugadores(request):
    context ={
        "list_jugadores": jugadores.objects.all,
        
    }
    return render(request, "home/list_jugadores.html",context)

def create_jugadores(request):
    form = jugadoresform(request.POST or None)
    if request.user.is_authenticated:
            error = "User Logged"
            if form.is_valid():
                form.save()
                return redirect('list_jugadores')
    else:
        error = "User Mis Be Logged"
    context ={
        "form" : form,
        "message": error


    }
    return render(request,"home/create.html",context)


def detail_jugadores(request , id):
    queryset = jugadores.objects.get(pk = id)
    context = {
        "object": queryset
    }
    return render(request,"home/detail_jugadores.html",context)


def update_jugadores(request , id):
    queryset = jugadores.objects.get(pk = id)
    if request.method == "POST":
        form = jugadoresform(request.POST, instance = queryset )
        if  form.is_valid():
            form.save()
            return redirect('list_jugadores')

    else :
         form = jugadoresform(instance= queryset)
   
    return render(request,"home/update.html", {'form' :form} )
    
def delete_jugadores(request , id):
    queryset = jugadores.objects.get(pk = id)

    if queryset:
        queryset.delete()
    
        return redirect('list_jugadores')

   
    
    
    