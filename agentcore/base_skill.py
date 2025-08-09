from abc import ABC, abstractmethod
from typing import Dict, Any

class BaseSkill(ABC):
    """
    Abstract base class all skills must inherit from.
    Ensures consistent skill implementation across all agents.
    """
    
    @property
    @abstractmethod
    def skill_id(self) -> str:
        """Unique identifier for this skill"""
        pass
    
    @property
    @abstractmethod
    def description(self) -> str:
        """Human-readable skill description"""
        pass
    
    @abstractmethod
    def validate_params(self, params: Dict[str, Any]) -> bool:
        """
        Validate input parameters before execution.
        Raises ValueError if invalid.
        """
        pass
    
    @abstractmethod
    def execute(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """
        Execute the skill with given parameters.
        Returns results as dictionary.
        """
        pass
    
    def __str__(self):
        return f"{self.skill_id}: {self.description}"