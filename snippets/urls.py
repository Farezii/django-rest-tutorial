from django.urls import path, include
from snippets import views
from rest_framework.routers import DefaultRouter

# For making posts with curl, use the following template
# curl -X POST http://localhost:8000/url/ -d some_data='text'
# -X to determine if its POST or GET
# -d to give out data like specific fields

#create router and register viewsets
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet, basename='snippet')
router.register(r'users', views.UserViewSet, basename='user')

#API URLs are now automatically determined by the router
urlpatterns = [
    path('', include(router.urls)),
]
