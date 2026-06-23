# test_empty_box.py
import sys
from pathlib import Path

# Add current directory to path
sys.path.append(str(Path(__file__).parent))

from agents.email_agent import process_email

test_email = """
Hello,
I purchased Product X last week.
The item arrived, and the box was empty; there was no item in it.
What do I do now?
Thank you.
"""

print("=" * 60)
print("📧 TESTING EMPTY BOX EMAIL")
print("=" * 60)
print(f"📝 Email:\n{test_email.strip()}")
print("\n" + "-" * 60)

steps, result = process_email(test_email)

print("\n📊 Results:")
print(f"   Intent: {result['intent']}")
print(f"   Category: {result['category']}")
print(f"   Priority: {result['priority']}")
print(f"\n📝 Draft Response:\n{result['draft_response']}")
print("\n" + "=" * 60)