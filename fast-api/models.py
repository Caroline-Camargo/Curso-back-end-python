from pydantic import BaseModel # Base class for data validation
from uuid import UUID, uuid4 # Id generator randomic
from typing import Optional, List # Optional data type
from enum import Enum # Library to create enumerations

class Role(str, Enum):
    role_1 = "adimin"
    role_2 = "aluna"
    role_3 = "instrutor"

class User(BaseModel):
    id: Optional[UUID] = uuid4() 
    first_name: str
    last_name: str
    email: str
    role: List[Role] # List of roles
