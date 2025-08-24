from django.urls import path
from django import *
from adminss import views

urlpatterns = [
    path('admins',views.admins,name="admins"),
    path('ta',views.teachapr,name="teachapr"),
    path('tad/<int:uid>',views.teachaproved,name="teachaproved"),
    path('sa',views.studapr,name="studapr"),
    path('sad/<int:uid>',views.studaproved,name="studaproved"),
    path('stfa',views.staffapr,name="staffapr"),
    path('stfad/<int:uid>',views.staffaproved,name="staffaproved"),
    path('dt',views.deleteteach,name="deleteteach"),
    path('dlt/<int:uid>',views.delteach,name="delteach"),
    path('ds',views.deletestud,name="deletestud"),
    path('dls/<int:uid>',views.delstud,name="delstud"),
    path('dv',views.deletevid,name="deletevid"),
    path('dvid/<int:uid>',views.delvid,name="delvid"),
    path('dsyl',views.deletesyl,name="deletesyl"),
    path('dsylla/<int:uid>',views.delsyl,name="delsyl"),
    
]

