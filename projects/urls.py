from django.conf.urls import url
from  projects.views import *
from django.urls import include, path


app_name = "projects"

urlpatterns = [
    
    
    # English

    #deprem
    url(r'^(?P<id>\d+)/depremCalculateResponses/$', depremCalculateResponses, name='depremCalculateResponses'),
    url(r'^depremAllProject/$',depremAllProject,name='depremAllProject'),
    url(r'^(?P<id>\d+)/depremView/$',depremView,name='depremView'),
    url(r'^depremCreate/$', depremProjectCreate, name='depremCreate'),
    url(r'^(?P<id>\d+)/depremUpdate/$', depremUpdate,name='depremUpdate'),
    url(r'^(?P<id>\d+)/depremDelete/$', depremProjectDelete,name='depremDelete'),
    url(r'^(?P<id>\d+)/depremInfUpdate/$', depremProjectInfUpdate,name='depremInfUpdate'),
    url(r'^(?P<id>\d+)/depremFeatureUpdate/$', depremFeatureUpdate,name='depremFeatureUpdate'),
    url(r'^(?P<id>\d+)/depremTermPrj/$', depremTermPrj,name='depremTermPrj'),
    url(r'^(?P<id>\d+)/depremDeltaMaxes/$', depremDeltaMaxes,name='depremDeltaMaxes'),
    path('newResponseDpr/<int:pId>/<int:rId>/', newResponseDpr, name='newResponseDpr'),
    path('viewResponseDpr/<int:pId>/<int:rId>/', viewResponseDpr, name='viewResponseDpr'),
    path('deleteResponseDpr/<int:pId>/<int:rId>/', deleteResponseDpr, name='deleteResponseDpr'),
    path('addResponseDpr/<int:pId>/', addResponseDpr, name='addResponseDpr'),
    url(r'^(?P<id>\d+)/depremInfView/$', depremInfView, name='depremInfView'),


    #sel
    url(r'^selAllProject/$',selAllProject,name='selAllProject'),
    url(r'^(?P<id>\d+)/selView/$',selView,name='selView'),
    url(r'^selCreate/$', selProjectCreate, name='selCreate'),
    url(r'^(?P<id>\d+)/selUpdate/$', selUpdate,name='selUpdate'),
    url(r'^(?P<id>\d+)/selDelete/$', selProjectDelete,name='selDelete'),
    url(r'^(?P<id>\d+)/selInfUpdate/$', selProjectInfUpdate,name='selInfUpdate'),
    url(r'^(?P<id>\d+)/selFeatureUpdate/$', selFeatureUpdate,name='selFeatureUpdate'),
    url(r'^(?P<id>\d+)/selTermPrj/$', selTermPrj,name='selTermPrj'),
    url(r'^(?P<id>\d+)/selCalculateResponses/$', selCalculateResponses,name='selCalculateResponses'),
    url(r'^(?P<id>\d+)/selDeltaMaxes/$', selDeltaMaxes,name='selDeltaMaxes'),
    path('newResponseSel/<int:pId>/<int:rId>/', newResponseSel, name='newResponseSel'),
    path('viewResponseSel/<int:pId>/<int:rId>/', viewResponseSel, name='viewResponseSel'),
    path('deleteResponseSel/<int:pId>/<int:rId>/', deleteResponseSel, name='deleteResponseSel'),
    path('addResponseSel/<int:pId>/', addResponseSel, name='addResponseSel'),
    url(r'^(?P<id>\d+)/selInfView/$', selInfView, name='selInfView'),
    
    url(r'^about/$',about,name='about'),
    url(r'^allProject/$',allProject,name='allProject'),


    #Turkish

    # deprem
    url(r'^(?P<id>\d+)/depremCalculateResponsesTr/$', depremCalculateResponsesTr, name='depremCalculateResponsesTr'),
    url(r'^depremAllProjectTr/$', depremAllProjectTr, name='depremAllProjectTr'),
    url(r'^(?P<id>\d+)/depremViewTr/$', depremViewTr, name='depremViewTr'),
    url(r'^depremCreateTr/$', depremProjectCreateTr, name='depremCreateTr'),
    url(r'^(?P<id>\d+)/depremUpdateTr/$', depremUpdateTr, name='depremUpdateTr'),
    url(r'^(?P<id>\d+)/depremDeleteTr/$', depremProjectDeleteTr, name='depremDeleteTr'),
    url(r'^(?P<id>\d+)/depremInfUpdateTr/$', depremProjectInfUpdateTr, name='depremInfUpdateTr'),
    url(r'^(?P<id>\d+)/depremFeatureUpdateTr/$', depremFeatureUpdateTr, name='depremFeatureUpdateTr'),
    url(r'^(?P<id>\d+)/depremTermPrTrj/$', depremTermPrjTr, name='depremTermPrjTr'),
    url(r'^(?P<id>\d+)/depremDeltaMaxesTr/$', depremDeltaMaxesTr, name='depremDeltaMaxesTr'),
    path('newResponseDprTr/<int:pId>/<int:rId>/', newResponseDprTr, name='newResponseDprTr'),
    path('viewResponseDprTr/<int:pId>/<int:rId>/', viewResponseDprTr, name='viewResponseDprTr'),
    path('deleteResponseDprTr/<int:pId>/<int:rId>/', deleteResponseDprTr, name='deleteResponseDprTr'),
    path('addResponseDprTr/<int:pId>/', addResponseDprTr, name='addResponseDprTr'),
    url(r'^(?P<id>\d+)/depremInfViewTr/$', depremInfViewTr, name='depremInfViewTr'),

    # sel
    url(r'^(?P<id>\d+)/selCalculateResponsesTr/$', selCalculateResponsesTr, name='selCalculateResponsesTr'),
    url(r'^selAllProjectTr/$', selAllProjectTr, name='selAllProjectTr'),
    url(r'^(?P<id>\d+)/selViewTr/$', selViewTr, name='selViewTr'),
    url(r'^selCreateTr/$', selProjectCreateTr, name='selCreateTr'),
    url(r'^(?P<id>\d+)/selUpdateTr/$', selUpdateTr, name='selUpdateTr'),
    url(r'^(?P<id>\d+)/selDeleteTr/$', selProjectDeleteTr, name='selDeleteTr'),
    url(r'^(?P<id>\d+)/selInfUpdateTr/$', selProjectInfUpdateTr, name='selInfUpdateTr'),
    url(r'^(?P<id>\d+)/selFeatureUpdateTr/$', selFeatureUpdateTr, name='selFeatureUpdateTr'),
    url(r'^(?P<id>\d+)/selTermPrjTr/$', selTermPrjTr, name='selTermPrjTr'),
    url(r'^(?P<id>\d+)/selDeltaMaxesTr/$', selDeltaMaxesTr, name='selDeltaMaxesTr'),
    path('newResponseSelTr/<int:pId>/<int:rId>/', newResponseSelTr, name='newResponseSelTr'),
    path('viewResponseSelTr/<int:pId>/<int:rId>/', viewResponseSelTr, name='viewResponseSelTr'),
    path('deleteResponseSelTr/<int:pId>/<int:rId>/', deleteResponseSelTr, name='deleteResponseSelTr'),
    path('addResponseSelTr/<int:pId>/', addResponseSelTr, name='addResponseSelTr'),
    url(r'^(?P<id>\d+)/selInfViewTr/$', selInfViewTr, name='selInfViewTr'),

    url(r'^aboutTr/$', aboutTr, name='aboutTr'),
    url(r'^allProjectTr/$', allProjectTr, name='allProjectTr'),

]
