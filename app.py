from fastapi import FastAPI, Request
from pydantic import BaseModel

app = FastAPI()

data = []

class Person(BaseModel):
    name: str
    occupation: str
    address: str
  

# @app.post("/person")



# async def create_item(data: Person):
#     name=data.name
#     occupation=data.occupation
#     address=data.address
#     data.append(name)

#     if ((name or occupation or address)==""):
#          return {
#                     "success": False,
#                     "result": {"error_message": "invalid request"}
#         }
#     else :
#         state= True
#         return {
#             "success": state,
#             "name": name,
#             "occupation": occupation,
#             "address": address,
#         }

@app.post("/person")
async def add_person(person: Person):
    if all([person.name, person.occupation, person.address]):
        data.append(person.dict())
        return {"success": True, "result": person}
    else:
        name = person.name
        occupation = person.occupation
        address = person.address
        if not all([name, occupation, address]):
            return {
                "success": False,
                "result": {"error_message": "invalid request"}
            }

@app.get("/person")
def get_person():
    return data