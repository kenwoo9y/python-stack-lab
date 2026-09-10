from datetime import datetime
from typing import Optional

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import EmailStr
from pydantic import Field
from pydantic import field_validator

# RFC 5321 4.5.3.1.1で規定されている@より前の部分（ローカルパート）の最大長
EMAIL_LOCAL_PART_MAX_LENGTH = 64


class UserBase(BaseModel):
    username: str = Field(..., max_length=30, min_length=3)
    email: EmailStr = Field(..., max_length=80)
    first_name: Optional[str] = Field(None, max_length=40)
    last_name: Optional[str] = Field(None, max_length=40)

    @field_validator("email")
    @classmethod
    def validate_email_local_part_length(cls, v: Optional[str]) -> Optional[str]:
        if v is not None:
            local_part = v.rsplit("@", 1)[0]
            if len(local_part) > EMAIL_LOCAL_PART_MAX_LENGTH:
                raise ValueError(
                    f"The part before the @-sign must be {EMAIL_LOCAL_PART_MAX_LENGTH} characters or fewer."
                )
        return v


class UserCreate(UserBase):
    pass


class UserUpdate(UserBase):
    username: Optional[str] = Field(None, max_length=30, min_length=3)
    email: Optional[EmailStr] = Field(None, max_length=80)
    first_name: Optional[str] = Field(None, max_length=40)
    last_name: Optional[str] = Field(None, max_length=40)


class UserResponse(UserBase):
    id: Optional[int] = Field(None)
    created_at: Optional[datetime] = Field(None)
    updated_at: Optional[datetime] = Field(None)


class User(UserBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
