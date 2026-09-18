from fastapi import FastAPI
from fastapi import Request
import uvicorn

app = FastAPI(
    title= "Swiggy Order Service",
    description= "This is a sample order service for Swiggy",
    version= "1.0.0",
    docs_url= "/docs",
    redoc_url="/redoc",
    openapi_url= "/openapi.json"
)

@app.get("/")
def read_root():
    """Root endpoint health check"""

    # FastAPI converts the dictionary to JSON and returns it as a response
    return {"message": "Welcome to the Swiggy Order Service!",
            "status": "Healthy",
            }

@app.get("/about")
def about():
    """About endpoint"""

    return {"message": "This is a sample order service for Swiggy",
            "author": "Prakash",
            }

@app.get("/debug/request-info")
async def request_info(request: Request):
    """Inspects the raw request object"""

    return {
        "method": request.method,
        "url": str(request.url),
        "headers": dict(request.headers),
        "query_params": dict(request.query_params),
        "path_params": request.path_params,
    }
