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

@app.get("/get/courses/all/name/id/")
def get_courses_all():
    try:
        result = dao.get_all_courses_name_and_id()
        response = {"msg": result}
    except Exception as e:
        response = {"msg": "Ao visualizar o status do banco de dados: {}".format(e)}

    return JSONResponse(response)

@app.get("/get/course/periods/{id_course}/")
def get_curse_periods_by_id_course(id_course: int):
    try:
        result = dao.get_courses_all_periods_by_id_course(id_course)
        response = {"msg": result}
    except Exception as e:
        response = {"msg": "Ao visualizar o status do banco de dados: {}".format(e)}
    
    return JSONResponse(response)

@app.get("/get/professors/{period}/{id_course}/")
def get_professors_by_period_and_id_course(period: int, id_course: int):
    try:
        result = dao.get_all_professor_by_period_id_course(period, id_course)
        response = {"msg": "o id do curso passado foi: {}".format(result)}
    except Exception as e:
        response = {"msg": "Ao visualizar o status do banco de dados: {}".format(e)}
    
    return JSONResponse(response)

@app.get("/get/contacts/{id_professor}/")
def get_contacts_by_id_professor(id_professor: int):
    try:
        response = {"msg": "o id do curso passado foi: {}".format(id_professor)}
    except Exception as e:
        response = {"msg": "Ao visualizar o status do banco de dados: {}".format(e)}
    
    return JSONResponse(response)


@app.get("/get/subject/all/")
def get_subject_all():
    try:
        response = {"msg": "Sucesso"}
    except Exception as e:
        response = {"msg": "Ao visualizar o status do banco de dados: {}".format(e)}
    
    return JSONResponse(response)

@app.get("/get/subject/{id_class}")
def get_subject_by_id_class(id_class: int):
    try:
        response = {"msg": "o id do curso passado foi: {}".format(id_class)}
    except Exception as e:
        response = {"msg": "Ao visualizar o status do banco de dados: {}".format(e)}
    
    return JSONResponse(response)

@app.get("/get/class/all/")
def get_class_all():
    try:
        response = {"msg": "Sucesso"}
    except Exception as e:
        response = {"msg": "Ao visualizar o status do banco de dados: {}".format(e)}
    
    return JSONResponse(response)

@app.get("/get/class/{id_professor}}")
def get_class_by_id_professor(id_professor: int):
    try:
        response = {"msg": "o id do curso passado foi: {}".format(id_professor)}
    except Exception as e:
        response = {"msg": "Ao visualizar o status do banco de dados: {}".format(e)}
    
    return JSONResponse(response)
