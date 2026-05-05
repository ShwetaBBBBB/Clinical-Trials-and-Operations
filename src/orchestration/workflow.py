from langgraph.graph import StateGraph, END
from src.orchestration.state import AgentState
from src.agents.question_categorizer_agent import QuestionCategorizerAgent
from src.agents.clinical_experts import (
    CTGIntelligenceAgent, BiomedicalConceptAgent, SemanticMappingAgent,
    USDMJSONBuilderAgent, OSBIngestionAgent, ProtocolGeneratorAgent,
    SynopsisToJSONAgent, DataRetrievalAgent, OntologyLookupAgent,
    KnowledgeGraphAgent, RiskAssessmentAgent
)

def create_workflow():
    # Initialize agents
    categorizer = QuestionCategorizerAgent()
    ctg = CTGIntelligenceAgent()
    biomedical = BiomedicalConceptAgent()
    semantic = SemanticMappingAgent()
    usdm = USDMJSONBuilderAgent()
    osb = OSBIngestionAgent()
    protocol = ProtocolGeneratorAgent()
    synopsis = SynopsisToJSONAgent()
    data_retrieval = DataRetrievalAgent()
    ontology = OntologyLookupAgent()
    kg = KnowledgeGraphAgent()
    risk = RiskAssessmentAgent()

    # Define the graph
    workflow = StateGraph(AgentState)

    # Add nodes
    workflow.add_node("categorizer", categorizer.process)
    workflow.add_node("ctg_intelligence", ctg.process)
    workflow.add_node("biomedical_concept", biomedical.process)
    workflow.add_node("semantic_mapping", semantic.process)
    workflow.add_node("usdm_json_builder", usdm.process)
    workflow.add_node("osb_ingestion", osb.process)
    workflow.add_node("protocol_generator", protocol.process)
    workflow.add_node("synopsis_to_json", synopsis.process)
    workflow.add_node("data_retrieval", data_retrieval.process)
    workflow.add_node("ontology_lookup", ontology.process)
    workflow.add_node("knowledge_graph", kg.process)
    workflow.add_node("risk_assessment", risk.process)

    # Define conditional edges from categorizer
    def route_decision(state: AgentState):
        return state["next_agent"]

    workflow.set_entry_point("categorizer")
    
    workflow.add_conditional_edges(
        "categorizer",
        route_decision,
        {
            "ctg_intelligence": "ctg_intelligence",
            "biomedical_concept": "biomedical_concept",
            "semantic_mapping": "semantic_mapping",
            "usdm_json_builder": "usdm_json_builder",
            "osb_ingestion": "osb_ingestion",
            "protocol_generator": "protocol_generator",
            "synopsis_to_json": "synopsis_to_json",
            "data_retrieval": "data_retrieval",
            "ontology_lookup": "ontology_lookup",
            "knowledge_graph": "knowledge_graph",
            "risk_assessment": "risk_assessment",
            "general": END
        }
    )

    # All experts go to END
    workflow.add_edge("ctg_intelligence", END)
    workflow.add_edge("biomedical_concept", END)
    workflow.add_edge("semantic_mapping", END)
    workflow.add_edge("usdm_json_builder", END)
    workflow.add_edge("osb_ingestion", END)
    workflow.add_edge("protocol_generator", END)
    workflow.add_edge("synopsis_to_json", END)
    workflow.add_edge("data_retrieval", END)
    workflow.add_edge("ontology_lookup", END)
    workflow.add_edge("knowledge_graph", END)
    workflow.add_edge("risk_assessment", END)

    return workflow.compile()
