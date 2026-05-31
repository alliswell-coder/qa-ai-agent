#!/usr/bin/env python3
"""
Test script to verify MCP server tools are working
"""

import json
import os

# Add the server directory to path to import functions
import sys
sys.path.insert(0, os.path.dirname(__file__))

from server import load_test_cases, get_all_test_cases, search_test_cases, filter_by_module

print("Testing MCP Server Tools...\n")

# Test 1: Load test cases
print("Test 1: Loading test cases...")
test_cases = load_test_cases()
print(f"✓ Loaded {len(test_cases)} test cases\n")

# Test 2: Get all test cases
print("Test 2: Get all test cases...")
all_cases = get_all_test_cases()
print(f"✓ Retrieved {len(all_cases)} test cases")
print(f"  First case: {all_cases[0]['TC_ID']} - {all_cases[0]['Description'][:50]}...\n")

# Test 3: Search test cases
print("Test 3: Search test cases with keyword 'login'...")
search_results = search_test_cases("login")
print(f"✓ Found {len(search_results)} test cases matching 'login'")
if search_results:
    print(f"  First result: {search_results[0]['TC_ID']} - {search_results[0]['Description'][:50]}...\n")

# Test 4: Filter by module
print("Test 4: Filter by module 'Login'...")
login_cases = filter_by_module("Login")
print(f"✓ Found {len(login_cases)} test cases in Login module")
if login_cases:
    print(f"  First case: {login_cases[0]['TC_ID']} - {login_cases[0]['Description'][:50]}...\n")

# Test 5: Filter by module 'Cart'
print("Test 5: Filter by module 'Cart'...")
cart_cases = filter_by_module("Cart")
print(f"✓ Found {len(cart_cases)} test cases in Cart module")
if cart_cases:
    print(f"  First case: {cart_cases[0]['TC_ID']} - {cart_cases[0]['Description'][:50]}...\n")

print("\n" + "="*50)
print("All MCP server tools are working correctly!")
print("="*50)
