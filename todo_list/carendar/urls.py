from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

app_name = "carendar"
urlpatterns = [ 
    path("", login_required(views.index), name="index"),
    path("done/<int:pk>/", login_required(views.done), name="done"),
    path("delete/<int:pk>/", login_required(views.delete), name="delete"),
    path('update-event/', login_required(views.update_event), name='update_event'),
]

