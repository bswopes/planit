from django.http import HttpResponse
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
def activity(request):
    return HttpResponse('Activites!')
