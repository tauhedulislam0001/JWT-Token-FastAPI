# This function will check reqeust is authorize or not [Verification of the protected route]

from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from .jwt_handler import decode_jwt

class JWTBearer(HTTPBearer):
    def __init__(self, auto_Error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_Error)

    async  def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(JWTBearer, self).__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(status_code= 403, details= "Invalid or Expired Token!")
            return credentials.credentials
        else:
            raise HTTPException(status_code=403, details="Invalid or Expired Token!")

    def verify_jwt(self, jwt_token: str):
        isTokenValid: bool = False
        payload: decode_jwt(jwt_token)
        if payload:
            isTokenValid = True
        return isTokenValid