from enum import Enum
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class IssueStatus(str, Enum):
    open = "open"
    in_progress = "in_progress"
    closed = "closed"


class IssuePriority(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"


class Issue(BaseModel):
    title: str = Field(..., min_length=3, max_length=100)
    desc: str = Field(..., min_length=3, max_length=1000)
    status: IssueStatus = Field(default=IssueStatus.open)
    priority: IssuePriority = Field(default=IssuePriority.medium)
    created_at: datetime = Field(default_factory=datetime.now)


class IssueUpdate(BaseModel):
    title: Optional[str] = Field(default=None, min_length=3, max_length=100)
    desc: Optional[str] = Field(default=None, min_length=3, max_length=1000)
    status: Optional[IssueStatus] = Field(default=None)
    priority: Optional[IssuePriority] = Field(default=None)


class IssueOut(BaseModel):
    id: str
    title: str
    desc: str
    status: IssueStatus
    priority: IssuePriority
    created_at: datetime
