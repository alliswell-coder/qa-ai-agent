"""
Main entry point for Crew.ai Test Generation System
Takes GitHub issue number as input and generates test artifacts
"""

import sys
import argparse
from crew import create_crew


def main():
    """Main function to run the test generation crew"""
    parser = argparse.ArgumentParser(
        description="Generate test artifacts from GitHub issues using Crew.ai"
    )
    parser.add_argument(
        "issue_number",
        type=int,
        help="GitHub issue number to analyze"
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Enable verbose output"
    )
    
    args = parser.parse_args()
    
    print("="*60)
    print("Crew.ai Test Generation System")
    print("="*60)
    print(f"Analyzing GitHub Issue: #{args.issue_number}")
    print("="*60)
    print()
    
    try:
        # Create and run the crew
        crew = create_crew(args.issue_number)
        result = crew.kickoff()
        
        print()
        print("="*60)
        print("✓ Test Generation Complete!")
        print("="*60)
        print(f"Generated files:")
        print("  - output/test_plan.md")
        print("  - output/test_cases.md")
        print("  - output/playwright_tests.md")
        print()
        
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
