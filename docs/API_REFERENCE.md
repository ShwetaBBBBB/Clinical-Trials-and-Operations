# 📖 API Reference

This document provides a technical overview of the primary classes and modules within the ClinOps AI ecosystem.

## `src.core`

### `LLMClient`
A singleton class that manages the connection to Azure OpenAI.
- **`llm`**: Property that returns a `langchain_openai.AzureChatOpenAI` instance.

### `Settings`
Pydantic model for configuration.
- Fields: `azure_openai_api_key`, `azure_openai_endpoint`, `azure_openai_deployment_name`, `api_version`.

## `src.agents`

### `BaseAgent(ABC)`
The foundation for all intelligent agents.
- **`__init__(name, system_prompt)`**: Initializes the agent with a name and identity.
- **`get_completion(user_request, history)`**: Sends a request to the LLM and returns the response.
- **`process(state)`**: Abstract method to be implemented by experts to handle state updates.

### `QuestionCategorizerAgent`
Extends `BaseAgent`.
- **`process(state)`**: Updates `state["next_agent"]` based on the user query.

### `Clinical Experts`
Multiple classes (e.g., `BiomedicalConceptAgent`, `USDMJSONBuilderAgent`) that extend `BaseAgent`.
- Each implements `process(state)` to update `state["final_response"]`.

## `src.orchestration`

### `AgentState`
A `TypedDict` used by LangGraph.
- Keys: `user_query`, `next_agent`, `history`, `final_response`, and various expert outputs (`biomedical_output`, etc.).

### `create_workflow()`
Function that compiles the LangGraph state machine.
- Returns a `CompiledGraph` object.

## `src.ui`

### `header()`, `sidebar()`, `footer()`
Streamlit UI components for consistent layout and styling.
- Defined in `src.ui.components`.
