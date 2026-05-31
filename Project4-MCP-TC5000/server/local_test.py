#!/usr/bin/env python3
"""
Local web interface to test MCP server tools
Run this and open http://localhost:5000 in your browser
"""

from flask import Flask, render_template_string, request, jsonify
import sys
import os

# Add the server directory to path to import functions
sys.path.insert(0, os.path.dirname(__file__))

from server import get_all_test_cases, search_test_cases, filter_by_module

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>MCP Server Local Test</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 1200px; margin: 0 auto; padding: 20px; }
        h1 { color: #333; }
        .tool-section { margin: 20px 0; padding: 20px; border: 1px solid #ddd; border-radius: 8px; }
        .tool-section h2 { color: #4472C4; margin-top: 0; }
        input, select, button { padding: 10px; margin: 5px; border: 1px solid #ddd; border-radius: 4px; }
        button { background: #4472C4; color: white; cursor: pointer; }
        button:hover { background: #3355AA; }
        .results { margin-top: 15px; padding: 15px; background: #f5f5f5; border-radius: 4px; }
        .test-case { margin: 10px 0; padding: 10px; background: white; border-left: 4px solid #4472C4; }
        .tc-id { font-weight: bold; color: #4472C4; }
        .tc-desc { margin: 5px 0; }
        .tc-meta { color: #666; font-size: 0.9em; }
        pre { background: #f0f0f0; padding: 10px; overflow-x: auto; }
    </style>
</head>
<body>
    <h1>🧪 MCP Server Local Test Interface</h1>
    
    <div class="tool-section">
        <h2>📊 Get All Test Cases</h2>
        <button onclick="getAllTestCases()">Get All Test Cases</button>
        <div id="all-results" class="results"></div>
    </div>
    
    <div class="tool-section">
        <h2>🔍 Search Test Cases</h2>
        <input type="text" id="search-keyword" placeholder="Enter keyword (e.g., 'login')">
        <button onclick="searchTestCases()">Search</button>
        <div id="search-results" class="results"></div>
    </div>
    
    <div class="tool-section">
        <h2>📁 Filter by Module</h2>
        <select id="module-select">
            <option value="">Select Module</option>
            <option value="Login">Login</option>
            <option value="Cart">Cart</option>
            <option value="Address">Address</option>
            <option value="Delivery">Delivery</option>
            <option value="Payment">Payment</option>
            <option value="Order Review">Order Review</option>
            <option value="Order Confirmation">Order Confirmation</option>
            <option value="Edge Cases">Edge Cases</option>
            <option value="Negative Cases">Negative Cases</option>
            <option value="Performance">Performance</option>
        </select>
        <button onclick="filterByModule()">Filter</button>
        <div id="module-results" class="results"></div>
    </div>
    
    <script>
        function getAllTestCases() {
            fetch('/api/all')
                .then(r => r.json())
                .then(data => displayResults(data, 'all-results'));
        }
        
        function searchTestCases() {
            const keyword = document.getElementById('search-keyword').value;
            if (!keyword) return alert('Please enter a keyword');
            fetch('/api/search?keyword=' + encodeURIComponent(keyword))
                .then(r => r.json())
                .then(data => displayResults(data, 'search-results'));
        }
        
        function filterByModule() {
            const module = document.getElementById('module-select').value;
            if (!module) return alert('Please select a module');
            fetch('/api/filter/module?module=' + encodeURIComponent(module))
                .then(r => r.json())
                .then(data => displayResults(data, 'module-results'));
        }
        
        function displayResults(data, elementId) {
            const container = document.getElementById(elementId);
            if (data.length === 0) {
                container.innerHTML = '<p>No results found</p>';
                return;
            }
            
            let html = `<p>Found ${data.length} test cases</p>`;
            data.slice(0, 10).forEach(tc => {
                html += `
                    <div class="test-case">
                        <div class="tc-id">${tc.TC_ID} - ${tc.Scenario}</div>
                        <div class="tc-desc">${tc.Description}</div>
                        <div class="tc-meta">${tc.steps.length} steps</div>
                    </div>
                `;
            });
            
            if (data.length > 10) {
                html += `<p>... and ${data.length - 10} more</p>`;
            }
            
            container.innerHTML = html;
        }
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

@app.route('/api/all')
def api_all():
    return jsonify(get_all_test_cases())

@app.route('/api/search')
def api_search():
    keyword = request.args.get('keyword', '')
    return jsonify(search_test_cases(keyword))

@app.route('/api/filter/module')
def api_filter_module():
    module = request.args.get('module', '')
    return jsonify(filter_by_module(module))

if __name__ == '__main__':
    print("Starting local MCP test interface...")
    print("Open http://localhost:5000 in your browser")
    app.run(debug=True, port=5000)
