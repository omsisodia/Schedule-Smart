"""tt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from . import view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', view.callindex),
    path('contact/', view.contact),
    path('about/', view.about),
    path('login/', view.login),
    path('signin/', view.signin),
    path('timetable/', view.timetable),
    path('program/', view.program),
    path('faculty/', view.faculty),
    path('subject/', view.subject),
    path('lecture/', view.lecture),
    path('lab/', view.lab),
    path('generate/', view.generate),

# Final Timetable
    path('output/', view.output),


    path('view_course/', view.view_course),
    path('view_faculty/', view.view_faculty),
    path('view_labRoom/', view.view_labRoom),
    path('view_lectureRoom/', view.view_lectureRoom),
    path('view_program/', view.view_program),

# INPUTS
    path('loginadmin', view.loginadmin),
    path('callsignin', view.callsignin),

    path('callprogram', view.callprogram),
    path('callsubjects', view.callsubjects),
    path('calllecture', view.calllecture),
    path('calllab', view.calllab),
    path('callfaculty', view.callfaculty),

# VIEWS
    path('callview_course/', view.callview_course),
    path('callview_lectureRoom/', view.callview_lectureRoom),
    path('callview_labRoom/', view.callview_labRoom),
    path('callview_faculty/', view.callview_faculty),
    path('callview_program/', view.callview_program),
]
