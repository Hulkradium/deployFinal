from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("", views.index, name="index"),
    path("signup", views.signup, name="signup"),
    path("home", views.home, name="home"),
    path("login", views.login, name="login"),
    path("logout", views.logout, name="logout"),
    path("<str:lect_id>/home/", views.home, name="home"),
    path("<str:lect_id>/intervention_report/",
         views.intervention_report, name="intervention_report"),
    path("<str:lect_id>/intervention_list/",
         views.intervention_list, name="intervention_list"),
    path("<str:lect_id>/student_list/", views.student_list, name="student_list"),
    path("<str:lect_id>/intervention_list/update_intervention/<str:int_id>",
         views.update_intervention, name="update_intervention"),
    path("<str:lect_id>/intervention_list/update_intervention/save_update_intervention/<str:int_id>",
         views.save_update_intervention, name="save_update_intervention"),
    path("<str:lect_id>/intervention_list/delete_intervention/<int:int_id>/",
         views.delete_intervention, name='delete_intervention'),
]

urlpatterns += staticfiles_urlpatterns()
