from django.urls import path, include
from snippets import views
from rest_framework.routers import DefaultRouter
from django.conf import settings
import oauth2_provider.views as oauth2_views

# For making posts with curl, use the following template
# curl -X POST http://localhost:8000/url/ -d some_data='text'
# -X to determine if its POST or GET
# -d to give out data like specific fields

#create router and register viewsets
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet, basename='snippet')
router.register(r'users', views.UserViewSet, basename='user')

# OAuth2 provider endpoints
oauth2_endpoint_views = [
    path('authorize/', oauth2_views.AuthorizationView.as_view(), name='authorize'),
    path('token/', oauth2_views.TokenView.as_view(), name='token'),
    path('revoke-token/', oauth2_views.RevokeTokenView.as_view(), name='revoke-token'),
]

# Debug endpoints
if settings.DEBUG:
    # OAuth2 application management endpoints
    oauth2_endpoint_views += [
        path('applications/', oauth2_views.ApplicationList.as_view(), name='list'),
        path('applications/register/',
             oauth2_views.ApplicationRegistration.as_view(), name='register'),
        path('applications/<pk>/',
             oauth2_views.ApplicationDetail.as_view(), name='detail'),
        path('applications/<pk>/delete/',
             oauth2_views.ApplicationDelete.as_view(), name='delete'),
        path('applications/<pk>/update/',
             oauth2_views.ApplicationUpdate.as_view(), name='update'),
    ]

    # Oauth2 token management endpoints
    oauth2_endpoint_views += [
        path('authorized-tokens/', oauth2_views.AuthorizedTokensListView.as_view(),
             name='authorized-token-list'),
        path('authorized-tokens/<pk>/delete/', oauth2_views.AuthorizedTokenDeleteView.as_view(),
             name='authorized-token-delete'),
    ]

#API URLs are now automatically determined by the router
urlpatterns = [
    path('o/', include((oauth2_endpoint_views, 'oauth2_provider'), namespace='oauth2_provider')),
    path('', include(router.urls)),
]
