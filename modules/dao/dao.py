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

def trans_sql_select_with_conditions(table, *args, where=None, subcondition=None):
    # SELECT professor_id FROM professor_course WHERE periods = '1' and professor_id = '1' and professor_id = '2';
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
            sql_query += (" and (")

        if subcondition != None and where != None:
            cont = 0
            size = len(subcondition)
            for obj in subcondition:
                key, value = obj
                cont+=1
                
                if cont == 1:
                    sql_query += "{} = '{}'".format(key, value)
                elif cont == size:
                    sql_query += " or {} = '{}')".format(key, value)
                else:
                    sql_query += " or {} = '{}'".format(key, value)

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
        professor_course_id_list = get_select_executor(sql)
        print(professor_course_id_list)
        
        # test_trans_sql = trans_sql_select_with_conditions('professor_periods', 'professor_id',
        #                                  where="periods = '{}'".format(period), subcondition=[("professor_id", 1)
        #                                                                                       ,('professor_id', 2)
        #                                                                                       ,('professor_id', 3)
        #                                                                                       ,("professor_id", 4)])
        
        # print(test_trans_sql)
        
        professor_ids_list = list()
        
        print(professor_course_id_list == [])
        
        for val in professor_course_id_list:
            print(val)
            professor_ids_list.append(("professor_id", val[0]))

        # print(professor_ids_list)
        
        sql = trans_sql_select_with_conditions("professor_periods", "professor_id", where="periods = '{}'".format(period), 
                                               subcondition=professor_ids_list)
        print(sql)

        # sql = trans_sql_select("professor_periods", "professor_id", where="periods = '{}'".format(period))
        professor_periods_id_list = get_select_executor(sql)
        print(professor_periods_id_list)

        professor_list = list()
        professor_dict = dict()

        for professor_id in professor_periods_id_list:
            id = professor_id[0]
            print(id)

            sql = trans_sql_select("professor", "name", "slack", "email", "whatsapp", "other", "favorite",
                                   where="id = '{}'".format(id))

            print(sql)

            professor_values = get_select_executor(sql)

            professor_dict["name"] = professor_values[0][0]
            professor_dict["slack"] = professor_values[0][1]
            professor_dict["email"] = professor_values[0][2]
            professor_dict["whatsapp"] = professor_values[0][3]
            professor_dict["other"] = professor_values[0][4]
            professor_dict["favorite"] = professor_values[0][5]

            professor_list.append(professor_dict)

        return professor_list
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