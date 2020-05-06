import os
import json
import sqlalchemy
from sqlalchemy.dialects.mysql import insert
import pymysql
from pprint import pprint

def make_basic_record_list(list_to_import):
    new_records = []
    for tweet in list_to_import:
        record = {}
        record["created_at"] = tweet["created_at"]
        record["id_str"] = tweet["id_str"]

        record["user_id"] = tweet["user"]["id"]

        # if "extended_tweet" in tweet:
        #    record["text"] = tweet["extended_tweet"]["full_text"]
        # else:
        record["text"] = tweet["full_text"]

        new_records.append(record)

    return new_records


def init_db():

    engine = sqlalchemy.create_engine(
        'mysql+pymysql://root:cO2rm2JY9mHNPqkr0GSs@localhost/twitbotto')

    global connection
    connection = engine.connect()
    metadata = sqlalchemy.MetaData()
    global tweets
    tweets = sqlalchemy.Table(
        'tweets', metadata, autoload=True, autoload_with=engine)
    global searches
    searches = sqlalchemy.Table(
        'searches', metadata, autoload=True, autoload_with=engine)
    global users
    users = sqlalchemy.Table(
        'users', metadata, autoload=True, autoload_with=engine)


def make_search_id(search_date, search_term):

    add_search_record_query = sqlalchemy.insert(searches).values(
        search_term=search_term,
        date=search_date)

    get_last_id_query = sqlalchemy.text(
        "SELECT LAST_INSERT_ID()"
        )

    result_new_search_record = connection.execute(add_search_record_query)
    last_record_added = connection.execute(get_last_id_query)
    search_id = last_record_added.fetchone()
    search_id = search_id[0]
    return search_id


def insert_list(search_id, record_list):

    for t in record_list:
        t['search_id'] = search_id

    insert_stmt = insert(tweets).values(record_list)

    params = 'id_str'

    on_duplicate_key_stmt = insert_stmt.on_duplicate_key_update(
        text=insert_stmt.inserted.text,
    )

    connection.execute(on_duplicate_key_stmt)

# +++++++++++ TESTING +++++++++++++


'''
test_record_list = [
    {'created_at': 'Mon May 04 00:40:46 +0000 2020', 'id_str': '1257107866781130758', 'user_id': 14247236, 'text': 'BREAKING: Trump just admitted he was told in his security briefing for months about coronavirus. Trump knew about the threat and did nothing. His failed response led us to this catastrophe. He belongs in prison.'},
    {'created_at': 'Mon May 04 11:55:31 +0000 2020', 'id_str': '1257277674017472516', 'user_id': 39349894, 'text': 'Trump Boat Parade!!! Thank you Florida!!! 🇺🇸🇺🇸🇺🇸 https://t.co/Ex5yTKV3zg'}
]

init_db()

search_id = make_search_id('2020-05-04', 'trump')

insert_list(search_id, test_record_list)

'''
