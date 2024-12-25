from fastapi import FastAPI
app=FastAPI()

@app.get("/heartbeat")
def heartbeat():
    return "Application is working"