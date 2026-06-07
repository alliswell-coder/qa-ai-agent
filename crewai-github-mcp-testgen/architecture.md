# Architecture - Crew.ai GitHub Test Generation System

## System Architecture Overview

The Crew.ai GitHub Test Generation System is a multi-agent AI workflow that transforms GitHub issues into comprehensive testing artifacts. The system uses Crew.ai framework with Groq's Llama 3.1 8B Instant model for AI processing.

## High-Level Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         User Interface Layer                                  │
├─────────────────────────────────────────────────────────────────────────────┤
│  ┌─────────────────────┐              ┌─────────────────────┐              │
│  │   CLI Interface     │              │   Streamlit UI      │              │
│  │   (main.py)         │              │   (app.py)          │              │
│  └──────────┬──────────┘              └──────────┬──────────┘              │
└─────────────┼───────────────────────────────────────┼──────────────────────┘
              │                                       │
              └───────────────────┬───────────────────┘
                                  │
┌─────────────────────────────────▼───────────────────────────────────────────┐
│                         Orchestration Layer                                   │
├─────────────────────────────────────────────────────────────────────────────┤
│  ┌───────────────────────────────────────────────────────────────────────┐  │
│  │                     Crew.ai Framework (crew.py)                        │  │
│  │  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  ┌───────────┐  │  │
│  │  │   Agent 1    │  │   Agent 2    │  │   Agent 3    │  │  Agent 4  │  │  │
│  │  │  GitHub      │  │  Test        │  │  Test Case  │  │ Playwright│  │  │
│  │  │  Analyst    │  │  Planner     │  │  Writer      │  │ Developer │  │  │
│  │  └──────────────┘  └──────────────┘  └──────────────┘  └───────────┘  │  │
│  └───────────────────────────────────────────────────────────────────────┘  │
└─────────────────────────────────┬───────────────────────────────────────────┘
                                  │
┌─────────────────────────────────▼───────────────────────────────────────────┐
│                         AI Processing Layer                                   │
├─────────────────────────────────────────────────────────────────────────────┤
│  ┌───────────────────────────────────────────────────────────────────────┐  │
│  │                    Groq API (llama-3.1-8b-instant)                     │  │
│  │  ┌─────────────────────────────────────────────────────────────────┐  │  │
│  │  │  Base URL: https://api.groq.com/openai/v1                        │  │  │
│  │  │  Model: llama-3.1-8b-instant                                      │  │  │
│  │  │  Authentication: API Key via .env                                │  │  │
│  │  └─────────────────────────────────────────────────────────────────┘  │  │
│  └───────────────────────────────────────────────────────────────────────┘  │
└─────────────────────────────────┬───────────────────────────────────────────┘
                                  │
┌─────────────────────────────────▼───────────────────────────────────────────┐
│                         Data Sources Layer                                   │
├─────────────────────────────────────────────────────────────────────────────┤
│  ┌─────────────────────┐              ┌─────────────────────┐              │
│  │   GitHub API        │              │   Template Files    │              │
│  │   (Issue Data)      │              │   (Format Guide)    │              │
│  └─────────────────────┘              └─────────────────────┘              │
└─────────────────────────────────────────────────────────────────────────────┘
```

## Detailed Workflow Diagram

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           INPUT STAGE                                        │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  User Input: GitHub Issue Number                                           │
│         │                                                                  │
│         ▼                                                                  │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  Fetch GitHub Issue via GitHub API                                   │   │
│  │  - Issue Title                                                       │   │
│  │  - Issue Description                                                 │   │
│  │  - Labels, Priority, Assignee                                        │   │
│  └───────────────────────────┬─────────────────────────────────────────┘   │
│                              │                                             │
└──────────────────────────────┼──────────────────────────────────────────────┘
                               │
┌──────────────────────────────▼──────────────────────────────────────────────┐
│                         AGENT 1: GitHub Issue Analyst                         │
├─────────────────────────────────────────────────────────────────────────────┤
│  Input: GitHub Issue Data                                                   │
│  Process:                                                                   │
│    • Extract functional requirements                                        │
│    • Identify acceptance criteria                                           │
│    • Define test scope and boundaries                                       │
│    • Document key features to test                                         │
│  Output: Requirements Analysis Document                                    │
└──────────────────────────────┬──────────────────────────────────────────────┘
                               │
┌──────────────────────────────▼──────────────────────────────────────────────┐
│                         AGENT 2: Test Planning Specialist                     │
├─────────────────────────────────────────────────────────────────────────────┤
│  Input: Requirements Analysis                                                │
│  Process:                                                                   │
│    • Create 12-section test plan                                           │
│    • Define test strategy and approach                                      │
│    • Identify test environment requirements                                  │
│    • Plan test schedule and resources                                       │
│  Output: Comprehensive Test Plan (test_plan.md)                             │
└──────────────────────────────┬──────────────────────────────────────────────┘
                               │
┌──────────────────────────────▼──────────────────────────────────────────────┐
│                         AGENT 3: Test Case Writer                             │
├─────────────────────────────────────────────────────────────────────────────┤
│  Input: Requirements Analysis + Test Plan                                    │
│  Process:                                                                   │
│    • Write detailed test cases in grid format                                │
│    • Include: Test Case ID, Description, Steps, Expected Result, Actual     │
│    • Ensure each expected result has specific values                         │
│    • Cover happy path, edge cases, negative scenarios                        │
│  Output: Detailed Test Cases (test_cases.md)                                │
└──────────────────────────────┬──────────────────────────────────────────────┘
                               │
┌──────────────────────────────▼──────────────────────────────────────────────┐
│                         AGENT 4: Playwright Developer                         │
├─────────────────────────────────────────────────────────────────────────────┤
│  Input: Test Cases                                                           │
│  Process:                                                                   │
│    • Generate TypeScript Playwright scripts                                  │
│    • Include proper selectors and assertions                                  │
│    • Follow Playwright best practices                                       │
│    • Add error handling and comments                                         │
│  Output: Playwright Test Scripts (playwright_tests.md)                       │
└──────────────────────────────┬──────────────────────────────────────────────┘
                               │
┌──────────────────────────────▼──────────────────────────────────────────────┐
│                           OUTPUT STAGE                                       │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  Generated Files in output/ Directory:                               │   │
│  │                                                                     │   │
│  │  • test_plan.md          - 12-section test plan                    │   │
│  │  • test_cases.md         - Detailed test cases in grid format      │   │
│  │  • playwright_tests.md   - TypeScript Playwright scripts            │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

## Component Details

### 1. User Interface Layer

**CLI Interface (main.py)**
- Entry point for command-line usage
- Accepts GitHub issue number as argument
- Initiates Crew.ai workflow
- Displays progress and results

**Streamlit UI (app.py)**
- Web-based user interface
- Sidebar for configuration
- Issue number input
- Generate button
- File display and download options

### 2. Orchestration Layer

**Crew.ai Framework (crew.py)**
- Manages 4 AI agents
- Coordinates sequential task execution
- Handles context passing between agents
- Error handling and retry logic

**Agents:**
1. **GitHub Issue Analyst** - Analyzes GitHub issues
2. **Test Planning Specialist** - Creates test plans
3. **Test Case Writer** - Writes detailed test cases
4. **Playwright Developer** - Generates automation scripts

### 3. AI Processing Layer

**Groq API Integration**
- Provider: Groq (free tier)
- Model: Llama 3.1 8B Instant
- Base URL: https://api.groq.com/openai/v1
- Authentication: API Key from .env
- Purpose: Natural language processing and content generation

### 4. Data Sources Layer

**GitHub API**
- Fetches issue details
- Authentication via Personal Access Token
- Repository: alliswell-coder/qa-ai-agent

**Template Files**
- test_plan_template.md - Format guide for test plans
- test_case_template.md - Format guide for test cases

### 5. Output Layer

**Generated Files**
- test_plan.md - 12-section test plan
- test_cases.md - Grid format test cases
- playwright_tests.md - TypeScript automation scripts

## Data Flow

```
GitHub Issue → GitHub API → Issue Data → Agent 1 → Requirements 
                                                    ↓
Agent 2 ← Test Plan ← Agent 1 ← Requirements
    ↓
Test Cases → Agent 3 ← Test Plan
    ↓
Playwright Scripts → Agent 4 ← Test Cases
    ↓
Output Files → output/ Directory
```

## Technology Stack

- **Framework**: Crew.ai (Multi-agent AI orchestration)
- **AI Model**: Groq Llama 3.1 8B Instant
- **Language**: Python 3.13
- **Web UI**: Streamlit
- **API Integration**: GitHub API, Groq API
- **Configuration**: python-dotenv (.env file)

## Security Considerations

- API keys stored in .env file (not committed to git)
- .gitignore prevents sensitive file exposure
- GitHub token with minimal required permissions
- Groq API key authentication

## Performance Considerations

- Sequential agent execution (not parallel)
- Each agent makes multiple LLM API calls
- Typical execution time: 2-5 minutes per issue
- Groq provides fast inference speeds
- Caching not implemented (fresh generation each time)

## Error Handling

- GitHub API rate limiting
- AI model unavailability
- Invalid issue numbers
- API key authentication failures
- File system permissions

## Scalability

- Can process multiple issues sequentially
- No built-in parallel processing
- Dependent on Groq API rate limits
- Output files stored locally (not database)
