from abc import ABC, abstractmethod
from typing import Dict, Any, List, Optional
import asyncio
import uuid
from datetime import datetime
import os
import importlib
import inspect
import importlib.util  # ADD THIS
from pathlib import Path  # ADD THIS
from .base_skill import BaseSkill  # ADD THIS for skill discovery


class BaseAgent(ABC):
    """
    Abstract base class all Xmmersia agents must inherit from.
    Provides core functionality for awakening, reflection, and skill management.
    """
    
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.agent_id = str(uuid.uuid4())
        self.agent_type = config.get("agent_type", "mate")  # mate or sentinel
        self.role = config.get("role", "specialist")
        self.name = config.get("name", "UnnamedAgent")
        self.version = config.get("version", "1.0.0")
        self.agentcore_version = "1.0.0"
        self.skills = {}
        self.awakened = False
        self.reflection_history = []
        
    @abstractmethod
    async def awaken(self) -> None:
        """
        Initialize agent with institutional memory.
        Connect to knowledge base, load configuration, establish self-awareness.
        """
        pass
    
    @abstractmethod
    async def reflect(self) -> Dict[str, Any]:
        """
        Self-reflection on identity, purpose, and actions.
        Returns reflection data for institutional memory.
        """
        pass
    
    @abstractmethod
    async def process(self, message: Dict[str, Any]) -> Dict[str, Any]:
        """
        Process incoming messages (UI or A2A).
        Main entry point for all agent interactions.
        """
        pass
    
    def load_skills(self) -> Dict[str, Any]:
        """Automatically discover and load skills from /skills directory"""
        skills_dir = Path(self.config.get('skills_directory', './skills'))
        loaded_skills = {}
        
        if not skills_dir.exists():
            return loaded_skills
        
        # Find all Python files in skills directory
        for skill_file in skills_dir.glob('*.py'):
            if skill_file.name.startswith('__'):
                continue
                
            module_name = skill_file.stem
            try:
                # Dynamic import
                spec = importlib.util.spec_from_file_location(
                    f"skills.{module_name}", 
                    skill_file
                )
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                
                # Find all BaseSkill subclasses
                for name, obj in inspect.getmembers(module):
                    if (inspect.isclass(obj) and 
                        issubclass(obj, BaseSkill) and 
                        obj != BaseSkill):
                        skill_instance = obj()
                        loaded_skills[skill_instance.skill_id] = skill_instance
                        print(f"Loaded skill: {skill_instance.skill_id}")
                        
            except Exception as e:
                print(f"Failed to load skill from {skill_file}: {e}")
        
        self.skills = loaded_skills
        return loaded_skills
    
    def get_agent_card(self) -> Dict[str, Any]:
        """Generate A2A-compliant agent card"""
        return {
            "name": self.name,
            "version": self.version,
            "protocolVersion": "0.2.5",
            "xmmersia": {
                "type": self.agent_type,
                "role": self.role,
                "agentCoreVersion": self.agentcore_version,
                "inheritsFrom": "BaseAgent",
                "skillPattern": "modular"
            }
        }
    
    async def health_check(self) -> Dict[str, Any]:
        """Built-in health monitoring"""
        return {
            "status": "healthy" if self.awakened else "not_awakened",
            "agent_id": self.agent_id,
            "uptime": datetime.now().isoformat(),
            "skills_loaded": len(self.skills)
        }