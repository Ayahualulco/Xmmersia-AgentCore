"""
Xmmersia AgentCore - Immutable foundation for all agents
"""

from .base_agent import BaseAgent
from .base_skill import BaseSkill
from .reflection import ReflectionSystem
from .awakening import AwakeningSequence

__version__ = "1.0.0"
__all__ = ["BaseAgent", "BaseSkill", "ReflectionSystem", "AwakeningSequence"]