# Xmmersia-AgentCore

The immutable foundation for all Xmmersia agents. Like Bitcoin's core protocol, AgentCore provides the unchanging base that enables the entire ecosystem to scale without technical debt.

## What is AgentCore?

AgentCore provides:
- **BaseAgent**: Abstract class all agents inherit from
- **BaseSkill**: Abstract class for modular skills
- **ReflectionSystem**: Self-awareness protocols
- **AwakeningSequence**: Initialization patterns
- **A2AHandler**: Protocol communication standards

## Installation

```bash
pip install xmmersia-agentcore
```

## Quick Start

### Creating Your First Agent

```python
from agentcore import BaseAgent
from datetime import datetime

class MyAgent(BaseAgent):
    async def awaken(self):
        print(f"{self.name} is awakening...")
        self.awakened = True
        # Load your skills
        self.load_skills()
        
    async def reflect(self):
        return {
            "identity": self.name,
            "purpose": "My agent's purpose",
            "time": datetime.now().isoformat()
        }
    
    async def process(self, message):
        # Route to appropriate skill or handle directly
        return {"response": f"Processed: {message}"}

# Use your agent
import asyncio

async def main():
    agent = MyAgent({"name": "MyFirstAgent"})
    await agent.awaken()
    result = await agent.process({"text": "Hello"})
    print(result)

asyncio.run(main())
```

Creating a Custom Skill
python

```python
from agentcore import BaseSkill

class AnalysisSkill(BaseSkill):
    @property
    def skill_id(self):
        return "analyze"
    
    @property
    def description(self):
        return "Analyzes input data"
    
    def validate_params(self, params):
        if "data" not in params:
            raise ValueError("Missing 'data' parameter")
        return True
    
    def execute(self, params):
        self.validate_params(params)
        # Your skill logic here
        return {
            "status": "success",
            "analysis": f"Analyzed {len(params['data'])} items"
        }
```

## Why AgentCore?
Before AgentCore, every agent reimplemented:
* Awakening sequences
* Reflection protocols
* Skill management
* A2A handling

Now, agents inherit these patterns, ensuring consistency and enabling rapid development.

## Requirements
All agents MUST:
1. Inherit from BaseAgent
2. Place skills in `/skills` inheriting from BaseSkill
3. Implement awakening and reflection
4. Declare agentCoreVersion in agent cards

## Documentation
See `/docs` for:
* Migration Guide
* Skill Development
* API Reference

## 🎯 Success Criteria

AgentCore is successful when:
1. ✅ DevMate successfully migrates to use it
2. ✅ New agents can be created in hours, not days
3. ✅ Skills work identically from UI or A2A
4. ✅ Agents can switch between Mate/Sentinel via config
5. ✅ Zero code duplication across agents

## 🚦 Let's Start!

1. **First**: Create the GitHub repository
2. **Second**: Set up the basic structure
3. **Third**: Implement BaseAgent
4. **Fourth**: Test with a minimal example
5. **Fifth**: Begin DevMate migration