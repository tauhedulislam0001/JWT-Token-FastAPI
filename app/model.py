from pydantic import BaseModel, Field, EmailStr


class PostSchema(BaseModel):
    id: int = Field(default=None)
    title: str = Field(default=None)
    content: str = Field(default=None)

    class Config:
        schema_extra = {
            "post_demo": {
                "title": "some title about animal",
                "content": "some content about animal"
            }
        }


class UserSchema(BaseModel):
    username: str = Field(default=None)
    email: EmailStr = Field(default=None)
    password: str = Field(default=None)

    class Config:
        the_schema = {
            "user_demo": {
                "username": "Ben Khan",
                "email": "ben@gmail.com",
                "password": "123465"
            }
        }


class UserLoginSchema(BaseModel):
    email: EmailStr = Field(default=None)
    password: str = Field(default=None)

    class Config:
        the_schema = {
            "user_login_demo": {
                "email": "ben@gmail.com",
                "password": "123456"
            }
        }
