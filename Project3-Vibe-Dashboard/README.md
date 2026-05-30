# Project3 - Vibe Dashboard

A modern QA Dashboard for tracking Amazon Checkout Flow test results.

## Features

- **Summary Cards**: Displays total test cases, pass/fail counts, and pass rate
- **Failed Tests Table**: Detailed view of failed test cases with:
  - TC ID
  - Description
  - Actual Result
  - Priority
  - GitHub Issue links
- **Modern Dark Theme**: Clean, professional design with gradient background
- **Responsive Design**: Works on desktop and mobile devices

## Test Summary

- **Total TCs**: 7
- **Pass**: 2
- **Fail**: 5
- **Pass Rate**: 28%

## Failed Tests

| TC ID | Description | Actual Result | Priority | GitHub Issue |
|-------|-------------|---------------|----------|--------------|
| TC003 | Proceed to Checkout | 404 Error | High | [Issue #7](https://github.com/alliswell-coder/qa-ai-agent/issues/7) |
| TC004 | Empty Cart | Cart count wrong | High | [Issue #8](https://github.com/alliswell-coder/qa-ai-agent/issues/8) |
| TC046 | Saved Credit Card | No card displayed | High | [Issue #9](https://github.com/alliswell-coder/qa-ai-agent/issues/9) |
| TC007 | Payment Declined | App crashes | High | [Issue #11](https://github.com/alliswell-coder/qa-ai-agent/issues/11) |

## How to Use

1. Open `index.html` in a web browser
2. View the dashboard with test results and failed test details
3. Click on GitHub Issue links to view detailed bug reports

## Color Scheme

- **Green**: Pass status
- **Red**: Fail status
- **Blue**: Total count
- **Orange**: Pass rate

## Technologies Used

- HTML5
- CSS3 (Flexbox, Grid, CSS Variables)
- No external dependencies - pure HTML/CSS
