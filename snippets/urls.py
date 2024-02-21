from django.urls import path, include
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns

# For making posts with curl, use the following template
# curl -X POST http://localhost:8000/url/ -d some_data='text'
# -X to determine if its POST or GET
# -d to give out data like specific fields

# Urls for this app
urlpatterns = format_suffix_patterns([
    path('', views.api_root),
    path('snippets/', views.SnippetList.as_view(), name='snippet-list'),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view(), name='snippet-detail'),
    path('snippets/<int:pk>/highlight/',
         views.SnippetHighlight.as_view(), name='snippet-highlight'),
    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
])

# urlpatterns = format_suffix_patterns(urlpatterns)
