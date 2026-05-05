# 🧬 ClinOps AI: Advanced Clinical Trial Orchestration

[![Python](https://img.shields.io/badge/Python-3.12%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![LangChain](https://img.shields.io/badge/Orchestration-LangGraph-orange)](https://github.com/langchain-ai/langgraph)
[![Azure](https://img.shields.io/badge/Cloud-Azure%20AI%20Foundry-0078D4?logo=microsoft-azure&logoColor=white)](https://azure.microsoft.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**ClinOps AI** is a state-of-the-art multi-agent ecosystem designed to automate and optimize complex clinical trial operations. By leveraging **Azure AI Foundry** and **LangGraph**, it orchestrates a swarm of specialized agents to handle everything from biomedical concept extraction to USDM-compliant protocol generation.

---

## 🌟 Vision
Clinical trials are plagued by manual data entry, complex regulatory requirements, and fragmented information. **ClinOps AI** bridges this gap by providing an intelligent orchestration layer that connects expert agents to natural language queries, delivering structured, actionable insights in seconds.

---

## 🏗 Project Architecture

```text
Updated_clinops/
├── src/
│   ├── agents/         # 🧠 Intelligent Swarm (BaseAgent, Experts, Router)
│   ├── core/           # ⚙️ Core Services (Config, LLM Client, Logger)
│   ├── orchestration/  # 🕸️ LangGraph Workflow & State Management
│   ├── ui/             # 🎨 Premium Streamlit Interface
│   └── utils/          # 🛠️ Helper Utilities
├── tests/              # 🧪 Robust Unit & Integration Tests
├── docs/               # 📄 Detailed Documentation
├── .env.example        # 🔐 Environment Configuration Template
├── pyproject.toml      # 📦 Modern Dependency Management (uv)
└── main.py             # 🚀 Application Entry Point
```

For a deep dive into the system design, see [docs/ARCHITECTURE.md](docs/architecture.md).

---

## 🤖 The Multi-Agent Swarm

Our system utilizes a **Hierarchical Router Pattern** to ensure every query reaches the right expert:

| Agent | Expertise |
| :--- | :--- |
| **Router** | Intelligent classification and workload distribution. |
| **Biomedical** | NER and concept mapping (SNOMED, MedDRA). |
| **CTG Intelligence** | ClinicalTrials.gov data mining and benchmarking. |
| **Protocol Designer** | ICH M11-compliant document generation. |
| **USDM Builder** | Structured JSON modeling for clinical data. |
| **Semantic Mapper** | Cross-ontology relationship mapping. |
| **Risk Assessment** | Operational and regulatory risk identification. |

---

## 🚀 Getting Started

### 1. Prerequisites
- [uv](https://github.com/astral-sh/uv) installed (recommended for 10x faster installs).
- Azure OpenAI Service access.

### 2. Installation
```bash
# Clone the repository
git clone https://github.com/your-username/clinops-ai.git
cd clinops-ai

# Install dependencies
uv sync
```

### 3. Configuration
Copy the template and add your credentials:
```bash
cp .env.example .env
```
Edit `.env` with your Azure endpoint, API key, and deployment names.

### 4. Running the App
```bash
# Launch the Streamlit interface
uv run streamlit run src/ui/app.py
```

---

## 🧪 Quality Assurance
We maintain a high bar for code quality. Run the test suite:
```bash
uv run pytest
```

---

## 🛠 Built With
- **Framework**: [LangChain](https://langchain.com) & [LangGraph](https://github.com/langchain-ai/langgraph)
- **LLM**: Azure OpenAI (GPT-4o)
- **Frontend**: [Streamlit](https://streamlit.io)
- **Dependency Manager**: [uv](https://github.com/astral-sh/uv)
- **Configuration**: [Pydantic Settings](https://docs.pydantic.dev/)

---

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
<p align="center">Built with ❤️ for Clinical Operations Excellence</p>
