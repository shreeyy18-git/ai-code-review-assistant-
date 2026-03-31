from app.models.request import PrepPlannerRequest
from app.models.response import PrepPlannerResponse
from app.services.llm_service import generate_prep_plan
from app.utils.logger import setup_logger

logger = setup_logger(__name__)

async def process_prep_plan(request: PrepPlannerRequest) -> PrepPlannerResponse:
    logger.info(f"Generating prep plan for student_id: {request.student_id}, domain: {request.domain}")

    topics_section = f"Specific Topics: {request.topics}" if request.topics else "No specific topics mentioned."

    prompt = f"""
You are an expert study planner and learning coach.

A student needs an ULTIMATE one-day preparation plan for an upcoming exam or interview.

Student ID: {request.student_id}
Domain: {request.domain}
{topics_section}
Fixed Duration: 1 Day (Intense Preparation)
Current Level: {request.level}

STRICT RULES:
- Create a high-intensity, actionable one-day "Ultimate Prep" plan.
- Break the day into Morning, Afternoon, Evening, and Night sessions.
- Provide 4-5 high-impact "Important Questions" that are likely to be asked in exams/interviews for this domain/topic.
- IMPORTANT: Do NOT provide answers or hints for the questions. Only the questions themselves.
- Include specific resources (best YouTube videos, articles, or documentation) for quick learning.
- Tailor the plan to be the most efficient path to success in 24 hours.
- WORD LIMIT: Ensure the combined length of 'tips' and all 'tasks' descriptions is between 100 and 150 words.

Return JSON:
{{
  "student_id": "{request.student_id}",
  "study_plan_title": "Ultimate 1-Day Prep Plan for {request.domain}",
  "domain": "{request.domain}",
  "level": "{request.level}",
  "total_duration": "1 Day (Intense)",
  "daily_schedule": [
    {{
      "time_block": "Morning (8 AM - 12 PM)",
      "topic": "Core concepts",
      "tasks": ["task 1", "task 2"],
      "focus": "Conceptual understanding"
    }},
    {{
      "time_block": "Afternoon (1 PM - 5 PM)",
      "topic": "Practical/Problem solving",
      "tasks": ["task 1", "task 2"],
      "focus": "Hands-on practice"
    }}
  ],
  "important_questions": [
    {{
      "question": "What is ...?",
      "priority": "High"
    }}
  ],
  "resources": [
    {{
      "name": "resource name",
      "type": "video/article",
      "url": "link"
    }}
  ],
  "milestones": [
    {{
      "milestone": "Mastered X",
      "by_time": "2 PM"
    }}
  ],
  "tips": "Personalized 24-hour success tips"
}}
Ensure the output is valid JSON.
"""

    response = await generate_prep_plan(prompt.strip())

    # Ensure student_id is always present
    if not response.student_id:
        response.student_id = request.student_id

    return response
