from django.http import HttpResponse

def cal(request):
    return HttpResponse('In the schedule index')
def activity(request):
    return HttpResponse('Activites!')
