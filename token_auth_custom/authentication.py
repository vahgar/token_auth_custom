import datetime
from django.utils import timezone
from django.utils.timezone import utc
from rest_framework.authentication import TokenAuthentication
from rest_framework import exceptions

class ExpiringTokenAuthentication(TokenAuthentication):
    def authenticate_credentials(self, key):
        try:
            token = self.model.objects.get(key=key)
        except self.model.DoesNotExist:
            raise exceptions.AuthenticationFailed('Invalid token')

        if not token.user.is_active:
            raise exceptions.AuthenticationFailed('User inactive or deleted')

        # This is required for the time comparison
        utc_now = timezone.now()
        print(str(utc_now - token.created))

        if utc_now - token.created > datetime.timedelta(hours=24):
            token.delete()
            raise exceptions.AuthenticationFailed('Token has expired')

        return token.user, token
