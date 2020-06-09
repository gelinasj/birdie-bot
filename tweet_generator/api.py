#from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from tweeter.tweet import *

class PostTweet(APIView):
    def post(self, request, *args, **kwargs):
        response = tweet()
        if response.status_code >= 200 and response.status_code < 300:
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
