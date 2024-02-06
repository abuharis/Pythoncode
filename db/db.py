import sqlite3


class NotFoundError(Exception):
     pass

class NotAuthorized(Exception):
     pass

def blog_lst_to_json(item):
    return {
        'id': item[0],
        'published': item[1],
        'tilte': item[2],
        'content': item[3],
        'public': bool(item[4])
    }


def fetch_blogs():
    con = sqlite3.connect("C:\\Users\\abuharis.salih\\Documents\\database\\publish.db")
    cur = con.cursor()


    #Execute query
    cur.execute('SELECT * FROM posts')

    #Fetch data into a dict
    result = list(map(blog_lst_to_json, cur.fetchall()))

    con.close()

    return result


def fetch_blog(id: int):
    # try:
        con = sqlite3.connect("C:\\Users\\abuharis.salih\\Documents\\database\\publish.db")
        cur = con.cursor()


        #Execute query
        cur.execute(f"SELECT * FROM posts where id='{id}'")
        result = cur.fetchone()

        data = blog_lst_to_json(result)

        con.close()

        return data
    # except:
    #     raise FileNotFoundError("The data is not found in database. Check your query")


