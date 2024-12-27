from fastapi import FastAPI
app=FastAPI(docs_url="/docs",title="Acad Backend")

@app.get("/heartbeat")
def heartbeat():
    return "Application is working"