import uuid

from fastapi import APIRouter, HTTPException, status

from app.schemas import Issue, IssueOut, IssueUpdate
from app.storage import load, save

router = APIRouter(prefix="/api/v1/issues", tags=["issues"])


@router.get("/", response_model=list[IssueOut])
def get_issues():
    return load()


@router.post("/", response_model=IssueOut, status_code=status.HTTP_201_CREATED)
def create_issue(issue: Issue):
    issues = load()
    new_issue = {
        "id": str(uuid.uuid4())[:8],
        "title": issue.title,
        "desc": issue.desc,
        "status": issue.status.value,
        "priority": issue.priority.value,
        "created_at": issue.created_at.isoformat(),
    }
    issues.append(new_issue)
    save(issues)
    return new_issue


@router.get("/{issue_id}", response_model=IssueOut)
def get_issue(issue_id: str):
    for item in load():
        if item["id"] == issue_id:
            return item
    raise HTTPException(status_code=404, detail="Issue not found")


@router.put("/{issue_id}", response_model=IssueOut)
def update_issue(issue_id: str, issue: IssueUpdate):
    issues = load()
    for index, item in enumerate(issues):
        if item["id"] == issue_id:
            updates = issue.model_dump(exclude_unset=True)
            for key, value in updates.items():
                item[key] = value.value if hasattr(value, "value") else value
            issues[index] = item
            save(issues)
            return item
    raise HTTPException(status_code=404, detail="Issue not found")


@router.delete("/{issue_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_issue(issue_id: str):
    issues = load()
    for index, item in enumerate(issues):
        if item["id"] == issue_id:
            issues.pop(index)
            save(issues)
            return
    raise HTTPException(status_code=404, detail="Issue not found")
