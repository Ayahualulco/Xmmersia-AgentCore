import pytest
import asyncio
from typing import Dict, Any
from agentcore.base_agent import BaseAgent  # Use full import path

class TestAgent(BaseAgent):
    """Test implementation of BaseAgent"""
    
    async def awaken(self):
        self.awakened = True
        
    async def reflect(self) -> Dict[str, Any]:
        return {"test": "reflection"}
    
    async def process(self, message: Dict[str, Any]) -> Dict[str, Any]:
        return {"processed": message}

def test_agent_creation():
    """Test agent can be created"""
    config = {"name": "TestAgent", "agent_type": "mate"}
    agent = TestAgent(config)
    assert agent.name == "TestAgent"
    assert agent.agent_type == "mate"
    assert agent.awakened == False

def test_agent_card():
    """Test agent card generation"""
    config = {"name": "TestAgent"}
    agent = TestAgent(config)
    card = agent.get_agent_card()
    assert card["name"] == "TestAgent"
    assert card["protocolVersion"] == "0.2.5"
    assert card["xmmersia"]["inheritsFrom"] == "BaseAgent"

@pytest.mark.asyncio
async def test_awakening():
    """Test agent awakening"""
    config = {"name": "TestAgent"}
    agent = TestAgent(config)
    assert agent.awakened == False
    await agent.awaken()
    assert agent.awakened == True

@pytest.mark.asyncio
async def test_reflection():
    """Test agent reflection"""
    config = {"name": "TestAgent"}
    agent = TestAgent(config)
    reflection = await agent.reflect()
    assert reflection == {"test": "reflection"}

@pytest.mark.asyncio
async def test_process():
    """Test agent message processing"""
    config = {"name": "TestAgent"}
    agent = TestAgent(config)
    result = await agent.process({"input": "test"})
    assert result == {"processed": {"input": "test"}}

@pytest.mark.asyncio
async def test_health_check():
    """Test agent health check"""
    config = {"name": "TestAgent"}
    agent = TestAgent(config)
    health = await agent.health_check()
    assert health["status"] == "not_awakened"
    assert health["skills_loaded"] == 0
    
    await agent.awaken()
    health = await agent.health_check()
    assert health["status"] == "healthy"