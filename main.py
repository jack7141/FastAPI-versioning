import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    email: str

from fastapi_crudrouter import MemoryCRUDRouter

app = FastAPI()
app.include_router(MemoryCRUDRouter(schema=User))

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)