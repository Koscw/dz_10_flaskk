import sqlite3
import datetime
nw=datetime.time.strftime("%m/%d/%Y, %H:%M:%S")

connection = sqlite3.connect('test.db')
cursor = connection.cursor()

 
def cr_tbl():
	query ="""
	CREATE TABLE IF NOT EXISTS articles (
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		title varchar(24) UNIQUE,
		text TEXT,
		created_at nw
	)"""
	cursor.execute(query)
	connection.commit()

cr_tbl()

# cursor.execute('insert into users (email, password) values ("petr1@gmail.com", "qwerty123")')
# connection.commit()


# for i in range(5):
# 	email = input('Email: ')
# 	password = input('Password: ')
# 	name = input('Name: ')
# 	try:
# 		cursor.execute(f'insert into users (email, password, name) values ("{email}", "{password}", "{name}")')
# 		connection.commit()
# 	except sqlite3.IntegrityError:
# 		print('Email already exists')

keys = ['id', 'title', 'text', 'created_at']
cursor.execute('select * from articles order by id desc')
artcl = cursor.fetchone()
print(artcl)
# users = cursor.fetchall()  # Забираем все записи и возвращает список записей
#user = cursor.fetchone()  # Забираем одну запись

# users = [dict(zip(keys, user)) for user in users]

#print(user)

def get_article(search):
		cursor.execute(f"SELECT * FROM articles WHERE text LIKE '%{search}%' OR title LIKE '%{search}%' ")
		connection.commit()


def create_article(title, text , created_at):
	cursor.execute(f'insert into articles (title, text, created_at) values ("{title}", "{text}", "{created_at()}")')
	connection.commit()
def update_article(id,title,text):
	cursor.execute(f'UPDATE articles SET title=:title AND text=:text WHERE id=:id',
					{'title':title,'text':text , 'id':id })
def delete_article(id):
	cursor.execute(f'DELETE from articles WHERE id={id}')
#"DELETE from articles WHERE id=:id",{'id':id}'
"""
delete from demo where id = 1
select * from users where email like '%vasya%'
insert into users (email, password) values ("petr1@gmail.com", "qwerty123")
Update demo set name = "Changed name" where id = 2
"""

"""
Создать таблицу articles с полями:
id - идентификатор записи
title - заголовок
text - текст
created_at - дата создания

Написать функции для создания/редактирования/удаления/получения записей

При получении записей позволить пользователю искать по заголовоку или тексту
"""


