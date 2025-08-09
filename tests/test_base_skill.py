import pytest
from typing import Dict, Any
from agentcore.base_skill import BaseSkill  # Note: use full import path

class TestSkill(BaseSkill):
    """Test implementation of BaseSkill"""
    
    @property
    def skill_id(self) -> str:
        return "test_skill"
    
    @property
    def description(self) -> str:
        return "A test skill for unit testing"
    
    def validate_params(self, params: Dict[str, Any]) -> bool:
        if "input" not in params:
            raise ValueError("Missing required parameter: input")
        return True
    
    def execute(self, params: Dict[str, Any]) -> Dict[str, Any]:
        self.validate_params(params)
        return {
            "status": "success",
            "output": f"Processed: {params['input']}"
        }

def test_skill_creation():
    """Test skill can be created"""
    skill = TestSkill()
    assert skill.skill_id == "test_skill"
    assert skill.description == "A test skill for unit testing"

def test_skill_validation():
    """Test skill parameter validation"""
    skill = TestSkill()
    
    # Valid params
    assert skill.validate_params({"input": "test"}) == True
    
    # Invalid params
    with pytest.raises(ValueError) as exc_info:
        skill.validate_params({})
    assert "Missing required parameter" in str(exc_info.value)

def test_skill_execution():
    """Test skill execution"""
    skill = TestSkill()
    result = skill.execute({"input": "hello"})
    
    assert result["status"] == "success"
    assert result["output"] == "Processed: hello"

def test_skill_string_representation():
    """Test skill string representation"""
    skill = TestSkill()
    assert str(skill) == "test_skill: A test skill for unit testing"