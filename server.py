from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.responses import JSONResponse

app = FastAPI()

app.add_middleware(
    TrustedHostMiddleware, allowed_hosts=["*"]
)

@app.get("/")
def index():
    response = {"msg": "Hello World"}
    
    return JSONResponse(response)
