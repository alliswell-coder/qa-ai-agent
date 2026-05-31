# Project3 - QA AI Agents Portfolio

A professional portfolio showcasing three AI-powered QA automation agents.

## Overview

This portfolio page displays three intelligent QA automation agents designed to streamline quality assurance workflows:

- **Agent 1**: QA Test Case Generator (LangFlow + Groq)
- **Agent 2**: Automated Bug Reporter (n8n + Google Sheets + GitHub)
- **Agent 3**: QA Dashboard (HTML + CSS + JavaScript + Vercel)

## Features

- **Portfolio Landing Page**: Modern dark theme with professional card-based layout
- **Agent Cards**: Each agent displayed with description, tech stack, and navigation links
- **Responsive Design**: Works seamlessly on desktop and mobile devices
- **Interactive UI**: Hover effects and smooth transitions

## Agents

### Agent 1: QA Test Case Generator
- **Description**: Paste any requirement and get structured test cases instantly
- **Tech Stack**: LangFlow + Groq
- **Status**: Coming Soon

### Agent 2: Automated Bug Reporter
- **Description**: Log a failed test in Google Sheet, GitHub issue created automatically in 60 seconds
- **Tech Stack**: n8n + Google Sheets + GitHub
- **Status**: Coming Soon

### Agent 3: QA Dashboard
- **Description**: Live view of test execution results with pass/fail stats and GitHub issue links
- **Tech Stack**: HTML + CSS + JavaScript + Vercel
- **Status**: Available (View via portfolio page)

## How to Use

1. Open `index.html` in a web browser to view the portfolio landing page
2. Click on agent cards to navigate to individual agent pages
3. Agent 3 (QA Dashboard) is available via the "View Dashboard" button

## File Structure

```
Project3-Vibe-Dashboard/
├── index.html                    # Portfolio landing page
├── agent3.html                   # QA Dashboard (Agent 3)
├── README.md                     # This file
└── prompt for vibe coding.md     # Original prompt
```

## Technologies Used

- **Portfolio Page**: HTML5, CSS3 (Flexbox, Grid, CSS Variables)
- **QA Dashboard**: HTML5, CSS3, JavaScript
- No external dependencies - pure HTML/CSS/JS

## Original Prompt

```
Create a new folder called Project3-Vibe-Dashboard 
inside C:\Users\karth\qa-ai-agent

Inside that folder create:
- index.html - QA Dashboard with:
  - Header: "QA Dashboard - Amazon Checkout Flow"
  - Summary cards: Total TCs: 7, Pass: 2, Fail: 5, Pass Rate: 28%
  - Failed tests table with columns: TC ID, Description, 
    Actual Result, Priority, GitHub Issue
  - Data:
    TC003 | Proceed to Checkout | 404 Error | High | https://github.com/alliswell-coder/qa-ai-agent/issues/7
    TC004 | Empty Cart | Cart count wrong | High | https://github.com/alliswell-coder/qa-ai-agent/issues/8
    TC046 | Saved Credit Card | No card displayed | High | https://github.com/alliswell-coder/qa-ai-agent/issues/9
    TC007 | Payment Declined | App crashes | High | https://github.com/alliswell-coder/qa-ai-agent/issues/11
  - Green color for Pass, Red for Fail
  - Clean modern dark theme design
- README.md
```
