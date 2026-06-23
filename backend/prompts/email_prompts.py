# email_prompts.py


INTENT_PROMPT = """
You are an expert email classifier. Analyze the following customer email and extract the primary intent.

============================================================
CRITICAL RULES - YOU MUST FOLLOW THESE EXACTLY:
============================================================

1. If the email mentions ANY of these phrases, classify as "Missing Item / Empty Box":
   - "empty box"
   - "no item"
   - "box was empty"
   - "nothing inside"
   - "missing item"
   - "didn't receive"
   - "not in the box"
   - "there was no item"
   - "box is empty"
   - "empty package"

2. ONLY classify as "Damaged Product" if the item is physically damaged (cracked, broken, scratched, dented)

3. DO NOT classify empty box as damaged product - they are completely different issues!

Email: {email_text}

Choose EXACTLY ONE from these categories:
- Missing Item / Empty Box
- Damaged Product
- Return Request
- Replacement Request
- Shipping Inquiry
- Billing Question
- General Inquiry

Respond with ONLY ONE short phrase (2-5 words).

Intent:"""

CATEGORY_PROMPT = """
You are an expert email categorizer. Categorize this customer email.

============================================================
CRITICAL RULES:
============================================================

- If customer received an EMPTY BOX or MISSING ITEM → "Support Request"
- If customer has a complaint → "Complaint"
- If customer is giving feedback → "Feedback"
- If customer is asking for information → "Inquiry"
- If order has issues (wrong item, missing item) → "Order Issue"

Email: {email_text}

Choose EXACTLY ONE from: Support Request, Complaint, Feedback, Inquiry, Order Issue, Other

Category:"""

PRIORITY_PROMPT = """
You are an expert at determining email priority. Analyze this customer email.

============================================================
MANDATORY PRIORITY RULES:
============================================================

- EMPTY BOX or MISSING ITEM → ALWAYS "High" or "Urgent" (customer paid for nothing!)
- ANGRY or UPSET customer → "Urgent" or "High"
- DELIVERY DELAY → "High"
- DAMAGED ITEM → "Medium" or "High"
- GENERAL QUESTION → "Low"

Email: {email_text}

Choose from: Urgent, High, Medium, Low

Priority:"""

DRAFT_PROMPT = """
You are a professional customer support agent. Draft a response to this email.

============================================================
MANDATORY RESPONSE RULES:
============================================================

IF THE EMAIL SAYS ANYTHING ABOUT AN EMPTY BOX OR MISSING ITEM, 
YOU MUST USE THIS EXACT RESPONSE - DO NOT CHANGE ANYTHING:

---
Hello,

Thank you for contacting us. We sincerely apologize for this unusual situation where your item appears to be missing from the package. 
We understand how disappointing this must be and we want to resolve this immediately.

To help us investigate and send you a replacement as quickly as possible, please provide:
1. Your order number
2. Photos of the empty box and packaging (this helps us investigate with our shipping team)

We will prioritize your case and ship a replacement within 24 hours of receiving your information.

Best regards,
Support Team
---

IF THE EMAIL IS ABOUT A DAMAGED PRODUCT, USE THIS:
---
Hello,

Thank you for contacting us. We sincerely apologize that your item arrived in damaged condition. 
We would be happy to arrange a replacement at no additional cost.

To proceed, please provide:
1. Your order number
2. A photo of the damaged product

Once we receive this information, we will ship a replacement immediately.

Best regards,
Support Team
---

IF THE EMAIL IS A GENERAL INQUIRY, USE THIS:
---
Hello,

Thank you for contacting us. We appreciate your inquiry and are happy to assist you.

Our team is reviewing your request and we will get back to you within 24 hours. 
If you need immediate assistance, please reply to this email.

Best regards,
Support Team
---

Email: {email_text}

Draft Response (COPY THE EXACT RESPONSE THAT MATCHES THE EMAIL TYPE):"""
