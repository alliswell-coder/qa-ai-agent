# Agent 2 — Automated Bug Reporter

## The Problem
Every time a test fails, QA engineers spend 
10-15 minutes manually creating a GitHub issue.
Multiply that by 10 bugs — that's 2 hours of 
copy-paste work instead of actual testing.

## The Solution
Log your failed test in Google Sheet.
GitHub issue is created automatically within 60 seconds.
The issue link appears back in your sheet — zero manual work.

## Workflow
![n8n Workflow](Screenshot/Workflow%20Screenshot.png)

## How It Works
1. QA logs failed test in Google Sheet with Status = FAIL
2. n8n detects new row automatically every minute
3. Creates GitHub Issue with full bug details
4. Writes GitHub Issue URL back to the sheet

## Docs
- [Requirements](Docs/agent2-brd.md)
- [Sample Execution Report](Docs/agent2-sample-%20execution%20report.md)
- [GitHub Issues Output](Docs/Github-output.md)
- [Test Data CSV](Docs/Project2-n8n-Bug-Reporter_-Te....csv)

## Workflow File
- [n8n Workflow JSON](Workflow/QA%20Bug%20Reporter%20-%20Google%20Sheet%20t....json)

## Tech Stack
- Google Sheets
- n8n Cloud
- GitHub Issues

## Live GitHub Issues
[View Auto-Created Issues](https://github.com/alliswell-coder/qa-ai-agent/issues)
