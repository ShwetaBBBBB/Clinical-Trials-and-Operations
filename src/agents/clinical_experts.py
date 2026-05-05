from typing import Dict, Any
from src.agents.base_agent import BaseAgent

class CTGIntelligenceAgent(BaseAgent):
    def __init__(self):
        system_prompt = (
            "You are a CTG Intelligence Agent. Your role is to analyze ClinicalTrials.gov data "
            "to extract endpoints, eligibility, and comparators from similar studies. "
            "Input: Search criteria (indication, phase, sponsor). "
            "Output: Study summaries, design elements in a clear format."
        )
        super().__init__(name="CTGIntelligenceAgent", system_prompt=system_prompt)

    def process(self, state: Dict[str, Any]) -> Dict[str, Any]:
        user_query = state.get("user_query", "")
        response = self.get_completion(user_query)
        state["final_response"] = response
        return state

class BiomedicalConceptAgent(BaseAgent):
    def __init__(self):
        system_prompt = (
            "You are a Biomedical Concept Agent. Your role is to identify biomedical concepts "
            "from protocol text and map them to standard ontologies like SNOMED, MedDRA, etc. "
            "Input: Free-text synopsis or protocol sections. "
            "Output: JSON list of biomedical concepts with clear labels."
        )
        super().__init__(name="BiomedicalConceptAgent", system_prompt=system_prompt)

    def process(self, state: Dict[str, Any]) -> Dict[str, Any]:
        user_query = state.get("user_query", "")
        response = self.get_completion(user_query)
        state["final_response"] = response
        return state

class SemanticMappingAgent(BaseAgent):
    def __init__(self):
        system_prompt = (
            "You are a Semantic Mapping Agent. Your role is to link concepts to "
            "OSB (OpenStudyBuilder) Activity Concepts and CDISC Biomedical Concepts. "
            "Input: Concept list or USDM JSON. "
            "Output: Mapped OSB activity identifiers."
        )
        super().__init__(name="SemanticMappingAgent", system_prompt=system_prompt)

    def process(self, state: Dict[str, Any]) -> Dict[str, Any]:
        user_query = state.get("user_query", "")
        response = self.get_completion(user_query)
        state["final_response"] = response
        return state

class USDMJSONBuilderAgent(BaseAgent):
    def __init__(self):
        system_prompt = (
            "You are a USDM JSON Builder Agent. Your role is to convert structured protocol "
            "input into USDM-compliant JSON format. "
            "Input: Enriched protocol metadata. "
            "Output: Valid, well-indented USDM JSON object."
        )
        super().__init__(name="USDMJSONBuilderAgent", system_prompt=system_prompt)

    def process(self, state: Dict[str, Any]) -> Dict[str, Any]:
        user_query = state.get("user_query", "")
        response = self.get_completion(user_query)
        state["final_response"] = response
        return state

class OSBIngestionAgent(BaseAgent):
    def __init__(self):
        system_prompt = (
            "You are an OSB Ingestion Agent. Your role is to prepare and ingest "
            "enriched JSON study designs into OpenStudyBuilder via API. "
            "Input: Final USDM JSON. "
            "Output: Success/failure response and metadata."
        )
        super().__init__(name="OSBIngestionAgent", system_prompt=system_prompt)

    def process(self, state: Dict[str, Any]) -> Dict[str, Any]:
        user_query = state.get("user_query", "")
        response = self.get_completion(user_query)
        state["final_response"] = response
        return state

class ProtocolGeneratorAgent(BaseAgent):
    def __init__(self):
        system_prompt = (
            "You are a Protocol Generator Agent. Your role is to generate "
            "ICH M11-compliant protocol (DocX) from OSB definitions. "
            "Input: OSB study definition. "
            "Output: ICH M11-formatted protocol content."
        )
        super().__init__(name="ProtocolGeneratorAgent", system_prompt=system_prompt)

    def process(self, state: Dict[str, Any]) -> Dict[str, Any]:
        user_query = state.get("user_query", "")
        response = self.get_completion(user_query)
        state["final_response"] = response
        return state

class SynopsisToJSONAgent(BaseAgent):
    def __init__(self):
        system_prompt = (
            "You are a Synopsis-to-JSON Agent. Your role is to parse natural language "
            "protocol synopses into a structured JSON representation. "
            "Input: Free-text synopsis. "
            "Output: Structured protocol metadata (JSON)."
        )
        super().__init__(name="SynopsisToJSONAgent", system_prompt=system_prompt)

    def process(self, state: Dict[str, Any]) -> Dict[str, Any]:
        user_query = state.get("user_query", "")
        response = self.get_completion(user_query)
        state["final_response"] = response
        return state

class DataRetrievalAgent(BaseAgent):
    def __init__(self):
        system_prompt = (
            "You are a Data Retrieval Agent. Your role is to connect to and retrieve "
            "data from ClinicalTrials.gov, CDISC Library, and OSB APIs. "
            "Input: Data source config and query params. "
            "Output: Raw structured data (JSON, XML)."
        )
        super().__init__(name="DataRetrievalAgent", system_prompt=system_prompt)

    def process(self, state: Dict[str, Any]) -> Dict[str, Any]:
        user_query = state.get("user_query", "")
        response = self.get_completion(user_query)
        state["final_response"] = response
        return state

class OntologyLookupAgent(BaseAgent):
    def __init__(self):
        system_prompt = (
            "You are an Ontology Lookup Agent. Your role is to search for concepts "
            "in SNOMED, MeSH, MedDRA, and CDISC terminologies. "
            "Input: Concept label or code. "
            "Output: Standard term with definition and synonyms."
        )
        super().__init__(name="OntologyLookupAgent", system_prompt=system_prompt)

    def process(self, state: Dict[str, Any]) -> Dict[str, Any]:
        user_query = state.get("user_query", "")
        response = self.get_completion(user_query)
        state["final_response"] = response
        return state

class KnowledgeGraphAgent(BaseAgent):
    def __init__(self):
        system_prompt = (
            "You are a Knowledge Graph Agent. Your role is to navigate and reason "
            "over concept relationships using graph structures and vector search. "
            "Input: Concept list or semantic query. "
            "Output: Ranked concept matches and relationship explanations."
        )
        super().__init__(name="KnowledgeGraphAgent", system_prompt=system_prompt)

    def process(self, state: Dict[str, Any]) -> Dict[str, Any]:
        user_query = state.get("user_query", "")
        response = self.get_completion(user_query)
        state["final_response"] = response
        return state

class RiskAssessmentAgent(BaseAgent):
    def __init__(self):
        system_prompt = (
            "You are a Risk Assessment Agent. Your role is to identify and assess "
            "operational, clinical, and regulatory risks in clinical trial designs. "
            "Input: Protocol metadata or USDM JSON. "
            "Output: Risk matrix and mitigation strategies."
        )
        super().__init__(name="RiskAssessmentAgent", system_prompt=system_prompt)

    def process(self, state: Dict[str, Any]) -> Dict[str, Any]:
        user_query = state.get("user_query", "")
        response = self.get_completion(user_query)
        state["final_response"] = response
        state["risk_output"] = response
        return state

