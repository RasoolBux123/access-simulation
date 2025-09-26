from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.access import router as simulate_router

app = FastAPI(title="Employee Access Simulation")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(simulate_router, prefix="/api")

@app.get("/")
async def root():
    return {"message": "Employee Access Simulation API is running"}
