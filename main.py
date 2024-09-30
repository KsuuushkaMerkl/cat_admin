from fastapi import FastAPI

from cat.endpoints import router

app = FastAPI(
    title="Cats admin"
)


app.include_router(router, prefix="/cats", tags=["Cats"])
