# test_grungle.py

import io
import sys

# The corrected function from our solution
def display_treasures(treasure_chest):
  """
  Prints each item in the treasure_chest list, one per line.
  (Pythonic version)
  """
  for item in treasure_chest:
    print(item)

# --- Test Helper Function ---
def run_test_case(test_name, input_list, expected_output_str):
    print(f"Running test: {test_name}...")
    old_stdout = sys.stdout
    sys.stdout = captured_output = io.StringIO()

    display_treasures(input_list)

    sys.stdout = old_stdout
    actual_output_str = captured_output.getvalue()

    if actual_output_str == expected_output_str:
        print(f"PASS: {test_name}\n")
        return True
    else:
        print(f"FAIL: {test_name}")
        print("  Expected output:")
        # Print expected with indentation and handling empty string for clarity
        if not expected_output_str.strip(): # Check if string is empty or whitespace
             print("    '' (empty string or only newlines)")
        else:
            for line in expected_output_str.splitlines():
                print(f"    '{line}'")

        print("  Actual output:")
        if not actual_output_str.strip(): # Check if string is empty or whitespace
             print("    '' (empty string or only newlines)")
        else:
            for line in actual_output_str.splitlines():
                print(f"    '{line}'")
        print("") # Add a newline for separation
        return False

# --- Test Cases ---
def main():
    test_cases = [
        {
            "name": "Grungle's Original Loot",
            "input": ["Gold Coin", "Shiny Rock", "Mysterious Gem", "Old Sock"],
            "expected": "Gold Coin\nShiny Rock\nMysterious Gem\nOld Sock\n"
        },
        {
            "name": "Empty Treasure Chest",
            "input": [],
            "expected": "" # Expecting an empty string, no newlines
        },
        {
            "name": "Single Item Treasure Chest",
            "input": ["Solitary Diamond"],
            "expected": "Solitary Diamond\n"
        }
    ]

    all_passed = True
    results = []
    for tc in test_cases:
        result = run_test_case(tc["name"], tc["input"], tc["expected"])
        results.append(result)
        if not result:
            all_passed = False

    print("--- Test Summary ---")
    if all_passed:
        print("All test cases PASSED! The code is robust!")
        print("Grungle is thoroughly impressed and might even offer you a cup of grog.")
    else:
        print("Some test cases FAILED. Grungle is tapping his foot impatiently.")
        num_failed = results.count(False)
        print(f"Number of failed tests: {num_failed} out of {len(test_cases)}")

if __name__ == "__main__":
    main()
