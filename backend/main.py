import os
import sys
import time
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Dict, Any, List

# Add backend dir to path so imports work
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from agents.email_agent import process_email

app = FastAPI(
    title="Agent Factory - Email Demo API",
    description="AI-powered email processing and response generation",
    version="1.0.0"
)

# ============================================================
# CORS Configuration - Allow frontend access
# ============================================================
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ============================================================
# Request/Response Models
# ============================================================
class EmailRequest(BaseModel):
    email_text: str

class EmailRequestAlt(BaseModel):
    content: str

class EmailResponse(BaseModel):
    steps: List[Dict[str, Any]]
    result: Dict[str, Any]
    elapsed_seconds: float

# ============================================================
# Health Check Endpoints
# ============================================================

@app.get("/")
def root():
    """Root endpoint - API status"""
    return {
        "status": "Agent Factory API is running",
        "version": "1.0.0",
        "endpoints": {
            "process_email": "/api/process-email",
            "process_email_alt": "/process-email",
            "health": "/health"
        }
    }

@app.get("/health")
def health():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "model": os.getenv("MODEL_NAME", "gemini-2.5-flash"),
        "api_key_configured": bool(os.getenv("GEMINI_API_KEY"))
    }

# ============================================================
# Primary Endpoint: /api/process-email
# ============================================================

@app.post("/api/process-email", response_model=EmailResponse)
def api_process_email(req: EmailRequest):
    """
    Process an email through the full agent workflow.
    
    Request body:
    {
        "email_text": "Your email content here"
    }
    
    Returns:
    - steps: List of processing steps with results
    - result: Final intent, category, priority, and draft response
    - elapsed_seconds: Processing time
    """
    try:
        if not req.email_text or not req.email_text.strip():
            raise HTTPException(status_code=400, detail="Email content cannot be empty")
        
        start_time = time.time()
        steps, result = process_email(req.email_text)
        elapsed = round(time.time() - start_time, 2)
        
        return {
            "steps": steps,
            "result": result,
            "elapsed_seconds": elapsed,
        }
    except Exception as e:
        print(f"❌ Error processing email: {e}")
        raise HTTPException(status_code=500, detail=str(e))

# ============================================================
# Alternative Endpoint: /process-email (without /api/)
# ============================================================

@app.post("/process-email", response_model=EmailResponse)
def process_email_simple(req: EmailRequest):
    """
    Process an email (simpler URL without /api/).
    
    Request body:
    {
        "email_text": "Your email content here"
    }
    """
    try:
        if not req.email_text or not req.email_text.strip():
            raise HTTPException(status_code=400, detail="Email content cannot be empty")
        
        start_time = time.time()
        steps, result = process_email(req.email_text)
        elapsed = round(time.time() - start_time, 2)
        
        return {
            "steps": steps,
            "result": result,
            "elapsed_seconds": elapsed,
        }
    except Exception as e:
        print(f"❌ Error processing email: {e}")
        raise HTTPException(status_code=500, detail=str(e))

# ============================================================
# Alternative Endpoint: Accepts 'content' field
# ============================================================

@app.post("/api/process-email-alt", response_model=EmailResponse)
def api_process_email_alt(req: EmailRequestAlt):
    """
    Process an email using 'content' field instead of 'email_text'.
    
    Request body:
    {
        "content": "Your email content here"
    }
    """
    try:
        if not req.content or not req.content.strip():
            raise HTTPException(status_code=400, detail="Email content cannot be empty")
        
        start_time = time.time()
        steps, result = process_email(req.content)
        elapsed = round(time.time() - start_time, 2)
        
        return {
            "steps": steps,
            "result": result,
            "elapsed_seconds": elapsed,
        }
    except Exception as e:
        print(f"❌ Error processing email: {e}")
        raise HTTPException(status_code=500, detail=str(e))

# ============================================================
# Alternative Endpoint: /process-email-alt (without /api/)
# ============================================================

@app.post("/process-email-alt", response_model=EmailResponse)
def process_email_alt(req: EmailRequestAlt):
    """
    Process an email using 'content' field (simpler URL without /api/).
    
    Request body:
    {
        "content": "Your email content here"
    }
    """
    try:
        if not req.content or not req.content.strip():
            raise HTTPException(status_code=400, detail="Email content cannot be empty")
        
        start_time = time.time()
        steps, result = process_email(req.content)
        elapsed = round(time.time() - start_time, 2)
        
        return {
            "steps": steps,
            "result": result,
            "elapsed_seconds": elapsed,
        }
    except Exception as e:
        print(f"❌ Error processing email: {e}")
        raise HTTPException(status_code=500, detail=str(e))

# ============================================================
# Run the app (for local development)
# ============================================================
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        app,
        host=os.getenv("API_HOST", "0.0.0.0"),
        port=int(os.getenv("API_PORT", 8001)),
        reload=True
    )


#* How to run

#     # Backend (set GEMINI_API_KEY in backend/.env first)
#     cd backend
#     pip install -r requirements.txt
#^     python -m uvicorn main:app --reload --port 8000
#^     python -m uvicorn main:app --reload --port 8001

#     # Frontend
#     cd frontend
#^     npm run dev

#   Open http://localhost:3000 — the demo works even without the backend (it simulates results). With the
#   backend + Gemini key, it generates real AI responses.
