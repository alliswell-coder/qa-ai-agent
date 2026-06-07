# Crew.ai GitHub Test Generation System

An automated test generation system using Crew.ai that takes GitHub issues and generates complete testing artifacts including test plans, test cases, and Playwright automation scripts.

## Overview

This system uses 4 AI agents to transform a GitHub issue into comprehensive testing deliverables:

1. **GitHub Issue Analyst** - Extracts requirements from GitHub issues
2. **Test Planning Specialist** - Creates 12-section test plans
3. **Test Case Writer** - Writes detailed test cases
4. **Playwright Developer** - Generates TypeScript Playwright scripts

## Project Structure

```
crewai-github-mcp-testgen/
├── .env.example              # Environment variables template
├── .gitignore                # Git ignore file
├── crew.py                   # All agents, tasks, and crew orchestration
├── main.py                   # CLI entry point
├── app.py                    # Streamlit web UI
├── requirements.txt           # Python dependencies
├── templates/                # Template files for format consistency
│   ├── test_plan_template.md
│   └── test_case_template.md
└── output/                   # Generated files
    ├── test_plan.md
    ├── test_cases.md
    └── playwright_tests.md
```

## Installation

### Prerequisites
- **Python 3.13** (Required for compatibility with dependencies)
- GitHub Personal Access Token
- Groq API Key (Free tier available)

### Setup

1. **Clone or create the project directory**

2. **Create virtual environment with Python 3.13**
```bash
py -3.13 -m venv .venv
```

3. **Activate virtual environment**
```bash
# Windows (PowerShell)
.venv\Scripts\activate

# Windows (Git Bash)
source .venv/Scripts/activate
```

4. **Install dependencies**
```bash
pip install -r requirements.txt
```

5. **Configure environment variables**
```bash
cp .env.example .env
```

Edit `.env` and add your credentials:
```env
GITHUB_TOKEN=ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
GITHUB_OWNER=alliswell-coder
GITHUB_REPO=qa-ai-agent
GROQ_API_KEY=gsk_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

### Get GitHub Token
1. Go to GitHub Settings → Developer settings → Personal access tokens
2. Generate new token (classic)
3. Select scopes: `repo` (for private repos) or `public_repo` (for public repos)
4. Copy and paste into `.env`

### Get Groq API Key (Free)
1. Go to https://console.groq.com
2. Sign up/login (free account)
3. Create API key
4. Copy and paste into `.env`

## Usage

### Option 1: Command Line Interface

```bash
.venv\Scripts\python.exe main.py <issue_number>
```

Example:
```bash
.venv\Scripts\python.exe main.py 7
```

### Option 2: Streamlit Web UI

```bash
.venv\Scripts\streamlit run app.py
```

When prompted for email, press Enter to skip. Then open http://localhost:8501 in your browser.

**In the Streamlit UI:**
1. Enter GitHub issue number in the sidebar (change from default 1 to your desired issue)
2. Click "Generate Test Artifacts"
3. Wait for AI agents to complete
4. View and download generated files

## Workflow

```
GitHub Issue → Requirements Analysis → Test Plan → Test Cases → Playwright Scripts
```

### Agent 1: GitHub Issue Analyst
- Fetches GitHub issue details
- Extracts functional requirements
- Identifies acceptance criteria
- Defines test scope

### Agent 2: Test Planning Specialist
- Creates comprehensive test plan with 12 sections:
  1. Test Scope
  2. Test Strategy
  3. Test Environment
  4. Test Schedule
  5. Resources Required
  6. Test Deliverables
  7. Risk Assessment
  8. Entry Criteria
  9. Exit Criteria
  10. Test Cases Overview
  11. Defect Reporting
  12. Sign-off Process

### Agent 3: Test Case Writer
- Writes detailed test cases
- Includes test steps and expected results
- Covers happy path, edge cases, negative scenarios
- Assigns priority levels

### Agent 4: Playwright Developer
- Generates TypeScript Playwright scripts
- Includes proper selectors and assertions
- Follows Playwright best practices
- Handles errors gracefully

## Output Files

### test_plan.md
Complete test plan with all 12 sections based on requirements analysis.

### test_cases.md
Detailed test cases in table format with:
- Test Case ID
- Title
- Description
- Preconditions
- Test Steps
- Expected Results
- Priority

### playwright_tests.md
TypeScript Playwright test scripts with:
- Proper imports and fixtures
- Test functions for each test case
- Selectors and assertions
- Error handling
- Comments for clarity

## Testing

The system has been tested with GitHub issues from the `alliswell-coder/qa-ai-agent` repository:

```bash
# Test with issue #7 (Proceed to Checkout 404 Error)
.venv\Scripts\python.exe main.py 7

# Test with issue #8 (Add to Cart functionality)
.venv\Scripts\python.exe main.py 8
```

Or use the Streamlit UI and enter different issue numbers.

## Important Configuration Notes

### Python Version
- **Must use Python 3.13** for compatibility with all dependencies
- Python 3.14 has compatibility issues with some packages (tiktoken, regex)
- Python 3.11-3.12 may also work but 3.13 is recommended

### AI Provider
- **Currently using Groq** (free tier available) with `llama-3.1-8b-instant` model
- Previously attempted Anthropic (organization disabled) and OpenAI (quota issues)
- Groq provides free API access with good performance

### Model Configuration
- Current model: `llama-3.1-8b-instant` (Groq)
- Base URL: `https://api.groq.com/openai/v1`
- This model is fast, free, and suitable for test generation tasks

## Troubleshooting

### Python Version Issues
**Error: ModuleNotFoundError or compilation errors**
- Ensure you're using Python 3.13: `py --list`
- Recreate virtual environment with correct Python version
- Delete `.venv` folder and recreate with `py -3.13 -m venv .venv`

### Groq Model Issues
**Error: Model not found or decommissioned**
- Current working model: `llama-3.1-8b-instant`
- If model becomes unavailable, check https://console.groq.com/docs/deprecations
- Update model name in `crew.py` line 21

### GitHub API Issues
**Error: GitHub API rate limit**
- Wait for rate limit to reset (typically 1 hour)
- Ensure your GitHub token has proper permissions

**Error: Issue not found**
- Verify the issue number exists in your repository
- Check GitHub owner and repository name in `.env`

### Streamlit UI Issues
**Error: Streamlit not opening at localhost:8501**
- Ensure Streamlit is running: Check terminal for "You can now view your Streamlit app"
- If email prompt appears, press Enter to skip
- Try accessing http://localhost:8501 directly in browser

### Python Cache Issues
**Error: Old model being used after code changes**
- Clear Python cache: `Remove-Item -Recurse -Force __pycache__`
- Restart the application

### Environment Variable Issues
**Error: API key not found or invalid**
- Verify `.env` file exists in project root
- Check that API keys are correctly formatted
- Ensure no extra spaces or quotes around values

## Technologies Used

- **Crew.ai** - Multi-agent AI framework
- **Groq** - AI model provider (free tier)
- **Llama 3.1 8B Instant** - AI model for agents
- **GitHub API** - Fetch issue details
- **Streamlit** - Web UI
- **Python 3.13** - Core language

## Migration History

This project went through several AI provider configurations:
1. **Anthropic** - Organization disabled, switched to OpenAI
2. **OpenAI** - Quota exceeded, switched to Groq
3. **Groq** - Currently working with free tier

## License

MIT License

## Contributing

This is a demonstration project for Crew.ai multi-agent systems. Feel free to extend it with additional features or agents.
