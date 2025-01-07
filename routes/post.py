from fastapi import APIRouter, HTTPException
from models.post import Post
from models.updatepost import UpdatePost
from db.database import DataBase

router = APIRouter()

@router.get("/post")
async def get_all_post():
    result = None
    try:
        db = DataBase()
        result = db.get_posts()
        db.close_conn()
        if result:
            return result
        else:
            raise HTTPException(status_code=400, detail="Error get all posts")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/post", response_model=Post)
async def create_post(new_post: Post):
    result = None
    try:
        db = DataBase()
        result = db.add_post(new_post)
        db.close_conn()
        if result:
            new_post.id = result
            return new_post
        else:
            raise HTTPException(status_code=400, detail="Error in create post")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/post/{id}")
async def update_post(id: int, post: UpdatePost):
    return {"message": "Update post"}

@router.delete("/post/{id}")
async def delete_post(id: int):
    return {"message": "Delete post"}

@router.get("/post/{id}")
async def get_id_post(id: int):
    return {"message": "Get post for id"}

@router.get("/post/term/{term}")
async def get_term_post(term: str):
    return {"message": f"Get post for {term}"}
    



