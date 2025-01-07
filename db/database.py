import pymysql
from models.post import Post

class DataBase():
    def __init__(self):
        self.conexion = self.conn_db()

    def conn_db(self):
        try:
            conn = pymysql.connect(
                host='localhost',
                user='root',
                password='facebookalec7',
                database='project'
            )
            print("Conexión exitosa a la base de datos.")
            return conn
        except Exception as e:
            print(e)
    
    def close_conn(self):
        if self.conexion:
            self.conexion.close()
            return
    
    def add_post(self, post: Post):
        last_id = None
        cursor = self.conexion.cursor()
        sql = "INSERT INTO posts (title, content, category, tags, createdAt, updateAt) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (post.title, post.content, post.category, str(post.tags), post.createdAt, post.updateAt)
        try:
            cursor.execute(sql, val)
            self.conexion.commit()
            print("Post add succesfully")
            last_id = cursor.lastrowid
        except Exception as e:
            print("Error in add the post: ", e)
            self.conexion.rollback()
        finally:
            cursor.close()
            return last_id
    
    def get_posts(self):
        cursor = self.conexion.cursor()
        sql = "SELECT * FROM posts"
        try:
            cursor.execute(sql)
            self.conexion.commit()
            registers = cursor.fetchall()
            posts = []
            for register in registers:
                list_format = eval(register[4])
                post = Post(
                    id=register[0],         
                    title=register[1],
                    content=register[2],     
                    category=register[3],
                    tags=list_format,        
                    createdAt=str(register[5]),   
                    updateAt=str(register[6])     
                )
                posts.append(post.dict())
            return posts
        except Exception as e:
            print("Error in get all post: ", e)
            self.conexion.rollback()
        finally:
            cursor.close()
    
    def get_post(self, id):
        cursor = self.conexion.cursor()
        sql = "SELECT * FROM posts WHERE postID =%s"
        val = id
        try:
            cursor.execute(sql, val)
            self.conexion.commit()
            register = cursor.fetchone()
            list_format = eval(register[4])
            post = Post(
                id=register[0],         
                title=register[1],
                content=register[2],     
                category=register[3],
                tags=list_format,        
                createdAt=str(register[5]),   
                updateAt=str(register[6])     
            )
            return post
        except Exception as e:
            print("Error in get the post: ", e)
            self.conexion.rollback()
        finally:
            cursor.close()
    
    def del_post(self, id):
        cursor = self.conexion.cursor()
        sql = "DELETE FROM `posts` WHERE `postID`=%s"
        val = id
        try:
            cursor.execute(sql, val)
            self.conexion.commit()
            affected_rows = cursor.rowcount
            if affected_rows > 0:
                return True
            else:
                return False
            
        except Exception as e:
            print("Error in delete the post: ", e)
            self.conexion.rollback()
        finally:
            cursor.close()