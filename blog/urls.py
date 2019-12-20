from django.urls import path,include
from .views import *
urlpatterns = [
    path('',Site,name='site'),
    path('registr/',Registration.as_view(),name='registration'),
    path('auth/',Auth.as_view(),name='auth1'),
    path('logout/',logout.as_view(),name='logout'),
    path('notions/',Nots.as_view(),name = 'create_notes'),
    path('profile/', Profile.as_view(), name='profile'),
    path('delete/',Delete_notes.as_view(),name='delete_notes'),
    path('calendare/',Calendare.as_view(),name='calendare')
]
