from fastapi import FastAPI, Path
import json
from pydantic import BaseModel, Field
from typing import Annotated
app=FastAPI()


class pydantic_data(BaseModel):
    name: Annotated[str|None,  Field(default=None, max_length=20)] = None
    age: Annotated[int|None,  Field(default=None, lt=70, gt=10)] = None
    salary: Annotated[float|None,  Field(default=None)] = None

# class pydantic_data(BaseModel):
#     name: str
#     age: int 
#     salary: float


def load_data():

    with open("data.json", "r") as f:
        data = json.load(f)
        return data 
    
def save_data(data):
    with open("data.json", "w") as f:
        json.dump(data, f, indent=4)


@app.get("/")
def first():
    return {"Messagre": "hello world"}
@app.get("/view")
def secound():
    data = load_data()
    return data


@app.post("/patient")
def creat_patinet(patident_id: str, patient_data:pydantic_data):
    # data is now a proper Python dictionary
    data = load_data()
    if patident_id in data:
        return {"error": "Yeh patient pehlai sai exist krta hai"}
    # Now this assignment will work successfully
    data[patident_id] = patient_data.model_dump()  #dict mai convert 
    # (Optional) Save the updated dictionary back to your JSON file
    save_data(data)
    return {
        "message": "patient succesfut add hogia",
        "patient_id": patident_id,
        "patient_data": patient_data,
    }

#  Put APi
@app.put("/update")
def  update_data(patident_id: str=Path(description="Yahan id dai data update kai liye"), patient_data: dict= Path(description="yahan updated data dena hai")):
    data = load_data()
    if patident_id not in data:
        return {"MessAGE":   "yEH Id HAI HI NI KAISIA MAI UPdATE KRO "}
    data[patident_id].update(patient_data)
    save_data(data)
    return {
            "message": "patient update hogia ",
            "patient_id": patident_id,
            "patient_data": patient_data,


        }
@app.delete("/delete")
def update_data(patident_id: str=Path(description="Yeh api delete krni ki hai ", example="p001")):
    data = load_data()
    if patident_id not in data:
        return {"MessAGE":   "yEH Id HAI HI NI KAISIA delete klro"}
    
    delete_item =data.pop(patident_id)
    save_data(data)
    return {
            "message": "patient delete hogia ",
            "patient_id": patident_id,
            "patient_data": delete_item,
        }