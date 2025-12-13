"""tourist_db URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from touristapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$', views.index, name='index'),
    re_path(r'^reg/$', views.reg, name='reg'),
    re_path(r'^login/$', views.login, name='login'),
    re_path(r'^admin_home/$', views.admin_home, name='admin_home'),
    re_path(r'^user_home/$', views.user_home, name='user_home'),
    re_path(r'^reg_view/$', views.reg_view, name='reg_view'),

    re_path(r'^bookinfo/(?P<pk>\d+)/$', views.bookinfo, name='bookinfo'),
    re_path(r'^bookinfo_view/$', views.bookinfo_view, name='bookinfo_view'),
    re_path(r'^bookinfo_view_u/$', views.bookinfo_view_u, name='bookinfo_view_u'),
    re_path(r'^bookinfo_del/(?P<pk>\d+)/$', views.bookinfo_del, name='bookinfo_del'),
    re_path(r'^bookinfo_update/(?P<pk>\d+)/$', views.bookinfo_update, name='bookinfo_update'),
    re_path(r'^bookinfo_db/$', views.bookinfo_db, name='bookinfo_db'),

    re_path(r'^customerinfo/$', views.customerinfo, name='customerinfo'),
    re_path(r'^customerinfo_view/$', views.customerinfo_view, name='customerinfo_view'),
    re_path(r'^customer_del/(?P<pk>\d+)/$', views.customerinfo_del, name='customerinfo_del'),
    re_path(r'^customer_update/(?P<pk>\d+)/$', views.customerinfo_update, name='customerinfo_update'),
    re_path(r'^customerinfo_db/$', views.customerinfo_db, name='customerinfo_db'),

    re_path(r'^feedbackinfo/$', views.feedbackinfo, name='feedbackinfo'),
    re_path(r'^feedbackinfo_view/$', views.feedbackinfo_view, name='feedbackinfo_view'),
    re_path(r'^feedbackinfo_del/(?P<pk>\d+)/$', views.feedbackinfo_del, name='feedbackinfo_del'),
    re_path(r'^feedbackinfo_update/(?P<pk>\d+)/$', views.feedbackinfo_update, name='feedbackinfo_update'),
    re_path(r'^feedbackinfo_db/$', views.feedbackinfo_db, name='feedbackinfo_db'),

    re_path(r'^login/$', views.login, name='login'),

    re_path(r'^paymentinfo/(?P<pk>\d+)/$', views.paymentinfo, name='paymentinfo'),
    re_path(r'^paymentinfo_view/$', views.paymentinfo_view, name='paymentinfo_view'),
    re_path(r'^paymentinfo_del/(?P<pk>\d+)/$', views.paymentinfo_del, name='paymentinfo_del'),
    re_path(r'^paymentinfo_update/(?P<pk>\d+)/$', views.paymentinfo_update, name='paymentinfo_update'),
    re_path(r'^paymentinfo_db/$', views.paymentinfo_db, name='paymentinfo_db'),

    re_path(r'^placeinfo/$', views.placeinfo, name='placeinfo'),
    re_path(r'^placeinfo_view/$', views.placeinfo_view, name='placeinfo_view'),
    re_path(r'^placeinfo_view_c/$', views.placeinfo_view_c, name='placeinfo_view_c'),
    re_path(r'^placeinfo_view2_c/$', views.placeinfo_view2_c, name='placeinfo_view2_c'),

    re_path(r'^placeinfo_del/(?P<pk>\d+)/$', views.placeinfo_del, name='placeinfo_del'),
    re_path(r'^placeinfo_update/(?P<pk>\d+)/$', views.placeinfo_update, name='placeinfo_update'),
    re_path(r'^placeinfo_db/$', views.placeinfo_db, name='placeinfo_db'),

    re_path(r'^resortinfo/$', views.resortinfo, name='resortinfo'),
    re_path(r'^resortinfo_view/$', views.resortinfo_view, name='resortinfo_view'),
    re_path(r'^resortinfo_view_c/$', views.resortinfo_view_c, name='resortinfo_view_c'),
    re_path(r'^resortinfo_update/(?P<pk>\d+)/$', views.resortinfo_update, name='resortinfo_update'),

    re_path(r'^routeinfo/(?P<pk>\d+)/$', views.routeinfo, name='routeinfo'),
    re_path(r'^routeinfo_view/(?P<pk>\d+)/$', views.routeinfo_view, name='routeinfo_view'),
    re_path(r'^routeinfo_del/(?P<pk>\d+)/$', views.routeinfo_del, name='routeinfo_del'),
    re_path(r'^routeinfo_update/(?P<pk>\d+)/$', views.routeinfo_update, name='routeinfo_update'),
    re_path(r'^routeinfo_db/$', views.routeinfo_db, name='routeinfo_db'),

    re_path(r'^vehicleinfo/$', views.vehicleinfo, name='vehicleinfo'),
    re_path(r'^vehicleinfo_view/$', views.vehicleinfo_view, name='vehicleinfo_view'),
    re_path(r'^vehicleinfo_view_c/$', views.vehicleinfo_view_c, name='vehicleinfo_view_c'),
    re_path(r'^vehicleinfo_del/(?P<pk>\d+)/$', views.vehicleinfo_del, name='vehicleinfo_del'),
    re_path(r'^vehicleinfo_update/(?P<pk>\d+)/$', views.vehicleinfo_update, name='vehicleinfo_update'),
    re_path(r'^vehicleinfo_db/$', views.vehicleinfo_db, name='vehicleinfo_db'),

    re_path(r'^reg_del/(?P<pk>\d+)/$', views.reg_del, name='reg_del'),

    re_path(r'^simple_upload/$', views.simple_upload, name='simple_upload'),
    re_path(r'^simple_upload_view/$', views.simple_upload_view, name='simple_upload_view'),

    re_path(r'^change_password/$', views.change_password, name='change_password'),

    re_path(r'^send_email/$', views.send_email, name='send_email'),
    re_path(r'^mainindex/$', views.mainindex, name='mainindex'),

    re_path(r'^forgotpass/$', views.forgotpass, name='forgotpass'),
    re_path(r'^otp/$', views.otp, name='otp'),
    re_path(r'^pass_db/$', views.pass_db, name='pass_db'),
    re_path(r'^google_map/(?P<stype>\w+)/$', views.google_map, name='google_map'),

    re_path(r'^place_wise_year/$', views.place_wise_year, name='place_wise_year'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

