from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from talk.models import Talk
from api.serializers import TalkSerializer

# Create your views here.

@api_view(['GET', 'POST'])
def talk_list(request):
    if request.method == 'GET':
        talks = Talk.objects.all()
        serializer = TalkSerializer(talks, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TalkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def talk_detail(request, pk):
    try:
        talk = Talk.objects.get(pk=pk)
    except Talk.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TalkSerializer(talk)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TalkSerializer(talk, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        talk.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



