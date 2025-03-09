# aws-bedrock-agent-poc


## Overview

This is a Python Fast API PoC to use AWS Bedrock LLM.

### Plan for implementing your Python backend

Start with a basic Flask API:

Create endpoints for conversation
Implement Bedrock LLM integration
Add session management for conversations


Implement HR time-off functionality:

Build prompts for understanding time-off requests
Create functions to handle time-off balance inquiries (mock data)
Develop the Outlook calendar integration logic


Add conversational context management:

Store conversation history
Implement prompt engineering to maintain context
Add proper error handling

## How To Start

1. Use the create-project.sh to create the basic file structure.
2. Next, Install Dependencies

First, set up your virtual environment and install the required packages:

```
cd hr-timeoff-bedrock
python -m venv venv

# Activate the virtual environment
# On Windows:
# venv\Scripts\activate
# On Unix or MacOS:
source venv/bin/activate

# Install required packages
pip install -r requirements.txt
```

3. Create the AWS Bedrock Service: app/services/bedrock_service.py
4. Create Conversation Management: app/services/conversation_service.py
5. Create Outlook Service (Mock): app/services/outlook_service.py
6. Create API Routes: pdate the file at app/api/api.py
7. Test the API: Run FastAPI application
8. Connect with Your Angular App

Next Steps

AWS Credentials: Make sure the environment has AWS credentials configured to access Bedrock
Testing: Test the API endpoints using the Swagger UI at /docs
Angular Integration: Test the integration with your existing Angular UI
Enhanced Features: Add more sophisticated HR-specific functionality based on the demo needs