"""
Pedagogical content and cognitive framework definitions for the Assessment Staircase.
Scaffolded across 4 increasing levels of Bloom's Revised Taxonomy.
"""

LEVELS_CONFIG = [
    {
        "id": 1,
        "name": "FOUNDATION — Explain",
        "short_name": "Foundation",
        "action_tag": "Explain & Define",
        "cognitive_domain": "Remember & Understand",
        "icon": "1️⃣",
        "color": "#3b82f6",
        "tag_bg": "#dbeafe",
        "tag_color": "#1d4ed8",
        "description": "Establish conceptual baseline. Retrieval of facts, defining terminology, clarifying core mechanisms, and explaining 'how' or 'why' something works.",
        "guiding_question": "What fundamental concept, definition, or mechanism must a learner master before moving to practical use?",
        "verbs": ["Define", "Describe", "Explain", "Identify", "Summarize", "Outline", "Classify", "Clarify"],
        "example_prompt": "Explain the difference between supervised and unsupervised learning, providing one distinct real-world characteristic of each.",
        "evidence_hint": "Clear, accurate conceptual definition using domain terminology without confusing terms."
    },
    {
        "id": 2,
        "name": "APPLICATION — Apply",
        "short_name": "Application",
        "action_tag": "Apply & Implement",
        "cognitive_domain": "Apply",
        "icon": "2️⃣",
        "color": "#0ea5e9",
        "tag_bg": "#e0f2fe",
        "tag_color": "#0369a1",
        "description": "Execute or implement knowledge in a concrete, unfamiliar context. Using learned formulas, procedures, or algorithms to produce a specific outcome.",
        "guiding_question": "How can students apply this concept or method to solve a realistic problem or dataset they haven't seen in the lecture?",
        "verbs": ["Implement", "Calculate", "Execute", "Apply", "Demonstrate", "Solve", "Construct", "Operate"],
        "example_prompt": "Given a customer churn dataset with missing values, write a script to impute missing entries and calculate the mean churn rate by demographic group.",
        "evidence_hint": "Correct execution of method, accurate numerical/code results, and proper handling of edge conditions."
    },
    {
        "id": 3,
        "name": "ANALYSIS — Analyse",
        "short_name": "Analysis",
        "action_tag": "Analyse & Diagnose",
        "cognitive_domain": "Analyze",
        "icon": "3️⃣",
        "color": "#8b5cf6",
        "tag_bg": "#ede9fe",
        "tag_color": "#6d28d9",
        "description": "Break down information into constituent parts. Identify underlying relationships, diagnose failure modes, inspect anomalies, and dissect cause-and-effect.",
        "guiding_question": "What scenario forces students to investigate *why* a system failed, compare competing elements, or uncover hidden trade-offs?",
        "verbs": ["Analyse", "Diagnose", "Compare", "Dissect", "Differentiate", "Deconstruct", "Investigate", "Trace"],
        "example_prompt": "Examine the classification report and confusion matrix of Model A vs Model B. Dissect why Model A achieves 95% accuracy but suffers from severe false negatives in minority classes.",
        "evidence_hint": "Systematic breakdown of evidence, logical attribution of causes, and identification of data bias or structural anomalies."
    },
    {
        "id": 4,
        "name": "EVALUATION / CREATION — Evaluate / Create",
        "short_name": "Evaluation / Creation",
        "action_tag": "Evaluate & Synthesize",
        "cognitive_domain": "Evaluate & Create",
        "icon": "4️⃣",
        "color": "#10b981",
        "tag_bg": "#d1fae5",
        "tag_color": "#047857",
        "description": "Peak cognitive demand. Make and defend critical judgments against explicit standards, or synthesize diverse principles to design an original solution or framework.",
        "guiding_question": "How can students make an evidence-based judgment or invent/synthesize a novel solution to a complex, open-ended challenge?",
        "verbs": ["Evaluate", "Justify", "Critique", "Synthesize", "Design", "Formulate", "Recommend", "Architect"],
        "example_prompt": "Critique three architectural proposals for a high-concurrency healthcare data pipeline. Justify your chosen architecture against HIPAA compliance, latency, and cost, then design an end-to-end fallback strategy.",
        "evidence_hint": "Rigorous multi-criteria justification, defense of trade-offs, and cohesive, original solution design."
    }
]

EXAMPLE_DISCIPLINES = {
    "Data Science & AI": {
        "topic": "Supervised Machine Learning & Model Generalization",
        "levels": [
            "Explain what overfitting means, how variance and bias interact, and why cross-validation mitigates optimistic performance estimation.",
            "Using scikit-learn on a housing price dataset, implement Ridge and Lasso regression, tuning the regularization alpha via 5-fold cross-validation.",
            "Analyse the residual plots and learning curves of your regularized models. Identify heteroscedasticity and determine which features dominate the prediction error.",
            "Compare the predictive accuracy, explainability, and computational latency of Lasso vs Random Forest for loan default assessment. Justify the deployed model under regulatory audit constraints and design a continuous drift-monitoring protocol."
        ]
    },
    "Business Management": {
        "topic": "Supply Chain Resilience & Risk Hedging",
        "levels": [
            "Explain the bullwhip effect in multi-tier supply chains and define the key drivers of demand distortion.",
            "Apply safety stock and reorder point formulas to calculate optimal inventory levels for a retail distributor facing seasonal volatility.",
            "Analyse vendor lead-time variance across domestic vs overseas suppliers to identify critical failure bottlenecks in a just-in-time assembly line.",
            "Evaluate dual-sourcing vs single-supplier cost structures under geopolitical disruption scenarios. Justify your risk mitigation strategy to executive stakeholders."
        ]
    },
    "Computer Science & Software": {
        "topic": "RESTful API Architecture & Authentication",
        "levels": [
            "Explain the six architectural constraints of REST and clarify the statelessness principle in HTTP interactions.",
            "Implement a secure token-based authentication middleware in Python/FastAPI using JSON Web Tokens (JWT) with token expiration checks.",
            "Inspect network traces and thread-pool metrics to diagnose why an authentication service experiences cascading 504 timeouts under sudden traffic spikes.",
            "Evaluate OAuth 2.0 with PKCE against mTLS for microservices authentication in a banking ecosystem. Justify the trade-offs and architect a zero-trust gateway."
        ]
    }
}
