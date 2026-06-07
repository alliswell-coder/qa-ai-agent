# Test Cases Template

## Test Case Format

Each test case should include the following fields:

| TC_ID | Title | Description | Preconditions | Test Steps | Expected Results | Priority |
|-------|-------|-------------|----------------|------------|------------------|----------|
| TC001 | [Test case title] | [Description of what is being tested] | [Conditions that must be met before test execution] | 1. [Step 1]<br>2. [Step 2]<br>3. [Step 3] | [Expected outcome after executing test steps] | High/Medium/Low |

## Test Case Categories

- **Happy Path**: Normal flow scenarios
- **Edge Cases**: Boundary conditions and unusual inputs
- **Negative Scenarios**: Error handling and invalid inputs
- **Security Tests**: Authentication, authorization, data protection
- **Performance Tests**: Load, stress, and response time
- **UI/UX Tests**: User interface and user experience

## Example Test Case

| TC_ID | Title | Description | Preconditions | Test Steps | Expected Results | Priority |
|-------|-------|-------------|----------------|------------|------------------|----------|
| TC001 | User Login with Valid Credentials | Verify user can login with correct username and password | User account exists and is active | 1. Navigate to login page<br>2. Enter valid username<br>3. Enter valid password<br>4. Click login button | User is redirected to dashboard and sees welcome message | High |
