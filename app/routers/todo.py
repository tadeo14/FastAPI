
from typing import Union, Annotated, Optional
from fastapi import  HTTPException,Path, File, APIRouter
from pydantic import BaseModel, Field


router = APIRouter(
	prefix="/todo",
	tags=["Todo"]
)
TODO_LIST = [
	    {"id":1, "description": "Learn Python", "complete": True},
		{"id":2, "description": "FastAPI", "complete": False},
		{"id":3, "description": "FastAPI", "complete": True}
		
]

class Todo(BaseModel):
	id: Optional[int] = None 
	description: str = Field(min_length=5, max_length=500)
	complete: bool = Field(default=False)




@router.get("")
async def get_all(complete: Union[bool, None] = None): #se pone como filtro los todo completo
	if complete is not None:
		filtered_todos = list(filter(lambda todo :todo ["complete"] == complete, TODO_LIST))
		return filtered_todos
	return TODO_LIST

@router.get("/{todo_id}")
async def get_todo(todo_id: int):
	try:	
			todo_data = next(todo for todo in TODO_LIST if todo["id"] == todo_id)
			return todo_data
	except:
			raise HTTPException(status_code=404, detail="Todo not found")

@router.post("", response_model=Todo, name="Create TODO",
		  summary="Create a TODO element",
		  description="Creates a TODO element given an id, a description and a complete status",
		  status_code=201)
async def create_todo(data: Todo):
    TODO_LIST.append(data)
    return data

@router.post("/{todo_id}/attachment")
async def upload_file(todo_id: Annotated[int, Path()], file: Annotated[bytes, File()]):
	try:
		todo_data = next(todo for todo in TODO_LIST if todo["id"]== todo_id)
		todo_data["file_size"] = len(file)
		return todo_data
	except:
		raise HTTPException(status_code=404, detail="TODO not found")