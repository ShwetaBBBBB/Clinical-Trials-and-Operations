from typing import TypedDict, List, Union, Dict, Any

class AgentState(TypedDict, total=False):
    user_query: str
    next_agent: str
    router_feedback: str
    biomedical_output: str
    ctgov_output: str
    protocol_output: str
    usdm_output: str
    semantic_output: str
    risk_output: str
    final_response: str
    history: List[Dict[str, str]]
