CREATE TABLE `courses` ( `id` INT(10) NULL AUTO_INCREMENT , `name` VARCHAR(255) NOT NULL , `periods` TINYINT(3) NOT NULL , `type` VARCHAR(255) NOT NULL , PRIMARY KEY (`id`)) ENGINE = InnoDB;
CREATE TABLE `subjects` ( `id` INT(10) NULL AUTO_INCREMENT , `name` VARCHAR(255) NOT NULL , `period` INT NOT NULL , PRIMARY KEY (`id`)) ENGINE = InnoDB;
CREATE TABLE `class` ( `id` INT(10) NULL AUTO_INCREMENT , `course_id` INT(10) NOT NULL , `period` TINYINT(3) NOT NULL, `zoom_id` VARCHAR(255) NOT NULL, PRIMARY KEY (`id`)) ENGINE = InnoDB;
CREATE TABLE `professor` ( `id` INT(10) NULL AUTO_INCREMENT , `name` VARCHAR(255) NOT NULL , `slack` VARCHAR(255) NOT NULL , `email` VARCHAR(255) NOT NULL , `whatsapp` VARCHAR(255) NOT NULL , `other` VARCHAR(255) NOT NULL , `favorite` TINYINT(3) NOT NULL , PRIMARY KEY (`id`)) ENGINE = InnoDB;
CREATE TABLE `classroom_code` ( `id` INT(10) NULL AUTO_INCREMENT , `subject_id` VARCHAR(255) NOT NULL , `classroom_id` VARCHAR(255) NOT NULL , PRIMARY KEY (`id`)) ENGINE = InnoDB;


ALTER TABLE `classroom_code` ADD `class_id` INT(10) NOT NULL AFTER `subject_id`;
CREATE TABLE `professor_course` ( `id` INT(10) NULL AUTO_INCREMENT , `professor_id` INT(10) NOT NULL , `course_id` INT(10) NOT NULL , PRIMARY KEY (`id`)) ENGINE = InnoDB;
CREATE TABLE `professor_class` ( `id` INT(10) NULL AUTO_INCREMENT , `professor_id` INT(10) NOT NULL , `subject_id` INT(10) NOT NULL , PRIMARY KEY (`id`)) ENGINE = InnoDB;
CREATE TABLE `test` ( `status` VARCHAR(30));

INSERT INTO `test` VALUES ('Running with success!');