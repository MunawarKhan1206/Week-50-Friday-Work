# Week 50 - AI & Data Science Learning Project

This project was created during our Week 50 class, where we explored Artificial Intelligence, Large Language Models (LLMs), and API-based AI tools such as Gemini.

We learned how to:

- work with Python and virtual environments
- understand FastAPI and backend APIs
- use Pydantic for data validation
- create basic CRUD operations
- work with AI models in Colab
- use Gemini / Google Generative AI with an API key
- understand how LLMs generate text from prompts

## What we did in class

During this week, we focused on the following concepts:

- AI and Data Science fundamentals
- Large Language Models (LLMs)
- Generative AI tools like Gemini
- Using Google AI Studio / API keys
- Importing the `google.generativeai` library in Colab
- Sending prompts to the model and analyzing responses
- Learning how APIs connect our code to AI services

## Project idea

This project is a simple backend example built while learning FastAPI. It helps us understand how APIs work and how we can connect them with AI tools later.

The code includes a patient management system where we can:

- add a patient
- view all patients
- update patient data
- delete a patient

This is a beginner-friendly project that teaches how to build REST APIs using Python.

## What the code does

The project contains a small FastAPI app that stores patient records in a JSON file.

### Main functions in the code

- `read_data()`
  - reads patient records from `data.json`
  - creates the file if it does not exist

- `write_data(data)`
  - writes the updated patient dictionary back to the JSON file

- `create_patient()`
  - accepts a patient ID and patient details
  - checks if the patient already exists
  - saves the new record

- `update_patient()`
  - finds the patient by ID
  - updates only the fields provided by the user

- `delete_patient()`
  - removes the patient from the stored records

### Pydantic validation

The `pydantic_data` model validates the patient object before saving it:

- `name` - string with a max length
- `age` - integer value within a safe range
- `salary` - float value

This shows how input validation works in FastAPI and how we can protect the app from bad data.

## FastAPI endpoints

This app contains the following routes:

- `GET /` - welcome message
- `GET /view` - view all patient data
- `POST /patient` - add a patient
- `PUT /update/{patient_id}` - update a patient
- `DELETE /delete/{patient_id}` - delete a patient

## AI / LLM exploration part

Along with API development, we also explored AI tools in Colab using Gemini.

### Typical workflow we learned

- install or import `google.generativeai`
- generate a model object
- add the Gemini API key
- send a prompt to the model
- receive a generated response
- analyze the result and refine the input

### Example concept

```python
import google.generativeai as genai

genai.configure(api_key="YOUR_API_KEY")
model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("Explain AI and LLMs in simple words")
print(response.text)
```

This is a basic example of how we use an LLM in Python and connect it with an API key to generate text.

## Tools and libraries used

- Python
- FastAPI
- Pydantic
- Uvicorn
- JSON file storage
- Google Generative AI / Gemini
- Colab
- API key authentication

## Project structure

- `main.py` - main FastAPI application
- `hello.py` - Pydantic model and file-handling functions
- `data.json` - local storage for patient records
- `readme.md` - project documentation
- `venv/` - virtual environment

## How to run the project

### 1. Create a virtual environment

```bash
python -m venv venv
```

### 2. Activate the environment

Windows:

```bash
venv\Scripts\activate
```

macOS/Linux:

```bash
source venv/bin/activate
```

### 3. Install required packages

```bash
pip install fastapi pydantic uvicorn
```

### 4. Start the app

```bash
uvicorn main:app --reload
```

Then open:

- `http://127.0.0.1:8000`
- `http://127.0.0.1:8000/docs`

## Example API usage

### Add patient

```bash
curl -X POST "http://127.0.0.1:8000/patient?patient_id=P001" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Ali",
    "age": 30,
    "salary": 50000
  }'
```

### View all patients

```bash
curl http://127.0.0.1:8000/view
```

### Update patient

```bash
curl -X PUT "http://127.0.0.1:8000/update/P001" \
  -H "Content-Type: application/json" \
  -d '{
    "salary": 65000
  }'
```

### Delete patient

```bash
curl -X DELETE "http://127.0.0.1:8000/delete/P001"
```

## Learning summary

This week taught us a lot about both backend development and AI:

- how APIs work in real-world applications
- how to validate incoming data with Pydantic
- how JSON storage works for small apps
- how AI tools like Gemini are accessed through APIs
- how prompts, keys, and model settings are used in generative AI

## Final note

This project is a simple example of how we combine coding skills and AI learning in the same journey. It shows that backend development and machine learning are connected, and both are important in modern data science and AI work.

We learned not only how to build an API, but also how to think like problem solvers using code, data, and AI tools.
