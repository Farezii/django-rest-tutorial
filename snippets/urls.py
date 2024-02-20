from django.urls import path
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns

# For making posts with curl, use the following template
# curl -X POST http://localhost:8000/url/ -d some_data='text'
# -X to determine if its POST or GET
# -d to give out data like specific fields

# Urls for this app
urlpatterns = [
    path('snippets/', views.snippet_list),
    path('snippets/<int:pk>/', views.snippet_detail)
]

urlpatterns = format_suffix_patterns(urlpatterns)