from django.urls import path
from . import views

app_name = "carendar"
urlpatterns = [ 
    path("", views.index, name="index"),
    path("done/<int:pk>/", views.done, name="done"),
    path("delete/<int:pk>/", views.delete, name="delete"),
    path('update-event/', views.update_event, name='update_event'),
]

