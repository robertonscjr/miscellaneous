from google.oauth2 import id_token
from google.auth.transport import requests

USER_EMAIL = "bob@gmail.com"
USER_ID = "11123456"


def verify_google_id_token(token, audience=None):
    try:
        idinfo = id_token.verify_oauth2_token(token, requests.Request(), audience)
        return True, idinfo
    except ValueError:
        return False, None
        
is_valid, decoded_google_token = auth_utils.verify_google_id_token(google_token)

if not is_valid:
    raise Exception("Token is not valid or it's expired")

# token params
issuer = decoded_google_token['iss']
user_id = decoded_google_token['sub']
email = decoded_google_token['email']
email_verified = decoded_google_token['email_verified']
image_url = decoded_google_token['picture']
first_name = decoded_google_token['given_name']
last_name = decoded_google_token['family_name']

is_from_this_user = (email == USER_EMAIL or username == USER_ID)

if not is_from_this_user or not email_verified or "accounts.google.com" not in issuer:
    raise Exception("Unauthorized token")
