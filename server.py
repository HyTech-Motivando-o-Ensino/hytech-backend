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
    response = {"msg": "Hello World!!"}
    
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

@app.post("/set/name/")
def set_name(request: Request):
    try:
        response = {"msg": "Como eu posso chamar você?"}
    except Exception as e:
        response = {"msg": "Não foi possível: {}".format(e)}
    
    return JSONResponse(response)

@app.get("/get/name/")
def get_name():
    try:
        response = {"msg": "Oi, Jorge"}
    except Exception as e:
        response = {"msg": "Não foi possível...: {}".format(e)}
    
    return JSONResponse(response)

@app.post("/set/pronoun/")
def set_pronoun(request: Request):
    try:
        response = {"msg": "Que pronome eu devo usar com você?"}
    except Exception as e:
        response = {"msg": "Não foi possível...: {}".format(e)}
    
    return JSONResponse(response)

@app.get("/get/pronoun/")
def get_pronoun():
    try:
        response = {"msg": "pronome feminino"}
    except Exception as e:
        response = {"msg": "Não foi possível...: {}".format(e)}
    
    return JSONResponse(response)

@app.get("/get/zoom_class_link/")
def get_zoom_class():
    try:
        response = {"msg": "https://cesar.zoom.us/j/94027650998"}
    except Exception as e:
        response = {"msg": "Não foi possível...: {}".format(e)}
    
    return JSONResponse(response)

@app.post("/set/academic_period/")
def set_academic_period(request: Request):
    try:
        response = {"msg": "Qual seu período?"}
    except Exception as e:
        response = {"msg": "Não foi possível...: {}".format(e)}
    
    return JSONResponse(response)

@app.get("/get/academic_period/")
def get_academic_period():
    try:
        response = {"msg": "2º"}
    except Exception as e:
        response = {"msg": "Não foi possível...: {}".format(e)}
    
    return JSONResponse(response)

@app.post("/set/course/")
def set_course(request: Request):
    try:
        response = {"msg": "Qual seu curso?"}
    except Exception as e:
        response = {"msg": "Não foi possível...: {}".format(e)}
    
    return JSONResponse(response)

@app.get("/get/course/")
def get_course():
    try:
        response = {"msg": "CC"}
    except Exception as e:
        response = {"msg": "Não foi possível...: {}".format(e)}
    
    return JSONResponse(response)

@app.post("/set/class/")
def set_class(request: Request):
    try:
        response = {"msg": "Qual a turma?"}
    except Exception as e:
        response = {"msg": "Não foi possível...: {}".format(e)}
    
    return JSONResponse(response)

@app.get("/get/class/")
def get_class():
    try:
        response = {"msg": "B"}
    except Exception as e:
        response = {"msg": "Não foi possível...: {}".format(e)}
    
    return JSONResponse(response)

@app.get("/get/classroom_code/")
def get_classroom_code():
    try:
        response = {"msg": "O código do classroom é..."}
    except Exception as e:
        response = {"msg": "Não foi possível...: {}".format(e)}
    
    return JSONResponse(response)

@app.get("/get/notices/")
def get_notices():
    try:
        response = {"msg": "Avisos:"}
    except Exception as e:
        response = {"msg": "Não foi possível...: {}".format(e)}
    
    return JSONResponse(response)

@app.get("/get/notices/discipline/")
def get_notices_discipline():
    try:
        response = {"msg": "Aviso da Disciplina..."}
    except Exception as e:
        response = {"msg": "Não foi possível...: {}".format(e)}
    
    return JSONResponse(response)
