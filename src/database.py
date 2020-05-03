import os
import json
import sqlalchemy

def init_db():
	
	engine = sqlalchemy.create_engine(
    	'mysql+pymysql://root:cO2rm2JY9mHNPqkr0GSs@localhost/twitbotto')

	connection = engine.connect()
	metadata = sqlalchemy.MetaData()
	tweets = sqlalchemy.Table(
	    'tweets', metadata, autoload=True, autoload_with=engine)
	searches = sqlalchemy.Table(
	    'searches', metadata, autoload=True, autoload_with=engine)
	users = sqlalchemy.Table(
	    'users', metadata, autoload=True, autoload_with=engine)


def insert_list():
	query = sqlalchemy.insert(newTable).values(
	    id=1,
	    name='Software Ninjaneer',
	    salary=60000.00,
	    active=True)

	result_proxy = connection.execute(query)

	query = sqlalchemy.insert(newTable)

	new_records = [{'id': '2', 'name': 'record1', 'salary': 80000, 'active': False},
	               {'id': '3', 'name': 'record2', 'salary': 70000, 'active': True}]

	result_proxy = connection.execute(query, new_records)
