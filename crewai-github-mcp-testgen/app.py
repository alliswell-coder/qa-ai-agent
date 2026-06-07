"""
Streamlit UI for Crew.ai Test Generation System
Provides web interface for generating test artifacts from GitHub issues
"""

import streamlit as st
import os
from crew import create_crew


def main():
    st.set_page_config(
        page_title="Crew.ai Test Generator",
        page_icon="🧪",
        layout="wide"
    )
    
    st.title("🧪 Crew.ai Test Generation System")
    st.markdown("---")
    
    # Sidebar configuration
    st.sidebar.header("Configuration")
    
    # GitHub issue input
    issue_number = st.sidebar.number_input(
        "GitHub Issue Number",
        min_value=1,
        value=1,
        step=1,
        help="Enter the GitHub issue number to analyze"
    )
    
    # Display current configuration
    st.sidebar.markdown("---")
    st.sidebar.subheader("Current Configuration")
    st.sidebar.text(f"Issue: #{issue_number}")
    
    # Main content area
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("Generate Test Artifacts")
        st.markdown("""
        This system will generate:
        - **Test Plan** (12 sections)
        - **Test Cases** (detailed with steps)
        - **Playwright Scripts** (TypeScript automation)
        
        from a GitHub issue using 4 AI agents.
        """)
    
    with col2:
        st.subheader("Workflow")
        st.markdown("""
        1. 📋 Analyze GitHub Issue
        2. 📝 Create Test Plan
        3. ✍️ Write Test Cases
        4. 🎭 Generate Playwright Scripts
        """)
    
    # Generate button
    st.markdown("---")
    if st.button("🚀 Generate Test Artifacts", type="primary", use_container_width=True):
        with st.spinner("Generating test artifacts... This may take a few minutes."):
            try:
                # Create and run the crew
                crew = create_crew(issue_number)
                result = crew.kickoff()
                
                # Success message
                st.success("✅ Test Generation Complete!")
                st.markdown("---")
                
                # Display generated files
                st.subheader("📁 Generated Files")
                
                # Test Plan
                if os.path.exists("output/test_plan.md"):
                    with open("output/test_plan.md", "r", encoding="utf-8") as f:
                        test_plan_content = f.read()
                    
                    with st.expander("📋 Test Plan", expanded=True):
                        st.markdown(test_plan_content)
                        st.download_button(
                            label="Download Test Plan",
                            data=test_plan_content,
                            file_name="test_plan.md",
                            mime="text/markdown"
                        )
                
                # Test Cases
                if os.path.exists("output/test_cases.md"):
                    with open("output/test_cases.md", "r", encoding="utf-8") as f:
                        test_cases_content = f.read()
                    
                    with st.expander("✍️ Test Cases", expanded=True):
                        st.markdown(test_cases_content)
                        st.download_button(
                            label="Download Test Cases",
                            data=test_cases_content,
                            file_name="test_cases.md",
                            mime="text/markdown"
                        )
                
                # Playwright Scripts
                if os.path.exists("output/playwright_tests.md"):
                    with open("output/playwright_tests.md", "r", encoding="utf-8") as f:
                        playwright_content = f.read()
                    
                    with st.expander("🎭 Playwright Scripts", expanded=True):
                        st.markdown(playwright_content)
                        st.download_button(
                            label="Download Playwright Scripts",
                            data=playwright_content,
                            file_name="playwright_tests.md",
                            mime="text/markdown"
                        )
                
            except Exception as e:
                st.error(f"❌ Error: {e}")
                st.markdown("""
                **Troubleshooting:**
                - Ensure `.env` file is configured correctly
                - Check GitHub token has proper permissions
                - Verify GitHub issue number exists
                - Check OpenAI API key is valid
                """)
    
    # Instructions
    st.markdown("---")
    st.subheader("📖 Instructions")
    with st.expander("How to use"):
        st.markdown("""
        1. **Configure .env file**:
           - Add your GitHub token
           - Add your OpenAI API key
           - Set GitHub owner and repository
        
        2. **Enter GitHub Issue Number**:
           - Find the issue number from GitHub
           - Enter it in the sidebar
        
        3. **Click Generate**:
           - Click the "Generate Test Artifacts" button
           - Wait for the AI agents to complete
           - Review and download the generated files
        
        4. **Review Outputs**:
           - Check the test plan for completeness
           - Verify test cases cover requirements
           - Review Playwright scripts for accuracy
        """)


if __name__ == "__main__":
    main()
