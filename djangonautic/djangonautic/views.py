from django.http import HttpResponse

def home(request):
    return HttpResponse("homepage")

def about(request):
    return HttpResponse("about")