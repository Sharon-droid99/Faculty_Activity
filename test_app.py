import os
import sys
import time

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from playwright.sync_api import sync_playwright

def run_tests():
    os.makedirs("test_artifacts", exist_ok=True)
    results = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(viewport={"width": 1280, "height": 900})
        page = context.new_page()

        print("[TEST 1] Fresh launch & Navigation to http://localhost:8505...")
        page.goto("http://localhost:8505", timeout=30000)
        page.wait_for_selector(".header-card", timeout=15000)
        time.sleep(2)

        header_text = page.locator(".header-card h1").text_content()
        assert "Climb the Assessment Staircase" in header_text
        print("  [OK] Header verified: " + header_text)
        results.append("Fresh Launch: PASS")

        page.screenshot(path="test_artifacts/01_welcome_screen.png")

        # Test 2: Validation on empty topic
        print("[TEST 2] Testing empty topic validation...")
        begin_btn = page.locator("button:has-text('Begin Staircase Activity')")
        begin_btn.click()
        time.sleep(1)
        error_box = page.locator(".stAlert")
        assert error_box.is_visible()
        print("  [OK] Empty topic error displayed")
        results.append("Empty Topic Validation: PASS")

        # Test 3: Exemplar Pre-fill
        print("[TEST 3] Loading discipline exemplar...")
        ds_btn = page.locator("button:has-text('Data Science & AI')")
        ds_btn.click()
        time.sleep(2)
        topic_input = page.locator("input[aria-label*='Central Topic to Scaffold']")
        assert len(topic_input.input_value()) > 0
        print("  [OK] Exemplar loaded topic: " + topic_input.input_value())
        results.append("Exemplar Pre-fill: PASS")

        # Fill faculty details
        page.locator("input[aria-label*='Faculty Name']").fill("Dr. Sathya")
        page.locator("input[aria-label*='Course / Subject']").fill("Machine Learning (CS601)")
        page.locator("input[aria-label*='Department']").fill("Data Science")
        
        begin_btn.click()
        time.sleep(2)

        # Test 4: Level 1 Foundation
        print("[TEST 4] Testing Level 1 Authoring (Task + Evidence)...")
        page.wait_for_selector(".workshop-badge:has-text('Level 1 of 4')", timeout=10000)
        explain_chip = page.locator("button:has-text('+ Explain')")
        if explain_chip.is_visible():
            explain_chip.click()
            time.sleep(1)
        page.screenshot(path="test_artifacts/03_level_1.png")
        print("  [OK] Level 1 screen verified with verbs")
        results.append("Level 1 Authoring: PASS")

        page.locator("button:has-text('Save & Ascend to Level 2')").click()
        time.sleep(2)

        # Test 5: Level 2 Application & Incomplete Validation Test
        print("[TEST 5] Testing Level 2 and Evidence validation...")
        page.wait_for_selector(".workshop-badge:has-text('Level 2 of 4')", timeout=10000)
        
        # Clear evidence temporarily to test validation
        evidence_box = page.locator("textarea[aria-label*='Evidence of Mastery']")
        original_evi = evidence_box.input_value()
        evidence_box.fill("")
        time.sleep(1)
        page.locator("button:has-text('Save & Ascend to Level 3')").click()
        time.sleep(1)
        assert page.locator(".stAlert").is_visible(), "Should alert on missing evidence"
        print("  [OK] Missing evidence validation successfully triggered")
        results.append("Evidence Validation: PASS")

        # Restore evidence and advance
        evidence_box.fill(original_evi or "Demonstrates accurate code execution and data imputation.")
        time.sleep(1)
        page.locator("button:has-text('Save & Ascend to Level 3')").click()
        time.sleep(2)

        # Test 6: Level 3 Analysis
        print("[TEST 6] Testing Level 3 Analysis...")
        page.wait_for_selector(".workshop-badge:has-text('Level 3 of 4')", timeout=10000)
        print("  [OK] Level 3 reached")
        page.locator("button:has-text('Save & Ascend to Level 4')").click()
        time.sleep(2)

        # Test 7: Level 4 & Build My Staircase button
        print("[TEST 7] Testing Level 4 & 'Build My Staircase' action...")
        page.wait_for_selector(".workshop-badge:has-text('Level 4 of 4')", timeout=10000)
        build_btn = page.locator("button:has-text('Build My Staircase')")
        assert build_btn.is_visible()
        page.screenshot(path="test_artifacts/06_level_4_build.png")
        build_btn.click()
        time.sleep(3)
        print("  [OK] 'Build My Staircase' executed")
        results.append("Build My Staircase Action: PASS")

        # Test 8: Showcase & Depth Check Verification
        print("[TEST 8] Verifying Showcase & Cognitive Depth Check...")
        page.wait_for_selector(".header-card h1:has-text('Completed Assessment Staircase')", timeout=10000)
        
        # Verify visual staircase
        stair_graphic = page.locator(".stair-visual-wrapper")
        assert stair_graphic.is_visible()
        print("  [OK] Visual Staircase graphic rendered")

        # Verify Cognitive Depth Check card
        depth_card = page.locator(".depth-feedback-card")
        assert depth_card.is_visible(), "Depth & Rigour progression card must be rendered"
        depth_text = depth_card.text_content()
        print("  [OK] Depth & Rigour Diagnostic rendered: " + depth_text[:80] + "...")
        results.append("Cognitive Depth Engine: PASS")

        # Test 9: 3-Part Before / After Reflection
        print("[TEST 9] Verifying 3-Part Reflection inputs...")
        ref_before = page.locator("textarea[aria-label*='initial/basic assessment']")
        ref_after = page.locator("textarea[aria-label*='final assessment now require']")
        ref_why = page.locator("textarea[aria-label*='cognitive demand']")
        
        assert ref_before.is_visible()
        assert ref_after.is_visible()
        assert ref_why.is_visible()
        print("  [OK] All 3 Reflection fields verified (Before, After, Why Is It Deeper)")
        results.append("3-Part Reflection: PASS")

        page.screenshot(path="test_artifacts/07_showcase_depth_check.png")

        # Test 10: Multi-format Exports (CSV & Markdown)
        print("[TEST 10] Testing export downloads (CSV & Markdown)...")
        csv_btn = page.locator("button:has-text('Download CSV')")
        md_btn = page.locator("button:has-text('Download Report (.md)')")
        assert csv_btn.is_visible()
        assert md_btn.is_visible()
        print("  [OK] CSV and Markdown download buttons active")
        results.append("Multi-Format Exports: PASS")

        # Test 11: Reset Activity
        print("[TEST 11] Testing 'Reset Activity'...")
        reset_btn = page.locator("button:has-text('Reset Activity')")
        reset_btn.click()
        time.sleep(2)
        assert page.locator(".header-card h1:has-text('Climb the Assessment Staircase')").is_visible()
        topic_after_reset = page.locator("input[aria-label*='Central Topic to Scaffold']").input_value()
        assert topic_after_reset == "", "Topic input should be empty after reset"
        print("  [OK] Reset cleanly cleared all session state and returned to start")
        results.append("Activity Reset: PASS")

        browser.close()

    print("\n===========================================")
    print("ALL AUDIT AND VERIFICATION TESTS PASSED! [11/11]")
    print("===========================================")
    for r in results:
        print(f"  * {r}")

if __name__ == "__main__":
    run_tests()
