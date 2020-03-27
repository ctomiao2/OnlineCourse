# -*- coding: utf-8 -*-
# desc: mysql表维护脚本
import MySQLdb
import os
import sys
print os.getcwd()
sys.path.append(os.getcwd())
import conf.db_conf as db_conf

def _create_table(db, cursor, sql):
	try:
		cursor.execute(sql)
		db.commit()
	except:
		db.rollback()
		import sys
		sys.excepthook(*sys.exc_info())

def create_user_table(db, cursor):
	print 'start create_user_table'
	sql = """ CREATE TABLE IF NOT EXISTS USER (
			  id INT UNSIGNED AUTO_INCREMENT,
			  name VARCHAR(20) NOT NULL,
			  birth DATE,
			  psw VARCHAR(32) NOT NULL,
			  PRIMARY KEY (id),
			  INDEX index_name (name)
	) """
	_create_table(db, cursor, sql)

def create_course_table(db, cursor):
	print 'start create_course_table'
	sql = """ CREATE TABLE IF NOT EXISTS COURSE (
			  id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
			  name VARCHAR(20) NOT NULL,
			  category VARCHAR(20),
			  subscribes INT UNSIGNED,
			  likes INT UNSIGNED,
			  unlikes INT UNSIGNED,
			  INDEX index_likes (likes),
			  INDEX index_subscribes (subscribes),
			  INDEX index_name (name),
			  INDEX index_category (category)

	) """
	_create_table(db, cursor, sql)

def create_subscribe_table(db, cursor):
	print 'start create_subscribe_table'
	sql = """ CREATE TABLE IF NOT EXISTS SUBSCRIBE (
			  course_id INT UNSIGNED NOT NULL,
			  user_id INT UNSIGNED NOT NULL,
			  score INT UNSIGNED,
			  PRIMARY KEY (course_id, user_id),
			  INDEX index_user (user_id),
			  INDEX index_score (score)
	) """
	_create_table(db, cursor, sql)

def create_similarity_table(db, cursor):
	print 'start create_similarity_table'
	sql = """ CREATE TABLE IF NOT EXISTS SIMILARITY (
			  user_id_1 INT UNSIGNED NOT NULL,
			  user_id_2 INT UNSIGNED NOT NULL,
			  score INT UNSIGNED,
			  PRIMARY KEY (user_id_1, user_id_2),
			  INDEX index_user2 (user_id_2),
			  INDEX index_score (score)
	) """
	_create_table(db, cursor, sql)

def main():
	print 'begin establish tables...'
	db = MySQLdb.connect(db_conf.MySQL.Host, db_conf.MySQL.LoginUser, db_conf.MySQL.Password, 
		db_conf.MySQL.DBName, charset=db_conf.MySQL.Charset)
	cursor = db.cursor()
	create_user_table(db, cursor)
	create_course_table(db, cursor)
	create_subscribe_table(db, cursor)
	create_similarity_table(db, cursor)
	print 'finish establish tables...'
	db.close()

if __name__ == '__main__':
	main()