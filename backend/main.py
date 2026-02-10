from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Azure AI Search Backend is running"}

@app.get("/search")
def search(q: str):
    return {"query": q, "results": []}
