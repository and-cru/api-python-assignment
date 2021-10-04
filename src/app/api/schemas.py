from typing import List, Optional
from pydantic import BaseModel

class AppointmentBase(BaseModel):
    title: str
    description: Optional[str] = None
    bean_type: Optional[str] = None
    brew_time: Optional[float] = 0.0
    brew_method: Optional[str] = None
    taste_notes: Optional[str] = None
    tags: Optional[str] = None

class AppointmentCreate(AppointmentBase):
    pass

class Appointment(AppointmentBase):
    id: int
    patient_id: int

    class Config:
        orm_mode = True

class PatientBase(BaseModel):
    name: str

class PatientCreate(PatientBase):
    pass

class Patient(PatientBase):
    id: int
    appointments: Optional[List[Appointment]] = []

    class Config:
        orm_mode = True
