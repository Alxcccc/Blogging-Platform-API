from db.database import DataBase
from fastapi import APIRouter, HTTPException
from models.post import Post
from models.updatepost import UpdatePost

router = APIRouter()


@router.post(
    "/post",
    summary="Create a new post.",
    response_model=Post,
    tags=["CRUD Blogging Platform API"],
)
async def create_post(new_post: Post) -> Post:
    """
    Create a new post with the provided information.

    - **title**: The title of the post (required).
    - **content**: The main content of the post (required).
    - **category**: The category under which the post is classified (optional).
    - **tags**: A list of unique tag strings associated with the post (optional).
    - **createdAt**: Timestamp indicating when the post was created (automatically set).
    - **updateAt**: Timestamp indicating when the post was last updated (automatically set).

    **Returns**:
        A Post object with the newly created post's details, including its ID.

    **Raises**:
        HTTPException: If there is an error during the creation process or if required fields are missing.
    """
    try:
        db = DataBase()
        result = db.add_post(new_post)
        if result:
            new_post.id = result
            return new_post
        else:
            raise HTTPException(status_code=400, detail="Error in creating post.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error in create post: {e}")
    finally:
        db.close_conn()


@router.get(
    "/post",
    summary="Retrieve all posts from the database.",
    response_model=list[Post],
    tags=["CRUD Blogging Platform API"],
)
async def get_all_post() -> list:
    """
    Retrieve all posts from the database.

    **Returns**:
        A list of Post objects representing all posts.

    **Raises**:
        HTTPException: If there is an error retrieving posts from the database.
    """
    try:
        db = DataBase()
        result = db.get_posts()
        db.close_conn()
        if result:
            return result
        else:
            raise HTTPException(status_code=400, detail="No posts found.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error in get posts: {e}")


@router.get(
    "/post/{id}",
    summary="Retrieve a specific post by its ID.",
    response_model=Post,
    tags=["CRUD Blogging Platform API"],
)
async def get_id_post(id: int) -> Post:
    """
    Retrieve a specific post by its ID.

    **Parameters**:
        id (int): The ID of the post to retrieve.

    **Returns**:
        A Post object representing the requested post.

    **Raises**:
        HTTPException: If the post with the specified ID is not found or if there is an error retrieving it.
    """
    try:
        db = DataBase()
        result = db.get_post(id)
        db.close_conn()
        if result:
            return result
        else:
            raise HTTPException(status_code=404, detail=f"Post with ID {id} not found.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error in get post: {e}")


@router.get(
    "/post/term/{term}",
    summary="Search for posts that match a specific search term in their title, content, or tags.",
    response_model=list[Post],
    tags=["CRUD Blogging Platform API"],
)
async def get_term_post(term: str):
    """
    Search for posts that match a specific search term in their title, content, or tags.

    **Parameters**:
        term (str): The search term to filter posts.

    **Returns**:
        A list of Post objects that match the search term.

    **Raises**:
        HTTPException: If there is an error retrieving posts based on the search term.
    """
    try:
        db = DataBase()
        result = db.get_post_term(term)
        db.close_conn()
        if result:
            return result
        else:
            raise HTTPException(
                status_code=404, detail="No posts found matching the search term."
            )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error in get posts: {e}")


@router.post(
    "/post/{id}",
    summary="Update an existing post by its ID with new information.",
    response_model=Post,
    tags=["CRUD Blogging Platform API"],
)
async def update_post(id: int, new_post: UpdatePost):
    """
    Update an existing post by its ID with new information.

    **Parameters**:
        id (int): The ID of the post to update.
        new_post (UpdatePost): An object containing updated information for the post.

    **Returns**:
        A Post object representing the updated post.

    **Raises**:
        HTTPException: If there is an error updating the post or if the specified ID does not exist.
    """
    try:
        db = DataBase()
        result_update = db.upd_post(id, new_post)
        db.close_conn()

        if result_update:
            return result_update
        else:
            raise HTTPException(status_code=404, detail=f"Post with ID {id} not found.")

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error in update post: {e}")


@router.delete(
    "/post/{id}",
    summary="Delete a specific post by its ID.",
    response_model=dict,
    tags=["CRUD Blogging Platform API"],
)
async def delete_post(id: int) -> dict:
    """
    Delete a specific post by its ID.

    **Parameters**:
        id (int): The ID of the post to delete.

    **Returns**:
        A dictionary indicating success and a message about the deletion.

    **Raises**:
        HTTPException: If there is an error deleting the post or if the specified ID does not exist.
    """
    try:
        db = DataBase()
        result = db.del_post(id)
        db.close_conn()

        if result:
            return {
                "status": True,
                "message": f"The post {id} was deleted successfully.",
                "data": None,
            }
        else:
            raise HTTPException(status_code=404, detail=f"Not Found the id: {id}")

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error in delete post: {e}")
