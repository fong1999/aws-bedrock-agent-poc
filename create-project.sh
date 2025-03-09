#!/bin/bash

# Create project directory and basic structure
mkdir -p hr-timeoff-bedrock/app/api hr-timeoff-bedrock/app/services hr-timeoff-bedrock/app/utils

# Create main.py
cat > hr-timeoff-bedrock/main.py << 'EOF'
import uvicorn
from app.api.api import app

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
EOF

# Create app/api/api.py
cat > hr-timeoff-bedrock/app/api/api.py << 'EOF'
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="HR Time-off Bot")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "HR Time-off Bot API"}
EOF

# Create requirements.txt
cat > hr-timeoff-bedrock/requirements.txt << 'EOF'
fastapi==0.103.1
uvicorn==0.23.2
boto3==1.28.44
pydantic==2.3.0
python-dotenv==1.0.0
httpx==0.24.1
EOF

echo "FastAPI project structure created in hr-timeoff-bedrock directory"