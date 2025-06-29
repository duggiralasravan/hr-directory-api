from pydantic import BaseModel
from typing import Optional

class SearchQuery(BaseModel):
    status: Optional[str] = None
    location: Optional[str] = None
    company: Optional[str] = None
    department: Optional[str] = None
    position: Optional[str] = None
    organization_id: int

class EmployeeResponse(BaseModel):
    id: int
    name: str
    department: Optional[str]
    location: Optional[str]
    position: Optional[str]

class SearchQuery(BaseModel):
    status: Optional[str] = None
    location: Optional[str] = None
    company: Optional[str] = None
    department: Optional[str] = None
    position: Optional[str] = None
    organization_id: int
    limit: int = 10           # default page size
    offset: int = 0           # default starting record

