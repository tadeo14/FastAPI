from pydantic import BaseModel, field


class TodoSchema(BaseModel):
    title: str = Field (min_length=3, max_length=100)
    