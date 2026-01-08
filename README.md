# 💼 Resume Bullet Point Improver

## Overview
The **Resume Bullet Point Improver** is an AI-powered tool that enhances weak or vague resume bullet points using a **self-reflection loop**.  

It uses **LangChain** and **LangGraph** to simulate a conversation between two agents:  

1. **Rewrite Agent** – rewrites bullets concisely and professionally.  
2. **Recruiter Critic** – provides short, actionable feedback to refine the bullet.  

The feedback loops back to the Rewrite Agent, resulting in polished, professional resume bullets.  

---

## Features
- **Iterative self-improvement:** Rewrite → Critique → Rewrite  
- **Token-efficient prompts** to save API usage  
- **Clean final output** of resume bullets  
- **Streamlit UI** for easy interaction  
- **Iteration trace** to visualize the AI’s thought process  

---

## Technologies
- **Python 3.10+**  
- **LangChain-Core**  
- **LangGraph**  
- **OpenAI GPT-4o-mini**  
- **Streamlit**  

---

## Installation & Setup

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/resume_bullet_improver.git
cd resume_bullet_improver
# resume_bullet_improver

2. ****

## Usage

1. Enter a weak or vague resume bullet in the text area.  
2. Click **Improve Bullet**.  
3. The app will display:
   - **Iteration Trace:** Shows each rewrite and recruiter feedback  
   - **Final Improved Bullet:** The polished, professional output  

---

## Example Run

**Input:**

