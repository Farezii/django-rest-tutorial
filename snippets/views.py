from .models import Snippet
from .serializers import SnippetSerializer
from rest_framework import mixins, generics
# Create your views here.


class SnippetList(generics.GenericAPIView, mixins.CreateModelMixin, mixins.ListModelMixin):
    '''
    List all code snippets, or create a new snippet
    '''
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class SnippetDetail(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    '''
    Retrieve, update or delete a code snippet
    '''
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def get(self, request, *args, **kwargs):
       return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
