"""Custom exceptions for AgentCore"""

class AgentCoreException(Exception):
    """Base exception for all AgentCore errors"""
    pass

class AwakeningException(AgentCoreException):
    """Raised when agent awakening fails"""
    pass

class SkillException(AgentCoreException):
    """Raised when skill execution fails"""
    pass

class ReflectionException(AgentCoreException):
    """Raised when reflection fails"""
    pass

class ValidationException(AgentCoreException):
    """Raised when validation fails"""
    pass