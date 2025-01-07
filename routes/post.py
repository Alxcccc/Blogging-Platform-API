from fastapi import APIRouter, HTTPException
from models.post import Post
from models.updatepost import UpdatePost
from db.database import DataBase

router = APIRouter()

@router.get("/post", response_model=list[Post])
async def get_all_post() -> list:
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
async def create_post(new_post: Post) -> Post:
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

@router.post("/post/{id}", response_model=Post)
async def update_post(id: int, new_post: UpdatePost):
    try:
        db = DataBase()
        result_update = db.upd_post(id, new_post)
        db.close_conn()
        if result_update:
            return result_update
        else:
            raise HTTPException(status_code=400, detail="Error update post")
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/post/{id}", response_model=dict)
async def delete_post(id: int) -> dict:
    try:
        db = DataBase()
        result = db.del_post(id)
        db.close_conn()
        if result:
            return {"status": True, "message": f"The post {id} was deleted successfully.", "data": None}
        else:
            raise HTTPException(status_code=400, detail="Error delete post: the postID not exits")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/post/{id}", response_model=Post)
async def get_id_post(id: int) -> Post:
    try:
        db = DataBase()
        result = db.get_post(id)
        db.close_conn()
        if result:
            return result
        else:
            raise HTTPException(status_code=400, detail="Error get post")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/post/term/{term}", response_model=list[Post])
async def get_term_post(term: str):
    return {"message": f"Get post for {term}"}




