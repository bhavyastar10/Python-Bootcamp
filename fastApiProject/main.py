from fastapi import FastAPI, HTTPException
import mysql.connector
from pydantic import BaseModel

app = FastAPI()

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="test"
)

cursor = db.cursor()

class Item(BaseModel):
    name: str

@app.get("/items", tags=["items"])
def read_items():
    try:
        cursor.execute("SELECT * FROM items")
        items = [{"id": row[0], "name": row[1]} for row in cursor.fetchall()]
        return items
    except:
        raise HTTPException(status_code=500, detail="Database error")

@app.post("/items", response_model=Item)
def create_item(item: Item):
    try:
        query = "INSERT INTO items (name) VALUES (%s)"
        cursor.execute(query, (item.name, ))
        db.commit()
        return {"name" : item.name}
    except:
        raise HTTPException(status_code=500, detail="Database error")

@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item: Item):
    try:
        query = "UPDATE items SET name=%s WHERE id=%s"
        cursor.execute(query, (item.name, item_id))
        db.commit()
        if(cursor.rowcount == 0):
            raise HTTPException(status_code=404, detail="Item not found")
        return {"id": item_id, "name":item.name }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    try:
        query = "DELETE FROM items WHERE id=%s"
        cursor.execute(query, (item_id,))
        db.commit()
        if(cursor.rowcount == 0):
            raise HTTPException(status_code=404, detail="Item not found")
        return {"message": "Item deleted"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")





# @app.get("/")
# async def root():
#     return {"message": "Hello World"}
#
#
# @app.get("/hello/{name}")
# async def say_hello(name: str):
#     return {"message": f"Hello {name}"}
