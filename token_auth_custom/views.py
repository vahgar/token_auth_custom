import datetime
from django.utils import timezone
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from django.http import HttpResponse
import json

class ObtainExpiringAuthToken(ObtainAuthToken):
    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            token, created =  Token.objects.get_or_create(user=serializer.validated_data['user'])
            user = serializer.validated_data['user']
            print(user)
            response_data = {}
            response_data['token'] = token.key
            return HttpResponse(json.dumps(response_data), content_type="application/json")
        response_data = {}
        response_data['detail'] = "Please Check Your Credentials"
        return HttpResponse(json.dumps(response_data), content_type="application/json")

obtain_expiring_auth_token = ObtainExpiringAuthToken.as_view()
