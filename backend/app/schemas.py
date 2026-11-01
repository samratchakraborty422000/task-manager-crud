from datetime import datetime
from pydantic import BaseModel, ConfigDict, EmailStr, Field

class UserCreate(BaseModel):
    
    email: EmailStr
    password:str = Field(min_length=8,max_length=128)
    
class UserOut(BaseModel):
    
    id:int
    email:EmailStr
    
    model_config = ConfigDict(from_attributes=True)
    
class Token(BaseModel):
    
    access_token:str
    token_type:str = "bearer"
    
class TaskCreate(BaseModel):
    
    title:str = Field(min_length=1,max_length=200)
    description:str = Field(default="",max_length=5000)
    
class TaskUpdate(BaseModel):
    
    title:str = Field(min_length=1,max_length=200)
    description:str | None = Field(default=None,max_length=5000)
    completed:bool | None = None

#task output
class TaskOut(BaseModel):
    
    id:int
    title:str
    description:str
    completed:bool
    created_at:datetime
    owner_id:int
    
    model_config = ConfigDict(from_attributes=True)