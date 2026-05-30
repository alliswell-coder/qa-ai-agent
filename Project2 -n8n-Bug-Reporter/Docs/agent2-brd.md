# Agent 2 — Automated Bug Reporter

## The Problem
As a QA engineer, every time a test fails you have to:
- Open GitHub manually
- Create a new issue
- Copy paste TC ID, steps, expected vs actual result
- Come back to your sheet and update the issue link

If 5 tests fail in one run, that's 30-45 minutes of 
copy-paste work. Not testing. Just admin.

## What This Agent Does
You add a failed test to Google Sheet.
Within 60 seconds — GitHub issue is created and 
the link appears in your sheet automatically.
Zero manual work.

## How It Works
1. You run your test cases
2. Any test that fails → add it to Google Sheet 
   with Status = FAIL
3. n8n checks the sheet every minute
4. Detects the new FAIL row
5. Creates a GitHub Issue with all bug details
6. Writes the GitHub Issue URL back to your sheet
7. When the sheet is added with any new issue, the agent will create a new GitHub issue automatically
## What the GitHub Issue Contains
- TC ID
- What failed (Description)
- How to reproduce (Steps)
- What should have happened (Expected Result)
- What actually happened (Actual Result)
- How urgent it is (Priority)

## Time Saved
- Before: 10-15 minutes per bug manually
- After: 0 minutes — fully automated

## Tools Used
- Google Sheets — test execution log
- n8n — automation engine  
- GitHub Issues — bug tracking