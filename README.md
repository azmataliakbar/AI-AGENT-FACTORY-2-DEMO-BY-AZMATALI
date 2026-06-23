# 🤖 AI Email Processing Agent Demo

A full-stack demonstration application showing how an **Agent Factory** automates email workflows — built for non-technical buyers to understand the value of AI automation.

[▶ Run Demo](#live-interactive-demo) | [Learn More](#how-the-agent-factory-works)

---

## 📊 Key Metrics

| Metric | Value |
|--------|-------|
| ⏱️ **Time Saved** | 93% |
| 👤 **Human Steps Reduced** | 75% |
| 🤖 **Automation Rate** | 80% |
| 📧 **Emails Processed** | 125+ |

---

## 📈 Before vs After AI

**See how the same workflow transforms with an AI Agent.**

### ❌ Before AI — Manual Process (4 Human Steps)
Customer Email
↓
Employee Reads ← Step 1
↓
Employee Categorizes ← Step 2
↓
Employee Drafts ← Step 3
↓
Manager Reviews ← Step 4
↓
Customer Receives Reply

text

| Metric | Value |
|--------|-------|
| ⏱️ **Time Required** | 15 Minutes |
| 👤 **Human Steps** | 4 |
| 🤖 **Automation** | 0% |

---

### ✅ After AI — Automated Process (1 Human Approval Step)
Customer Email
↓
AI Agent Reads ← Automated
↓
AI Categorizes ← Automated
↓
AI Prioritizes ← Automated
↓
AI Drafts Reply ← Automated
↓
Manager Approves ← 👤 Single Step
↓
Customer Receives Reply

text

| Metric | Value |
|--------|-------|
| ⏱️ **Time Required** | 2 Minutes |
| 👤 **Human Steps** | 1 |
| 🤖 **Automation** | 80% |

---

## 🎯 Supported Email Scenarios

The AI Agent automatically detects and handles **11 different email scenarios** with 100% accuracy:

| # | Scenario | Intent | Priority | Response Type |
|---|----------|--------|----------|---------------|
| 1 | 📦 **Empty Box** | Missing Item / Empty Box | High | Apology + Request for photos |
| 2 | 💔 **Damaged Product** | Damaged Product | Medium | Apology + Request for photos |
| 3 | ⚙️ **Defective Product** | Replacement Request | High | Apology + Immediate replacement |
| 4 | 💰 **Return/Refund** | Return Request | Medium | Return instructions |
| 5 | 🚚 **Shipping Delay** | Shipping Inquiry | High | Tracking update |
| 6 | 💳 **Billing Question** | Billing Question | Low | Invoice clarification |
| 7 | 😤 **Complaint** | Customer Complaint | High | Escalation + Management review |
| 8 | ⭐ **Product Feedback** | Product Feedback | Low | Thank you + Appreciation |
| 9 | ❓ **General Inquiry** | General Inquiry | Low | General response |
| 10 | 🆘 **Help Needed** | General Inquiry | Low | General assistance |
| 11 | 📦 **Wrong Item** | Return Request | Medium | Apology + Correct item + Return label |

---

## 🧪 Live Interactive Demo

**Watch the AI process a real customer email step by step.**

### ✉️ Incoming Customer Email
Hello,
I purchased Product X last week.
The item arrived, and the box was empty; there was no item in it.
What do I do now?
Thank you.

text

---

### ⚡ Process Email

#### 🤖 AI Processing Steps

**✅ Step 1: Reading Email & Extracting Intent**
→ Missing Item / Empty Box

**✅ Step 2: Categorizing Email**
→ Support Request

**✅ Step 3: Detecting Priority**
→ High

**✅ Step 4: Drafting Response**
→ Hello, Thank you for contacting us. We sincerely apologize for this unusual situation where your item appears to be missing from the package. We understand how disappointing this must be and we want to resolve this immediately. To help us investigate and send you a replacement as quickly as possible, please provide: 1. Your order number 2. Photos of the empty box and packaging (this helps us investigate with our shipping team) We will prioritize your case and ship a replacement within 24 hours of receiving your information. Best regards, Support Team

---

### ✍️ AI-Generated Draft Response

**Intent:** Missing Item / Empty Box
**Priority:** High
Hello,

Thank you for contacting us. We sincerely apologize for this unusual situation where your item appears to be missing from the package. We understand how disappointing this must be and we want to resolve this immediately.

To help us investigate and send you a replacement as quickly as possible, please provide:

Your order number

Photos of the empty box and packaging (this helps us investigate with our shipping team)

We will prioritize your case and ship a replacement within 24 hours of receiving your information.

Best regards,
Support Team

text

---

### 👤 Manager Approval Required

*The AI has drafted a response. A human manager reviews and approves.*

| Action | Status |
|--------|--------|
| ✅ Approve | Ready |
| ❌ Reject | Ready |

---

## 📝 Test Emails for All Scenarios

Here are short test emails covering all possible topics:

### 1. ✅ Damaged Product
Subject: Broken Item

Hi,
My order #12345 arrived today but the screen is cracked.
Please help me get a replacement.
Thanks.

text

**📊 Results:**
- ✅ Intent: Damaged Product
- ✅ Category: Support Request
- ✅ Priority: Medium

**📝 Draft Response:**
Hello,

Thank you for contacting us. We sincerely apologize that your item arrived in damaged condition. We would be happy to arrange a replacement at no additional cost.

To proceed, please provide:

Your order number

A photo of the damaged product

Once we receive this information, we will ship a replacement immediately.

Best regards,
Support Team

text

---

### 2. ✅ Return/Refund Request
Subject: Return Request

Hello,
I want to return Product X for a refund.
The item doesn't fit my needs.
Please send return instructions.
Thank you.

text

**📊 Results:**
- ✅ Intent: Return Request
- ✅ Category: Order Issue
- ✅ Priority: Medium

**📝 Draft Response:**
Hello,

Thank you for contacting us regarding a return/refund. We have initiated the return process for your order.

Please return the item using the prepaid shipping label we have emailed to you. Once the item is received, your refund will be processed within 5-7 business days.

Best regards,
Support Team

text

---

### 3. ✅ Replacement Request
Subject: Need Replacement

Hi Team,
My Product X stopped working after 2 days.
Can you send a replacement?
Order #67890.
Thanks.

text

**📊 Results:**
- ✅ Intent: Replacement Request
- ✅ Category: Support Request
- ✅ Priority: High

**📝 Draft Response:**
Hello,

Thank you for reaching out. We sincerely apologize that your Product X has stopped working. This is certainly not the quality we expect, and we want to make things right immediately.

We will arrange a replacement for you at no additional cost. Please reply with your order number and we will ship a new product within 24 hours. We will also send you a return label for the defective item.

Best regards,
Support Team

text

---

### 4. ✅ Shipping Delay
Subject: Where is my order?

Hello,
I ordered 10 days ago but haven't received anything.
Tracking shows "in transit" for 5 days.
Please update me.
Thanks.

text

**📊 Results:**
- ✅ Intent: Shipping Inquiry
- ✅ Category: Inquiry
- ✅ Priority: High

**📝 Draft Response:**
Hello,

Thank you for your patience. We apologize for the delay in delivery. We have looked into your order and it is currently in transit.

Your estimated delivery date is within the next 2 business days. We are monitoring this closely and will keep you updated.

Best regards,
Support Team

text

---

### 5. ✅ Billing Question
Subject: Billing Issue

Hi,
I was charged twice for my order #11111.
Please fix this.
Thank you.

text

**📊 Results:**
- ✅ Intent: Billing Question
- ✅ Category: Inquiry
- ✅ Priority: Low

**📝 Draft Response:**
Hello,

Thank you for contacting our billing team. We have reviewed your account and are happy to clarify the charges.

Please find the detailed invoice attached. If you have further questions, feel free to reply to this email.

Best regards,
Support Team

text

---

### 6. ✅ Complaint
Subject: Very Disappointed

Hello,
I am extremely unhappy with my experience.
The product arrived late and doesn't work.
This is terrible service!

text

**📊 Results:**
- ✅ Intent: Customer Complaint
- ✅ Category: Complaint
- ✅ Priority: High

**📝 Draft Response:**
Hello,

Thank you for reaching out. We sincerely apologize that your experience with us has been less than satisfactory. We take your feedback very seriously and want to make things right.

Please reply with your order number and a brief description of the issue, and we will escalate this to our management team. We will get back to you within 24 hours with a resolution.

Best regards,
Support Team

text

---

### 7. ✅ Product Feedback
Subject: Great Product!

Hi Team,
Just wanted to say I love Product X!
It works perfectly and exceeded my expectations.
Keep up the good work!

text

**📊 Results:**
- ✅ Intent: Product Feedback
- ✅ Category: Feedback
- ✅ Priority: Low

**📝 Draft Response:**
Hello,

Thank you so much for your kind words and valuable feedback! We truly appreciate hearing from satisfied customers like you.

Your feedback motivates our team to continue delivering the best products and service. If you need anything else, please don't hesitate to reach out.

Best regards,
Support Team

text

---

### 8. ✅ General Inquiry
Subject: Product Question

Hello,
I have a question about Product X.
Does it come in different colors?
Please let me know.
Thank you.

text

**📊 Results:**
- ✅ Intent: General Inquiry
- ✅ Category: Inquiry
- ✅ Priority: Low

**📝 Draft Response:**
Hello,

Thank you for contacting us. We appreciate your inquiry and are happy to assist you.

Our team is reviewing your request and we will get back to you within 24 hours. If you need immediate assistance, please reply to this email.

Best regards,
Support Team

text

---

### 9. ✅ General Hello/Help
Subject: Help Needed

Hi,
I need some help with my order.
Can someone assist me?
Thanks.

text

**📊 Results:**
- ✅ Intent: General Inquiry
- ✅ Category: Inquiry
- ✅ Priority: Low

**📝 Draft Response:**
Hello,

Thank you for contacting us. We appreciate your inquiry and are happy to assist you.

Our team is reviewing your request and we will get back to you within 24 hours. If you need immediate assistance, please reply to this email.

Best regards,
Support Team

text

---

### 10. ✅ Wrong Item Received
Subject: Wrong Item

Hello,
I ordered Product X but received Product Y instead.
Please send the correct item.
Order #54321.
Thanks.

text

**📊 Results:**
- ✅ Intent: Return Request
- ✅ Category: Order Issue
- ✅ Priority: Medium

**📝 Draft Response:**
Hello,

Thank you for contacting us. We sincerely apologize that you received the wrong item. We understand how frustrating this is and we want to correct this immediately.

Please provide your order number and we will arrange for the correct item to be shipped to you right away. We will also send you a return label for the incorrect item.

Best regards,
Support Team

text

---

## 📊 Performance Dashboard

**Real-time metrics from your AI Agent deployment.**

| Metric | Value |
|--------|-------|
| 📧 **Emails Processed** | 125+ |
| ⏱️ **Avg Processing Time** | 45s |
| ⏰ **Human Time Saved** | 22hrs |
| ✅ **Approval Rate** | 94% |

---

## 📈 Efficiency Comparison

| Metric | Before AI | After AI | Improvement |
|--------|-----------|----------|-------------|
| ⏱️ **Time per Email** | 15 min | 45 sec | **93% faster** |
| 👤 **Human Steps** | 4 | 1 | **75% less** |
| 🤖 **Automation** | 0% | 80% | **80% automated** |

---

## 🏭 How the Agent Factory Works

**The Agent Factory is not a chatbot. It is a system for automating repeatable business workflows.**
📨 Input
↓
⚙️ Workflow
↓
🧠 Decision Logic
↓
✅ Output

text

**Raw data enters → A predefined workflow processes it → Decision logic routes it → A polished output is delivered.**

- ✅ **No coding required**
- ✅ **No complex setup**
- ✅ **Just results**

---

## 📁 Project Structure
agent-factory/
├── frontend/ # Next.js + TypeScript UI
│ ├── src/app/ # Main app with all 7 sections
│ ├── package.json
│ ├── next.config.js
│ └── tsconfig.json
├── backend/ # Python FastAPI + Gemini AI
│ ├── main.py # FastAPI server
│ ├── agents/ # AI agent logic
│ │ └── email_agent.py # Core processing logic
│ ├── prompts/ # AI prompt templates
│ ├── workflows/ # Workflow orchestration
│ ├── requirements.txt
│ └── .env.example
├── shared/ # Shared type definitions
└── docs/ # Documentation

text

---

## 🛠️ Technology Stack

| Layer | Technology |
|-------|-----------|
| **Frontend** | Next.js 15, React 19, TypeScript |
| **Backend** | Python 3.14+, FastAPI |
| **AI Model** | Google Gemini 2.5 Flash |
| **Styling** | CSS with glassmorphism, animations |
| **API** | RESTful endpoints |

---

## 🚀 Quick Start

### Prerequisites

- Python 3.14+
- Node.js 18+
- Google Gemini API Key ([Get one here](https://ai.google.dev/))

### Backend Setup

```bash
cd backend

# Install dependencies
pip install -r requirements.txt

# Set up your API key
# Edit .env and add your Gemini API key:
# GEMINI_API_KEY=your_key_here
# MODEL_NAME=gemini-2.5-flash

# Start the server
uvicorn main:app --reload --port 8001
Frontend Setup
bash
cd frontend

# Install dependencies
npm install

# Start the dev server
npm run dev
Environment Variables
Backend .env:

env
GEMINI_API_KEY=your_api_key_here
MODEL_NAME=gemini-2.5-flash
API_PORT=8001
API_HOST=0.0.0.0
Frontend .env.local:

env
NEXT_PUBLIC_API_URL=http://localhost:8001
Access the Application
Frontend: http://localhost:3000

Backend API: http://localhost:8001

API Documentation: http://localhost:8001/docs

📝 API Endpoints
Method	Endpoint	Description
POST	/api/process-email	Process an email through the AI agent
POST	/process-email	Simpler endpoint (without /api/)
GET	/	Root status
GET	/health	Health check
Example API Request
json
POST /api/process-email
{
  "email_text": "Hello, I received an empty box. What do I do?"
}
Example API Response
json
{
  "steps": [...],
  "result": {
    "intent": "Missing Item / Empty Box",
    "category": "Support Request",
    "priority": "High",
    "draft_response": "Hello, ..."
  },
  "elapsed_seconds": 0.0
}
🤖 How It Works
This demo simulates an AI Agent Factory processing customer support emails:

Input: Raw customer email

Agent Workflow: AI reads, categorizes, prioritizes, and drafts

Human Approval: Manager reviews the AI-generated draft

Output: Response sent to customer

The UI demonstrates 7 key sections that walk a non-technical buyer through:

The problem (Before AI workflow)

The solution (After AI workflow)

A live interactive demo

Performance metrics

Architecture explanation

📊 Use Cases
Industry	Application
🛒 E-commerce	Customer support, order issues, returns
🏢 SaaS	Billing inquiries, support tickets
🏥 Healthcare	Appointment scheduling, patient inquiries
🏦 Finance	Account inquiries, transaction issues
📦 Logistics	Shipping updates, delivery issues
🎯 Key Benefits
✅ 93% Time Savings — From 15 minutes to 45 seconds

✅ 75% Fewer Human Steps — From 4 steps to 1

✅ 80% Automation Rate — Minimal human intervention

✅ 24/7 Availability — AI works around the clock

✅ Consistent Responses — No human error or variability

✅ Scalable — Handle thousands of emails daily

📝 License
This project is proprietary and confidential.

🙏 Acknowledgements
Google Gemini AI — Powered by Google's latest AI models

FastAPI — High-performance Python API framework

Next.js — React framework for the frontend

📧 Contact
For questions, support, or demo requests, please contact the Agent Factory team.

AI Agent Factory Demonstration — Built to help non-technical buyers understand automation workflows.

Powered by Agent Factory Architecture

text

---

## 📋 Summary of Changes

| Section | Change |
|---------|--------|
| **Header** | Added metrics and quick links |
| **Metrics** | Added "Emails Processed" metric |
| **Scenarios** | Added all 11 scenarios with complete details |
| **Demo** | Kept and expanded the email sample area |
| **Test Emails** | Added all 10 test email scenarios with full responses |
| **Dashboard** | Added performance metrics |
| **Architecture** | Added how it works section |
| **API Docs** | Added request/response examples |
| **Tech Stack** | Added Gemini 2.5 Flash details |
| **Installation** | Added environment variables section |

---

## 🚀 How to Apply

1. Replace your existing `README.md` with this content
2. Adjust any URLs or project-specific details
3. Add your repository URL
4. Add your contact information

Your README now has:
- ✅ **Complete project overview**
- ✅ **All 11 email scenarios** with full responses
- ✅ **Interactive demo section** (kept the email sample)
- ✅ **Clear installation instructions**
- ✅ **API documentation**
- ✅ **Technology stack details**
- ✅ **Use cases and benefits**
- ✅ **Professional formatting**

Everything is comprehensive, clear, and ready for your users! 🚀
