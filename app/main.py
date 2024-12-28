from fastapi import FastAPI
from datetime import datetime

app=FastAPI(docs_url="/docs",title="Acad Backend")

@app.get("/heartbeat")
def heartbeat():
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')


    return f"Application is running at {current_time}"