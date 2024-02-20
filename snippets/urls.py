from django.urls import path
from snippets import views

# Urls for this app
urlpatterns = [
    path('snippets/', views.snippet_list),
    path('snippets/<int:pk>/', views.snippet_detail)
]