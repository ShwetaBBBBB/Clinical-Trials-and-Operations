from abc import ABC, abstractmethod
from typing import Dict, Any, List
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from src.core.llm_client import llm_client
from src.core.logger import logger

class BaseAgent(ABC):
    def __init__(self, name: str, system_prompt: str):
        self.name = name
        self.system_prompt = system_prompt
        self.model = llm_client.llm

    @abstractmethod
    def process(self, state: Dict[str, Any]) -> Dict[str, Any]:
        """Process the current state and return updated state."""
        pass

    def get_completion(self, user_request: str, history: List[Dict[str, str]] = None) -> str:
        """Helper to get a completion from the LLM."""
        try:
            logger.info(f"Agent {self.name} is generating completion...")
            messages = [SystemMessage(content=self.system_prompt)]
            
            # Add history if provided
            if history:
                for msg in history:
                    if msg["role"] == "user":
                        messages.append(HumanMessage(content=msg["content"]))
                    elif msg["role"] == "assistant":
                        messages.append(AIMessage(content=msg["content"]))
            
            messages.append(HumanMessage(content=user_request))
            
            response = self.model.invoke(messages)
            return response.content
                
        except Exception as e:
            logger.error(f"Error in {self.name}: {e}")
            return f"Error: {str(e)}"
