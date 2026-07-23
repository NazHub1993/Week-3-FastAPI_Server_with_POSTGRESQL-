# defines the format of incoming and outgoing data
from pydantic import BaseModel

class TaskCreate(BaseModel):
    title: str   

class TaskUpdate(BaseModel):
    title: str
    done: bool

class Task(BaseModel):
    id : int 
    title : str
    done : bool
