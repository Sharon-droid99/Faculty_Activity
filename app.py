"""
Assessment Staircase — Interactive Faculty Workshop Activity
Comprehensive refactored application integrating progressive authoring,
depth & rigour progression analysis, 3-part reflection, and multi-format exports.
"""

import streamlit as st
import datetime
import io
import csv
from content import LEVELS_CONFIG, EXAMPLE_DISCIPLINES
from styles import CUSTOM_CSS, render_ladder_nav, render_staircase_graphic
from depth_engine import analyze_staircase_depth

# Configure Streamlit page
st.set_page_config(
    page_title="Assessment Staircase | Faculty Workshop",
    page_icon="🪜",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Inject custom CSS cleanly via st.html
st.html(CUSTOM_CSS)

# ---------------------------------------------------------
# State Management Initialization
# ---------------------------------------------------------
if "current_screen" not in st.session_state:
    st.session_state.current_screen = "welcome"  # 'welcome', 'level_1', 'level_2', 'level_3', 'level_4', 'showcase'

if "faculty_name" not in st.session_state:
    st.session_state.faculty_name = ""

if "course_name" not in st.session_state:
    st.session_state.course_name = ""

if "department" not in st.session_state:
    st.session_state.department = ""

if "topic" not in st.session_state:
    st.session_state.topic = ""

if "prompts" not in st.session_state:
    st.session_state.prompts = {
        1: {"prompt": "", "evidence": "", "format": "Conceptual Short Answer"},
        2: {"prompt": "", "evidence": "", "format": "Applied Problem / Computation"},
        3: {"prompt": "", "evidence": "", "format": "Diagnostic / Analytical Case"},
        4: {"prompt": "", "evidence": "", "format": "Synthesis / Multi-criteria Critique"}
    }

# 3-part structured reflection
if "reflection_before" not in st.session_state:
    st.session_state.reflection_before = ""

if "reflection_after" not in st.session_state:
    st.session_state.reflection_after = ""

if "reflection_why" not in st.session_state:
    st.session_state.reflection_why = ""

if "depth_analysis" not in st.session_state:
    st.session_state.depth_analysis = None

if "validation_errors" not in st.session_state:
    st.session_state.validation_errors = []


# ---------------------------------------------------------
# Navigation & Helper Functions
# ---------------------------------------------------------
def go_to_screen(screen_name):
    st.session_state.validation_errors = []
    st.session_state.current_screen = screen_name
    st.rerun()

def load_example(discipline_name):
    """Pre-fills form with a discipline exemplar so faculty can observe the pattern."""
    ex = EXAMPLE_DISCIPLINES.get(discipline_name)
    if ex:
        st.session_state.topic = ex["topic"]
        for idx, lvl_text in enumerate(ex["levels"], 1):
            st.session_state.prompts[idx]["prompt"] = lvl_text
            st.session_state.prompts[idx]["evidence"] = f"Demonstrates clear mastery at {LEVELS_CONFIG[idx-1]['short_name']} level."
        
        # Populate pre-filled reflection
        st.session_state.reflection_before = "Initial assessment asked students to define terminology and recall equations without applying them."
        st.session_state.reflection_after = "Final assessment requires evaluating multi-model trade-offs under regulatory constraints and designing a fallback protocol."
        st.session_state.reflection_why = "Shifted cognitive demand from passive factual recall to contextual reasoning, diagnostic dissection, and defensible synthesis."

def validate_all_levels():
    """Validates that all required fields across all 4 levels are complete."""
    errors = []
    if not st.session_state.topic.strip():
        errors.append(("Topic is missing", "welcome"))

    for idx in range(1, 5):
        lvl_meta = LEVELS_CONFIG[idx - 1]
        task_txt = st.session_state.prompts[idx].get("prompt", "").strip()
        evidence_txt = st.session_state.prompts[idx].get("evidence", "").strip()
        
        if not task_txt:
            errors.append((f"Level {idx} ({lvl_meta['short_name']}) Task is missing", f"level_{idx}"))
        if not evidence_txt:
            errors.append((f"Level {idx} ({lvl_meta['short_name']}) Evidence of Learning is missing", f"level_{idx}"))
            
    return errors

def build_my_staircase():
    """Triggers staircase construction with complete validation and depth check."""
    errs = validate_all_levels()
    if errs:
        st.session_state.validation_errors = errs
        st.rerun()
    else:
        st.session_state.validation_errors = []
        # Run cognitive depth analysis engine
        st.session_state.depth_analysis = analyze_staircase_depth(st.session_state.prompts)
        go_to_screen("showcase")

def reset_activity():
    st.session_state.current_screen = "welcome"
    st.session_state.faculty_name = ""
    st.session_state.course_name = ""
    st.session_state.department = ""
    st.session_state.topic = ""
    st.session_state.prompts = {
        1: {"prompt": "", "evidence": "", "format": "Conceptual Short Answer"},
        2: {"prompt": "", "evidence": "", "format": "Applied Problem / Computation"},
        3: {"prompt": "", "evidence": "", "format": "Diagnostic / Analytical Case"},
        4: {"prompt": "", "evidence": "", "format": "Synthesis / Multi-criteria Critique"}
    }
    st.session_state.reflection_before = ""
    st.session_state.reflection_after = ""
    st.session_state.reflection_why = ""
    st.session_state.depth_analysis = None
    st.session_state.validation_errors = []
    st.rerun()


# ---------------------------------------------------------
# Header Component
# ---------------------------------------------------------
def render_header(title="🪜 Climb the Assessment Staircase", subtitle="Progressively scaffold cognitive rigour from foundation to evaluation and creation"):
    st.html(f"""
    <div class="header-card">
        <span class="workshop-badge">Faculty Development Activity</span>
        <h1>{title}</h1>
        <p>{subtitle}</p>
    </div>
    """)


# ---------------------------------------------------------
# Screen 0: Welcome, Orientation & Topic Setup
# ---------------------------------------------------------
def render_welcome_screen():
    render_header()

    col1, col2 = st.columns([1.1, 0.9], gap="large")

    with col1:
        st.html("""
        <div class="staircase-card">
            <h3 style="margin-top:0; font-size:20px; color:#0f172a;">🎯 The Staircase Methodology</h3>
            <p style="color:#475569; font-size:15px; line-height:1.6;">
                Most assessments cluster around lower-order recall or jump abruptly to complex evaluation without foundational scaffolding. 
                The <strong>Assessment Staircase</strong> guides you to design a continuous pedagogical progression around <strong>one central topic</strong> across four cognitive tiers:
            </p>
            <div style="margin:16px 0;">
                <div style="padding:10px 14px; background:#eff6ff; border-radius:10px; margin-bottom:8px; border-left:4px solid #3b82f6;">
                    <strong>Step 1 — Foundation:</strong> Explain fundamental definitions, principles, and mechanisms.
                </div>
                <div style="padding:10px 14px; background:#f0f9ff; border-radius:10px; margin-bottom:8px; border-left:4px solid #0ea5e9;">
                    <strong>Step 2 — Application:</strong> Apply methods, formulas, or procedures to novel scenarios.
                </div>
                <div style="padding:10px 14px; background:#faf5ff; border-radius:10px; margin-bottom:8px; border-left:4px solid #8b5cf6;">
                    <strong>Step 3 — Analysis:</strong> Dissect failure modes, examine relationships, and diagnose causes.
                </div>
                <div style="padding:10px 14px; background:#ecfdf5; border-radius:10px; margin-bottom:8px; border-left:4px solid #10b981;">
                    <strong>Step 4 — Evaluation & Creation:</strong> Justify multi-criteria decisions and design original solutions.
                </div>
            </div>
            <p style="font-size:13.5px; color:#64748b; margin-bottom:0;">
                💡 <em>Rule of Thumb:</em> All 4 levels must address the <strong>exact same topic</strong>, demonstrating how cognitive demand climbs.
            </p>
        </div>
        """)

        # Disciplinary exemplar loader
        st.html("""
        <div class="staircase-card">
            <h4 style="margin-top:0; font-size:16px; color:#0f172a;">⚡ Need Inspiration? Load a Workshop Sample</h4>
            <p style="color:#64748b; font-size:13.5px;">Click any exemplar to pre-fill a sample academic topic and scaffolded questions:</p>
        </div>
        """)
        
        btn_cols = st.columns(3)
        for i, (disc_title, disc_data) in enumerate(EXAMPLE_DISCIPLINES.items()):
            with btn_cols[i]:
                if st.button(f"📘 {disc_title}", key=f"ex_{i}", use_container_width=True):
                    load_example(disc_title)
                    st.success(f"Loaded: {disc_data['topic']}")
                    st.rerun()

    with col2:
        st.html("""
        <div class="staircase-card">
            <h3 style="margin-top:0; font-size:20px; color:#0f172a;">👤 Participant & Topic Setup</h3>
            <p style="color:#64748b; font-size:14px; margin-bottom:16px;">
                Specify your academic context and the core subject topic you want to scaffold today.
            </p>
        </div>
        """)

        faculty_name = st.text_input(
            "Faculty Name *",
            value=st.session_state.faculty_name,
            placeholder="e.g. Dr. Priya Sharma",
            help="Your name as it should appear on the assessment report"
        )
        
        c_sub1, c_sub2 = st.columns(2)
        with c_sub1:
            course_name = st.text_input(
                "Course / Subject",
                value=st.session_state.course_name,
                placeholder="e.g. Machine Learning (CS402)"
            )
        with c_sub2:
            department = st.text_input(
                "Department",
                value=st.session_state.department,
                placeholder="e.g. Computer Science"
            )

        topic = st.text_input(
            "Central Topic to Scaffold *",
            value=st.session_state.topic,
            placeholder="e.g. Regularization and Overfitting in Machine Learning",
            help="This single topic will be scaffolded across all 4 cognitive tiers."
        )

        if st.session_state.validation_errors:
            for err_msg, _ in st.session_state.validation_errors:
                st.error(f"⚠️ {err_msg}")

        st.markdown("<div style='height:12px;'></div>", unsafe_allow_html=True)
        if st.button("🚀 Begin Staircase Activity →", type="primary", use_container_width=True):
            if not topic.strip():
                st.session_state.validation_errors = [("Please specify a Central Topic before proceeding.", "welcome")]
                st.rerun()
            else:
                st.session_state.faculty_name = faculty_name.strip()
                st.session_state.course_name = course_name.strip()
                st.session_state.department = department.strip()
                st.session_state.topic = topic.strip()
                st.session_state.validation_errors = []
                go_to_screen("level_1")


# ---------------------------------------------------------
# Screens 1-4: Progressive Level Authoring Studio
# ---------------------------------------------------------
def render_level_authoring_screen(level_id):
    level_meta = LEVELS_CONFIG[level_id - 1]
    
    # Topic Banner
    st.html(f"""
    <div class="header-card" style="padding:16px 20px; margin-bottom:16px; text-align:left;">
        <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:10px;">
            <div>
                <span class="workshop-badge" style="margin-top:0;">Level {level_id} of 4</span>
                <span style="font-size:15px; font-weight:700; color:#1e293b; margin-left:10px;">
                    Topic: <span style="color:#2563eb;">{st.session_state.topic}</span>
                </span>
            </div>
            <div style="font-size:13px; color:#64748b;">
                Faculty: <strong>{st.session_state.faculty_name or 'Participant'}</strong>
            </div>
        </div>
    </div>
    """)

    col_nav, col_work = st.columns([0.85, 1.35], gap="large")

    # Left Column: Ladder Visualizer & Level Context
    with col_nav:
        st.markdown("### 🪜 Staircase Progression")
        ladder_html = render_ladder_nav(current_step=level_id, total_steps=4, steps_data=LEVELS_CONFIG)
        st.html(ladder_html)

        st.html(f"""
        <div class="staircase-card" style="border-left: 5px solid {level_meta['color']};">
            <div style="display:flex; align-items:center; gap:8px; margin-bottom:6px;">
                <span style="font-size:22px;">{level_meta['icon']}</span>
                <h4 style="margin:0; font-size:17px; color:#0f172a;">{level_meta['name']}</h4>
            </div>
            <div style="display:inline-block; padding:3px 10px; background:{level_meta['tag_bg']}; color:{level_meta['tag_color']}; border-radius:12px; font-size:12px; font-weight:700; margin-bottom:10px;">
                Cognitive Target: {level_meta['cognitive_domain']}
            </div>
            <p style="font-size:13.5px; color:#475569; line-height:1.5;">
                {level_meta['description']}
            </p>
            <hr style="border:none; border-top:1px solid #e2e8f0; margin:12px 0;">
            <div style="font-size:12.5px; color:#334155;">
                <strong>🤔 Guiding Question:</strong><br>
                <em>{level_meta['guiding_question']}</em>
            </div>
        </div>
        """)

        with st.expander("💡 View Benchmark Exemplar"):
            st.html(f"""
            <div style="background:#f8fafc; padding:12px; border-radius:10px; border:1px solid #e2e8f0; font-size:13px;">
                <strong>Sample Task:</strong><br>
                {level_meta['example_prompt']}
                <br><br>
                <strong>Expected Evidence:</strong><br>
                <span style="color:#64748b;">{level_meta['evidence_hint']}</span>
            </div>
            """)

    # Right Column: Authoring Studio
    with col_work:
        st.html(f"""
        <div class="staircase-card">
            <h3 style="margin-top:0; font-size:21px; color:#0f172a;">
                ✍️ Author Level {level_id} Assessment Task & Evidence
            </h3>
            <p style="color:#64748b; font-size:14px; margin-bottom:12px;">
                Craft a specific question and the observable evidence of learning for <strong>{level_meta['short_name']}</strong>.
            </p>
        </div>
        """)

        # Verbs Helper Bar
        st.markdown("<div style='font-size:12px; font-weight:700; color:#475569; margin-bottom:6px;'>RECOMMENDED ACTION VERBS (CLICK TO INSERT):</div>", unsafe_allow_html=True)
        verb_cols = st.columns(4)
        for idx, verb in enumerate(level_meta['verbs'][:8]):
            with verb_cols[idx % 4]:
                if st.button(f"+ {verb}", key=f"verb_{level_id}_{verb}", use_container_width=True):
                    current_txt = st.session_state.prompts[level_id]["prompt"]
                    if not current_txt.strip():
                        st.session_state.prompts[level_id]["prompt"] = f"{verb} "
                    else:
                        st.session_state.prompts[level_id]["prompt"] = f"{current_txt} {verb} "
                    st.rerun()

        st.markdown("<div style='height:8px;'></div>", unsafe_allow_html=True)

        prompt_val = st.text_area(
            f"Assessment Task / Question Prompt (Level {level_id}) *",
            value=st.session_state.prompts[level_id]["prompt"],
            height=130,
            placeholder=f"e.g. {level_meta['example_prompt']}",
            help="The actual challenge or problem statement students will answer."
        )
        st.session_state.prompts[level_id]["prompt"] = prompt_val

        col_fmt, col_evi = st.columns([1, 1.4])
        with col_fmt:
            format_options = [
                "Conceptual Short Answer",
                "Applied Problem / Computation",
                "Code / Lab Experiment",
                "Diagnostic / Analytical Case",
                "Comparative Evaluation Essay",
                "Design / Synthesis Project",
                "Multiple Choice with Justification"
            ]
            default_fmt = st.session_state.prompts[level_id].get("format", format_options[0])
            fmt_val = st.selectbox(
                "Assessment Format",
                options=format_options,
                index=format_options.index(default_fmt) if default_fmt in format_options else 0,
                key=f"fmt_select_{level_id}"
            )
            st.session_state.prompts[level_id]["format"] = fmt_val

        with col_evi:
            evidence_val = st.text_area(
                "Evidence of Mastery / Success Criteria *",
                value=st.session_state.prompts[level_id].get("evidence", ""),
                height=90,
                placeholder="e.g. Accurate mathematical derivation and explanation of variance trade-off without confusing with bias.",
                help="What observable student responses prove they mastered this specific level?"
            )
            st.session_state.prompts[level_id]["evidence"] = evidence_val

        # Granular validation callouts
        if st.session_state.validation_errors:
            for err_msg, target_screen in st.session_state.validation_errors:
                if target_screen == f"level_{level_id}":
                    st.error(f"⚠️ {err_msg}")

        # Navigation controls
        nav_prev_col, nav_next_col = st.columns([1, 1.4])
        with nav_prev_col:
            if level_id == 1:
                if st.button("← Back to Setup", use_container_width=True):
                    go_to_screen("welcome")
            else:
                if st.button(f"← Back to Level {level_id - 1}", use_container_width=True):
                    go_to_screen(f"level_{level_id - 1}")

        with nav_next_col:
            is_last = (level_id == 4)
            if is_last:
                if st.button("🏗️ Build My Staircase →", type="primary", use_container_width=True):
                    # Validate current step first
                    if not st.session_state.prompts[4]["prompt"].strip() or not st.session_state.prompts[4]["evidence"].strip():
                        st.session_state.validation_errors = []
                        if not st.session_state.prompts[4]["prompt"].strip():
                            st.session_state.validation_errors.append(("Level 4 Task Prompt is required.", "level_4"))
                        if not st.session_state.prompts[4]["evidence"].strip():
                            st.session_state.validation_errors.append(("Level 4 Evidence of Learning is required.", "level_4"))
                        st.rerun()
                    else:
                        build_my_staircase()
            else:
                next_label = f"Save & Ascend to Level {level_id + 1} →"
                if st.button(next_label, type="primary", use_container_width=True):
                    # Validate step
                    missing = []
                    if not st.session_state.prompts[level_id]["prompt"].strip():
                        missing.append((f"Level {level_id} Task Prompt is required.", f"level_{level_id}"))
                    if not st.session_state.prompts[level_id]["evidence"].strip():
                        missing.append((f"Level {level_id} Evidence of Learning is required.", f"level_{level_id}"))
                    
                    if missing:
                        st.session_state.validation_errors = missing
                        st.rerun()
                    else:
                        st.session_state.validation_errors = []
                        go_to_screen(f"level_{level_id + 1}")


# ---------------------------------------------------------
# Screen 5: Final Showcase & Assessment Staircase Summary
# ---------------------------------------------------------
def render_showcase_screen():
    render_header(
        title="🎉 Completed Assessment Staircase",
        subtitle="Your four-tiered assessment sequence has been constructed and analyzed for cognitive rigour"
    )

    # Participant & Topic Summary Strip
    st.html(f"""
    <div class="staircase-card" style="padding:18px 24px;">
        <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:14px;">
            <div>
                <span class="workshop-badge" style="margin-top:0;">Final Pedagogical Artefact</span>
                <div style="font-size:22px; font-weight:800; color:#0f172a; margin-top:4px;">
                    {st.session_state.topic}
                </div>
            </div>
            <div style="display:flex; gap:20px; font-size:13.5px; color:#475569;">
                <div><strong>Faculty:</strong> {st.session_state.faculty_name or 'Anonymous Participant'}</div>
                <div><strong>Course:</strong> {st.session_state.course_name or 'N/A'}</div>
                <div><strong>Dept:</strong> {st.session_state.department or 'N/A'}</div>
            </div>
        </div>
    </div>
    """)

    # Visual Staircase Graphic
    st.markdown("### 🪜 The Cognitive Staircase Visualisation")
    stair_graphic = render_staircase_graphic(LEVELS_CONFIG, st.session_state.prompts)
    st.html(stair_graphic)

    # ---------------------------------------------------------
    # Cognitive Depth & Rigour Progression Check Results
    # ---------------------------------------------------------
    depth_res = st.session_state.depth_analysis or analyze_staircase_depth(st.session_state.prompts)
    st.session_state.depth_analysis = depth_res

    st.markdown("### 🔍 Cognitive Depth & Rigour Progression Check")
    st.html(f"""
    <div class="depth-feedback-card" style="border-left: 6px solid {depth_res['color']};">
        <div class="depth-header-strip">
            <div style="display:flex; align-items:center; gap:10px;">
                <span class="depth-badge" style="background:#f1f5f9; color:{depth_res['color']};">
                    {depth_res['status_badge']} {depth_res['status']}
                </span>
                <span style="font-size:13.5px; font-weight:600; color:#475569;">
                    Bloom's Tier Alignment: {depth_res['target_matches']} of 4 Tiers Verified
                </span>
            </div>
            <span style="font-size:12px; color:#64748b;">Automated Workshop Diagnostic</span>
        </div>
        <p style="font-size:14.5px; color:#1e293b; margin:0 0 14px 0; line-height:1.5;">
            {depth_res['summary']}
        </p>
        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(220px, 1fr)); gap:12px; margin-top:10px;">
            <div style="background:#f8fafc; padding:12px; border-radius:10px; border:1px solid #e2e8f0; font-size:12.5px;">
                <strong>Level 1 (Foundation):</strong><br>
                Action: {depth_res['level_feedback'][1]['verbs_identified']}<br>
                <span style="color:#64748b;">{depth_res['level_feedback'][1]['tip']}</span>
            </div>
            <div style="background:#f8fafc; padding:12px; border-radius:10px; border:1px solid #e2e8f0; font-size:12.5px;">
                <strong>Level 2 (Application):</strong><br>
                Action: {depth_res['level_feedback'][2]['verbs_identified']}<br>
                <span style="color:#64748b;">{depth_res['level_feedback'][2]['tip']}</span>
            </div>
            <div style="background:#f8fafc; padding:12px; border-radius:10px; border:1px solid #e2e8f0; font-size:12.5px;">
                <strong>Level 3 (Analysis):</strong><br>
                Action: {depth_res['level_feedback'][3]['verbs_identified']}<br>
                <span style="color:#64748b;">{depth_res['level_feedback'][3]['tip']}</span>
            </div>
            <div style="background:#f8fafc; padding:12px; border-radius:10px; border:1px solid #e2e8f0; font-size:12.5px;">
                <strong>Level 4 (Evaluation/Creation):</strong><br>
                Action: {depth_res['level_feedback'][4]['verbs_identified']}<br>
                <span style="color:#64748b;">{depth_res['level_feedback'][4]['tip']}</span>
            </div>
        </div>
    </div>
    """)

    # ---------------------------------------------------------
    # Four Detailed Level Cards (Task + Evidence)
    # ---------------------------------------------------------
    st.markdown("### 📋 Detailed Assessment Sequence")
    for idx, lvl in enumerate(LEVELS_CONFIG, 1):
        prompt_data = st.session_state.prompts.get(idx, {})
        evidence_snippet = f"""<div style="margin-top:10px; font-size:13px; color:#475569;"><strong>Expected Evidence of Learning:</strong> {prompt_data.get('evidence')}</div>""" if prompt_data.get('evidence') else ""
        
        st.html(f"""
        <div class="showcase-step-card step-{idx}">
            <div class="showcase-header">
                <div>
                    <span style="font-size:18px; margin-right:6px;">{lvl['icon']}</span>
                    <span class="showcase-title">Level {idx}: {lvl['name']}</span>
                </div>
                <div>
                    <span class="pill" style="background:{lvl['tag_bg']}; color:{lvl['tag_color']};">
                        {lvl['cognitive_domain']}
                    </span>
                    <span class="pill" style="background:#f1f5f9; color:#475569;">
                        {prompt_data.get('format', 'Problem')}
                    </span>
                </div>
            </div>
            <div class="showcase-prompt-box">
                <strong>Task Prompt:</strong><br>
                {prompt_data.get('prompt', 'No prompt provided')}
            </div>
            {evidence_snippet}
        </div>
        """)

    # ---------------------------------------------------------
    # Structured 3-Part Before / After Reflection
    # ---------------------------------------------------------
    st.markdown("### 💭 Before / After Pedagogical Reflection")
    st.html("""
    <div class="staircase-card" style="margin-bottom:14px;">
        <h4 style="margin-top:0; font-size:16.5px; color:#0f172a;">Reflect on the Transformation Across the Staircase</h4>
        <p style="color:#64748b; font-size:13.5px; margin-bottom:0;">
            Compare your baseline conceptual question with the peak evaluation/creation challenge.
        </p>
    </div>
    """)

    ref_col1, ref_col2, ref_col3 = st.columns(3, gap="medium")
    
    with ref_col1:
        st.markdown("**1. BEFORE (Baseline Assessment)**")
        st.session_state.reflection_before = st.text_area(
            "What did the initial/basic assessment ask students to do?",
            value=st.session_state.reflection_before,
            placeholder="e.g. Students simply defined overfitting and recalled the bias-variance formula.",
            height=110,
            key="ref_before"
        )
    
    with ref_col2:
        st.markdown("**2. AFTER (High-Rigour Assessment)**")
        st.session_state.reflection_after = st.text_area(
            "What does the final assessment now require students to do?",
            value=st.session_state.reflection_after,
            placeholder="e.g. Students compare two models under constraints and justify a fail-safe deployment strategy.",
            height=110,
            key="ref_after"
        )

    with ref_col3:
        st.markdown("**3. WHY IS IT DEEPER? (Cognitive Transformation)**")
        st.session_state.reflection_why = st.text_area(
            "What changed in cognitive demand (reasoning, judgement, synthesis)?",
            value=st.session_state.reflection_why,
            placeholder="e.g. Moved from rote recall to multi-criteria evaluation, trade-off defense, and novel synthesis.",
            height=110,
            key="ref_why"
        )

    # ---------------------------------------------------------
    # Export & Action Suite (CSV + Markdown + Print + Revision)
    # ---------------------------------------------------------
    st.markdown("<div style='height:15px;'></div>", unsafe_allow_html=True)
    
    date_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    
    # Generate CSV Export
    csv_buffer = io.StringIO()
    csv_writer = csv.writer(csv_buffer)
    csv_writer.writerow([
        "Faculty Name", "Department", "Course", "Topic", "Timestamp",
        "Level 1 Task", "Level 1 Evidence", "Level 1 Format",
        "Level 2 Task", "Level 2 Evidence", "Level 2 Format",
        "Level 3 Task", "Level 3 Evidence", "Level 3 Format",
        "Level 4 Task", "Level 4 Evidence", "Level 4 Format",
        "Cognitive Progression Status", "Reflection Before", "Reflection After", "Reflection Why Is It Deeper"
    ])
    csv_writer.writerow([
        st.session_state.faculty_name, st.session_state.department, st.session_state.course_name, st.session_state.topic, date_str,
        st.session_state.prompts[1].get('prompt'), st.session_state.prompts[1].get('evidence'), st.session_state.prompts[1].get('format'),
        st.session_state.prompts[2].get('prompt'), st.session_state.prompts[2].get('evidence'), st.session_state.prompts[2].get('format'),
        st.session_state.prompts[3].get('prompt'), st.session_state.prompts[3].get('evidence'), st.session_state.prompts[3].get('format'),
        st.session_state.prompts[4].get('prompt'), st.session_state.prompts[4].get('evidence'), st.session_state.prompts[4].get('format'),
        depth_res.get('status'), st.session_state.reflection_before, st.session_state.reflection_after, st.session_state.reflection_why
    ])
    csv_data = csv_buffer.getvalue()

    # Generate Plain Text (.txt) Export Content
    export_content = f"""ASSESSMENT STAIRCASE
====================

Faculty Name: {st.session_state.faculty_name or 'N/A'}

Department: {st.session_state.department or 'N/A'}

Course / Subject: {st.session_state.course_name or 'N/A'}

Concept / Topic: {st.session_state.topic}

Generated on: {date_str}


1. FOUNDATION — EXPLAIN
-----------------------
Format: {st.session_state.prompts[1].get('format')}

Assessment Task:
{st.session_state.prompts[1].get('prompt')}

Evidence of Learning:
{st.session_state.prompts[1].get('evidence')}


2. APPLICATION — APPLY
----------------------
Format: {st.session_state.prompts[2].get('format')}

Assessment Task:
{st.session_state.prompts[2].get('prompt')}

Evidence of Learning:
{st.session_state.prompts[2].get('evidence')}


3. ANALYSIS — ANALYSE
---------------------
Format: {st.session_state.prompts[3].get('format')}

Assessment Task:
{st.session_state.prompts[3].get('prompt')}

Evidence of Learning:
{st.session_state.prompts[3].get('evidence')}


4. EVALUATION / CREATION
------------------------
Format: {st.session_state.prompts[4].get('format')}

Assessment Task:
{st.session_state.prompts[4].get('prompt')}

Evidence of Learning:
{st.session_state.prompts[4].get('evidence')}


REFLECTION
----------

BEFORE (Baseline Assessment):
{st.session_state.reflection_before or 'N/A'}

AFTER (High-Rigour Assessment):
{st.session_state.reflection_after or 'N/A'}

WHY IS IT DEEPER?:
{st.session_state.reflection_why or 'N/A'}


COGNITIVE PROGRESSION
---------------------

Status: {depth_res.get('status')}

{depth_res.get('summary')}
"""

    act_col1, act_col2, act_col3, act_col4 = st.columns([1.2, 1.2, 1, 1], gap="medium")
    
    with act_col1:
        st.download_button(
            label="📥 Download CSV (.csv)",
            data=csv_data,
            file_name=f"Assessment_Staircase_{(st.session_state.topic[:20].replace(' ', '_'))}.csv",
            mime="text/csv",
            type="primary",
            use_container_width=True
        )

    with act_col2:
        safe_topic = "".join([c if c.isalnum() else "_" for c in st.session_state.topic[:20]]).strip("_")
        st.download_button(
            label="📄 Download Report (.txt)",
            data=export_content,
            file_name=f"Assessment_Staircase_{safe_topic}.txt",
            mime="text/plain",
            use_container_width=True
        )

    with act_col3:
        if st.button("✏️ Revise Any Level", use_container_width=True):
            go_to_screen("level_1")

    with act_col4:
        if st.button("🔄 Reset Activity", use_container_width=True):
            reset_activity()


# ---------------------------------------------------------
# Screen Router
# ---------------------------------------------------------
screen = st.session_state.current_screen

if screen == "welcome":
    render_welcome_screen()
elif screen == "level_1":
    render_level_authoring_screen(1)
elif screen == "level_2":
    render_level_authoring_screen(2)
elif screen == "level_3":
    render_level_authoring_screen(3)
elif screen == "level_4":
    render_level_authoring_screen(4)
elif screen == "showcase":
    render_showcase_screen()
else:
    render_welcome_screen()
