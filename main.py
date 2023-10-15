import uvicorn
from fastapi import FastAPI, Body, Depends
from app.model import PostSchema, UserSchema, UserLoginSchema
from app.auth.jwt_handler import sign_jwt
from app.auth.jwt_bearer import JWTBearer

posts = [
    {
        "id": 1,
        "title": "penguins ",
        "text": "Penguins are a group of aquatic flightless birds. "
    },
    {
        "id": 2,
        "title": "tigers ",
        "text": "Tigers are the largest living cat species and a members of the genus Panthera. "
    },
    {
        "id": 3,
        "title": "Koalas ",
        "text": "Koalas is arboreal herbivorous marsupial native to Australia. "
    },
]

users = []
app = FastAPI()


# Get for testing
@app.get('/', tags=['test'])
def greet():
    return {"Hello": "world!"}


# GET all post
@app.get("/posts", dependencies=[Depends(JWTBearer())], tags=["posts"])
def get_posts():
    return {
        "data": posts
    }


# GET single post {id}
@app.get("/posts/{id}", tags=["posts"])
def get_single_post(id: int):
    if id > len(posts):
        return {
            "Error": "Posts with this ID does not exit!"
        }
    for post in posts:
        if post["id"] == id:
            return {
                "data": post
            }


# Post a single blog post [A handler for creating a post]
@app.post("/posts/add", tags=["posts"])
def add_post(post: PostSchema):
    post.id = len(posts) + 1
    posts.append(post.dict())
    return {"info": "Post added!"}


# User Signup [Create a new user]
@app.post("/user/signup", tags=["users"])
def user_signup(user: UserSchema = Body(default=None)):
    users.append(user)
    return sign_jwt(user.email)


def user_check(data: UserLoginSchema):
    for user in users:
        if user.email == data.email and user.password == data.password:
            return True
        return False


@app.post("/user/login", tags=["users"])
def user_login(user: UserLoginSchema = Body(default=None)):
    if user_check(user):
        return sign_jwt(user.email)
    else:
        return {"Error": "Invalid login credential!"}
