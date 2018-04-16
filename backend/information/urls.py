from django.conf.urls import url

from information.views import *

app_name = 'information'

urlpatterns = [

    url(r'^information/reports/$', ReportViewSet.as_view(), name='view-reports'),
    url(r'^information/accounts/$', AccountViewSet.as_view(), name='view-accounts'),
    url(r'^information/careers/$', CareerViewSet.as_view(), name='view-careers'),
    url(r'^information/tenders/$', TenderViewSet.as_view(), name='view-tenders'),
    url(r'^information/teqip/$', TEQIPViewSet.as_view(), name='view-teqip'),
    url(r'^information/rti/$', RTIViewSet.as_view(), name='view-rti'),
    url(r'^information/nirf/$', NIRFViewSet.as_view(), name='view-nirf'),
    url(r'^information/nba/$', NBAViewSet.as_view(), name='view-nba'),
    url(r'^information/more/$', MoreViewSet.as_view(), name='view-more'),

    ]
