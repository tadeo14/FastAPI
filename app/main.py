from pydantic import BaseModel, Field
from typing import Union, Optional, Annotated
from fastapi import FastAPI, HTTPException, Form, Path, File, UploadFile



app = FastAPI(
	title="FastAPI",
)   #se le llama instancia 

TODO_LIST = [
	    {"id":1, "description": "Learn Python", "complete": True},
		{"id":2, "description": "FastAPI", "complete": False},
		{"id":3, "description": "FastAPI", "complete": True}
		
]

class Todo(BaseModel):
	id: Optional[int] = None 
	description: str = Field(min_length=5, max_length=500)
	complete: bool = Field(default=False)



