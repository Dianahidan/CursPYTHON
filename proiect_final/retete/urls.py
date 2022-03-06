from django.urls import path
from retete.views import retete_view

app_name = 'retete'

urlpatterns = [
     path('', retete_view),
]