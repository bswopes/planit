from django.http import HttpResponse
from planit.settings import STATIC_URL
from django.shortcuts import get_object_or_404 as get, get_list_or_404 as get_list
from schedule.models import User, UserActivity
import timeline

def cal(request, user_id):
    p = get(User, pk=user_id)
    user_activities = get_list(UserActivity, user=p)
    activities = [activity.activity for activity in user_activities]
    activity_names = [activity.name for activity in activities]
    info = [ (p.name, [(activity.pk, activity.name, activity.event, str(activity.startTime), str(activity.endTime), activity.description)  for activity in activities]) ]
    return HttpResponse('In the schedule index for user %s, %s: %s, %s' % (user_id, p, str(activity_names), timeline.genPage(info)))
#    return render_to_response('templates/image.html',{'laser': STATIC_URL})

def activity(request):
    return HttpResponse('Activites!')

from django.template import RequestContext, Context
from django.shortcuts import get_object_or_404, render_to_response
from schedule.models import Activity

def activity(request, activity_id):
    p = get_object_or_404(Activity, pk=activity_id)
    #q = get_object_or_404(UserActivity, pk=useractivity_id)
    #return HttpResponse("Activity %s" % activity_id)
    #return HttpResponse("Activity %s" % p.name)
    user_list = Activity.objects.select_related()
    return render_to_response('templates/activity2.html', {'activity': p, 'user_list': user_list},
    context_instance=RequestContext(request))
