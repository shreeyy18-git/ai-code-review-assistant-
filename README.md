# AI Code Review Assistant 🤖✨

**Developed by Shreeyash Asati (ML Engineer)**

🌟 **Live API Endpoint**: [Test the Code Reviewer Here](https://ai-code-review-assistant-n7po.onrender.com/docs#/)  
📸 **Instagram**: [@learnedge.co.in](https://www.instagram.com/learnedge.co.in)  
📧 **Contact**: [learnedge.asper@gmail.com](mailto:learnedge.asper@gmail.com)  

An intelligent, asynchronous FastAPI backend that acts as an expert programming mentor and preparation planner. It leverages Groq's Lightning-Fast AI (Llama 3.1) to analyze student code and generate ultimate study plans.

---

## 🚀 Key Features

### 1. Mentorship-Driven Code Reviews (`/review-code`)
* **Bug Detection**: Identifies exact bugs (Syntax, Logical, Type) and explains why they happen.
* **Auto-Language Detection**: Supports Python, Java, C++, JS, etc., and provides the `fixed_code` in the exact same language.
* **Fuzzy Parsing**: Accepts various naming conventions (`question name`, `student_solution`, etc.) to prevent `422` errors.
* **Dynamic Logic**: Uses a local `questions.json` for verified answers or dynamically deduces the intent for unknown problems.

### 2. Ultimate 1-Day Prep Planner (`/prep-planner`)
* **High-Intensity Strategy**: Generates a complete 24-hour mission-critical study plan.
* **Time-Blocked Schedule**: Breaks the day into Morning, Afternoon, Evening, and Night sessions.
* **Top 5 Important Questions**: Provides the 4-5 most likely interview/exam questions for the chosen domain.
* **Quick Resources**: Recommends the fastest learning materials (Videos/Articles) for 1-day success.

---

## 🛠️ Technology Stack

* **Framework**: [FastAPI](https://fastapi.tiangolo.com/)
* **AI Provider**: [Groq API](https://groq.com/) using `llama-3.1-8b-instant`
* **Validation**: [Pydantic V2](https://docs.pydantic.dev/latest/)
* **Runtime**: [Uvicorn](https://www.uvicorn.org/)

---

## 📡 API Usage

### **1. Code Review (`POST /api/v1/review-code`)**
**Request:**
```json
{
  "question_name": "Two Sum",
  "student_id": "STU123",
  "student_solution": "def add(a, b):\n    return a - b"
}
```
**Response:**
```json
{
  "status": "needs_work",
  "issues": ["Logical Error detected..."],
  "fixed_code": "def add(a, b):\n    return a + b",
  "explanation": "...",
  "hint": "..."
}
```

### **2. Prep Planner (`POST /api/v1/prep-planner`)**
**Request:**
```json
{
  "student_id": "STU123",
  "domain": "Web Development",
  "topics": "React Hooks, Next.js Routing",
  "level": "Beginner"
}
```
**Response:**
```json
{
  "study_plan_title": "Ultimate 1-Day Prep Plan for Web Development",
  "daily_schedule": [...],
  "important_questions": [
    {
      "question": "What is the difference between UseState and UseEffect?",
      "priority": "High"
    }
  ],
  "tips": "Focus on..."
}
```

---

## ⚙️ Quick Start

1. **Clone & Setup**
   ```bash
   git clone https://github.com/learnedge-team/LearnEdge-LLM-AI-Code-Review-Assistant.git
   pip install -r requirements.txt
   ```

2. **Environment**
   Add your `GROQ_API_KEY` to the `.env` file.

3. **Run**
   ```bash
   python run.py
   ```

---

## 📁 Project Structure

```text
├── app/
│   ├── api/routes.py            # API Endpoints
│   ├── models/                  # Pydantic Schemas (Request/Response)
│   ├── services/
│   │   ├── review_service.py    # Code Review Logic
│   │   └── prep_service.py      # Study Plan Logic
│   ├── utils/prompt_builder.py  # AI Prompt Engineering
│   └── main.py                  # App Entry Point
├── main.py                      # Root Entry for Render
└── run.py                       # Local Run Script
```
