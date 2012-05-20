from django.http import HttpResponse

from planit.settings import STATIC_URL
from django.shortcuts import get_object_or_404 as get, get_list_or_404 as get_list
from schedule.models import User
import timeline

def cal(request, user_id):
    users = [get(User, pk=user_id)]
    if user_id == '1':
        for uid in '23':
            users += [get(User, pk=uid)]
    info = []
    for u in users:
        activities = u.activities.all()

        friends = [len([user for user in activity.user_set.all() if user.name != users[0].name]) for activity in activities]
        info.append( \
            (u.name, \
                 [(activities[i].pk, \
                   activities[i].name + \
                   ' <i>(' + str(friends[i]) + ')</i>', \
                   str(activities[i].event), \
                   str(activities[i].startTime), \
                   str(activities[i].endTime), \
                   activities[i].description) \
                   for i in range(len(activities))]) )
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
