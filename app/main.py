from fastapi import FastAPI, Request, Depends
from fastapi.responses import JSONResponse
from .schemas import SearchQuery, EmployeeResponse
from .crud import search_employees
from .rate_limiter import RateLimiter
from typing import List,Dict,Any

app = FastAPI()
rate_limiter = RateLimiter(max_requests=5, per_seconds=60)

@app.middleware("http")
async def rate_limit(request: Request, call_next):
    client_ip = request.client.host
    if not rate_limiter.allow_request(client_ip):
        return JSONResponse(status_code=429, content={"detail": "Rate limit exceeded"})
    return await call_next(request)

@app.get("/employees/search", response_model=list[Dict[str,Any]])
def search_employees_api(params: SearchQuery = Depends()):
    return search_employees(params)
