from django.http import HttpResponse

def cal(request, user_id):
    return HttpResponse('In the schedule index for user %s' % user_id)
def activity(request):
    return HttpResponse('Activites!')
