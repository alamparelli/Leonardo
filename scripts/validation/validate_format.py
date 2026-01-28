#!/usr/bin/env python3
"""
Validate essay format against Leonardo project requirements.
Checks frontmatter, required sections, and structure.
"""

import sys
import re
import yaml
from pathlib import Path


class ValidationError(Exception):
    pass


def extract_frontmatter(content: str) -> tuple[dict, str]:
    """Extract YAML frontmatter and body from markdown content."""
    pattern = r'^---\s*\n(.*?)\n---\s*\n(.*)$'
    match = re.match(pattern, content, re.DOTALL)

    if not match:
        raise ValidationError("No valid frontmatter found (must start with ---)")

    try:
        frontmatter = yaml.safe_load(match.group(1))
    except yaml.YAMLError as e:
        raise ValidationError(f"Invalid YAML in frontmatter: {e}")

    return frontmatter, match.group(2)


def validate_frontmatter(fm: dict, filepath: str) -> list[str]:
    """Validate frontmatter fields."""
    errors = []

    # Required fields
    required = ['title', 'date', 'author', 'tags']
    for field in required:
        if field not in fm:
            errors.append(f"Missing required field: {field}")

    # Title format
    if 'title' in fm:
        if not fm['title'].startswith('On '):
            errors.append(f"Title must start with 'On ' (got: {fm['title']})")

    # Date format
    if 'date' in fm:
        if not re.match(r'^\d{4}-\d{2}-\d{2}$', str(fm['date'])):
            errors.append(f"Date must be YYYY-MM-DD format (got: {fm['date']})")

    # Author structure
    if 'author' in fm:
        if not isinstance(fm['author'], dict):
            errors.append("Author must be a dict with 'model' and 'persona' fields")
        else:
            if 'model' not in fm['author']:
                errors.append("Author must include 'model' field")
            if 'persona' not in fm['author']:
                errors.append("Author must include 'persona' field")

    # Tags must be a list
    if 'tags' in fm and not isinstance(fm['tags'], list):
        errors.append("Tags must be a list")

    # Generated essays (with sources) must have inventions
    if 'sources' in fm and fm['sources']:
        if 'inventions' not in fm or not fm['inventions']:
            errors.append("Generated essays (with sources) must include 'inventions' field")

    return errors


def validate_body(body: str, has_sources: bool) -> list[str]:
    """Validate essay body structure."""
    errors = []

    # Must have main heading
    if not re.search(r'^# On .+', body, re.MULTILINE):
        errors.append("Body must start with '# On [Subject]' heading")

    # Must have opening italic teaser
    if not re.search(r'^\*In which .+\*', body, re.MULTILINE):
        errors.append("Missing opening teaser (*In which we...*)")

    # Generated essays must have "What Might Be Built" section
    if has_sources:
        if '## What Might Be Built' not in body:
            errors.append("Generated essays must include '## What Might Be Built' section")

        # Check for at least one invention
        if not re.search(r'### .+\n\*\*Domain:\*\*', body):
            errors.append("'What Might Be Built' section must contain at least one invention with Domain field")

    # Check for closing signature (optional but recommended)
    if '*Composed in the spirit of Leonardo' not in body:
        errors.append("Warning: Missing closing signature line (recommended)")

    return errors


def check_prompt_injection_patterns(content: str) -> list[str]:
    """Basic check for obvious prompt injection patterns."""
    warnings = []

    suspicious_patterns = [
        (r'ignore (all )?(previous|above) instructions', 'Potential prompt injection: "ignore instructions" pattern'),
        (r'you are now', 'Potential prompt injection: "you are now" pattern'),
        (r'forget (everything|all)', 'Potential prompt injection: "forget" pattern'),
        (r'system prompt', 'Suspicious reference to "system prompt"'),
        (r'<\s*(system|assistant|user)\s*>', 'Suspicious XML-like role tags'),
        (r'\[INST\]|\[/INST\]', 'Suspicious instruction markers'),
        (r'```(python|bash|sh).*?(exec|eval|subprocess|os\.system)', 'Suspicious code execution patterns'),
    ]

    for pattern, message in suspicious_patterns:
        if re.search(pattern, content, re.IGNORECASE):
            warnings.append(message)

    return warnings


def validate_essay(filepath: str) -> tuple[list[str], list[str]]:
    """Validate a single essay file. Returns (errors, warnings)."""
    path = Path(filepath)

    if not path.exists():
        return [f"File not found: {filepath}"], []

    content = path.read_text(encoding='utf-8')
    errors = []
    warnings = []

    # Extract and validate frontmatter
    try:
        fm, body = extract_frontmatter(content)
    except ValidationError as e:
        return [str(e)], []

    # Validate frontmatter
    errors.extend(validate_frontmatter(fm, filepath))

    # Validate body
    has_sources = 'sources' in fm and fm['sources']
    body_errors = validate_body(body, has_sources)

    # Separate warnings from errors
    for err in body_errors:
        if err.startswith('Warning:'):
            warnings.append(err)
        else:
            errors.append(err)

    # Check for prompt injection patterns
    injection_warnings = check_prompt_injection_patterns(content)
    warnings.extend(injection_warnings)

    return errors, warnings


def main():
    if len(sys.argv) < 2:
        print("Usage: validate_format.py <essay1.md> [essay2.md ...]")
        sys.exit(1)

    all_errors = []
    all_warnings = []

    for filepath in sys.argv[1:]:
        if not filepath.strip():
            continue

        print(f"\n📄 Validating: {filepath}")
        errors, warnings = validate_essay(filepath)

        if errors:
            print(f"  ❌ Errors:")
            for err in errors:
                print(f"     - {err}")
            all_errors.extend([(filepath, e) for e in errors])

        if warnings:
            print(f"  ⚠️  Warnings:")
            for warn in warnings:
                print(f"     - {warn}")
            all_warnings.extend([(filepath, w) for w in warnings])

        if not errors and not warnings:
            print(f"  ✅ Valid")

    print("\n" + "="*50)

    if all_errors:
        print(f"\n❌ VALIDATION FAILED: {len(all_errors)} error(s) found")
        sys.exit(1)
    elif all_warnings:
        print(f"\n⚠️  VALIDATION PASSED with {len(all_warnings)} warning(s)")
        sys.exit(0)
    else:
        print("\n✅ ALL VALIDATIONS PASSED")
        sys.exit(0)


if __name__ == '__main__':
    main()
