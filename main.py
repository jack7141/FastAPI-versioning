import uvicorn
from fastapi import FastAPI
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.openapi.utils import get_openapi
from api.versioned.v1.router import router as v1_router
from api.versioned.v2.router import router as v2_router

app = FastAPI(docs_url=None)
app.include_router(v1_router, prefix="/api/v1")
app.include_router(v2_router, prefix="/api/v2")


# 각 버전별 OpenAPI 스키마 생성
@app.get("/api/v1/openapi.json", include_in_schema=False)
async def v1_openapi():
    return get_openapi(title="API v1", version="1.0.0", routes=app.routes)


@app.get("/api/v2/openapi.json", include_in_schema=False)
async def v2_openapi():
    return get_openapi(title="API v2", version="2.0.0", routes=app.routes)


# 각 버전별 문서
@app.get("/api/v1/docs", include_in_schema=False)
async def v1_docs():
    return get_swagger_ui_html(openapi_url="/api/v1/openapi.json", title="API v1")


@app.get("/api/v2/docs", include_in_schema=False)
async def v2_docs():
    return get_swagger_ui_html(openapi_url="/api/v2/openapi.json", title="API v2")


if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)
