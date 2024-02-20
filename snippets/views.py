from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
# Create your views here.


@api_view(['GET', 'POST'])
def snippet_list(request, format=None):
    '''
    List all code snippets, or create a new snippet
    '''
    # Queries the database for all snippets
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)
    # Parses the request data into json and into a serializer
    elif request.method == 'POST':
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def snippet_detail(request, pk, format=None):
    '''
    Retrieve, update or delete a code snippet
    '''
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # Obtain a specific code snippet
    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)
    
    # If successful, updates a code snippet entry in the DB
    elif request.method == 'PUT':
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_204_NO_CONTENT)

    # Deletes a code nsippet entry
    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
