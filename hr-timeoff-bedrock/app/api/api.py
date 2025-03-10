# from fastapi import FastAPI, HTTPException
# from fastapi.middleware.cors import CORSMiddleware
# from pydantic import BaseModel
# from typing import Optional, Dict, Any

# from app.services.conversation_service import ConversationService
# from app.services.outlook_service import OutlookService

# app = FastAPI(title="HR Time-off Bot")

# # Configure CORS
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # In production, replace with specific origins
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # Initialize services
# conversation_service = ConversationService()
# outlook_service = OutlookService()

# # Request models
# class ChatRequest(BaseModel):
#     message: str
#     sessionId: Optional[str] = None

# class OotoRequest(BaseModel):
#     startDate: str
#     endDate: str
#     message: str

# @app.get("/")
# def read_root():
#     return {"message": "HR Time-off Bot API"}

# @app.post("/api/chat")
# def chat(request: ChatRequest):
#     """
#     Process a chat message and return a response from the HR bot
#     """
#     result = conversation_service.process_message(
#         message=request.message,
#         session_id=request.sessionId
#     )
#     return result

# @app.post("/api/create-ooto")
# def create_ooto(request: OotoRequest):
#     """
#     Create an Out-of-Office event in Outlook calendar
#     """
#     result = outlook_service.create_ooto_event(
#         start_date=request.startDate,
#         end_date=request.endDate,
#         message=request.message
#     )
    
#     if not result['success']:
#         raise HTTPException(status_code=400, detail=result['message'])
    
#     return result


from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional

from app.services.conversation_service import ConversationService

app = FastAPI(title="HR Time-off Bot")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize services
conversation_service = ConversationService()

# Request models
class ChatRequest(BaseModel):
    message: str
    sessionId: Optional[str] = None

@app.get("/")
def read_root():
    return {"message": "HR Time-off Bot API"}

@app.post("/api/chat")
def chat(request: ChatRequest):
    """
    Process a chat message and return a response from the HR bot
    """
    result = conversation_service.process_message(
        message=request.message,
        session_id=request.sessionId
    )
    return result
