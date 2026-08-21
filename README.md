# VertexOps — AI Order Agent on Google Cloud
### Built for Vertex AI Agent Builder (Reasoning Engines)

**Category:** Cloud-Native Agent | **Deployment:** Google Cloud (Mumbai region available) | **Sector:** E-commerce, Logistics, Any GCP organization

---

## Overview

VertexOps is a managed AI agent deployed on **Google Vertex AI Reasoning Engines** —
Google's enterprise agent runtime. It answers order-status questions using your
business logic as callable tools, with Google-grade scaling, security and monitoring.

Ships with an offline demo mode so you can evaluate the exact logic before any cloud
spend, plus one-command deployment to `asia-south1` (Mumbai) for Indian data
residency.

## Key Features

- Python function tools (e.g., `get_order_status`) — extend with any business API
- Managed runtime: no servers to patch; scales automatically
- Deploy/query CLI included (`--deploy`, `--query`)
- Offline demo mode for zero-cost evaluation
- Mumbai region support for DPDP-aligned data residency

## Business Value

| Need | Solution |
|------|----------|
| Scalable customer-facing agent | Google-managed infra, no DevOps burden |
| Data residency in India | asia-south1 deployment |
| Fast integration | Wrap existing APIs as tools in minutes |

## How It Works

```
User Query ──► Reasoning Engine ──► Tool Call: get_order_status(order_id)
            ◄── Natural Answer ◄── Your Order System / Firestore
```

## Technical Requirements

- Google Cloud project with Vertex AI API enabled (client account)
- Service account key or `gcloud` authentication
- A GCS staging bucket

## Installation & Setup — Step by Step

```powershell
# 1. Enter the project folder
cd 09-vertex-ai-agent-builder

# 2. Create isolated environment
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# 3. Install dependencies
pip install -r requirements.txt

# 4. Configure GCP settings
copy .env.example .env
notepad .env        # set project id, staging bucket, region=asia-south1

# 5. Authenticate
gcloud auth application-default login

# 6. Evaluate offline first (no GCP cost)
python agent.py

# 7. Deploy to Google Cloud
python agent.py --deploy

# 8. Query the deployed agent
python agent.py --query "<resource-name-from-step-7>" --order-id OD1001
```

## Customization for Your Business

- Replace the mock order store with Firestore/BigQuery/your OMS API
- Add tools: refunds, delivery-slot booking, escalation ticketing
- Front-end via Dialogflow CX voice/chat channels (guide included)

## What's Included

- Complete source code (`agent.py`) with deploy/query CLI
- Dialogflow CX alternative architecture guide
- Deployment documentation and 1 working session with your GCP admin

---

*Infrastructure billed by Google at usage; idle engines can be deleted anytime.*
