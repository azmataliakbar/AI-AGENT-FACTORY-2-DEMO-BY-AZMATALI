# test_api.py
import requests
import json

email = """
Hello,
I purchased Product X last week.
The item arrived, and the box was empty; there was no item in it.
What do I do now?
Thank you.
"""

try:
    response = requests.post(
        "http://localhost:8001/api/process-email",  # Note: /api/process-email
        json={"email_text": email},  # Note: email_text, not content
        timeout=30
    )
    
    print(f"Status Code: {response.status_code}")
    
    if response.status_code == 200:
        data = response.json()
        print("\n" + "=" * 60)
        print("📧 API RESPONSE")
        print("=" * 60)
        print(f"Steps: {len(data['steps'])} steps completed")
        print(f"Elapsed: {data['elapsed_seconds']} seconds")
        print(f"\nIntent: {data['result']['intent']}")
        print(f"Category: {data['result']['category']}")
        print(f"Priority: {data['result']['priority']}")
        print(f"\n📝 Draft Response:\n{data['result']['draft_response']}")
    else:
        print(f"Error: {response.text}")
        
except requests.exceptions.ConnectionError:
    print("❌ Could not connect to server. Make sure it's running.")
except Exception as e:
    print(f"❌ Error: {e}")
