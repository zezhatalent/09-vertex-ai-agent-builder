# VertexOps — 09-vertex-ai-agent-builder
### Built on Google Vertex AI

**Category:** Managed Cloud AI | **Deployment:** Your Server / Google Vertex AI Cloud | **Sector:** Enterprise-ready, India-tuned

---

## Overview

VertexOps packages a production-grade **Google Vertex AI** agent: Vertex Agent Builder (Mumbai: asia-south1)

Ships with an **offline demo / dry-run mode** that runs instantly without credentials — the same code path as live, so you validate before spending on API keys. When ready, add one key and the bridge switches to live platform calls.

> **Honest positioning:** This is an implementation package for Google Vertex AI. You get working code, configs, and the exact Google Vertex AI objects to recreate — not a hosted SaaS clone. Offline mode proves the contract.

## Key Features

- **Offline-first design:** Demo with mock data today; flip to live with one env var
- **Config-driven:** Edit `config.json` to add intents/queues/policies without touching code
- **Bridge pattern:** `agent.py` implements the exact webhook/API contract Google Vertex AI expects
- **India-ready:** INR pricing examples, Hinglish utterances, and +91 phone validation where relevant
- **Production guardrails:** Input validation, error handling, and audit-friendly logging built in

## Business Value

| Metric | Before | After |
|--------|--------|-------|
| Time to first demo | Days (platform setup) | Minutes (`python agent.py`) |
| Vendor lock-in risk | High (black-box SaaS) | Low (you own the bridge + config) |
| Cost to validate | API spend + onboarding calls | Zero (offline) |

## Architecture

```
User / Trigger ──> agent.py ──> Google Vertex AI API (live) ─┐
                  └─> MOCK engine (offline) ───────────┘─> JSON result -> downstream
Config: config.json ───────────────────────────────────────┘
```

## Folder Structure

```
09-vertex-ai-agent-builder/
├── .env.example
├── .gitignore
├── README.md
├── agent.py
├── requirements.txt
├── .env.example      # copy to .env and add live keys
└── README.md         # you are here
```

## Prerequisites

| Requirement | Version | Needed For | Install |
|-------------|---------|------------|---------|
| **Python** | 3.10+ | All agents | `winget install Python.Python.3.12` |
| **Git** | any | Clone repos | `winget install Git.Git` |
| **Python 3.10+** | latest | This agent (only 03/06) | See below |
| **Google Vertex AI account** | — | Live mode only | Client-provided (offline works without) |

Verify Python:
```powershell
python --version   # expect Python 3.12.x
```

## Installation — Step by Step (Proper)

### Step 1 — Clone / Enter Folder
```powershell
git clone https://github.com/zezhatalent/09-vertex-ai-agent-builder.git
cd 09-vertex-ai-agent-builder
# or if already local:
cd "D:\SOFTWARE\ANTIGRAVITY\AI AGENTS\09-vertex-ai-agent-builder"
```

### Step 2 — Create Isolated Environment (first time only)
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
# if blocked: Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

### Step 3 — Install Dependencies
```powershell
pip install -r requirements.txt
# verify:
pip list
```

### Step 4 — Configure Environment
```powershell
copy .env.example .env
notepad .env
```
Fill per table:

| Variable | Required | Example | Where to Get |
|---|---|---|---|
| `GOOGLE_CLOUD_PROJECT` | Yes (live) | `your-gcp-project-id` | Google Vertex AI dashboard |
| `GOOGLE_CLOUD_LOCATION` | Yes (live) | `asia-south1` | Google Vertex AI dashboard |
| `GOOGLE_APPLICATION_CREDENTIALS` | Yes (live) | `path/to/service-account.json` | Google Vertex AI dashboard |
| `GOOGLE_CLOUD_STAGING_BUCKET` | Yes (live) | `gs://your-staging-bucket` | Google Vertex AI dashboard |

> **Never commit `.env`**. It is git-ignored and per-machine.

### Step 5 — Run Offline Demo (no key needed)
```powershell
python agent.py
```
**Expected:** JSON or table with mock results printed to console (see “Usage Examples” below). No external calls made.

### Step 6 — Run Live Mode (optional, needs key)
```powershell
# after adding key to .env:
python agent.py        # or: python agent.py --live
# For webhook services:
# uvicorn agent:app --port 8000
# then test:
# curl.exe -X POST http://localhost:8000/webhook -H "Content-Type: application/json" -d '{"test": 1}'
```

### Step 7 — Verify
```powershell
python -m py_compile agent.py
# should print nothing = success
```

## Configuration

- **Primary config:** `config.json` — intents, queues, SLA tables, or workflow nodes. Edit and restart; no rebuild.
- **Env file:** `.env` (from `.env.example`) — live keys only. Offline ignores missing keys and uses `MOCK` data in `agent.py`.
- **Requirements:** `requirements.txt` — pinned minimal deps; stdlib-only folders use a comment stub.

## Usage Examples

### Example 1 — Offline Demo (instant)
```powershell
python agent.py
# -> {"status":"offline demo","product":"VertexOps"}
```

### Example 2 — Live Call (after .env)
```powershell
python agent.py --live
# -> live Google Vertex AI API response with real data
```

### Example 3 — As Webhook (if FastAPI service)
```powershell
uvicorn agent:app --port 8000
curl.exe -X POST http://localhost:8000/webhook -H "Content-Type: application/json" -d '{"message":"hello"}'
```

## How It Works

1. **Config load:** `agent.py` reads `config.json` at startup (policies, prompts, routing tables).
2. **Input ingest:** CLI args or webhook JSON (`/webhook` / `/events`).
3. **Branch:** If env key present → live Google Vertex AI HTTP call; else → deterministic mock.
4. **Output:** Structured JSON + console summary; webhook returns JSON to platform.

## Customization for Your Business

- **Add intents/queues:** Edit `config.json` — add rows; scorer auto-picks them.
- **Connect your systems:** Replace `MOCK` dict in `agent.py` with your API (CRM/ERP/dialer) — contract unchanged.
- **Language:** Add Hinglish variants in config keyword lists; templates already support en/hi.
- **Scale:** Run behind `uvicorn --workers 4` or Docker; stateless so horizontal.

## Troubleshooting

| Symptom | Cause | Fix |
|---------|-------|-----|
| `ModuleNotFoundError` | venv not activated or deps not installed | Activate `.venv` and `pip install -r requirements.txt` |
| `401 / invalid_api_key` | Wrong or expired key in `.env` | Re-copy from Google Vertex AI dashboard; no quotes/spaces |
| `port already in use` | Another agent on same port | Change `--port` or stop other service |
| Offline demo shows MOCK | No key in `.env` (expected) | Add key and rerun for live |
| `Activate.ps1 cannot be loaded` | PowerShell policy | `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` |

## What’s Included

- Bridge/runtime: `agent.py` (`2378 bytes`)
- Config: `config.json`
- Env template: `.env.example` + dependency list `requirements.txt`
- This README (client-facing sales sheet) + 1 customization session

---

*Offline first, live when ready — VertexOps on Google Vertex AI with India-ready defaults.*
