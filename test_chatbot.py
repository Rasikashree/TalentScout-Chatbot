"""
Test suite for TalentScout Chatbot components
Run with: python test_chatbot.py
"""

import sys
import os
from src.utils import (
    validate_email,
    validate_phone,
    validate_years_of_experience,
    is_conversation_ending,
    extract_tech_stack,
)

# Test configuration
TESTS_PASSED = 0
TESTS_FAILED = 0


def test_function(name, condition, expected=True):
    """Helper function to run tests."""
    global TESTS_PASSED, TESTS_FAILED

    result = "✓ PASS" if condition == expected else "✗ FAIL"
    print(f"{result}: {name}")

    if condition == expected:
        TESTS_PASSED += 1
    else:
        TESTS_FAILED += 1


def run_tests():
    """Run all tests."""
    print("\n" + "=" * 60)
    print("TalentScout Chatbot - Unit Tests")
    print("=" * 60 + "\n")

    # Email validation tests
    print("📧 Email Validation Tests")
    test_function("Valid email format", validate_email("john@example.com"), True)
    test_function("Invalid email - no @", validate_email("johnexample.com"), False)
    test_function("Invalid email - empty", validate_email(""), False)
    print()

    # Phone validation tests
    print("☎️  Phone Validation Tests")
    test_function("Valid phone 1", validate_phone("1234567890"), True)
    test_function("Valid phone with dashes", validate_phone("123-456-7890"), True)
    test_function("Valid phone with parentheses", validate_phone("(123) 456-7890"), True)
    test_function("Too short", validate_phone("123"), False)
    print()

    # Experience validation tests
    print("📅 Experience Validation Tests")
    is_valid, years = validate_years_of_experience("5 years")
    test_function("Valid: 5 years", is_valid and years == 5, True)

    is_valid, years = validate_years_of_experience("10")
    test_function("Valid: 10", is_valid and years == 10, True)

    is_valid, years = validate_years_of_experience("-5 years")
    test_function("Invalid: negative years", is_valid, False)

    is_valid, years = validate_years_of_experience("hello")
    test_function("Invalid: non-numeric", is_valid, False)
    print()

    # Conversation ending tests
    print("🚪 Conversation Ending Tests")
    test_function("Detect 'goodbye'", is_conversation_ending("goodbye"), True)
    test_function("Detect 'bye'", is_conversation_ending("bye"), True)
    test_function("Detect 'exit'", is_conversation_ending("exit"), True)
    test_function("Detect 'quit'", is_conversation_ending("quit"), True)
    test_function("Detect 'thank you'", is_conversation_ending("thank you"), True)
    test_function("Normal message", is_conversation_ending("I work with Python"), False)
    print()

    # Tech stack extraction tests
    print("🛠️  Tech Stack Extraction Tests")
    tech_stack = extract_tech_stack("Python, Django, PostgreSQL")
    test_function("Extract 3 techs", len(tech_stack) == 3, True)
    test_function("Correct extraction", "Python" in tech_stack, True)

    tech_stack = extract_tech_stack("React, Vue.js, Angular")
    test_function("Extract frameworks", len(tech_stack) == 3, True)

    tech_stack = extract_tech_stack("")
    test_function("Empty input", len(tech_stack) == 0, True)
    print()

    # Print summary
    print("=" * 60)
    print(f"Tests Passed: {TESTS_PASSED}")
    print(f"Tests Failed: {TESTS_FAILED}")
    total = TESTS_PASSED + TESTS_FAILED
    if total > 0:
        percentage = (TESTS_PASSED / total) * 100
        print(f"Success Rate: {percentage:.1f}%")
    print("=" * 60 + "\n")

    return TESTS_FAILED == 0


if __name__ == "__main__":
    print("Starting test suite...")
    success = run_tests()

    if success:
        print("✓ All tests passed!")
        sys.exit(0)
    else:
        print("✗ Some tests failed!")
        sys.exit(1)
