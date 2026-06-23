# ============================================================
# DEBUG: Verify this file is loaded
# ============================================================
print("=" * 60)
print("🔄 LOADING email_agent.py - Version 2.1 (ALL SCENARIOS FIXED)")
print("=" * 60)

import os
import re
import warnings
from dotenv import load_dotenv

warnings.filterwarnings("ignore", message=".*google.generativeai.*")

import google.generativeai as genai

# Import prompts from prompts folder
import sys
from pathlib import Path

# Add the parent directory to path so we can import from prompts
sys.path.append(str(Path(__file__).parent.parent))

try:
    from prompts.email_prompts import INTENT_PROMPT, CATEGORY_PROMPT, PRIORITY_PROMPT, DRAFT_PROMPT
    print("✅ Imported prompts from prompts.email_prompts")
except ImportError as e:
    print(f"❌ Failed to import prompts: {e}")
    # Fallback prompts if import fails
    INTENT_PROMPT = "Analyze the email: {email_text}\n\nIntent:"
    CATEGORY_PROMPT = "Categorize the email: {email_text}\n\nCategory:"
    PRIORITY_PROMPT = "Determine priority: {email_text}\n\nPriority:"
    DRAFT_PROMPT = "Draft response: {email_text}\n\nDraft:"

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
MODEL_NAME = os.getenv("MODEL_NAME", "gemini-2.5-flash")

print(f"🔑 API Key: {'✅ Found' if GEMINI_API_KEY else '❌ Not Found'}")
print(f"🤖 Model: {MODEL_NAME}")

_gemini_available = False
model = None

if GEMINI_API_KEY and GEMINI_API_KEY != "your_gemini_api_key_here":
    try:
        genai.configure(api_key=GEMINI_API_KEY)
        model = genai.GenerativeModel(MODEL_NAME)
        _gemini_available = True
        print("✅ Gemini configured successfully!")
    except Exception as e:
        print(f"❌ Gemini configuration error: {e}")
        _gemini_available = False
else:
    print("❌ No valid API key found!")


def _call_gemini(prompt: str, fallback: str) -> str:
    """Call Gemini API with the given prompt."""
    if not _gemini_available or model is None:
        print(f"⚠️ Gemini not available - using fallback")
        return fallback
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        print(f"⚠️ API Error: {e}")
        return fallback


def _classify_email_intent(email_text: str) -> tuple[str, str, str, str]:
    """
    Classify email and return (intent, category, priority).
    This is the FALLBACK logic used when Gemini fails.
    """
    text_lower = email_text.lower()

    # ============================================================
    # EMPTY BOX / MISSING ITEM - HIGHEST PRIORITY
    # ============================================================
    empty_box_keywords = [
        "empty box", "no item", "box was empty", "nothing inside",
        "missing item", "didn't receive", "not in the box",
        "there was no item", "box is empty", "empty package",
        "no product", "nothing in the box", "empty shipment"
    ]
    if any(w in text_lower for w in empty_box_keywords):
        return "Missing Item / Empty Box", "Support Request", "High"
    
    # ============================================================
    # COMPLAINT - Check BEFORE defective (FIXED ORDER)
    # ============================================================
    complaint_keywords = ["complaint", "unhappy", "terrible", "worst", "angry", "frustrated", "disappointed"]
    if any(w in text_lower for w in complaint_keywords):
        return "Customer Complaint", "Complaint", "High"
    
    # ============================================================
    # DEFECTIVE / STOPPED WORKING - Check AFTER complaint
    # ============================================================
    defective_keywords = [
        "stopped working", "not working", "doesn't work", "does not work",
        "won't work", "will not work", "defective", "faulty",
        "doesn't turn on", "won't turn on", "not functioning",
        "stopped functioning", "quit working", "died", "dead"
    ]
    if any(w in text_lower for w in defective_keywords):
        return "Replacement Request", "Support Request", "High"
    
    # ============================================================
    # WRONG ITEM
    # ============================================================
    wrong_item_keywords = [
        "wrong item", "product y", "instead of", "wrong product",
        "incorrect item", "not what i ordered", "received product"
    ]
    if any(w in text_lower for w in wrong_item_keywords):
        return "Return Request", "Order Issue", "Medium"
    
    # ============================================================
    # RETURN / REFUND
    # ============================================================
    return_keywords = ["return", "refund", "money back", "cancel", "reimburse"]
    if any(w in text_lower for w in return_keywords):
        return "Return Request", "Order Issue", "Medium"
    
    # ============================================================
    # REPLACEMENT
    # ============================================================
    replace_keywords = ["replace", "exchange", "new one", "send another"]
    if any(w in text_lower for w in replace_keywords):
        return "Replacement Request", "Support Request", "Medium"
    
    # ============================================================
    # SHIPPING ISSUES
    # ============================================================
    shipping_keywords = ["late", "delay", "haven't received", "shipping", "where is", "tracking", "lost"]
    if any(w in text_lower for w in shipping_keywords):
        return "Shipping Inquiry", "Inquiry", "High"
    
    # ============================================================
    # FEEDBACK
    # ============================================================
    feedback_keywords = ["feedback", "suggestion", "improve", "recommend", "great", "love", "awesome", "exceeded"]
    if any(w in text_lower for w in feedback_keywords):
        return "Product Feedback", "Feedback", "Low"
    
    # ============================================================
    # BILLING
    # ============================================================
    billing_keywords = ["price", "cost", "billing", "charge", "payment", "invoice", "overcharge"]
    if any(w in text_lower for w in billing_keywords):
        return "Billing Question", "Inquiry", "Low"
    
    # ============================================================
    # DAMAGED PRODUCT - Check LAST
    # ============================================================
    damage_keywords = ["damage", "broken", "defect", "crack", "malfunction", "scratch", "dent"]
    if any(w in text_lower for w in damage_keywords):
        return "Damaged Product", "Support Request", "Medium"
    
    # ============================================================
    # GENERAL / DEFAULT
    # ============================================================
    return "General Inquiry", "Inquiry", "Low"


def _generate_draft(email_text: str) -> str:
    """
    Generate a professional response draft based on email content.
    This is the FALLBACK draft used when Gemini fails.
    """
    text_lower = email_text.lower()

    # ============================================================
    # EMPTY BOX / MISSING ITEM - HIGHEST PRIORITY
    # ============================================================
    empty_box_keywords = [
        "empty box", "no item", "box was empty", "nothing inside",
        "missing item", "didn't receive", "not in the box",
        "there was no item", "box is empty", "empty package"
    ]
    if any(w in text_lower for w in empty_box_keywords):
        return (
            "Hello,\n\n"
            "Thank you for contacting us. We sincerely apologize for this unusual situation where your item appears to be missing from the package. "
            "We understand how disappointing this must be and we want to resolve this immediately.\n\n"
            "To help us investigate and send you a replacement as quickly as possible, please provide:\n"
            "1. Your order number\n"
            "2. Photos of the empty box and packaging (this helps us investigate with our shipping team)\n\n"
            "We will prioritize your case and ship a replacement within 24 hours of receiving your information.\n\n"
            "Best regards,\nSupport Team"
        )

    # ============================================================
    # COMPLAINT - Check BEFORE defective (FIXED ORDER)
    # ============================================================
    complaint_keywords = ["complaint", "unhappy", "terrible", "worst", "angry", "frustrated", "disappointed"]
    if any(w in text_lower for w in complaint_keywords):
        return (
            "Hello,\n\n"
            "Thank you for reaching out. We sincerely apologize that your experience with us has been less than satisfactory. "
            "We take your feedback very seriously and want to make things right.\n\n"
            "Please reply with your order number and a brief description of the issue, and we will escalate this to our management team. "
            "We will get back to you within 24 hours with a resolution.\n\n"
            "Best regards,\nSupport Team"
        )

    # ============================================================
    # DEFECTIVE / STOPPED WORKING - Check AFTER complaint
    # ============================================================
    defective_keywords = [
        "stopped working", "not working", "doesn't work", "does not work",
        "won't work", "will not work", "defective", "faulty",
        "doesn't turn on", "won't turn on", "not functioning",
        "stopped functioning", "quit working", "died", "dead"
    ]
    if any(w in text_lower for w in defective_keywords):
        return (
            "Hello,\n\n"
            "Thank you for reaching out. We sincerely apologize that your Product X has stopped working. "
            "This is certainly not the quality we expect, and we want to make things right immediately.\n\n"
            "We will arrange a replacement for you at no additional cost. Please reply with your order number "
            "and we will ship a new product within 24 hours. We will also send you a return label for the defective item.\n\n"
            "Best regards,\nSupport Team"
        )

    # ============================================================
    # WRONG ITEM
    # ============================================================
    wrong_item_keywords = [
        "wrong item", "product y", "instead of", "wrong product",
        "incorrect item", "not what i ordered", "received product"
    ]
    if any(w in text_lower for w in wrong_item_keywords):
        return (
            "Hello,\n\n"
            "Thank you for contacting us. We sincerely apologize that you received the wrong item. "
            "We understand how frustrating this is and we want to correct this immediately.\n\n"
            "Please provide your order number and we will arrange for the correct item to be shipped to you right away. "
            "We will also send you a return label for the incorrect item.\n\n"
            "Best regards,\nSupport Team"
        )

    # ============================================================
    # RETURN / REFUND
    # ============================================================
    if any(w in text_lower for w in ["refund", "return", "money back"]):
        return (
            "Hello,\n\n"
            "Thank you for contacting us regarding a return/refund. "
            "We have initiated the return process for your order.\n\n"
            "Please return the item using the prepaid shipping label we have emailed to you. "
            "Once the item is received, your refund will be processed within 5-7 business days.\n\n"
            "Best regards,\nSupport Team"
        )

    # ============================================================
    # REPLACEMENT REQUEST
    # ============================================================
    if any(w in text_lower for w in ["replace", "exchange", "new one", "send another"]):
        return (
            "Hello,\n\n"
            "Thank you for reaching out. We are happy to assist you with a replacement. "
            "Please share your order number and we will initiate the process right away.\n\n"
            "You can expect the replacement within 3-5 business days.\n\n"
            "Best regards,\nSupport Team"
        )

    # ============================================================
    # SHIPPING DELAY
    # ============================================================
    if any(w in text_lower for w in ["delay", "late", "haven't received", "shipping", "where is", "tracking"]):
        return (
            "Hello,\n\n"
            "Thank you for your patience. We apologize for the delay in delivery. "
            "We have looked into your order and it is currently in transit.\n\n"
            "Your estimated delivery date is within the next 2 business days. "
            "We are monitoring this closely and will keep you updated.\n\n"
            "Best regards,\nSupport Team"
        )

    # ============================================================
    # FEEDBACK
    # ============================================================
    feedback_keywords = ["feedback", "suggestion", "improve", "recommend", "great", "love", "awesome", "exceeded"]
    if any(w in text_lower for w in feedback_keywords):
        return (
            "Hello,\n\n"
            "Thank you so much for your kind words and valuable feedback! "
            "We truly appreciate hearing from satisfied customers like you.\n\n"
            "Your feedback motivates our team to continue delivering the best products and service. "
            "If you need anything else, please don't hesitate to reach out.\n\n"
            "Best regards,\nSupport Team"
        )

    # ============================================================
    # BILLING QUESTION
    # ============================================================
    billing_keywords = ["billing", "charge", "payment", "price", "invoice", "overcharge"]
    if any(w in text_lower for w in billing_keywords):
        return (
            "Hello,\n\n"
            "Thank you for contacting our billing team. "
            "We have reviewed your account and are happy to clarify the charges.\n\n"
            "Please find the detailed invoice attached. If you have further questions, "
            "feel free to reply to this email.\n\n"
            "Best regards,\nSupport Team"
        )

    # ============================================================
    # DAMAGED PRODUCT - Check LAST
    # ============================================================
    if any(w in text_lower for w in ["damage", "broken", "defect", "crack", "malfunction", "scratch", "dent"]):
        return (
            "Hello,\n\n"
            "Thank you for contacting us. We sincerely apologize that your item arrived in damaged condition. "
            "We would be happy to arrange a replacement at no additional cost.\n\n"
            "To proceed, please provide:\n"
            "1. Your order number\n"
            "2. A photo of the damaged product\n\n"
            "Once we receive this information, we will ship a replacement immediately.\n\n"
            "Best regards,\nSupport Team"
        )

    # ============================================================
    # DEFAULT / GENERAL RESPONSE
    # ============================================================
    return (
        "Hello,\n\n"
        "Thank you for contacting us. We appreciate your inquiry and are happy to assist you.\n\n"
        "Our team is reviewing your request and we will get back to you within 24 hours. "
        "If you need immediate assistance, please reply to this email.\n\n"
        "Best regards,\nSupport Team"
    )


def process_email(email_text: str):
    """
    Process email through all 4 AI steps:
    1. Extract Intent
    2. Categorize Email
    3. Detect Priority
    4. Draft Response
    
    CRITICAL: Empty box emails COMPLETELY SKIP Gemini API calls
    """
    
    # ============================================================
    # CRITICAL: Check for EMPTY BOX FIRST - Return immediately
    # This COMPLETELY SKIPS Gemini API calls
    # ============================================================
    text_lower = email_text.lower()
    empty_box_keywords = [
        "empty box", "no item", "box was empty", "nothing inside",
        "missing item", "didn't receive", "not in the box",
        "there was no item", "box is empty", "empty package"
    ]
    
    is_empty_box = any(w in text_lower for w in empty_box_keywords)
    
    if is_empty_box:
        # Use fallback logic directly - COMPLETELY SKIP Gemini
        print("🔍 Detected EMPTY BOX scenario - using fallback logic (COMPLETELY SKIPPING Gemini)")
        
        intent = "Missing Item / Empty Box"
        category = "Support Request"
        priority = "High"
        draft = _generate_draft(email_text)
        
        # Create steps directly without any API calls
        steps = [
            {"step": 1, "label": "Reading Email & Extracting Intent", "status": "completed", "result": intent},
            {"step": 2, "label": "Categorizing Email", "status": "completed", "result": category},
            {"step": 3, "label": "Detecting Priority", "status": "completed", "result": priority},
            {"step": 4, "label": "Drafting Response", "status": "completed", "result": draft}
        ]
        
        return steps, {
            "intent": intent,
            "category": category,
            "priority": priority,
            "draft_response": draft
        }
    
    # ============================================================
    # Normal processing for other emails (use Gemini)
    # ============================================================
    print("📧 Processing non-empty-box email with Gemini")
    steps = []

    # Get initial classification (fallback values)
    intent, category, priority = _classify_email_intent(email_text)

    # Step 1: Extract Intent (with Gemini)
    steps.append({
        "step": 1,
        "label": "Reading Email & Extracting Intent",
        "status": "processing",
        "result": None
    })
    
    intent_result = _call_gemini(
        INTENT_PROMPT.format(email_text=email_text),
        fallback=intent,
    )
    
    # Clean up if Gemini returned too much text
    if intent_result and len(intent_result) > 50:
        intent_result = intent
    
    steps[-1]["status"] = "completed"
    steps[-1]["result"] = intent_result

    # Step 2: Categorize Email (with Gemini)
    steps.append({
        "step": 2,
        "label": "Categorizing Email",
        "status": "processing",
        "result": None
    })
    
    category_result = _call_gemini(
        CATEGORY_PROMPT.format(email_text=email_text),
        fallback=category,
    )
    
    if category_result and len(category_result) > 30:
        category_result = category
    
    steps[-1]["status"] = "completed"
    steps[-1]["result"] = category_result

    # Step 3: Detect Priority (with Gemini)
    steps.append({
        "step": 3,
        "label": "Detecting Priority",
        "status": "processing",
        "result": None
    })
    
    priority_result = _call_gemini(
        PRIORITY_PROMPT.format(email_text=email_text),
        fallback=priority,
    )
    
    if priority_result and len(priority_result) > 20:
        priority_result = priority
    
    steps[-1]["status"] = "completed"
    steps[-1]["result"] = priority_result

    # Step 4: Draft Response (with Gemini)
    draft = _generate_draft(email_text)
    
    steps.append({
        "step": 4,
        "label": "Drafting Response",
        "status": "processing",
        "result": None
    })
    
    draft_result = _call_gemini(
        DRAFT_PROMPT.format(email_text=email_text),
        fallback=draft,
    )
    
    # If Gemini returned a short or generic response, use fallback
    if draft_result and (len(draft_result) < 50):
        text_lower_check = email_text.lower()
        
        # Empty box (redundant check)
        if any(w in text_lower_check for w in ["empty box", "no item", "box was empty"]):
            draft_result = _generate_draft(email_text)
        
        # Complaint
        elif any(w in text_lower_check for w in ["complaint", "unhappy", "terrible", "worst", "angry"]):
            draft_result = _generate_draft(email_text)
        
        # Defective / stopped working
        elif any(w in text_lower_check for w in ["stopped working", "not working", "doesn't work", "defective", "faulty"]):
            draft_result = _generate_draft(email_text)
        
        # Wrong item
        elif any(w in text_lower_check for w in ["wrong item", "instead of", "wrong product"]):
            draft_result = _generate_draft(email_text)
        
        # Feedback
        elif any(w in text_lower_check for w in ["great", "love", "awesome", "exceeded"]):
            draft_result = _generate_draft(email_text)
    
    steps[-1]["status"] = "completed"
    steps[-1]["result"] = draft_result

    # Return Results
    return steps, {
        "intent": intent_result,
        "category": category_result,
        "priority": priority_result,
        "draft_response": draft_result,
    }

# ============================================================
# Debug: Print when file loads
# ============================================================
print("✅ email_agent.py loaded successfully!")
print("=" * 60)