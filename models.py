from typing import Optional, List
from uuid import UUID, uuid4
from enum import Enum
from pydantic import BaseModel


class Gender(str, Enum):
    male = "male"
    female = "female"


class Role(str, Enum):
    user = "user"
    support_admin = "support_admin"
    super_admin = "super_admin"


class User(BaseModel):
    id: Optional[UUID] = uuid4()
    first_name: str
    last_name: str
    middle_name: Optional[str]
    gender: Gender
    roles: List[Role]

class UserUpdateRequest(BaseModel):
    first_name: str
    last_name: str
    middle_name: Optional[str]
    gender: Gender
    roles: List[Role]
