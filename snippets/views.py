from .models import Snippet
from .serializers import SnippetSerializer, UserSerializer
from rest_framework import generics, permissions, renderers, viewsets, status
from django.contrib.auth.models import User
from django.contrib.auth.models import User
from django.contrib.auth import logout
from .permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from django.http import HttpResponseRedirect
from rest_framework.reverse import reverse
from rest_framework.views import APIView
# Create your views here.

class SnippetViewSet(viewsets.ModelViewSet):
    '''
    This viewset automatically provides 'list', 'create', 'retrieve', 'update' and 'destroy' actions.
    
    Additionaly, we also provide an extra 'highlight' action
    '''
    queryset=Snippet.objects.all()
    serializer_class=SnippetSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    
    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    '''
    This viewset automatically provides 'list' and 'retrieve' actions
    '''
    queryset = User.objects.all()
    serializer_class = UserSerializer

class LogoutView(APIView):
    """
    Djano 5 does not have GET logout route anymore, so Django Rest Framework UI can't log out.
    This is a workaround until Django Rest Framework implements POST logout.
    Details: https://github.com/encode/django-rest-framework/issues/9206
    """
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/')

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'snippets': reverse('snippet-list', request=request, format=format),
    })