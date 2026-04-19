from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List

# Initialize FastAPI application
app = FastAPI()

# Define Pydantic model for Item
class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    price: float

# Sample data storage (in-memory)
items_db: List[Item] = [
    Item(id=1, name="Sample Item", description="A sample item", price=9.99)
]

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the Item API"}

# TODO: Implement the following endpoints:
# 1. GET /items - Retrieve all items
# 2. GET /items/{item_id} - Retrieve a specific item by ID
# 3. POST /items - Create a new item
# 4. PUT /items/{item_id} - Update an existing item
# 5. DELETE /items/{item_id} - Delete an item

# To run this application:
# 1. Install FastAPI: pip install fastapi
# 2. Install Uvicorn server: pip install uvicorn
# 3. Run the server: uvicorn starter-code:app --reload
# 4. Visit http://localhost:8000/docs for interactive API documentation
