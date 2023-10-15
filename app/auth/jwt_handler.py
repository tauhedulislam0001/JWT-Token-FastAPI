# This file is responsible for sign in, encoding, decoding and returning JWTs.

import time
import jwt
from decouple import config

JWT_SECRET = config("secret")
JWT_ALGORITHM = config('algorithm')


# Return generated token
def token_response(token: str):
    return {
        "access token": token
    }


# Function used for signin the JWT string
def sign_jwt(user_id: str):
    payload = {
        "userID": user_id,
        "expiry": time.time() + 600
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return token_response(token)


# Function used for decode jwt
def decode_jwt(token: str):
    try:
        decode_token = jwt.decode(token, JWT_SECRET, algorithm=JWT_ALGORITHM)
        return decode_token if decode_token["expiry"] >= time.time() else None
    except:
        return {}
