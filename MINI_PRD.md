# MINI PRD: Assessment Staircase Activity

## 1. Product Goal
Enable higher-education faculty workshop participants to progressively scaffold and design an assessment task around a single academic topic across four levels of increasing cognitive complexity, visualizing their progression up an interactive assessment staircase.

## 2. Target User
Faculty participants in Quality Improvement Programs (QIP), Faculty Development Programs (FDP), or teaching pedagogy workshops.

## 3. User Journey
1. **Welcome & Registration / Orientation:**
   - Understand the purpose of the Assessment Staircase.
   - Enter participant details (Name, Course / Subject, Academic Discipline) and the **Central Topic**.
2. **Step-by-Step Guided Staircase Progression:**
   - **Step 1: FOUNDATION — Explain** (Recall, define, explain core concepts)
   - **Step 2: APPLICATION — Apply** (Apply concepts/formulas/methods to new scenarios or datasets)
   - **Step 3: ANALYSIS — Analyse** (Examine relationships, dissect errors, compare components, diagnose causes)
   - **Step 4: EVALUATION & CREATION — Evaluate / Create** (Critique, justify choices, design or synthesize novel solutions)
   Each step features:
   - Dynamic Staircase/Ladder sidebar/top visualizer showing current level, completed levels, and upcoming levels.
   - Cognitive level definition, action verbs cheat-sheet, and contextual example.
   - Assessment prompt/question input with task description, criteria/expected evidence, and estimated time/marks.
   - Validation & Next/Back navigation preserving state.
3. **Reflection & Self-Assessment:**
   - Cognitive leap reflection (How does the difficulty scale from Step 1 to Step 4?).
4. **Final Staircase & Summary Showcase:**
   - Visual 4-tiered Staircase graphic displaying the faculty member's authored assessment tasks.
   - Clean summary card with metadata (Faculty Name, Topic, Course).
   - Action buttons: Copy to Clipboard, Download Markdown / Text Report, Print-friendly view, Restart / Design New Staircase.

## 4. Screen-by-Screen Specification
- **Screen 0: Welcome & Topic Setup**
  - Card 1: Workshop Introduction & Pedagogy Brief (Bloom's Revised Taxonomy framing).
  - Card 2: Faculty Information & Central Topic selector/input with discipline examples.
- **Screen 1 to 4: Progressive Staircase Steps (Levels 1 to 4)**
  - Left Column (or Visual Ladder): Staircase status indicator (Step 1 to 4 with status: Completed, Active, Upcoming).
  - Right Column (Authoring Workspace):
    - Level Badge & Cognitive Demand overview.
    - Helpful Action Verbs & Benchmark Example.
    - Assessment Task Prompt (Textarea, required).
    - Expected Student Response / Evidence of Thinking (Textarea, optional/recommended).
    - Cognitive Check / Tag (e.g. formative vs. summative, question type).
    - Navigation: `← Previous Level` and `Continue to Level X →`.
- **Screen 5: Final Staircase Showcase & Export**
  - Hero Celebration banner: *"🎉 Assessment Staircase Complete!"*
  - Interactive Visual Staircase: 4 ascending steps styled with cards, icons, cognitive badges, and the faculty's custom questions.
  - Summary table / download report.
  - "Start New Staircase" button.

## 5. Visual Design Tokens (Derived from Reference Application)
- **Background:** `linear-gradient(135deg, #eef2ff, #f8fafc)`
- **Font:** Inter / System Sans-Serif (`Arial, Helvetica, sans-serif`)
- **Primary Color:** `#2563eb` (Hover `#1d4ed8`)
- **Success Color:** `#16a34a` (Completed badge `#dcfce7`)
- **Card Background:** `#ffffff` with border-radius `18px` and shadow `0 8px 30px rgba(0,0,0,0.07)`
- **Level Badges:** Circular numbered icons (`1`, `2`, `3`, `4`) with ascending stair offsets.

## 6. Technical Architecture
- **Language/Framework:** Streamlit (Python 3.10+)
- **State Management:** `st.session_state` (step tracking, form inputs, validation flags)
- **Custom UI:** Inline CSS with scoped styling, SVG visual staircase, custom HTML badges for authentic reference parity.
- **Zero External DB:** Session-only state, instant execution.
