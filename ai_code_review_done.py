import re

def analyze_code_quality(code_snippet):
    """Simulates AI code analysis to identify potential issues.

    This function represents a simplified AI code reviewer.
    It checks for common issues like unused variables, missing docstrings,
    and basic style violations.
    """
    issues = []
    lines = code_snippet.splitlines()

    # Basic check for unused variables (simplified)
    # In a real AI, this would be much more sophisticated.
    defined_vars = set()
    used_vars = set()
    for line in lines:
        # Detect variable definitions (very basic regex)
        match_def = re.search(r'\b(var|let|const|def|\w+)\s+(\w+)', line)
        if match_def:
            defined_vars.add(match_def.group(2))

        # Detect variable usage (very basic regex)
        for var in defined_vars:
            if re.search(r'\b' + re.escape(var) + r'\b', line) and not match_def:
                used_vars.add(var)

    unused = defined_vars - used_vars
    if unused:
        issues.append(f"Potential unused variables: {', '.join(unused)}")

    # Check for missing docstrings for functions
    in_function = False
    for i, line in enumerate(lines):
        if line.strip().startswith('def '):
            in_function = True
            # Look ahead for docstring
            has_docstring = False
            for j in range(i + 1, min(i + 5, len(lines))):
                if '"""' in lines[j] or "'''" in lines[j]:
                    has_docstring = True
                    break
            if not has_docstring:
                issues.append(f"Function defined on line {i+1} might be missing a docstring.")
        elif in_function and not line.strip(): # End of function block (simplified)
            in_function = False

    # Basic check for overly long lines
    for i, line in enumerate(lines):
        if len(line) > 100:
            issues.append(f"Line {i+1} is too long ({len(line)} characters).")

    return issues

def is_code_done(code_snippet):
    """Determines if the code is 'done' based on AI analysis.

    'Done' here is defined as having no critical issues identified by the AI.
    This is a simplified definition; real-world 'done' involves many more factors.
    """
    issues = analyze_code_quality(code_snippet)
    if not issues:
        return True, "No critical issues found by the AI."
    else:
        return False, "\n".join(issues)

# --- Example Usage ---

# Code snippet that might be considered 'done' by a simple AI reviewer
clean_code = """
def greet(name):
    """Greets the user by name."""
    message = f"Hello, {name}!"
    print(message)

if __name__ == "__main__":
    greet("World")
"""

# Code snippet with potential issues
problematic_code = """
def calculate_sum(a, b):
    result = a + b
    # Missing docstring
    print(result)

    # This variable is defined but not used
    unused_var = 100

    # Example of a very long line that might exceed typical limits
    long_variable_name_that_is_very_long_and_makes_the_line_exceed_standard_coding_guidelines_for_line_length = a * b * result
    print(long_variable_name_that_is_very_long_and_makes_the_line_exceed_standard_coding_guidelines_for_line_length)

if __name__ == "__main__":
    calculate_sum(5, 10)
"""

print("--- Analyzing Clean Code ---")
done_clean, message_clean = is_code_done(clean_code)
print(f"Is 'done': {done_clean}\n{message_clean}\n")

print("--- Analyzing Problematic Code ---")
done_problematic, message_problematic = is_code_done(problematic_code)
print(f"Is 'done': {done_problematic}\n{message_problematic}\n")

print("\nNote: The definition of 'done' is simplified. Real AI tools and human review consider many more factors.")
