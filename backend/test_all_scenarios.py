# test_all_scenarios.py
import sys
from pathlib import Path

# Add the current directory to path so we can import from agents
sys.path.append(str(Path(__file__).parent))

from agents.email_agent import process_email

test_cases = [
    {
        "name": "📦 Empty Box",
        "email": """
Hello,
I purchased Product X last week.
The item arrived, and the box was empty; there was no item in it.
What do I do now?
Thank you.
"""
    },
    {
        "name": "💔 Damaged Product",
        "email": """
Hi,
My order #12345 arrived today but the screen is cracked.
Please help me get a replacement.
Thanks.
"""
    },
    {
        "name": "💰 Return/Refund Request",
        "email": """
Hello,
I want to return Product X for a refund.
The item doesn't fit my needs.
Please send return instructions.
Thank you.
"""
    },
    {
        "name": "🔄 Replacement Request",
        "email": """
Hi Team,
My Product X stopped working after 2 days.
Can you send a replacement?
Order #67890.
Thanks.
"""
    },
    {
        "name": "🚚 Shipping Delay",
        "email": """
Hello,
I ordered 10 days ago but haven't received anything.
Tracking shows "in transit" for 5 days.
Please update me.
Thanks.
"""
    },
    {
        "name": "💳 Billing Question",
        "email": """
Hi,
I was charged twice for my order #11111.
Please fix this.
Thank you.
"""
    },
    {
        "name": "😤 Complaint",
        "email": """
Hello,
I am extremely unhappy with my experience.
The product arrived late and doesn't work.
This is terrible service!
"""
    },
    {
        "name": "⭐ Product Feedback",
        "email": """
Hi Team,
Just wanted to say I love Product X!
It works perfectly and exceeded my expectations.
Keep up the good work!
"""
    },
    {
        "name": "❓ General Inquiry",
        "email": """
Hello,
I have a question about Product X.
Does it come in different colors?
Please let me know.
Thank you.
"""
    },
    {
        "name": "🆘 Help Needed",
        "email": """
Hi,
I need some help with my order.
Can someone assist me?
Thanks.
"""
    },
    {
        "name": "📦 Wrong Item Received",
        "email": """
Hello,
I ordered Product X but received Product Y instead.
Please send the correct item.
Order #54321.
Thanks.
"""
    }
]

print("\n" + "="*80)
print("🧪 TESTING ALL EMAIL SCENARIOS")
print("="*80)
print("🔄 Processing", len(test_cases), "test cases...\n")

for i, test in enumerate(test_cases, 1):
    print("\n" + "-"*80)
    print(f"📧 TEST {i}/{len(test_cases)}: {test['name']}")
    print("-"*80)
    print(f"📝 Email: {test['email'].strip()}")
    
    try:
        steps, result = process_email(test['email'])
        
        print(f"\n📊 Results:")
        print(f"   ✅ Intent: {result['intent']}")
        print(f"   ✅ Category: {result['category']}")
        print(f"   ✅ Priority: {result['priority']}")
        print(f"\n📝 Draft Response:\n{result['draft_response']}")
    except Exception as e:
        print(f"\n❌ ERROR: {e}")

print("\n" + "="*80)
print("✅ ALL TESTS COMPLETE!")
print("="*80)

# cd C:\Projects\agents_factory\demo_project2\agent-factory\backend
# python test_all_scenarios.py