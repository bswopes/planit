from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'planit.views.home', name='home'),
    # url(r'^planit/', include('planit.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^cal/(?P<user_id>\d+)$', 'schedule.views.cal'),
    url(r'^activity/(?P<activity_id>\d+)/$', 'schedule.views.activity'),
    url(r'^activity/(?P<activity_id>\d+)/join/$', 'schedule.views.join_activity'),
    url(r'^activity/(?P<activity_id>\d+)/unjoin/$', 'schedule.views.unjoin_activity'),
    #url(r'^activity/$', 'schedule.views.activity'),
)
