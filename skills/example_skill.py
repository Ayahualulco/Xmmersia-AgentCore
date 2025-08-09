from agentcore.base_skill import BaseSkill
from typing import Dict, Any
from datetime import datetime

class ExampleSkill(BaseSkill):
    """Example skill implementation showing the pattern"""
    
    @property
    def skill_id(self) -> str:
        return "example_skill"
    
    @property
    def description(self) -> str:
        return "An example skill that echoes input with timestamp"
    
    def validate_params(self, params: Dict[str, Any]) -> bool:
        if "message" not in params:
            raise ValueError("Missing required parameter: message")
        if not isinstance(params["message"], str):
            raise ValueError("Parameter 'message' must be a string")
        return True
    
    def execute(self, params: Dict[str, Any]) -> Dict[str, Any]:
        self.validate_params(params)
        message = params["message"]
        return {
            "status": "success",
            "original_message": message,
            "echo": f"Echo: {message}",
            "processed_at": datetime.now().isoformat(),
            "skill_id": self.skill_id
        }