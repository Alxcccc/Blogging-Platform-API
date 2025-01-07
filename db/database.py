import pymysql
from models.post import Post
from models.updatepost import UpdatePost

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
    
    def get_post(self, id: int):
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
    
    def del_post(self, id: int):
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
    
    def upd_post(self, id: int, post: UpdatePost):
        cursor = self.conexion.cursor()
        cursor.execute("SELECT title, content, category, tags FROM posts WHERE postID = %s", (id,))
        current_record = cursor.fetchone()
        
        if current_record:
            current_title, current_content, current_category, current_tags = current_record
            updates = []
            values = []
            if post.title is not None and post.title != current_title:
                updates.append("title = %s")
                values.append(post.title)
            if post.content is not None and post.content != current_content:
                updates.append("content = %s")
                values.append(post.content)
            if post.category is not None and post.category != current_category:
                updates.append("category = %s")
                values.append(post.category)
            if post.tags is not None and post.tags != current_tags:
                updates.append("tags = %s")
                values.append(post.tags)
            if not updates:
                return False
            sql = f"UPDATE posts SET updateAt = '{post.updateAt}', {', '.join(updates)} WHERE postID = %s"
            values.append(id)
            try:
                    cursor.execute(sql, values)
                    self.conexion.commit()
                    result = self.get_post(id)
                    return result
            except Exception as e:
                    print("Error in updating the post: ", e)
                    self.conexion.rollback()
                    return False
            finally:
                cursor.close()
        else:
            return False

    def get_post_term(self, term: str):
        cursor = self.conexion.cursor()
        sql = f"SELECT * FROM posts WHERE title LIKE '%{term}%' OR content LIKE '%{term}%' OR category LIKE '%{term}%' LIMIT 100"
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