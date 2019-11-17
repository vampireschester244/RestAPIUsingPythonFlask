import pymysql
from dbconfig import MySql
from application import application
from flask import Flask, jsonify, request

# CRUD Operation - CREATE
@application.route('/add', methods=['POST'])
def add_book():
	try:
		json = request.json
		book_name = json['book_name']
		author_name = json['author_name']
		publisher_name = json['publisher_name']
		if book_name and author_name and publisher_name and request.method == 'POST':
			SQL_Query = "INSERT INTO books(book_name, author_name, publisher_name) VALUES(%s, %s, %s)"
			data = (book_name, author_name, publisher_name,)
			connection =MySql.connect()
			Pointer = connection.cursor()
			Pointer.execute(SQL_Query, data)
			connection.commit()
			response = jsonify('Book added!')
			response.status_code = 200
			return response
		else:
			return not_found()
	except Exception as e:
		print(e)
	finally:
		Pointer.close()
		connection.close()

#CRUD Operation - READ
@application.route('/book/<int:id>')
def book(id):
	try:
		connection =MySql.connect()
		Pointer = connection.cursor(pymysql.cursors.DictCursor)
		Pointer.execute("SELECT * FROM books WHERE book_id=%s", id)
		record = Pointer.fetchone()
		response = jsonify(record)
		response.status_code = 200
		return response
	except Exception as e:
		print(e)
	finally:
		Pointer.close()
		connection.close()

#CRUD Operation - UPDATE
@application.route('/update', methods=['POST'])
def update_book():
	try:
		json = request.json
		id = json['id']
		book_name = json['book_name']
		author_name = json['author_name']
		publisher_name = json['publisher_name']
		if book_name and author_name and publisher_name and id and request.method == 'POST':
			SQL_Query = "UPDATE books SET book_name=%s, author_name=%s, publisher_name=%s WHERE book_id=%s"
			data = (book_name, author_name, publisher_name, id,)
			connection =MySql.connect()
			Pointer = connection.cursor()
			Pointer.execute(SQL_Query, data)
			connection.commit()
			response = jsonify('Book updated!')
			response.status_code = 200
			return response
		else:
			return not_found()
	except Exception as e:
		print(e)
	finally:
		Pointer.close()
		connection.close()

#CRUD Operation - DELETE
@application.route('/delete/<int:id>')
def delete_book(id):
	try:
		connection =MySql.connect()
		Pointer = connection.cursor()
		Pointer.execute("DELETE FROM books WHERE book_id=%s", (id,))
		connection.commit()
		response = jsonify('book deleted!')
		response.status_code = 200
		return response
	except Exception as e:
		print(e)
	finally:
		Pointer.close()
		connection.close()

if __name__ == "__main__":
    application.run()