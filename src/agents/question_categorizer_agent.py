from typing import Dict, Any
from src.agents.base_agent import BaseAgent
from src.core.logger import logger

class QuestionCategorizerAgent(BaseAgent):
    def __init__(self):
        system_prompt = (
            "You are a Clinical Operations Router Agent. Your job is to categorize user queries "
            "into one of the following categories: ctg_intelligence, biomedical_concept, "
            "semantic_mapping, usdm_json_builder, osb_ingestion, protocol_generator, "
            "synopsis_to_json, data_retrieval, ontology_lookup, knowledge_graph, risk_assessment, or general. "
            "Respond ONLY with the category name."
        )
        super().__init__(name="QuestionCategorizerAgent", system_prompt=system_prompt)

    def process(self, state: Dict[str, Any]) -> Dict[str, Any]:
        user_query = state.get("user_query", "")
        logger.info(f"Categorizing query: {user_query}")
        
        category = self.get_completion(user_query).strip().lower()
        
        # Validation
        valid_categories = [
            "ctg_intelligence", "biomedical_concept", "semantic_mapping",
            "usdm_json_builder", "osb_ingestion", "protocol_generator",
            "synopsis_to_json", "data_retrieval", "ontology_lookup",
            "knowledge_graph", "risk_assessment", "general"
        ]
        
        target = "general"
        for cat in valid_categories:
            if cat in category:
                target = cat
                break
        
        state["next_agent"] = target
        state["router_feedback"] = category
        return state
