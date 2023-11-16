from flask import Flask,request,jsonify
import json
import sqlite3

app=Flask(__name__)



def db_connection():
    conn=None
    try:
        conn=sqlite3.connect('books.sqlite')
    except sqlite3.error as e:
        print(e)
    return conn
    
@app.route('/books',methods=['GET', 'POST'])
def view_books():
    conn=db_connection()
    cursor=conn.cursor()
    
    if request.method == 'GET':
        cursor=conn.execute("SELECT * FROM book")
        books=[
            dict(id=row[0],author=row[1],language=row[2],title=row[3])
            for row in cursor.fetchall()
        ]
        if books is not None:
            return jsonify(books)
        # if len(book_list)>0:
        #     return jsonify(book_list)
        # else:
        #     return "Nothing Found, 404"
        
    if request.method == 'POST':
        new_author=request.form['author']
        new_lang=request.form['language']
        new_title=request.form['title']
        # new_id=book_list[-1]['id']+1
        sql="""INSERT INTO book(author,language,title)
                VALUES(?,?,?)"""
        cursor=cursor.execute(sql,(new_author,new_lang,new_title))
        conn.commit()
        return f"Book with the id : {cursor.lastrowid} created sucessfully"
        
        
        # new_book={
        #     'id':new_id,
        #     'language':new_lang,
        #     'author':new_author,
        #     'title':new_title,
        # }
        # book_list.append(new_book)
        # return jsonify(book_list)
    
@app.route('/book/<int:id>',methods=['GET','PUT','DELETE'])
def books_modify(id):
    conn=db_connection()
    cursor=conn.cursor()
    book=None
    if request.method=="GET":
        cursor.execute("SELECT * FROM book WHERE id=?",(id,))
        rows=cursor.fetchall()
        for r in rows:
            book=r
        if book is not None:
            return jsonify(book)
        else:
            return "Something went wrong"
#         for books in book_list:
#             if books['id']==id:
#                 return jsonify(books)
#             pass
            
    if request.method=="PUT":
        sql="""UPDATE book
            SET title=?,
                author=?,
                language=?
            where id=?"""
        author=request.form['author']
        language=request.form['language']
        title=request.form['title']
        updated_book={
            "id":id,
            "author":author,
            "language":language,
            "title":title
        }
        conn.execute(sql,(author,language,title,id))
        conn.commit()
        return jsonify(updated_book)
#         for book in book_list:
#             if book['id']==id:
#                 new_author=request.form['author']
#                 new_lang=request.form['language']
#                 new_title=request.form['title']
#                 new_id=book_list[-1]['id']+1
                
#                 updated_book={
#                     'id':new_id,
#                     'language':new_lang,
#                     'author':new_author,
#                     'title':new_title,
#                 }
#                 return jsonify(updated_book)
    if request.method=='DELETE':
        sql=""" DELETE FROM book WHERE id=?"""
        conn.execute(sql,(id,))
        conn.commit()
        return f"The book with {id} is deleted successfully"
#         for index,book in enumerate(book_list):
#             if book['id']==id:
#                 book_list.pop(index)
#                 return jsonify(book_list)
        
    return jsonify({'message':'Invalid request'})
                
    
if __name__ == '__main__':
    app.run(debug=True)