# token_auth_custom
This is a helper package for django_rest_framework. This gives you ability to customise token authentication.

## Feature List: 
 1. A Token that expires in 24 Hours & deletes it as well
 2. Everytime you make a request with this Token, it extends the time limit to next 24 Hours
 3. You can also customise the time period by default it's 24Hours
