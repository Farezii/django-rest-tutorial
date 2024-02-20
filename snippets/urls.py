from django.urls import path, include
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns

# For making posts with curl, use the following template
# curl -X POST http://localhost:8000/url/ -d some_data='text'
# -X to determine if its POST or GET
# -d to give out data like specific fields

# Urls for this app
urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('snippets/', views.SnippetList.as_view()),
    path('users/', views.UserList.as_view()),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)