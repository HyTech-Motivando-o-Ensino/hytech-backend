from .connect import ConnectDB

# variavel que vai carregar a instância do banco de dados
db_instance = None
db_cursor = db_instance

def main():
    global db_instance
    global db_cursor
    
    db_instance = ConnectDB().connect()

def trans_sql_select(table, *args, where=None):
    try:
        sql_query = "SELECT "

        leng = len(args)
        cont = 0

        for arg in args:
            cont += 1
            if (cont == leng):
                arg = arg+" "
            else:
                arg = arg+", "
            
            sql_query += arg

        sql_query += "FROM "+table

        if where != None:
            sql_query += (" WHERE "+where)

        return sql_query
    except Exception as e:
        raise e

def get_status_db():
    try:
        sql = trans_sql_select('test', '*')
        result = get_select_executor(sql)
        return result[0][0]
    except Exception as e:
        raise e

def get_select_executor(sql):
    try:
        db_cursor = db_instance.cursor()
        db_cursor.execute(sql)
        fetchall = db_cursor.fetchall()
        return fetchall
    except Exception as e:
        raise e

def get_all_class():
    try:
        sql = trans_sql_select('class', 'id', 'course_id', 'period', 'zoom_id')
        result = get_select_executor(sql)

        list_class = list()

        for obj in result:
            list_class.append(obj)

        return list_class
    except Exception as e:
        raise e

def get_all_classroom_code():
    try:
        sql = trans_sql_select('classroom_code', 'id', 'subject_id', 'class_id', 'classroom_id')
        result = get_select_executor(sql)

        list_classroom_code = list()
        for obj in result:
            list_classroom_code.append(obj)

        return list_classroom_code
    except Exception as e:
        raise e

def get_all_courses():
    try:
        sql = trans_sql_select('courses', 'id', 'name', 'periods', 'type')
        result = get_select_executor(sql)
        
        list_courses = list()
        for obj in result:
            list_courses.append(obj)

        return list_courses
    except Exception as e:
        raise e

def get_all_courses_name_and_id():
    try:
        sql = trans_sql_select('courses', 'id', 'name')
        result = get_select_executor(sql)
        print(result)
        
        
        list_courses = list()
        
        for obj in result:
            courses = dict()
            courses['id'] = obj[0]
            courses['name'] = obj[1]
            
            list_courses.append(courses)

        return list_courses
    except Exception as e:
        raise e

def get_courses_all_periods_by_id_course(id_course):
    try:
        sql = trans_sql_select('courses', 'periods', where="id = '{}'".format(id_course))
        result = get_select_executor(sql)

        periods = dict()
        periods["periods"] = result[0][0]

        return periods
    except Exception as e:
        raise e

def get_all_professor_by_period_id_course(period, id_course):
    try:
        # pegar todos professor_id da tabela professor_course de um determinado curso(id)
        sql = trans_sql_select('professor_course', 'professor_id', where="course_id = '{}'".format(id_course))
        professor_class_id_list = get_select_executor(sql)
        print(professor_class_id_list)
        # pegar todos subjects_id de um determinado professor_id da tabela professor_class para poder separar os periodos
        
        # pegar todos subjects_id do 'periodo' passado
        
        # pegar todos contatos do professor no id passado
        

        # periods = dict()
        # periods["periods"] = result[0][0]

        return "success"
    except Exception as e:
        raise e

def get_all_professor():
    try:
        sql = trans_sql_select('professor', 'id', 'name', 'slack', 'email', 'whatsapp', 'contact')
        result = get_select_executor(sql)
        
        list_professor = list()
        for obj in result:
            list_professor.append(obj)

        return list_professor
    except Exception as e:
        raise e

def get_all_professor_class():
    try:
        sql = trans_sql_select('professor_class', 'id', 'professor_id', 'subject_id')
        result = get_select_executor(sql)
        
        list_professor_class = list()
        for obj in result:
            list_professor_class.append(obj)

        return list_professor_class
    except Exception as e:
        raise e

def get_all_professor_course():
    try:
        sql = trans_sql_select('professor_course', 'id', 'professor_id', 'course_id')
        result = get_select_executor(sql)
        
        list_professor_course = list()
        for obj in result:
            list_professor_course.append(obj)

        return list_professor_course
    except Exception as e:
        raise e

def get_all_subjects():
    try:
        sql = trans_sql_select('subjects', 'id', 'name', 'period')
        result = get_select_executor(sql)
        
        list_subjects = list()
        for obj in result:
            list_subjects.append(obj)

        return list_subjects
    except Exception as e:
        raise e

if __name__ == '__main__':
    main()