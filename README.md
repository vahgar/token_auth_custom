# token_auth_custom
This is a helper package for django_rest_framework. This gives you ability to customise token authentication.

## Feature List: 
 1. A Token that expires in 24 Hours & deletes it as well
 2. Everytime you make a request with this Token, it extends the time limit to next 24 Hours
 3. You can also customise the time period by default it's 24Hours

## Steps to include it in your django project:

## Install DjangoRestframework
    pip install djangorestframework

## Download:
 Download zip and Copy the folder "token_auth_custom" (The one which has __init__.py file) in your module which has user model defined in it.
## Check your settings.py:
      INSTALLED_APPS = (
       '.......',
       '.......',
       'rest_framework',
       'rest_framework.authtoken',
      )
      
      REST_FRAMEWORK = {
         'DEFAULT_AUTHENTICATION_CLASSES': (
           'rest_framework.authentication.SessionAuthentication',
           '"{youremodule}".token_auth_custom.authentication.ExpiringTokenAuthentication',
          ),

         'DEFAULT_PERMISSION_CLASSES': (
           'rest_framework.permissions.IsAuthenticated',
          )
      }
