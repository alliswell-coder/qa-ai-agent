# Project4 - MCP Test Cases Server

An MCP (Model Context Protocol) server for managing and querying QA test cases for Amazon Checkout Flow.

## Overview

This project provides:
- **500 structured test cases** for Amazon Checkout Flow across 10 modules
- **MCP Server** with FastMCP for AI assistant integration
- **Multiple output formats**: JSON, Excel with merged cells, HTML grid view
- **Local web interface** for testing MCP tools

## Project Structure

```
Project4-MCP-TC5000/
├── data/
│   ├── generate_test_cases.py    # Script to generate test cases
│   ├── convert_to_excel.py       # Convert JSON to Excel with merged cells
│   ├── test_cases.json           # 500 test cases in JSON format
│   ├── test_cases_readable_new.xlsx  # Excel with merged cells format
│   ├── test_cases_grid.html      # HTML grid view with filtering
│   └── test_cases.csv            # CSV format (legacy)
└── server/
    ├── server.py                 # MCP server with FastMCP
    ├── requirements.txt          # Python dependencies
    ├── claude_desktop_config.json # Claude Desktop configuration
    ├── local_test.py             # Local web interface for testing
    └── test_mcp.py               # Test script for MCP tools
```

## Features

### Test Case Generation
- 500 unique test cases across 10 modules
- Each test case has 4-6 steps with "should" language
- Modules: Login, Cart, Address, Delivery, Payment, Order Review, Order Confirmation, Edge Cases, Negative Cases, Performance

### MCP Server Tools
- `get_all_test_cases()` - Returns all 500 test cases
- `search_test_cases(keyword)` - Search by description
- `filter_by_module(module)` - Filter by module name
- `filter_by_priority(priority)` - Filter by priority level
- `filter_by_status(status)` - Filter by execution status

### Output Formats
- **JSON**: Structured format for programmatic access
- **Excel**: Merged cells format with TC_ID, Scenario, Description spanning step rows
- **HTML**: Interactive grid view with filtering capabilities

## Installation

### Prerequisites
- Python 3.8+
- pip

### Setup

1. **Install dependencies for MCP server**:
```bash
cd server
pip install -r requirements.txt
```

2. **Install dependencies for Excel conversion**:
```bash
cd data
pip install openpyxl
```

3. **Install Flask for local testing** (optional):
```bash
cd server
pip install flask
```

## Usage

### Generate Test Cases

```bash
cd data
python generate_test_cases.py
```

This creates `test_cases.json` with 500 test cases.

### Convert to Excel

```bash
cd data
python convert_to_excel.py
```

This creates `test_cases_readable_new.xlsx` with merged cells format.

### Run MCP Server

```bash
cd server
python server.py
```

The server will start and listen for MCP connections via stdio.

### Test MCP Tools

**Option 1: Test script**
```bash
cd server
python test_mcp.py
```

**Option 2: Local web interface**
```bash
cd server
python local_test.py
```
Then open http://localhost:5000 in your browser.

### Connect to Claude Desktop

1. Copy contents of `server/claude_desktop_config.json`
2. Add to your Claude Desktop settings:
   - Windows: `%APPDATA%\Claude\claude_desktop_config.json`
   - Mac: `~/Library/Application Support/Claude/claude_desktop_config.json`
3. Restart Claude Desktop

## Deployment

### Vercel Deployment

**❌ Not recommended for this project**

**Why Vercel is not suitable:**
- Vercel is designed for static sites and serverless functions
- MCP server uses stdio transport, which requires persistent connections
- Python MCP servers need to run as long-running processes
- Vercel's serverless model doesn't support stdio-based MCP servers

### Recommended Deployment Options

**1. Self-hosted (Recommended)**
- VPS (DigitalOcean, AWS EC2, Google Cloud)
- Run MCP server as a systemd service
- Use nginx as reverse proxy if needed

**2. Railway.app**
- Supports Python applications
- Can run MCP server with proper configuration
- Better for long-running processes than Vercel

**3. Render.com**
- Free tier for Python web services
- Supports persistent processes
- Good alternative to Vercel for this use case

**4. Docker**
- Containerize the MCP server
- Deploy to any cloud provider
- Easy scaling and management

### Example: Railway.app Deployment

1. Create a new Railway project
2. Connect your GitHub repository
3. Set environment variables if needed
4. Deploy - Railway will detect Python and install dependencies
5. Update Claude Desktop config to use Railway URL

## Test Case Format

Each test case includes:
- **TC_ID**: Unique identifier (TC001-TC500)
- **Scenario**: Module name (Login, Cart, etc.)
- **Description**: Test case description with "should" language
- **Steps**: Array of steps with:
  - Action: The step action
  - Expected: Expected result with "should" language
- **Actual Result**: Empty field for execution results
- **Status**: Empty field for execution status

## Modules Covered

1. **Login** (50 test cases)
2. **Cart** (50 test cases)
3. **Address** (50 test cases)
4. **Delivery** (50 test cases)
5. **Payment** (50 test cases)
6. **Order Review** (50 test cases)
7. **Order Confirmation** (50 test cases)
8. **Edge Cases** (50 test cases)
9. **Negative Cases** (50 test cases)
10. **Performance** (50 test cases)

## Technologies Used

- **Python**: Core language
- **FastMCP**: MCP server framework
- **openpyxl**: Excel file generation
- **Flask**: Local web interface
- **JSON**: Data storage format

## Contributing

This is a demonstration project for MCP server implementation. Feel free to extend it with additional features.

## License

MIT License
