
from typing import Union, Annotated
from fastapi import  HTTPException,Path, File, APIRouter




@app.get("/todo")
async def get_all(complete: Union[bool, None] = None): #se pone como filtro los todo completo
	if complete is not None:
		filtered_todos = list(filter(lambda todo :todo ["complete"] == complete, TODO_LIST))
		return filtered_todos
	return TODO_LIST

@app.get("/todo/{todo_id}")
async def get_todo(todo_id: int):
	try:	
			todo_data = next(todo for todo in TODO_LIST if todo["id"] == todo_id)
			return todo_data
	except:
			raise HTTPException(status_code=404, detail="Todo not found")

@app.post("/todo", response_model=Todo, name="Create TODO",
		  summary="Create a TODO element",
		  description="Creates a TODO element given an id, a description and a complete status",
		  status_code=201)
async def create_todo(data: Todo):
    TODO_LIST.append(data)
    return data

@app.post("/todo/{todo_id}/attachment")
async def upload_file(todo_id: Annotated[int, Path()], file: Annotated[bytes, File()]):
	try:
		todo_data = next(todo for todo in TODO_LIST if todo["id"]== todo_id)
		todo_data["file_size"] = len(file)
		return todo_data
	except:
		raise HTTPException(status_code=404, detail="TODO not found")