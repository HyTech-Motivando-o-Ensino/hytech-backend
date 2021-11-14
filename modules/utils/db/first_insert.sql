insert into subjects (name, period) values ("Fundamentos de Projetos I", 1);
select * from subjects;

insert into courses (name, periods, type) values ("Ciência da Computação", 8, 1);
describe courses;

insert into courses (name, periods, type) values ("Ciência da Computação", 8, 1);

insert into professor (name, slack, email, whatsapp, contact) 
values ("Guilherme Pereira", "@guilherme.pereira", "gp@cesar.school", "81987384911", "0");
describe professor;

insert into class (course_id, period, zoom_id) values (1, 1, "983 8944 9849");
select * from class;

insert into classroom_code (subject_id, class_id, classroom_id) values (1, 1, "xyajd");
describe classroom_code;

insert professor_class (professor_id, subject_id) values (1, 1);
describe professor_class;

insert professor_course (professor_id, course_id) values (1, 1);
