import asyncio
from agentcore import BaseAgent

class DiscoveryAgent(BaseAgent):
    async def awaken(self):
        self.awakened = True
        self.load_skills()
        print(f"✅ Awakened with {len(self.skills)} skills")
        for skill_id in self.skills:
            print(f"  - Found skill: {skill_id}")
    
    async def reflect(self):
        return {"skills_loaded": len(self.skills)}
    
    async def process(self, message):
        if "skill" in message and message["skill"] in self.skills:
            return self.skills[message["skill"]].execute(message)
        return {"error": "Skill not found"}

async def main():
    agent = DiscoveryAgent({
        "name": "SkillDiscoveryTest",
        "skills_directory": "./skills"
    })
    
    await agent.awaken()
    
    # Test the example skill if loaded
    if "example_skill" in agent.skills:
        result = agent.skills["example_skill"].execute({"message": "Testing!"})
        print(f"✅ Skill execution result: {result['echo']}")

if __name__ == "__main__":
    asyncio.run(main())