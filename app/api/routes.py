from fastapi import APIRouter
from app.models.request import CodeReviewRequest, PrepPlannerRequest
from app.models.response import CodeReviewResponse, PrepPlannerResponse
from app.services.review_service import process_code_review
from app.services.prep_service import process_prep_plan

router = APIRouter()

@router.post("/review-code", response_model=CodeReviewResponse)
async def review_code_endpoint(request: CodeReviewRequest):
    return await process_code_review(request)

@router.post("/prep-planner", response_model=PrepPlannerResponse)
async def prep_planner_endpoint(request: PrepPlannerRequest):
    return await process_prep_plan(request)
