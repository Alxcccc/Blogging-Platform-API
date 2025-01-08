
# RESTful API for Personal Blogging Platform

This is a RESTful API designed for a personal blogging platform. It allows users to create, read, update, and delete blog posts. The API is built with **FastAPI** and uses **MySQL** as the database for data storage.

Credits of idea for: https://roadmap.sh/projects/blogging-platform-api


## Features

- **Post Management**: CRUD (Create, Read, Update, Delete) operations for blog posts.
- **Tags and Categories**: Organizes posts by tags and categories.
- **Search Functionality**: Enables searching posts by title, content, or category.


## Technologies
- Python 3.13
- FastAPI
- MySQL
## Installation

To run the app, ensure you have Python installed and follow these steps:

1. Clone the repository:

```bash
git clone https://github.com/yourUsername/https://github.com/Alxcccc/Blogging-Platform-API.git

cd Blogging-Platform-API
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate # On Windows use venv\Scripts\activate
```

3. Install the dependencies:
```bash
pip install -r requirements.txt
```

4. Set up the database:
- Create a MySQL database named `blog`.
- Run the necessary SQL scripts to create the required tables (see the `db/models` folder).

5. Configure environment variables:

Create a `.env` file in the root of the project with the following content:
```bash
DB_HOST=your_host
DB_USER=your_user
DB_PASSWORD=your_password
DB_NAME=blog
```


    
## Usage

1. Start the server:
```bash
cd app
python main.py
```

2. Access the API at `http://localhost:8000`.



## API Reference

#### Posts Blog

- **GET /api/posts**: Retrieve all posts.
- **GET /api/posts/{id}**: Retrieve a specific post by ID.
- **POST /api/posts**: Create a new post.
- **PUT /api/posts/{id}**: Update an existing post.
- **DELETE /api/posts/{id}**: Delete a post.

#### Search

- **GET /api/posts/term/{term}**: Search posts by title, content, or category.




## Documentation
Interactive API documentation is available at [Swagger UI](http://localhost:8000/docs) and [ReDoc](http://localhost:8000/redoc)

