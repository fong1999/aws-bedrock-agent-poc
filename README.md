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

### Virtual Environment

Here's a step-by-step guide to using those commands to set up virtual environment:

1. First, make sure you're in project directory:
   ```bash
   cd hr-timeoff-bedrock
   ```

2. Create the virtual environment (only need to do this once):
   ```bash
   python -m venv venv
   ```
   This creates a folder called "venv" in project directory that contains a separate Python installation.

3. Activate the virtual environment:
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   You'll notice your command prompt changes to show "(venv)" at the beginning, indicating the virtual environment is active.

4. Install the required packages:
   ```bash
   pip install fastapi uvicorn boto3 pydantic python-dotenv httpx
   ```
   This installs all the packages into your virtual environment, not the system Python.

5. Run the application:
   ```bash
   python main.py
   ```

Every time we want to work on this project in a new terminal session, we'll need to activate the virtual environment (step 3) before running your code.

To deactivate the virtual environment when we're done working:
```bash
deactivate
```

This approach ensures that the project has its own isolated set of dependencies, which helps avoid conflicts between different projects requiring different versions of the same packages.

### Next Steps

* AWS Credentials: Make sure the environment has AWS credentials configured to access Bedrock
* Testing: Test the API endpoints using the Swagger UI at /docs
* Angular Integration: Test the integration with your existing Angular UI
* Enhanced Features: Add more sophisticated HR-specific functionality based on the demo needs