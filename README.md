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
```

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Add your OpenAI API key**
- Copy .env.example to .env
- Add your API key:

```bash
OPENAI_API_KEY=your_openai_api_key_here
```
4.**Run the Streamlit app**

```bash
streamlit run app.py
```
---
## Usage

1. **Enter a resume bullet:**  
   - Open the Streamlit app in your browser.  
   - Enter a weak, vague, or rough resume bullet in the text area.  

2. **Click "Improve Bullet":**  
   - The AI agents will process the input.  
   - The **Rewrite Agent** rewrites the bullet concisely and professionally.  
   - The **Recruiter Critic** provides short feedback on clarity, impact, and metrics.  
   - Feedback loops back to the Rewrite Agent for refinement.

3. **View the output:**  
   - **Iteration Trace:** Shows each rewrite and recruiter feedback step-by-step.  
   - **Final Improved Bullet:** Displays the polished, professional resume bullet.

---

### Example Run

**Input:**

```bash
Worked on a React project
```

**Iteration Trace::**

```bash
[Rewrite] Developed a React-based web application.
[Feedback/Input] Add action verbs and measurable impact.
[Rewrite] Developed a React-based web application, improving UI responsiveness and maintainability.
```

**Final Improved Bullet:**

```bash
Developed a React-based web application, improving UI responsiveness and maintainability.
```
---

## Sample Inputs to Try
- **“Built a machine learning model”**  
- **“Led a team for a college fest”**  
- **“Made a robot that dances”**  
- **“Worked on database project”**  
- **“Did something with AI”**

---

## Notes / Tips

- Use concise bullets for best results.  
- Feedback loop typically runs 1–2 iterations; adjust in `app.py` if needed.  
- Optimized recruiter prompt keeps token usage low.  
- Can extend to handle multiple bullets at once (future improvement).  
- Streamlit UI allows interactive testing and quick demo.

---

## Project Structure

```bash
resume_bullet_improver/
├── app.py                 # Streamlit UI + LangGraph agent
├── chains.py              # Rewrite + Recruiter chains
├── .env.example           # Example API key file
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```

### Description of files

- **app.py** – Main Streamlit app that handles user input, runs the LangGraph agent loop, and displays the output.  
- **chains.py** – Defines the Rewrite Agent and Recruiter Critic prompts and chains.  
- **.env.example** – Template for environment variables; contains placeholder for `OPENAI_API_KEY`.  
- **requirements.txt** – Lists all Python dependencies required to run the project.  
- **README.md** – Project documentation, usage instructions, and examples.
---

## Author

This project was created by **MR. MOHIT MURARKA**.  

- **GitHub:** [https://github.com/MohitMurarka](https://github.com/MohitMurarka)
- **LinkedIn:** [https://www.linkedin.com/in/Mohit-Murarka](https://www.linkedin.com/in/mohit-murarka-b165882aa/)  

Feel free to reach out for collaboration, feedback, or project inquiries.
