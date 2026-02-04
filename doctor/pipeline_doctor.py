import re
import sys
import argparse

# Define common CI/CD error patterns and their suggestions
ERROR_PATTERNS = [
    {
        "pattern": r"ModuleNotFoundError: No module named '([^']+)'",
        "suggestion": "Suggestion: The module '{0}' is missing. Try running 'pip install {0}' or adding it to requirements.txt.",
        "category": "Missing Dependency"
    },
    {
        "pattern": r"ImportError: cannot import name '([^']+)'",
        "suggestion": "Suggestion: Could not import '{0}'. Check if the name is correct or if there's a circular dependency.",
        "category": "Import Error"
    },
    {
        "pattern": r"Permission denied",
        "suggestion": "Suggestion: Permission denied. Try checking file permissions or using 'chmod +x' on the script.",
        "category": "Permission Error"
    },
    {
        "pattern": r"FileNotFoundError: \[Errno 2\] No such file or directory: '([^']+)'",
        "suggestion": "Suggestion: The file '{0}' was not found. Verify the file path and ensure it exists in the repository.",
        "category": "File Not Found"
    },
    {
        "pattern": r"SyntaxError: invalid syntax",
        "suggestion": "Suggestion: There is a syntax error in your code. Check for missing colons, brackets, or typos.",
        "category": "Syntax Error"
    },
    {
        "pattern": r"IndentationError: expected an indented block",
        "suggestion": "Suggestion: Fix the indentation in your code. Python is strict about whitespace.",
        "category": "Indentation Error"
    }
]

def analyze_logs(log_content):
    print("\n--- 🩺 Pipeline Doctor Analysis ---")
    found_issues = False
    
    for entry in ERROR_PATTERNS:
        matches = re.findall(entry["pattern"], log_content)
        if matches:
            found_issues = True
            for match in matches:
                # If match is a tuple (e.g. from multiple groups), format with all groups
                if isinstance(match, tuple):
                    suggestion = entry["suggestion"].format(*match)
                else:
                    suggestion = entry["suggestion"].format(match)
                
                print(f"[{entry['category']}] Detected!")
                print(f"👉 {suggestion}\n")
    
    if not found_issues:
        print("✅ No common issues detected. You might need to check the logs manually.")
    
    print("-----------------------------------\n")

def main():
    parser = argparse.ArgumentParser(description="Pipeline Doctor - Analyze CI/CD logs for common errors.")
    parser.add_argument("log_file", help="Path to the log file to analyze")
    args = parser.parse_args()

    try:
        with open(args.log_file, "r") as f:
            content = f.read()
            analyze_logs(content)
    except FileNotFoundError:
        print(f"Error: Log file '{args.log_file}' not found.")
        sys.exit(1)

if __name__ == "__main__":
    main()
