"""
main.py is the main entry point of this e-commerce platform app
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.products import router as product_router
from app.api.orders import router as order_router


app = FastAPI(
    title="e-commerce platform app",
    description="REST API endpoints using FastAPI framework",
    version="0.1.0"
)

#CORS middleware
app.add_middleware(
CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "welcome to e-commerce platform project!"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

# include the e-commerce api router
app.include_router(product_router)
app.include_router(order_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
