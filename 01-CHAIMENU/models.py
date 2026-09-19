# This is the file for defining the models for ChaiMenu Application using Pydantic Validation.

from pydantic import BaseModel

class MenuItem(BaseModel):
    id: int
    name: str
    category: str
    price: float
    description: str
    available: bool

class MenuResponse(BaseModel):
    status: str = "success"
    count : int
    items: list[MenuItem]