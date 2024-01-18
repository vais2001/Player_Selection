from .views import PlayerViewset,TeamSelectionAPIView
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('player', PlayerViewset, basename='player')

urlpatterns = [
    path('', include(router.urls)),
    path('player_selection/',TeamSelectionAPIView.as_view(),name='player_slection')
    
]

