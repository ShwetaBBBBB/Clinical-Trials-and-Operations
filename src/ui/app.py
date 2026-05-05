import streamlit as st
import sys
import os
from dotenv import load_dotenv

load_dotenv()

# Add the project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from src.ui.components import header, sidebar, footer
from src.orchestration.workflow import create_workflow
from src.core.logger import logger

def main():
    header()
    sidebar()

    # Main interaction area
    st.markdown("### 👋 Welcome to ClinOps Intelligence")
    st.write("Orchestrate complex clinical operations with a specialized multi-agent swarm.")

    # Initialize workflow
    try:
        app = create_workflow()
    except Exception as e:
        st.error(f"Failed to initialize workflow: {e}")
        return

    # User Input with improved styling
    with st.container():
        query = st.text_area("What clinical operations task can I assist with today?", 
                             placeholder="e.g., Extract biomedical concepts from this synopsis: ...",
                             height=150)

    if st.button("🚀 Execute Orchestration"):
        if query:
            with st.status("🧠 Orchestrating specialized agents...", expanded=True) as status:
                try:
                    # Initial state
                    initial_state = {
                        "user_query": query,
                        "history": []
                    }
                    
                    # Run workflow
                    st.write("🔍 Categorizing request...")
                    result = app.invoke(initial_state)
                    
                    status.update(label="✅ Orchestration Complete!", state="complete", expanded=False)
                    
                    # Display Result
                    st.markdown("---")
                    
                    col1, col2 = st.columns([1, 2])
                    
                    with col1:
                        st.markdown("#### 🤖 Routing Intelligence")
                        st.markdown(f"""
                        <div class='agent-card'>
                            <p style='margin-bottom: 5px; font-size: 0.9em; color: #94a3b8;'>TARGET AGENT</p>
                            <h3 style='margin-top: 0; color: #818cf8;'>{result.get('next_agent', 'N/A').replace('_', ' ').title()}</h3>
                            <p style='font-size: 0.8em;'>Feedback: {result.get('router_feedback', 'No feedback available.')}</p>
                        </div>
                        """, unsafe_allow_html=True)
                    
                    with col2:
                        st.markdown("#### 📄 Expert Response")
                        response_container = st.container()
                        with response_container:
                            st.markdown(result.get("final_response", "No response generated."))
                        
                except Exception as e:
                    status.update(label="❌ Error occurred", state="error")
                    st.error(f"An error occurred during orchestration: {e}")
                    logger.error(f"UI Error: {e}")
        else:
            st.warning("Please enter a query to begin.")

    footer()

if __name__ == "__main__":
    main()
