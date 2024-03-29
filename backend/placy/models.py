"""Module to contain models for back API."""

from typing import Union
from pydantic import BaseModel, validator
import datetime


class Email(BaseModel):
    """Model for the email."""

    email: str


class UpdatePassword(BaseModel):
    """Model for updated password."""

    email: str
    otp: str
    new_password: str


class OTP(BaseModel):
    """Model to store OTP system."""

    email: str
    otp: str
    exp: datetime.datetime
    used: bool


class User(BaseModel):
    """Model for the user."""

    username: str
    email: str
    role: str
    password: str

    name: str | None
    year: int | None
    gpa: float | None
    salt: str | None
    created_at: datetime.datetime | None
    updated_at: datetime.datetime | None
    profile_completed: bool | None
    communities: list[str] | None
    reputation: float | None
    isBanned: bool | None

    # VIT Validator.
    # @validator("email")
    # def validate_email(cls, email: str):
    #     """Validate email to end with @vitbhopal.ac.in."""
    #     assert email.endswith("@vitbhopal.ac.in"), "Not a VIT Bhopal email ID."
    #     return email

    @validator("year")
    def validate_year(cls, year: int):
        """Validate year of study."""
        assert year in {1, 2, 3, 4, 5}, "Not a valid year of study."
        return year

    @validator("gpa")
    def validate_gpa(cls, gpa: int):
        """Validate GPA."""
        assert 0 < gpa < 10, "Not a valid 10 point GPA."
        return gpa
