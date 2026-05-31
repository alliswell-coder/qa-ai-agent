#!/usr/bin/env python3
"""
QA Test Cases MCP Server
An MCP server for managing and querying QA test cases for Amazon Checkout Flow.
"""

import json
import os
from typing import List, Dict, Any, Optional
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("QA Test Cases MCP")

# Path to test cases JSON file
TEST_CASES_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "test_cases.json")


def load_test_cases() -> List[Dict[str, Any]]:
    """Load test cases from JSON file."""
    try:
        with open(TEST_CASES_PATH, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []


@mcp.tool()
def get_all_test_cases() -> List[Dict[str, Any]]:
    """
    Get all test cases from the test cases database.
    
    Returns:
        List of all test cases with their full details including TC_ID, Scenario, Description, Steps, Expected Results, etc.
    """
    test_cases = load_test_cases()
    return test_cases


@mcp.tool()
def search_test_cases(keyword: str) -> List[Dict[str, Any]]:
    """
    Search test cases by keyword in title or description.
    
    Args:
        keyword: The search term to look for in test case descriptions
    
    Returns:
        List of test cases that match the search keyword in their description
    """
    test_cases = load_test_cases()
    keyword_lower = keyword.lower()
    
    filtered = [
        tc for tc in test_cases
        if keyword_lower in tc.get('Description', '').lower()
    ]
    
    return filtered


@mcp.tool()
def filter_by_module(module: str) -> List[Dict[str, Any]]:
    """
    Filter test cases by module (scenario).
    
    Args:
        module: The module name to filter by (e.g., "Login", "Cart", "Payment")
    
    Returns:
        List of test cases belonging to the specified module
    """
    test_cases = load_test_cases()
    
    filtered = [
        tc for tc in test_cases
        if tc.get('Scenario', '').lower() == module.lower()
    ]
    
    return filtered


@mcp.tool()
def filter_by_priority(priority: str) -> List[Dict[str, Any]]:
    """
    Filter test cases by priority level.
    
    Args:
        priority: The priority level to filter by ("High", "Medium", "Low")
    
    Returns:
        List of test cases with the specified priority level
    """
    test_cases = load_test_cases()
    
    # Note: Current format doesn't have priority field, returning all test cases
    # This can be updated when priority is added to the test case structure
    filtered = [
        tc for tc in test_cases
        if tc.get('priority', '').lower() == priority.lower()
    ]
    
    return filtered


@mcp.tool()
def filter_by_status(status: str) -> List[Dict[str, Any]]:
    """
    Filter test cases by execution status.
    
    Args:
        status: The status to filter by ("Pass", "Fail", "Not Executed")
    
    Returns:
        List of test cases with the specified status
    """
    test_cases = load_test_cases()
    
    # Note: Current format doesn't have status field, returning all test cases
    # This can be updated when status is added to the test case structure
    filtered = [
        tc for tc in test_cases
        if tc.get('status', '').lower() == status.lower()
    ]
    
    return filtered


if __name__ == "__main__":
    # Run the MCP server
    mcp.run()
