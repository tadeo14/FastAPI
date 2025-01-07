from enum import Enum
from fastapi import FastAPI

from .routers import todo, support


class Tags(Enum):
    home: str = "Home",
	
    


app = FastAPI(
	title="FastAPI",
)   
#se le llama instancia 
app.include_router(todo.router)
app.include_router(support.router)


#instancia 
@app.get("/", tags=[Tags.home])
async def home():
    return {
        "name": "TODO rest api",
        "version": "1.0"
	}
