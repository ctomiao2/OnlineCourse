# -*- coding: utf-8 -*-
# desc: mysql crud, use connection pool
import MySQLdb
from DBUtils.PooledDB import PooledDB
from MySQLdb.cursors import DictCursor
import conf.db_conf as DBConf
import utils.log as log

class MySQLHelper(object):

	_conn_pool = None

	@staticmethod
	def _get_connection():
		if MySQLHelper._conn_pool is None:
			_conn_pool = PooledDB(creator=MySQLdb, mincached=DBConf.MySQL.MinCached, maxcached=DBConf.MySQL.MaxCached,
				host=DBConf.MySQL.Host, user=DBConf.MySQL.LoginUser, passwd=DBConf.MySQL.Password, db=DBConf.MySQL.DBName,
				autocommit=True, use_unicode=False, charset=DBConf.MySQL.Charset, cursorclass=DictCursor)

		return _conn_pool.connection()

	def __init__(self):
		self._conn = MySQLHelper._get_connection()
		self._cursor = self._conn.cursor()

	def db_find(self, sql, params=None, limit=None):
		if params is None:
			count = self._cursor.execute(sql)
		else:
			count = self._cursor.execute(sql, params)

		if count <= 0:
			return None

		if limit is None:
			return self._cursor.fetchall()
		else:
			return self._cursor.fetchmany(limit)

	def db_insert(self, sql, value):
		self._cursor.execute(sql, value)
		self._cursor.execute("SELECT @@IDENTITY AS id")
		result = self._cursor.fetchall()
		log.info('', 'MySQLHelper::db_insert', 'sql=%s, value=%s', sql, value)
		return result[0]['id']
	
	def db_insert_many(self, sql, values):
		count = self._cursor.executemany(sql, values)
		log.info('', 'MySQLHelper::db_insert_many', 'sql=%s, values=%s', sql, values)
		return count

	def db_update(self, sql, params=None):
		log.info('', 'MySQLHelper::db_update', 'sql=%s, params=%s', sql, params)
		return self._query(sql, params)

	def db_delete(self, sql, params=None):
		log.info('', 'MySQLHelper::db_delete', 'sql=%s, params=%s', sql, params)
		return self._query(sql, params)

	def _query(self, sql, params=None):
		if params is None:
			count = self._cursor.execute(sql)
		else:
			count = self._cursor.execute(sql, params)
		return count

	def transaction_begin(self):
		self._conn.autocommit(False)

	def transaction_end(self, is_commit=True):
		self._conn.autocommit(True)
		if is_commit:
			self._conn.commit()
		else:
			self._conn.rollback()

	def dispose(self, is_commit=True):
		self.transaction_end(is_commit)
		self._cursor.close()
		self._conn.close()




