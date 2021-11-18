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
    
@app.get("/test/db/")
def test_db():
    try:
        # testar o banco de dados
        # result = dao.trans_sql('class','id', 'course_id', 'period', 'zoom_id')
        result = dao.get_all_class()
        print(result)
        response = {"msg": result}
    except Exception as e:
        response = {"msg": "Ao visualizar o status do banco de dados: {}".format(e)}
    
    return JSONResponse(response)

@app.get("/get/courses/all/")
def get_courses_all():
    try:
        response = {"msg": "Sucesso"}
    except Exception as e:
        response = {"msg": "Ao visualizar o status do banco de dados: {}".format(e)}
    
    return JSONResponse(response)

@app.get("/get/periods/{id_course}/")
def get_periods_by_id_course(id_course: int):
    try:
        
        response = {"msg": "o id do curso passado foi: {}".format(id_course)}
    except Exception as e:
        response = {"msg": "Ao visualizar o status do banco de dados: {}".format(e)}
    
    return JSONResponse(response)