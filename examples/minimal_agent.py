from agentcore import BaseAgent
from datetime import datetime  # ADD THIS IMPORT
import asyncio  # ADD THIS FOR ASYNC EXECUTION

class MinimalAgent(BaseAgent):
    """Simplest possible agent implementation"""
    
    async def awaken(self):
        print(f"{self.name} is awakening...")
        self.awakened = True
        
    async def reflect(self):
        return {
            "identity": self.name,
            "purpose": "To demonstrate minimal implementation",
            "time": datetime.now().isoformat()
        }
    
    async def process(self, message):
        return {"response": f"{self.name} received: {message}"}

# Usage - wrap in async function
async def main():
    agent = MinimalAgent({"name": "TestAgent"})
    await agent.awaken()
    
    # Test reflection
    reflection = await agent.reflect()
    print(f"Reflection: {reflection}")
    
    # Test message processing
    response = await agent.process({"text": "Hello"})
    print(f"Response: {response}")

# Run the async main function
if __name__ == "__main__":
    asyncio.run(main())