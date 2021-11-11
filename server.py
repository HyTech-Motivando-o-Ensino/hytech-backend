from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.responses import JSONResponse
from modules.dao import dao

#initialize
app = FastAPI()
dao.main()

app.add_middleware(
    TrustedHostMiddleware, allowed_hosts=["*"]
)

@app.get("/")
def index():
    response = {"msg": "Hello World"}
    
    return JSONResponse(response)

@app.get("/status/db/")
def status_db():
    try:
        # testar o banco de dados
        result = dao.get_status_db()
        response = {"msg": result}
    except Exception as e:
        response = {"msg": "Ao visualizar o status do banco de dados: {}".format(e)}
    
    return JSONResponse(response)
    
