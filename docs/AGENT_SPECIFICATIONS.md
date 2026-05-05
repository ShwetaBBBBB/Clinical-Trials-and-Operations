# 🧠 Agent Swarm Specifications

ClinOps AI utilizes a hierarchical multi-agent system where each agent is an expert in a specific domain of clinical trial operations.

## 1. Question Categorizer (The Router)
- **Role**: Entry point for all queries. Analyzes intent and routes to the correct expert.
- **Logic**: Semantic classification using LLM reasoning.
- **Valid Categories**: `ctg_intelligence`, `biomedical_concept`, `semantic_mapping`, `usdm_json_builder`, `osb_ingestion`, `protocol_generator`, `synopsis_to_json`, `data_retrieval`, `ontology_lookup`, `knowledge_graph`, `risk_assessment`, `general`.

## 2. CTG Intelligence Agent
- **Expertise**: ClinicalTrials.gov (CTG) data analysis.
- **Function**: Extracts endpoints, eligibility criteria, and comparators from historical studies to benchmark new trial designs.

## 3. Biomedical Concept Agent
- **Expertise**: Natural Language Processing (NLP) of medical text.
- **Function**: Identifies diseases, drugs, and targets from synopses and maps them to standard terminologies.

## 4. Protocol Designer Agent
- **Expertise**: ICH M11 Compliance.
- **Function**: Generates structured protocol content based on study definitions.

## 5. USDM JSON Builder Agent
- **Expertise**: CDISC Unified Study Definitions Model (USDM).
- **Function**: Converts trial design metadata into valid, structured USDM-compliant JSON.

## 6. Semantic Mapping Agent
- **Expertise**: Interoperability and Ontologies.
- **Function**: Links local terms to global standards like SNOMED-CT, MedDRA, and CDISC.

## 7. Risk Assessment Agent
- **Expertise**: Clinical & Operational Risk.
- **Function**: Identifies potential failure points in trial designs, including recruitment risks and regulatory hurdles.

---

## 🛠️ Implementation Details

All agents inherit from the `BaseAgent` class, which provides:
- **Singleton LLM Access**: Shared connection to Azure OpenAI.
- **Context Management**: Automatic inclusion of system prompts and conversation history.
- **Standardized Processing**: Consistent `process(state)` interface for LangGraph compatibility.
