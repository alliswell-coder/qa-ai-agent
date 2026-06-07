"""
Crew.ai Test Generation System
4-agent workflow: GitHub Issue → Requirements → Test Plan → Test Cases → Playwright Scripts
"""

import os
import requests
from crewai import Agent, Task, Crew, LLM
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# GitHub API configuration
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GITHUB_OWNER = os.getenv("GITHUB_OWNER")
GITHUB_REPO = os.getenv("GITHUB_REPO")

# Configure Groq LLM for Crew.ai
groq_llm = LLM(
    model="llama-3.1-8b-instant",
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)


def get_github_issue(issue_number: int) -> dict:
    """Fetch GitHub issue details using GitHub API"""
    url = f"https://api.github.com/repos/{GITHUB_OWNER}/{GITHUB_REPO}/issues/{issue_number}"
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()


# Define Agents
github_analyst = Agent(
    role="GitHub Issue Analyst",
    goal="Analyze GitHub issues to extract detailed requirements for testing",
    backstory="""You are an expert requirements analyst specializing in software testing.
    You can extract functional requirements, acceptance criteria, and test scope from GitHub issues.
    You provide clear, structured analysis that serves as the foundation for test planning.""",
    verbose=True,
    allow_delegation=False,
    llm=groq_llm
)

test_planner = Agent(
    role="Test Planning Specialist",
    goal="Create comprehensive test plans with 12 standard sections based on requirements analysis",
    backstory="""You are a senior QA engineer with 10+ years of experience in test planning.
    You create detailed, professional test plans that cover all aspects of testing.
    Your test plans follow industry best practices and include all necessary sections for thorough testing.""",
    verbose=True,
    allow_delegation=False,
    llm=groq_llm
)

test_case_writer = Agent(
    role="Test Case Writer",
    goal="Write detailed, structured test cases based on requirements and test plan",
    backstory="""You are an expert test case writer with deep knowledge of testing methodologies.
    You create clear, actionable test cases with proper steps, expected results, and coverage.
    Your test cases are comprehensive and follow industry standards.
    
    IMPORTANT: Test cases must be in a grid/table format with these specific columns:
    - Test Case ID
    - Description
    - Steps (each step listed separately)
    - Expected Result (for each step)
    - Actual Result
    
    Each Expected Result MUST have a specific value (not generic text like "should work").
    Example: "User should see cart page" instead of "Page should load".""",
    verbose=True,
    allow_delegation=False,
    llm=groq_llm
)

playwright_developer = Agent(
    role="Playwright Test Developer",
    goal="Generate TypeScript Playwright automation scripts from test cases",
    backstory="""You are a skilled automation engineer specializing in Playwright.
    You convert test cases into robust, maintainable Playwright test scripts in TypeScript.
    Your scripts follow best practices and include proper selectors, assertions, and error handling.""",
    verbose=True,
    allow_delegation=False,
    llm=groq_llm
)


def create_crew(issue_number: int) -> Crew:
    """Create and return the Crew with all agents and tasks for a specific GitHub issue"""
    
    # Fetch GitHub issue
    issue_data = get_github_issue(issue_number)
    issue_title = issue_data['title']
    issue_body = issue_data.get('body', '')
    issue_url = issue_data['html_url']
    
    # Define Tasks
    task1 = Task(
        description=f"""Analyze the GitHub issue and extract detailed requirements.
        
        GitHub Issue: {issue_title}
        URL: {issue_url}
        
        Issue Description:
        {issue_body}
        
        Extract and document:
        1. Functional requirements
        2. Acceptance criteria
        3. Test scope and boundaries
        4. Key features to test
        5. Any constraints or assumptions
        
        Provide a comprehensive requirements analysis that will guide test planning.""",
        agent=github_analyst,
        expected_output="Detailed requirements analysis document with functional requirements, acceptance criteria, and test scope"
    )
    
    task2 = Task(
        description="""Create a comprehensive test plan based on the requirements analysis.
        
        The test plan MUST include these 12 sections:
        1. Test Scope - What features/functionality will be tested
        2. Test Strategy - Approach, methodologies, testing types
        3. Test Environment - Hardware, software, network requirements
        4. Test Schedule - Timeline, milestones, deadlines
        5. Resources Required - Team, tools, equipment needed
        6. Test Deliverables - Documents, reports, artifacts to be produced
        7. Risk Assessment - Potential risks, mitigation strategies
        8. Entry Criteria - Prerequisites before testing starts
        9. Exit Criteria - Conditions for test completion
        10. Test Cases Overview - Summary of test cases, coverage
        11. Defect Reporting - Bug tracking, severity classification
        12. Sign-off Process - Approval workflow, stakeholders
        
        Use the requirements analysis from the previous task to make each section relevant and specific.""",
        agent=test_planner,
        context=[task1],
        expected_output="Complete test plan with 12 sections in markdown format",
        output_file="output/test_plan.md"
    )
    
    task3 = Task(
        description="""Write detailed test cases based on the requirements analysis and test plan.
        
        CRITICAL: Test cases MUST be in a grid/table format with these exact columns:
        | Test Case ID | Description | Steps | Expected Result | Actual Result |
        
        For each test case:
        - Test Case ID (e.g., TC001, TC002)
        - Description - Brief overview of what is being tested
        - Steps - Each step listed separately in the Steps column
        - Expected Result - Specific value for each step (not generic text like "should work")
        - Actual Result - Leave blank for execution
        
        IMPORTANT: Each Expected Result MUST have a specific value.
        Example: "User should see cart page with items" instead of "Page should load"
        
        Ensure test cases cover:
        - Happy path scenarios
        - Edge cases
        - Negative scenarios
        - Error handling
        - Boundary conditions
        
        Use the requirements analysis and test plan as context to ensure comprehensive coverage.""",
        agent=test_case_writer,
        context=[task1, task2],
        expected_output="Detailed test cases table in markdown format with all required fields",
        output_file="output/test_cases.md"
    )
    
    task4 = Task(
        description="""Generate TypeScript Playwright test scripts based on the test cases.
        
        For each test case, create a Playwright test script that:
        - Uses TypeScript
        - Includes proper page object model or selectors
        - Has clear test steps matching the test case
        - Includes assertions for expected results
        - Handles errors gracefully
        - Follows Playwright best practices
        - Uses descriptive test names
        
        Structure:
        - Import necessary Playwright modules
        - Define test fixtures
        - Write test functions for each test case
        - Include proper setup and teardown
        - Add comments for clarity
        
        Ensure the scripts are production-ready and maintainable.""",
        agent=playwright_developer,
        context=[task3],
        expected_output="TypeScript Playwright test scripts in markdown format",
        output_file="output/playwright_tests.md"
    )
    
    # Create Crew
    crew = Crew(
        agents=[github_analyst, test_planner, test_case_writer, playwright_developer],
        tasks=[task1, task2, task3, task4],
        process="sequential",
        verbose=True
    )
    
    return crew


if __name__ == "__main__":
    # Example usage
    issue_number = 1  # Replace with actual GitHub issue number
    crew = create_crew(issue_number)
    result = crew.kickoff()
    print("\n" + "="*50)
    print("Test Generation Complete!")
    print("="*50)
    print(f"Generated files:")
    print("- output/test_plan.md")
    print("- output/test_cases.md")
    print("- output/playwright_tests.md")
