# 🪜 Assessment Staircase — Interactive Faculty Workshop Activity

An interactive web application developed with **Streamlit** and **Python** to enable faculty participants to progressively design, scaffold, and review assessment tasks across four tiers of increasing cognitive complexity.

---

## 🌟 Key Features

1. **Step-by-Step Cognitive Ladder**:
   - **Step 1: FOUNDATION — Explain** (Recall, define, clarify mechanisms)
   - **Step 2: APPLICATION — Apply** (Apply procedures to novel scenarios or datasets)
   - **Step 3: ANALYSIS — Analyse** (Dissect failure modes, examine relationships, diagnose causes)
   - **Step 4: EVALUATION & CREATION — Evaluate / Create** (Critique, justify trade-offs, design novel solutions)

2. **Visual Fidelity & Modern Aesthetics**:
   - Gradient palette (`linear-gradient(135deg, #eef2ff, #f8fafc)`)
   - Rounded floating cards with refined shadows (`border-radius: 18px`, soft depth)
   - Dynamic staircase & ladder visualizer reflecting active, completed, and pending states
   - Ascending architectural staircase graphic rendering participant's authored questions

3. **Faculty Authoring Tools**:
   - Click-to-insert action verbs based on Bloom's Revised Taxonomy
   - Pre-filled disciplinary exemplars (Data Science, Management, Computer Science)
   - Delivery format selectors (Conceptual Short Answer, Applied Computation, Diagnostic Case, Synthesis Project)
   - Expected Evidence criteria helper

4. **Showcase & Export**:
   - Comprehensive summary showcase
   - One-click **Markdown (.md) Download**
   - In-app revision flow and clean session restart

---

## 🚀 How to Run Locally

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Launch the Application
```bash
streamlit run app.py
```

The application will launch automatically in your default browser at `http://localhost:8501`.
