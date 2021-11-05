from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.responses import JSONResponse

app = FastAPI()


app.add_middleware(
    TrustedHostMiddleware, allowed_hosts=["127.0.0.1"]
)

app.get("/")
def index(request: Request):
    response = {"msg": "Hello World"}
    
    return JSONResponse(response)
