from django.http import HttpResponse

from planit.settings import STATIC_URL
from django.shortcuts import get_object_or_404 as get, get_list_or_404 as get_list
from schedule.models import User
import timeline

def cal(request, user_id):
    users = [get(User, pk=user_id)]
    if user_id == '1':
        users += [get(User, pk=2)]
    info = []
    for u in users:
        activities = u.activities.all()
        activity_names = [activity.name for activity in activities]
        info.append( (u.name, [(activity.pk, activity.name, activity.event, str(activity.startTime), str(activity.endTime), activity.description)  for activity in activities]) )
    return HttpResponse(timeline.genPage(info))
#    return render_to_response('templates/image.html',{'laser': STATIC_URL})

from django.template import RequestContext, Context
from django.shortcuts import get_object_or_404, render_to_response
from schedule.models import Activity


from django.template import RequestContext, Context
from django.shortcuts import get_object_or_404, render_to_response
from schedule.models import Activity, User

def activity(request, activity_id):
    p = get_object_or_404(Activity, pk=activity_id)
    return render_to_response('templates/activity2.html', {'activity': p, 
                                                           'user_list': p.user_set.all(),
                                                          },
    context_instance=RequestContext(request))
