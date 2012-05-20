from django.http import HttpResponse
from django.template import RequestContext, Context
from django.shortcuts import get_object_or_404, render_to_response
from schedule.models import Activity

def cal(request):
    return HttpResponse('In the schedule index')
def activity(request, activity_id):
    p = get_object_or_404(Activity, pk=activity_id)
    #q = get_object_or_404(UserActivity, pk=useractivity_id)
    #return HttpResponse("Activity %s" % activity_id)
    #return HttpResponse("Activity %s" % p.name)
    return render_to_response('templates/activity2.html', {'activity': p, 'user_list': p.user_set.all()},
    context_instance=RequestContext(request))
