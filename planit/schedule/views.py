from django.http import HttpResponse

def index(request):
    return HttpResponse('In the schedule index')
