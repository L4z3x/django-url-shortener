
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404, redirect
from .models import URL
from .serializers import URLSerializer

@api_view(['POST'])
def create_short_url(request):
    serializer = URLSerializer(data=request.data)
    if serializer.is_valid():
        print(serializer.validated_data)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def redirect_to_original(request, short_code):
    url_instance = get_object_or_404(URL, short_code=short_code)
    return redirect(url_instance.original_url)

@api_view(['GET'])
def list_urls(request):
    urls = URL.objects.all()
    serializer = URLSerializer(urls, many=True)
    return Response(serializer.data)
