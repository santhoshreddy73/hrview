"""HR_View URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from urllib.request import urlretrieve
from django.contrib import admin
from django.urls import path,include
from app import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    path('admin/', admin.site.urls),
    path('',views.home_login,name='main'),
    path('logout',views.logout_user,name='logout'),
    path('home',views.home,name='home'),
    path('create',views.new_appoint_letter,name='create-doc'),
    path('downloaddoc/<int:pk>',views.download_apt_letter_for_existing_user,name='dwnldDoc'),
    path('aptcreation',views.new_appoint_letter,name='appointmntcreation'),
    path('termination/<str:pk>',views.termination_letter,name="termination"),
    path('hike_info/<str:pk>',views.employee_hike,name='hike_info'),
    path('hike_issue/<str:pk>',views.hike_issue,name='hike_issue'),
    
    path('user_activities',views.user_activities,name='user_activities'),
    path('main',views.main,name='main'),
    path('user_downloads',views.user_downloads,name='user_downloads'),
    path('service_agreement_creation/<str:pk>',views.issue_new_service_agreement,name='create_service_agreement'),
    path('letter_of_intent_creation/<str:pk>/',views.issue_letter_of_intent,name="letter_of_intent_creation"),
    path('letters',views.view_issued_letters,name='files'),
    path('preview_apt/<str:pk>',views.preview_apt,name='preview_apt'),
    path('preview_int_ltr/<str:pk>',views.preview_int_ltr,name='privw_int_ltr'),
    path('preview_servc_agreement/<str:pk>',views.preview_servc_agreement,name='preview_servc_agreement'),
    path('intrn_crtificate_crtn/<str:pk>',views.internship_certificate_creation,name='intrn_crtificate_crtn'),
    path('view_intrn_certificate/<str:pk>',views.view_intern_certificate,name='view_intrn_certificate'),
    path('view_hik/<str:pk>',views.view_hik,name='view_hik'),
    path('hike_edit/<str:pk>',views.hike_edit,name='hike_edit'),
    path('offer_ltr/<str:pk>',views.offer_ltr_generator,name='offer_ltr'),
    path('view_offer_ltr/<str:pk>',views.view_offer_ltr,name='view_offer_ltr'),
    path('send_apt/<str:pk>',views.send_apt_pdf_mail_on_pdf,name='send_apt'),
    path('send_intL/<str:pk>',views.send_ltr_int,name='send_intL'),
    path('send_trm_ltr/<str:pk>',views.send_trm_ltr,name='send_trm_ltr'),
    path('send_srv_agmnt/<str:pk>',views.send_srv_agmnt,name='send_srv_agmnt'),
    path('send_hik_ltr/<str:pk>',views.send_hik_ltr,name='send_hik_ltr'),
    path('send_offer_ltr/<str:pk>',views.send_offer_ltr,name='send_offer_ltr'),

    path('send_Iltr/<str:pk>',views.send_internship_ltr,name='send_Iltr'),
    path('view_trm/<str:pk>',views.preview_trm,name='view_trm'),
    path('sidebar',views.template_test)

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

#https://trial.onelawindia.in/docs/ui/js_files/modal_popup.js