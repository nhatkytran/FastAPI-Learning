from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()


@app.get('/')
def root():
    return {'message': 'Hell beautiful World'}


@app.post('/createposts')
def create_posts(payload=Body()):
    print(payload)
    return {'message': 'Create posts'}
