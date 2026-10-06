"""
Cognitive Depth & Rigour Progression Engine for Assessment Staircase.
Analyzes authored tasks and evidence across Bloom's 4 tiers to provide
supportive, qualitative workshop-style feedback.
"""

import re

# Bloom's domain lexicon for heuristic cognitive demand checking
COGNITIVE_LEXICON = {
    1: {
        "domain": "Foundation (Explain)",
        "verbs": ["define", "describe", "explain", "identify", "summarize", "outline", "classify", "clarify", "state", "list", "recall", "distinguish"],
        "signals": ["what is", "meaning of", "definition", "concept", "principle", "overview", "mechanism"]
    },
    2: {
        "domain": "Application (Apply)",
        "verbs": ["apply", "implement", "calculate", "execute", "solve", "demonstrate", "construct", "operate", "compute", "use", "perform", "translate"],
        "signals": ["given a", "dataset", "scenario", "write code", "calculate", "run", "produce", "table", "result"]
    },
    3: {
        "domain": "Analysis (Analyse)",
        "verbs": ["analyse", "analyze", "diagnose", "compare", "dissect", "differentiate", "deconstruct", "investigate", "trace", "inspect", "audit", "distinguish"],
        "signals": ["why", "cause", "relationship", "difference between", "bottleneck", "anomaly", "failure", "trade-off", "correlation", "discrepancy"]
    },
    4: {
        "domain": "Evaluation / Creation (Evaluate / Create)",
        "verbs": ["evaluate", "justify", "critique", "synthesize", "design", "formulate", "recommend", "architect", "propose", "judge", "defend", "invent", "prioritize"],
        "signals": ["criteria", "standards", "trade-offs", "novel", "end-to-end", "decision", "justify why", "compliance", "strategy", "framework"]
    }
}

def analyze_staircase_depth(prompts_dict):
    """
    Performs a supportive qualitative depth check across the 4 levels.
    Returns:
        dict: {
            "status": "Strong Progression" | "Progression Developing" | "Revisit Cognitive Ascent",
            "status_badge": "🟢" | "🟡" | "🔵",
            "summary": str,
            "level_feedback": dict,
            "cognitive_jump_review": str,
            "evidence_quality": str
        }
    """
    level_scores = {}
    detected_verbs = {}
    
    for lvl in range(1, 5):
        task_text = prompts_dict.get(lvl, {}).get("prompt", "").lower()
        evidence_text = prompts_dict.get(lvl, {}).get("evidence", "").lower()
        
        target_lex = COGNITIVE_LEXICON[lvl]
        found_target_verbs = [v for v in target_lex["verbs"] if re.search(r'\b' + re.escape(v) + r'\b', task_text)]
        found_signals = [s for s in target_lex["signals"] if s in task_text]
        
        detected_verbs[lvl] = found_target_verbs
        
        # Word counts & depth signals
        word_count = len(task_text.split())
        evidence_word_count = len(evidence_text.split())
        
        level_scores[lvl] = {
            "has_target_verbs": len(found_target_verbs) > 0,
            "found_verbs": found_target_verbs,
            "word_count": word_count,
            "evidence_complete": evidence_word_count >= 5
        }

    # Analyze trajectory
    target_matches = sum(1 for lvl in range(1, 5) if level_scores[lvl]["has_target_verbs"])
    all_evidence_filled = all(level_scores[lvl]["evidence_complete"] for lvl in range(1, 5))
    
    # Assess cognitive transformation
    l1_text = prompts_dict.get(1, {}).get("prompt", "").lower()
    l4_text = prompts_dict.get(4, {}).get("prompt", "").lower()
    
    has_l1_to_l4_jump = (l1_text != l4_text) and (len(l4_text) > 15)
    
    if target_matches >= 3 and all_evidence_filled and has_l1_to_l4_jump:
        status = "Strong Scaffolding Progression"
        status_badge = "🟢"
        color = "#16a34a"
        summary = (
            "Excellent cognitive ascent. Your tasks clearly scale from foundational concept retrieval to high-demand "
            "evaluation and synthesis, avoiding cognitive cliff-jumps."
        )
    elif target_matches >= 2 or has_l1_to_l4_jump:
        status = "Progression Developing"
        status_badge = "🟡"
        color = "#d97706"
        summary = (
            "Good developmental scaffolding. The tasks show increasing expectations, though some intermediate tiers "
            "could use sharper action verbs (e.g. ensure Level 3 asks students to diagnose *why* rather than simply apply)."
        )
    else:
        status = "Cognitive Ascent Needs Sharpening"
        status_badge = "🔵"
        color = "#2563eb"
        summary = (
            "Your staircase establishes the topic, but the cognitive jump between levels can be made steeper. "
            "Consider pushing Level 4 toward multi-criteria justification or novel framework creation."
        )

    # Detailed per-level feedback
    feedback = {}
    for lvl in range(1, 5):
        meta = COGNITIVE_LEXICON[lvl]
        verbs = detected_verbs[lvl]
        verb_str = ", ".join(f"'{v}'" for v in verbs) if verbs else "Implicit action"
        feedback[lvl] = {
            "name": meta["domain"],
            "verbs_identified": verb_str,
            "evidence_status": "Concrete evidence defined" if level_scores[lvl]["evidence_complete"] else "Evidence needs more specificity",
            "tip": (
                f"Well-anchored {meta['domain']} demand." if verbs else
                f"Tip: Try explicitly leading with an action verb such as {', '.join(meta['verbs'][:3])}."
            )
        }

    return {
        "status": status,
        "status_badge": status_badge,
        "color": color,
        "summary": summary,
        "level_feedback": feedback,
        "target_matches": target_matches,
        "evidence_complete": all_evidence_filled
    }
