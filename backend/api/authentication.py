from rest_framework.authentication import TokenAuthentication as BaseTokenAuth
from rest_framework.authtoken.models import Token


class TokenAuthentication(BaseTokenAuth):
    keyword = "Bearer"
#for using this 1st we have to import it in views.py and remove default preinstall authentication