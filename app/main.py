from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def read_root():
    return {"message": "API CI/CD rodando com Docker"}

@app.get('/health')
def health():
    return {'status': 'ok'}
    
