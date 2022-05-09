from django.shortcuts import render

from .models import MasterDegrees, Modules

# Create your views here.



def module_searcher(request):
    
    context = {}
    return render(
        request,
        "search.html",
        context,
    )

def module_results(request, search):

    title = Modules.objects.filter(title__icontains=search)

    description = Modules.objects.filter(description__icontains=search)

    module_code = Modules.objects.filter(code__icontains=search)

    search_results = module_code | title | description

    search_results = search_results.distinct()

    all_master_degrees = MasterDegrees.objects.none()
    for result in search_results:
        master_degrees = MasterDegrees.objects.filter(modules=result)
        all_master_degrees = all_master_degrees | master_degrees

    all_master_degrees = all_master_degrees.distinct()

    print(all_master_degrees)

    context = {
        "master_degrees": all_master_degrees,
    }
    return render(
        request,
        "searchresults.html",
        context,
    )


def modules_list(request):

    all_modules = Modules.objects.all()
        
    context = {
        "modules": all_modules,
    }
    return render(
        request,
        "modules_list.html",
        context,
    )

def master_list(request):

    all_masters = MasterDegrees.objects.all()
        
    context = {
        "masters": all_masters,
    }
    return render(
        request,
        "master_list.html",
        context,
    )

def module(request, id):
    module = Modules.objects.get(id = id)
    related_masters = MasterDegrees.objects.filter(modules = module)
    context = {
        "module": module,
        "masters": related_masters,
    }
    return render(
        request,
        "module.html",
        context,
    )

def master(request, id):
    master = MasterDegrees.objects.get(id = id)
    context = {
        "master": master,
    }
    return render(
        request,
        "master.html",
        context,
    )

def aboutus(request):
    context = {}
    return render(
        request,
        "aboutus.html",
        context,
    )