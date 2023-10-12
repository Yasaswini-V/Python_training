from dbutils import result_as_dict

def get_all_users(cursor):
    cursor.execute('select * from REVIEWS')
    results=result_as_dict(cursor)
    for res in results:
            print(res)
    
def add_new_user(cursor,id,name,email):
    cursor.execute('insert into Users (User_ID,Name,Email) values (?,?,?)',id,name,email)

def get_user_review(cursor,id):
    cursor.execute('''SELECT R.userid,B.title, R.rating, R.review_text
                    FROM Reviews R
                    JOIN Books B ON R.bookid = B.bookid
                    WHERE R.userid = ?;''',id)
    results=result_as_dict(cursor)
    for res in results:
            print(res)