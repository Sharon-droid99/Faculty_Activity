"""
CSS styling and visual components for the Assessment Staircase.
Faithfully recreates and enhances the reference app aesthetics.
"""

CUSTOM_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"], .stApp {
    font-family: 'Plus Jakarta Sans', Arial, -apple-system, BlinkMacSystemFont, sans-serif !important;
    background: linear-gradient(135deg, #eef2ff 0%, #f8fafc 100%) !important;
    color: #172033 !important;
}

.main .block-container {
    max-width: 1100px !important;
    padding-top: 1.8rem !important;
    padding-bottom: 3.5rem !important;
}

header[data-testid="stHeader"] {
    background: transparent !important;
}

.header-card {
    text-align: center;
    background: white;
    border-radius: 20px;
    padding: 28px 24px;
    box-shadow: 0 10px 32px rgba(37, 99, 235, 0.08);
    margin-bottom: 22px;
    border: 1px solid rgba(226, 232, 240, 0.8);
    position: relative;
    overflow: hidden;
}

.header-card::before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 4px;
    background: linear-gradient(90deg, #2563eb, #3b82f6, #8b5cf6, #10b981);
}

.header-card h1 {
    margin: 0;
    font-size: 32px;
    font-weight: 800;
    color: #0f172a;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 12px;
}

.header-card p {
    margin: 8px 0 0;
    color: #64748b;
    font-size: 16px;
    font-weight: 500;
}

.workshop-badge {
    display: inline-block;
    margin-top: 10px;
    padding: 4px 14px;
    background: #eff6ff;
    color: #2563eb;
    border-radius: 9999px;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 0.5px;
    text-transform: uppercase;
    border: 1px solid #bfdbfe;
}

.staircase-card {
    background: white;
    border-radius: 18px;
    padding: 24px;
    box-shadow: 0 8px 30px rgba(0, 0, 0, 0.06);
    border: 1px solid #e2e8f0;
    margin-bottom: 20px;
}

/* Ladder Vertical Navigation */
.ladder-container {
    display: flex;
    flex-direction: column;
    gap: 12px;
    margin-bottom: 20px;
}

.ladder-step {
    padding: 14px 18px;
    border-radius: 14px;
    background: #f1f5f9;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 14px;
    opacity: 0.70;
    transition: all 0.25s ease-in-out;
    border: 1px solid #e2e8f0;
}

.ladder-step.active {
    opacity: 1;
    background: linear-gradient(135deg, #2563eb, #1d4ed8) !important;
    color: white !important;
    transform: translateX(4px);
    box-shadow: 0 8px 20px rgba(37, 99, 235, 0.25);
    border-color: #2563eb;
}

.ladder-step.active strong,
.ladder-step.active div,
.ladder-step.active span {
    color: white !important;
}

.ladder-step.completed {
    opacity: 1;
    background: #f0fdf4 !important;
    border: 1.5px solid #86efac !important;
    color: #166534 !important;
}

.step-num-circle {
    width: 36px;
    height: 36px;
    border-radius: 50%;
    background: white;
    color: #172033;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 800;
    font-size: 15px;
    box-shadow: 0 2px 6px rgba(0,0,0,0.1);
    flex-shrink: 0;
}

.ladder-step.active .step-num-circle {
    background: white;
    color: #2563eb;
}

.ladder-step.completed .step-num-circle {
    background: #16a34a;
    color: white;
}

/* Custom Staircase Visual SVG & Ascending Bars */
.stair-visual-wrapper {
    display: flex;
    align-items: flex-end;
    justify-content: space-between;
    gap: 16px;
    margin: 20px 0 30px 0;
    padding: 24px;
    background: white;
    border-radius: 18px;
    border: 1px solid #e2e8f0;
    box-shadow: 0 8px 30px rgba(0, 0, 0, 0.05);
}

.stair-step-column {
    flex: 1;
    display: flex;
    flex-direction: column;
    justify-content: flex-end;
    text-align: center;
}

.stair-bar {
    border-radius: 14px 14px 4px 4px;
    padding: 16px 12px;
    color: white !important;
    font-weight: 700;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    box-shadow: 0 4px 15px rgba(0,0,0,0.08);
}

.stair-bar div, .stair-bar span {
    color: white !important;
}

.stair-bar-1 { height: 120px; background: linear-gradient(180deg, #3b82f6, #1d4ed8); }
.stair-bar-2 { height: 170px; background: linear-gradient(180deg, #0284c7, #0369a1); }
.stair-bar-3 { height: 220px; background: linear-gradient(180deg, #7c3aed, #5b21b6); }
.stair-bar-4 { height: 270px; background: linear-gradient(180deg, #059669, #047857); }

/* Completed Showcase Card */
.showcase-step-card {
    background: white;
    border-radius: 14px;
    padding: 20px;
    margin-bottom: 16px;
    border: 1px solid #e2e8f0;
    box-shadow: 0 4px 16px rgba(0,0,0,0.04);
    position: relative;
    border-left: 6px solid #2563eb;
}

.showcase-step-card.step-1 { border-left-color: #3b82f6; }
.showcase-step-card.step-2 { border-left-color: #0ea5e9; }
.showcase-step-card.step-3 { border-left-color: #8b5cf6; }
.showcase-step-card.step-4 { border-left-color: #10b981; }

.showcase-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 12px;
    flex-wrap: wrap;
    gap: 8px;
}

.showcase-title {
    font-size: 16.5px;
    font-weight: 700;
    color: #0f172a;
}

.showcase-prompt-box {
    background: #f8fafc;
    border-radius: 10px;
    padding: 14px;
    font-size: 14.5px;
    line-height: 1.5;
    color: #1e293b;
    border: 1px solid #e2e8f0;
    font-weight: 500;
}

.pill {
    display: inline-block;
    padding: 4px 12px;
    border-radius: 20px;
    font-size: 12px;
    font-weight: 700;
    margin-left: 6px;
}

/* Depth & Rigour Check Box */
.depth-feedback-card {
    background: white;
    border-radius: 18px;
    padding: 24px;
    border: 1.5px solid #e2e8f0;
    box-shadow: 0 8px 30px rgba(0, 0, 0, 0.06);
    margin-bottom: 24px;
    position: relative;
    overflow: hidden;
}

.depth-header-strip {
    display: flex;
    align-items: center;
    justify-content: space-between;
    flex-wrap: wrap;
    gap: 12px;
    margin-bottom: 14px;
}

.depth-badge {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    padding: 6px 14px;
    border-radius: 999px;
    font-size: 13.5px;
    font-weight: 800;
}

.reflection-prompt-box {
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 12px;
    padding: 16px;
    margin-bottom: 14px;
}

/* Primary buttons override */
div.stButton > button {
    border-radius: 10px !important;
    padding: 10px 22px !important;
    font-weight: 700 !important;
    font-size: 15px !important;
    transition: all 0.2s ease !important;
    box-shadow: 0 2px 8px rgba(0,0,0,0.06) !important;
}

div.stButton > button[kind="primary"] {
    background: #2563eb !important;
    color: white !important;
    border: none !important;
}

div.stButton > button[kind="primary"]:hover {
    background: #1d4ed8 !important;
    transform: translateY(-1px);
    box-shadow: 0 6px 18px rgba(37, 99, 235, 0.3) !important;
}

div.stButton > button[kind="secondary"] {
    background: white !important;
    color: #334155 !important;
    border: 1.5px solid #cbd5e1 !important;
}

div.stButton > button[kind="secondary"]:hover {
    background: #f8fafc !important;
    border-color: #94a3b8 !important;
    color: #0f172a !important;
}

div[data-baseweb="input"] > div,
div[data-baseweb="textarea"] > div {
    border-radius: 10px !important;
    border-color: #cbd5e1 !important;
    background: #ffffff !important;
}

div[data-baseweb="input"]:focus-within > div,
div[data-baseweb="textarea"]:focus-within > div {
    border-color: #2563eb !important;
    box-shadow: 0 0 0 2px rgba(37, 99, 235, 0.2) !important;
}

.stAlert {
    border-radius: 12px !important;
}
</style>
"""

def clean_html(html_str):
    """Compacts HTML into a single line without any newlines or indentation."""
    return "".join(line.strip() for line in html_str.splitlines() if line.strip())

def render_ladder_nav(current_step, total_steps=4, steps_data=None):
    """Generates pure HTML for the progressive vertical Rigour Ladder indicator."""
    steps_html = []
    for idx in range(1, total_steps + 1):
        step_meta = steps_data[idx - 1] if steps_data and len(steps_data) >= idx else {
            "name": f"Level {idx}",
            "short_name": f"Level {idx}",
            "icon": f"{idx}️⃣"
        }
        
        status_class = ""
        badge_content = f"{idx}"
        status_text = "Pending"
        
        if idx == current_step:
            status_class = "active"
            status_text = "In Progress"
        elif idx < current_step:
            status_class = "completed"
            badge_content = "✓"
            status_text = "Completed"
        else:
            status_class = "upcoming"
            status_text = "Next"

        step_item = f"""<div class="ladder-step {status_class}"><div style="display:flex; align-items:center; gap:12px;"><div class="step-num-circle">{badge_content}</div><div><div style="font-weight:700; font-size:14.5px;">{step_meta['name']}</div><div style="font-size:12px; opacity:0.85;">{step_meta.get('cognitive_domain', '')}</div></div></div><span style="font-size:11.5px; font-weight:700; text-transform:uppercase; letter-spacing:0.5px; opacity:0.85;">{status_text}</span></div>"""
        steps_html.append(step_item)

    container = f"""<div class="ladder-container">{"".join(steps_html)}</div>"""
    return clean_html(container)

def render_staircase_graphic(steps_data, user_prompts=None):
    """Renders pure architectural visual staircase diagram representing the 4 levels."""
    user_prompts = user_prompts or {}
    bars_html = []
    
    for idx, step in enumerate(steps_data, 1):
        has_content = bool(user_prompts.get(idx, {}).get("prompt", "").strip())
        status_tag = "✓ Configured" if has_content else "Level " + str(idx)
        bar_class = f"stair-bar-{idx}"
        
        column = f"""<div class="stair-step-column"><div class="stair-bar {bar_class}"><div><div style="font-size:12px; opacity:0.9; text-transform:uppercase; letter-spacing:0.5px;">Level {idx}</div><div style="font-size:15px; font-weight:800; margin-top:2px;">{step['short_name']}</div></div><div style="margin-top:10px;"><div style="font-size:11px; padding:3px 8px; background:rgba(255,255,255,0.22); border-radius:999px; display:inline-block;">{status_tag}</div></div></div><div style="font-size:12px; font-weight:600; color:#64748b; margin-top:8px;">{step['action_tag']}</div></div>"""
        bars_html.append(column)
        
    wrapper = f"""<div class="stair-visual-wrapper">{"".join(bars_html)}</div>"""
    return clean_html(wrapper)
