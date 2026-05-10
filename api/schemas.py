from pydantic import BaseModel

"""
Schemas Module

Defines Pydantic models used for API request and response validation.
Ensures consistent data structure when interacting with the API layer.
"""

class BookResponse(BaseModel):
    id: int
    title: str
    author: str
    sales: float

    class Config:
        from_attributes = True
    