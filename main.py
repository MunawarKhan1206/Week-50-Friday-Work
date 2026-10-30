import json
from pathlib import Path

from fastapi import FastAPI, Path as FastAPIPath

from hello import pydantic_data


app = FastAPI()
DATA_FILE = Path(__file__).with_name("data.json")


def read_data() -> dict:
    if not DATA_FILE.exists():
        DATA_FILE.write_text("{}", encoding="utf-8")
    return json.loads(DATA_FILE.read_text(encoding="utf-8"))


def write_data(data: dict) -> None:
    DATA_FILE.write_text(json.dumps(data, indent=4), encoding="utf-8")


@app.get("/")
def first() -> dict[str, str]:
    return {"message": "Hello World"}


@app.get("/view")
def second() -> dict:
    return read_data()


@app.post("/patient", status_code=201)
def create_patient(patient_id: str, patient_data: pydantic_data) -> dict:
    data = read_data()

    if patient_id in data:
        return {"error": "Patient already exists"}

    data[patient_id] = patient_data.model_dump()
    write_data(data)

    return {
        "message": "Patient added successfully",
        "patient_id": patient_id,
        "patient_data": patient_data.model_dump(),
    }


@app.put("/update/{patient_id}")
def update_patient(
    patient_id: str = FastAPIPath(
        description="Enter the patient ID to update",
        examples=["P001"],
    ),
    patient_data: pydantic_data = ...,
) -> dict:
    data = read_data()

    if patient_id not in data:
        return {"error": "Patient does not exist"}

    updated_data = patient_data.model_dump(exclude_unset=True)
    data[patient_id].update(updated_data)
    write_data(data)

    return {
        "message": "Patient updated successfully",
        "patient_id": patient_id,
        "patient_data": data[patient_id],
    }


@app.delete("/delete/{patient_id}")
def delete_patient(
    patient_id: str = FastAPIPath(
        description="Enter the patient ID to delete",
        examples=["P001"],
    ),
) -> dict:
    data = read_data()

    if patient_id not in data:
        return {"error": "Patient does not exist"}

    deleted_patient = data.pop(patient_id)
    write_data(data)

    return {
        "message": "Patient deleted successfully",
        "patient_id": patient_id,
        "patient_data": deleted_patient,
    }