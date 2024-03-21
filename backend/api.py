# from flask import make_response
# from flask import render_template
import uvicorn

from fastapi import FastAPI

app = FastAPI()


# @app.errorhandler(404)
# def not_found(error):
#     resp = make_response(render_template('error.html'), 404)
#     resp.headers['X-Something'] = 'A value'
#     return resp


@app.get("/")
def read_root():
    return {"Hello": "World"}

if __name__ == "__main__":
    uvicorn.run("api:app", host="0.0.0.0" ,reload=True)
