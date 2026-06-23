from pydantic import BaseModel
from typing import Optional


class EmailRequest(BaseModel):
    email_text: str


class ProcessingStep(BaseModel):
    step: int
    label: str
    status: str  # processing | completed | pending
    result: Optional[str] = None


class ProcessedEmail(BaseModel):
    intent: str
    category: str
    priority: str
    draft_response: str


class EmailResponse(BaseModel):
    steps: list[ProcessingStep]
    result: ProcessedEmail
