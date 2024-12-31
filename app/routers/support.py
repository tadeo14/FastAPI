
from typing import  Annotated
from fastapi import Form




@app.post("/support")
async def create_support_ticket(title : Annotated[str,Form()], message : Annotated[str,Form()]):
	return {"title": title, "message": message}

