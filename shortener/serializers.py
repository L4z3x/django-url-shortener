from rest_framework import serializers
from .models import URL

class URLSerializer(serializers.ModelSerializer):
    original_url = serializers.URLField(required=True) 
    short_code = serializers.CharField(read_only=True,required=False)
    class Meta:
        model = URL
        fields = ['id','original_url', 'short_code', 'created_at']
        required = ['original_url']        