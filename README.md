# Market Research & AI Use Case Generation Agent

## Overview

This project designs a **Multi-Agent Architecture** system that generates relevant **AI** and **Generative AI (GenAI)** use cases for a given **Company or Industry**.

It conducts market research, understands the company's key areas, proposes AI/GenAI trends, collects resource assets, and delivers a final proposal.

- **Industry Chosen:** Web3
- **Company Chosen:** Solana

---

## Features

- 📚 Research Agent: Understands industry and company focus.
- 🔎 Market Standards Agent: Identifies AI/ML/GenAI trends.
- 🛠 Resource Collector Agent: Collects relevant datasets/tools.
- 📄 Final Report Generation: Compiles actionable insights and solutions.
- 🌐 Streamlit UI (BONUS): Web-based app for user interaction.
- 🎯 Bonus Proposed GenAI Solutions for internal/customer use cases.

---

## Project Structure

```plaintext
market_research_usecase_generator/
├── agents/
│   ├── research_agent.py
│   ├── market_standards_agent.py
│   └── resource_collector_agent.py
├── output/
│   ├── final_report.md
│   ├── dataset_links.md
├── app.py
├── main.py
├── architecture_flowchart.png
├── README.md

How to Run
Option 1: Run Backend Agents via CLI
bash

python main.py

Generates outputs inside output/ folder.

Option 2: Run Streamlit UI
bash

streamlit run app.py

Fill in Industry and Company details.

View live generated results.

```

References

McKinsey Blockchain Reports (2023)

Deloitte Web3 Trends (2024)

HuggingFace Datasets, Kaggle Datasets, GitHub Open Source Tools
