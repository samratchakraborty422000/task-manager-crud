from datetime import datetime,timezone
from sqlalchemy import Column, Integer, String, DateTime,Text,Boolean,ForeignKey

from sqlalchemy.orm import relationship
from .database import Base

# User table
class User(Base):
    
    __tablename__ = "users"
    
    id=Column(Integer,primary_key=True,index=True)
    email=Column(String, unique=True, index=True,nullable=False)
    hashed_password=Column(String,nullable=False)
    
    tasks=relationship("Task",back_populates="owner",cascade="all, delete-orphan")

# Task table 
class Task(Base):
    __tablename__ = "tasks"
    
    id=Column(Integer,primary_key=True,index=True)
    title=Column(String(200),nullable=False)
    description=Column(Text,default="")
    completed=Column(Boolean,default=False,nullable=False)
    created_at=Column(DateTime(timezone=True),default= lambda : datetime.now(timezone.utc))
    owner_id=Column(Integer,ForeignKey("users.id",ondelete="CASCADE"),nullable=False,index=True)
    
    owner=relationship("User",back_populates="tasks")
    
