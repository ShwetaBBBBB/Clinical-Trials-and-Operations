import streamlit as st

def header():
    st.set_page_config(
        page_title="ClinOps AI",
        page_icon="🧬",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600&display=swap');
        
        html, body, [class*="css"] {
            font-family: 'Outfit', sans-serif;
        }
        
        .stApp {
            background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 100%);
            color: #f8fafc;
        }
        
        .stButton>button {
            background: linear-gradient(90deg, #6366f1 0%, #a855f7 100%);
            color: white;
            border: none;
            padding: 10px 20px;
            font-weight: 600;
            transition: all 0.3s ease;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        }
        
        .stButton>button:hover {
            transform: translateY(-2px);
            box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.2);
            opacity: 0.9;
        }
        
        .agent-card {
            background: rgba(30, 41, 59, 0.7);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.1);
            padding: 15px;
            border-radius: 12px;
            margin-bottom: 10px;
        }
        
        h1, h2, h3 {
            color: #818cf8 !important;
        }
        
        .stTextInput>div>div>input {
            background-color: #1e293b !important;
            color: white !important;
        }
        </style>
    """, unsafe_allow_html=True)
    
    st.title("🧬 ClinOps AI")
    st.subheader("Advanced Clinical Trial Orchestration Platform")
    st.markdown("---")

def sidebar():
    with st.sidebar:
        st.image("https://img.icons8.com/fluency/96/artificial-intelligence.png", width=80)
        st.header("Control Center")
        st.info("System connected to Azure AI Foundry.")
        
        st.divider()
        st.header("🧬 Agent Swarm Status")
        agents = [
            "Question Categorizer",
            "Biomedical Expert",
            "CTG Intelligence",
            "Protocol Designer",
            "USDM Builder",
            "Semantic Mapper",
            "Risk Assessment"
        ]
        for agent in agents:
            st.markdown(f"🟢 **{agent}** is active")

def footer():
    st.divider()
    st.markdown(
        "<div style='text-align: center; color: #94a3b8; font-size: 0.8em;'>"
        "Powered by Azure AI Foundry & LangGraph • Built for Precision Clinical Operations"
        "</div>", 
        unsafe_allow_html=True
    )
