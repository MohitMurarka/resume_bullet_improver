import streamlit as st
from dotenv import load_dotenv
import os

# -------------------------------
# Load environment
# -------------------------------
load_dotenv(dotenv_path=".env", override=True)

from langchain_core.messages import AIMessage, HumanMessage
from langgraph.graph import END, MessageGraph
from chains import rewrite_chain, recruiter_chain

# -------------------------------
# Graph setup
# -------------------------------
REWRITE = "rewrite"
RECRUIT = "recruiter"

graph = MessageGraph()

def rewrite_node(state):
    return rewrite_chain.invoke({"messages": state})

def recruiter_node(state):
    response = recruiter_chain.invoke({"messages": state})
    return [HumanMessage(content=response.content)]

graph.add_node(REWRITE, rewrite_node)
graph.add_node(RECRUIT, recruiter_node)
graph.set_entry_point(REWRITE)

def should_continue(state):
    if len(state) >= 5:  # 1 input + 2 loops max
        return END
    return RECRUIT

graph.add_conditional_edges(REWRITE, should_continue)
graph.add_edge(RECRUIT, REWRITE)

app_graph = graph.compile()

# -------------------------------
# Helpers
# -------------------------------
def get_final_bullet(state):
    for msg in reversed(state):
        if isinstance(msg, AIMessage):
            return msg.content
    return None

# -------------------------------
# Streamlit UI
# -------------------------------
st.set_page_config(page_title="Resume Bullet Improver", page_icon="💼")
st.title("💼 Resume Bullet Point Improver")
st.write("Enter a weak or vague resume bullet, and see how AI improves it!")

user_input = st.text_area("Enter your bullet:", "", height=100)

if st.button("Improve Bullet"):
    if not user_input.strip():
        st.warning("Please enter a resume bullet point.")
    else:
        response = app_graph.invoke(HumanMessage(content=user_input))
        
        # Iteration trace
        st.subheader("🔄 Iteration Trace:")
        for msg in response:
            if isinstance(msg, HumanMessage):
                st.markdown(f"**[Feedback/Input]** {msg.content}")
            elif isinstance(msg, AIMessage):
                st.markdown(f"**[Rewrite]** {msg.content}")
        
        # Final bullet
        final_bullet = get_final_bullet(response)
        st.subheader("✅ Final Improved Bullet:")
        st.success(final_bullet)
