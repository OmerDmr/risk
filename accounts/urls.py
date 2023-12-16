from django.conf.urls import url
from .views import *

app_name = "accounts"

urlpatterns = [

    url(r'^login/$', login_view, name="login"),
    url(r'^logout/$', logout_view, name="logout"),
    url(r'^register/$', register_view, name="register"),
    url(r'^uptProfile/$', updateProfile, name="uptProfile"),
    url(r'^viewProfile/$', viewProfile, name="viewProfile"),
    url(r'^home/$', homeView, name="home"),
    url(r'^firstPage/$', firstPage, name="firstPage"),



    # Turkish

    url(r'^loginTr/$', login_viewTr, name="loginTr"),
    url(r'^logoutTr/$', logout_viewTr, name="logoutTr"),
    url(r'^registerTr/$', register_viewTr, name="registerTr"),
    url(r'^uptProfileTr/$', updateProfileTr, name="uptProfileTr"),
    url(r'^viewProfileTr/$', viewProfileTr, name="viewProfileTr"),
    url(r'^homeTr/$', homeViewTr, name="homeTr"),
    url(r'^firstPageTr/$', firstPageTr, name="firstPageTr"),



]