# src/state.py

from typing import Optional
from pydantic import BaseModel

class WorkflowState(BaseModel):
    topic: str                          # Topic chosen by user
    research: Optional[str] = None      # Filled by Researcher
    draft: Optional[str] = None         # Filled by Writer
    review: Optional[str] = None        # Placeholder for QA if needed
    next_step: str = "supervisor"       # Start with supervisor