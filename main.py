from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from dotenv import load_dotenv
from langchain_groq import ChatGroq
import os
from langchain.prompts import PromptTemplate

load_dotenv()

groq_api_key = os.getenv("Key")

llm = ChatGroq(
    api_key=groq_api_key,
    model="llama-3.3-70b-versatile",
    temperature=0.6
)

app = FastAPI()

# Enable CORS for frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (change in production)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve index.html
@app.get("/")
def serve_homepage():
    return FileResponse("index.html")

prompt_template = PromptTemplate(
    input_variables=['position', 'company', 'name', 'degree', 'college', 'experience', 'grad_year'],
    template='''
    - Write a cold email for me to apply in:
       - Company: {company}
       - Position: {position}
       - My Name: {name}
       - My Degree: {degree}
       - College: {college}
       - Years of Experience: {experience}
       - Graduation Year: {grad_year}

    ### INSTRUCTIONS
    - No Preamble
    - Describe how I am suitable for the role
    - Write as generically as possible
    '''
)

@app.get("/generate-email")
def generate_email(position: str, company: str, name: str, degree: str, college: str, experience: str, grad_year: str):
    query = prompt_template.format(position=position, company=company, name=name, degree=degree, college=college, experience=experience, grad_year=grad_year)
    response = llm.invoke(query)
    return {"email": response.content}
