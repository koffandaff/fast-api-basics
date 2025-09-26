# Creating a simple TODO application using FastAPI 
from typing import List, Optional # for better writting 
from enum import IntEnum # for better for loop usage 

from fastapi import FastAPI, HTTPException# HTTPException for error handling 
from pydantic import BaseModel, Field # for data validation and settings management using python type annotations
    
api=FastAPI() # creating an api

class PriorityLevel(IntEnum):
    LOW = 3
    MEDIUM = 2
    HIGH = 1

class TodoBase(BaseModel):
    todo_name: str = Field(..., min_length=2, max_length=150, description="Name of the todo task") # really important dude 
    todo_description: str = Field(..., max_length=300, description="Description of the todo task")
    priority: PriorityLevel = Field(defaul=PriorityLevel.LOW, description="Priority level of the todo task")
    completed: bool = Field(default=False, description="Status of the todo task")

class TodoCreate(TodoBase):
    pass 

class TodoUpdate(TodoBase): # all fields are optional as they may or may not be updated
    todo_name: Optional[str] = None 
    todo_description: Optional[str] = None
    priority: Optional[PriorityLevel] = None
    completed: Optional[bool] = None

class Todo(TodoBase):
    todo_id: int = Field(..., description="Unique identifier for the todo task")


all_todos = [
    
    Todo(todo_id=1, todo_name="Buy groceries", todo_description="Milk, Bread, Eggs", priority=PriorityLevel.MEDIUM, completed=False),
    Todo(todo_id=2, todo_name="Read a book", todo_description="Finish reading 'The Great Gatsby'", priority=PriorityLevel.LOW, completed=False),
    Todo(todo_id=3, todo_name="Sports", todo_description="Play football", priority=PriorityLevel.HIGH, completed=True),
    Todo(todo_id=4, todo_name="Workout", todo_description="Go to the gym for a workout session", priority=PriorityLevel.HIGH, completed=False),
    Todo(todo_id=5, todo_name="Call Mom", todo_description="Catch up with Mom over the phone", priority=PriorityLevel.MEDIUM, completed=False)
]

#GET, POST, PUT, DELETE

# using class and all
@api.get('/todo/{todo_id}' , response_model=Todo)  # responsive model to ensure the output is of type Todo with all fields
def get_todo(todo_id: int):
    for todo in all_todos:
        if todo.todo_id == todo_id:
            return todo
    raise HTTPException(status_code=404, detail="Todo not found") # raising an HTTP exception if todo not found

# Localhost:8000/todo?first_n=3 these are query parameters
@api.get('/todo', response_model=List[Todo]) # will return a list of Todo items through the response model
def get_todo(first_n: int =3 ):
    if first_n:
        return all_todos[:first_n]
    else:
        return all_todos
    
# Post endpoint to create a new todo
@api.post('/todo', response_model=Todo) # will return the created Todo item through the response model
def create_todo(todo: TodoCreate): # using TodoCreate model to ensure the input data is validated
    new_todo_id = max(todo.todo_id  for todo in all_todos) + 1 
    new_todo = Todo(todo_id=new_todo_id, 
                    todo_name=todo.todo_name,
                    todo_description=todo.todo_description,
                    priority=todo.priority,
                    completed=todo.completed) # unpacking the todo fields from the TodoCreate model
    
    all_todos.append(new_todo)
    raise HTTPException(status_code=201, detail="Todo created successfully") # raising an HTTP exception for successful creation


# Put endpoint to update an existing todo
@api.put('/todo/{todo_id}', response_model=Todo) # will return the updated Todo item through the response model
def update_todo(todo_id : int, updated_todo: TodoUpdate):
    for todo in all_todos:
        if todo.todo_id == todo_id:
            if updated_todo.todo_name is not None:
                todo.todo_name = updated_todo.todo_name
            if updated_todo.todo_description is not None:
                todo.todo_description = updated_todo.todo_description
            if updated_todo.priority is not None:
                todo.priority = updated_todo.priority
            if updated_todo.completed is not None:
                todo.completed = updated_todo.completed
            return {"message": "Todo updated successfully", "todo": todo}
    raise HTTPException(status_code=404, detail="Todo not found") # raising an HTTP exception if todo not found

# Delete endpoint to delete a todo
@api.delete('/todo/{todo_id}')
def delete_todo(todo_id: int):
    for index, todo in enumerate(all_todos):
        if todo.todo_id == todo_id:
         deleted_todo = all_todos.pop(index)
         return {"message": "Todo deleted successfully", "todo": deleted_todo}
    raise HTTPException(status_code=404, detail="Todo not found") # raising an HTTP exception if todo not found



# traditional way without class and all
'''
# Path parameter are the one that are defined after last/
#eg
@api.get('/todo/{todo_id}')
def get_todo(todo_id: int):
    for todo in all_todos:
        if todo['todo_id'] == todo_id:
            return todo
    return {"message": "Todo not found"}

# Localhost:8000/todo?first_n=3 these are query parameters
@api.get('/todo')
def get_todo(first_n: int =3 ):
    if first_n:
        return all_todos[:first_n]
    else:
        return all_todos
    
# Post endpoint to create a new todo
@api.post('/todo')
def create_todo(todo: dict):
    new_todo_id = max(todo['todo_id'] for todo in all_todos) + 1 
    new_todo_id={
        'todo_id': new_todo_id,
        'todo_name': todo['todo_name'],
        'todo_description': todo['todo_description'],
        'completed': todo['completed']
    }
    all_todos.append(new_todo_id)
    return {"message": "Todo created successfully", "todo": new_todo_id}

# Put endpoint to update an existing todo
@api.put('/todo/{todo_id}')
def update_todo(todo_id : int, updated_todo: dict):
    for todo in all_todos:
        if todo['todo_id'] == todo_id:
            todo['todo_name'] = updated_todo['todo_name']
            todo['todo_description'] = updated_todo['todo_description']
            todo['completed'] = updated_todo['completed']
            return {"message": "Todo updated successfully", "todo": todo}
    return {"message": "Todo not found"}

# Delete endpoint to delete a todo
@api.delete('/todo/{todo_id}')
def delete_todo(todo_id: int):
    for index, todo in enumerate(all_todos):
        if todo['todo_id'] == todo_id:
         deleted_todo = all_todos.pop(index)
         return {"message": "Todo deleted successfully", "todo": deleted_todo}
    return {"message": "Todo not found"}


'''














