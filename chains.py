from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI

# -------------------------------
# Rewrite Agent Prompt
# -------------------------------
rewrite_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are a professional resume writing assistant.
Rewrite resume bullets to be concise, impactful, and ATS-friendly.
- Use strong action verbs
- Keep to one line
- Maintain professional tone
- Revise based on feedback if provided
- Do not explain changes
"""
        ),
        MessagesPlaceholder(variable_name="messages"),
    ]
)

# -------------------------------
# Recruiter Critic Prompt (short & token-efficient)
# -------------------------------
recruiter_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are a senior recruiter reviewing resume bullets.
Provide concise, actionable feedback on:
- Clarity
- Impact
- Action verbs
- Metrics
- ATS-friendliness
Do not rewrite the bullet.
"""
        ),
        MessagesPlaceholder(variable_name="messages"),
    ]
)

# -------------------------------
# LLM Instance
# -------------------------------
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

# -------------------------------
# Chains
# -------------------------------
rewrite_chain = rewrite_prompt | llm
recruiter_chain = recruiter_prompt | llm
