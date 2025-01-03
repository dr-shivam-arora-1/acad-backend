from fastapi import FastAPI
from datetime import datetime
from app.router.resource import router
from app.config.constant import SWAGGER_TAGS

app = FastAPI(docs_url="/docs", title="Acad Backend", openapi_tags=SWAGGER_TAGS)
app.include_router(router, prefix="/resource")

@app.get("/heartbeat")
def heartbeat():
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return f"Application is running at {current_time}"