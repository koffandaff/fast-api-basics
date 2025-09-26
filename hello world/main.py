from fastapi import FastAPI

api = FastAPI()

# We have GET(get info) and POST(send info) PUT(update info) DELETE(delete info)
@api.get("/")
def index():
    return {"message": "Hello World"}

@api.get('/calculation')
def calculation():
    #do some calculation
    pass
    return "calculation done"

#gets database it may be async or sync
@api.get('/database')
def get_database():
    #get database
    pass
    return "database"