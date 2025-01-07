from fastapi import APIRouter, HTTPException
from models.post import Post
from models.updatepost import UpdatePost
from db.database import DataBase

router = APIRouter()

@router.post("/post", response_model=Post)
async def create_post(new_post: Post) -> Post:
    try:
        db = DataBase()
        result = db.add_post(new_post)
        if result:
            new_post.id = result
            return new_post
        else:
            raise HTTPException(status_code=400)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error in create post: {e}")
    finally:
        db.close_conn()
        
@router.get("/post", response_model=list[Post])
async def get_all_post() -> list:
    try:
        db = DataBase()
        result = db.get_posts()
        db.close_conn()
        if result:
            return result
        else:
            raise HTTPException(status_code=400)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error in get posts: {e}")
    
@router.get("/post/{id}", response_model=Post)
async def get_id_post(id: int) -> Post:
    try:
        db = DataBase()
        result = db.get_post(id)
        db.close_conn()
        if result:
            return result
        else:
            raise HTTPException(status_code=400)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error in get post: {e}")

@router.get("/post/term/{term}", response_model=list[Post])
async def get_term_post(term: str):
    try:
        db = DataBase()
        result = db.get_post_term(term)
        db.close_conn()
        if result:
            return result
        else:
            raise HTTPException(status_code=400)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error in get posts: {e}")

@router.post("/post/{id}", response_model=Post)
async def update_post(id: int, new_post: UpdatePost):
    try:
        db = DataBase()
        result_update = db.upd_post(id, new_post)
        db.close_conn()
        if result_update:
            return result_update
        else:
            raise HTTPException(status_code=400)
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error in update post: {e}")

@router.delete("/post/{id}", response_model=dict)
async def delete_post(id: int) -> dict:
    try:
        db = DataBase()
        result = db.del_post(id)
        db.close_conn()
        if result:
            return {"status": True, "message": f"The post {id} was deleted successfully.", "data": None}
        else:
            raise HTTPException(status_code=404, detail=f"Not Found the id: {id}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error in delete post: {e}")






