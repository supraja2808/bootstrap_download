from django.shortcuts import render

# Create your views here.

def bootstrap_download(request):
    return render(request,'bootstrap_download.html')


def modal(request):
    return render(request,'modal.html')


def navs(request):
    return render(request,'navs.html')


def navbar(request):
    return render(request,'navbar.html')

def pagination(request):
    return render(request,'pagination.html')


def popovers(request):
    return render(request,'popovers.html')


def progress(request):
    return render(request,'progress.html')


def scrollspy(request):
    return render(request,'scrollspy.html')


def spinners(request):
    return render(request,'spinners.html')


def toasts(request):
    return render(request,'toasts.html')

def tooltips(request):
    return render(request,'tooltips.html')


