# test_grungle.py

import io
import sys

# The corrected function from our solution
def display_treasures(treasure_chest):
  """
  Prints each item in the treasure_chest list, one per line.
  """
  for i in range(len(treasure_chest)):
    print(treasure_chest[i])

# --- Test Setup ---
grungles_loot = ["Gold Coin", "Shiny Rock", "Mysterious Gem", "Old Sock"]
expected_output = """Gold Coin
Shiny Rock
Mysterious Gem
Old Sock
"""

# --- Test Execution & Verification ---
# Capture stdout to check what's printed
old_stdout = sys.stdout
sys.stdout = captured_output = io.StringIO()

# Call the function
display_treasures(grungles_loot)

# Restore stdout
sys.stdout = old_stdout

# Get the captured output
actual_output = captured_output.getvalue()

# --- Test Assertion ---
if actual_output == expected_output:
  print("Test PASSED! The Off-By-One Ogre is impressed!")
  print("You can safely cross the Array Bridge.")
else:
  print("Test FAILED! The Ogre is still grumpy.")
  print("Expected output:")
  print(expected_output)
  print("Actual output:")
  print(actual_output)
