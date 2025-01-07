import pymysql
from models.post import Post
import ast

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
            records = cursor.fetchall()
            posts = []
            for record in records:
                post = Post(
                    id=record[0],         
                    title=record[1],       
                    content=record[2],     
                    category=record[3],    
                    tags=record[4],        
                    createdAt=str(record[5]),   
                    updateAt=str(record[6])     
                )
                posts.append(post.dict())  # Convertir a dict y agregar a la lista
            
            return posts  # Retornar la lista de diccionarios
        except Exception as e:
            print("Error in get all post: ", e)
            self.conexion.rollback()
        finally:
            cursor.close()
            
    
