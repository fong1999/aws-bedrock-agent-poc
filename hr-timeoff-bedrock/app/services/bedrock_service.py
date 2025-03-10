import boto3
import json
from typing import Dict, Any, Optional

class BedrockService:
    def __init__(self, region_name: str = "us-east-1"):
        self.client = boto3.client(
            service_name='bedrock-runtime',
            region_name=region_name
        )
    
    def invoke_model(
        self, 
        prompt: str, 
        model_id: str = 'anthropic.claude-3-sonnet-20240229-v1:0',
        temperature: float = 0.7,
        max_tokens: int = 1000
    ) -> str:
        """Invoke AWS Bedrock foundation model with prompt"""
        try:
            # Format request based on model provider
            request_body = self._format_request(prompt, model_id, temperature, max_tokens)
            
            # Call Bedrock
            response = self.client.invoke_model(
                modelId=model_id,
                body=json.dumps(request_body)
            )
            
            # Parse response based on model
            return self._parse_response(response, model_id)
            
        except Exception as e:
            print(f"Error invoking Bedrock: {str(e)}")
            return f"I encountered an error: {str(e)}"
    
    def _format_request(
        self, 
        prompt: str, 
        model_id: str,
        temperature: float,
        max_tokens: int
    ) -> Dict[str, Any]:
        """Format the request based on the model provider"""
        if "anthropic" in model_id:
            return {
                "prompt": prompt,
                "max_tokens_to_sample": max_tokens,
                "temperature": temperature,
            }
        elif "amazon" in model_id:
            return {
                "inputText": prompt,
                "textGenerationConfig": {
                    "maxTokenCount": max_tokens,
                    "temperature": temperature,
                }
            }
        else:
            # Default format for other providers
            return {"prompt": prompt}
    
    def _parse_response(self, response: Dict[str, Any], model_id: str) -> str:
        """Parse the response based on the model provider"""
        response_body = json.loads(response.get('body').read())
        
        if "anthropic" in model_id:
            return response_body.get('completion', '')
        elif "amazon" in model_id:
            return response_body.get('results', [{}])[0].get('outputText', '')
        else:
            return str(response_body)