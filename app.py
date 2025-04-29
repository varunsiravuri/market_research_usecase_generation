import streamlit as st
from agents.research_agent import ResearchAgent
from agents.market_standards_agent import MarketStandardsAgent
from agents.resource_collector_agent import ResourceCollectorAgent

def main():
    st.title("Market Research & Use Case Generator (Web3 - Solana) 🚀")

    st.sidebar.header("Enter Details")
    industry = st.sidebar.text_input("Industry", "Web3")
    company = st.sidebar.text_input("Company", "Solana")

    if st.sidebar.button("Generate Proposal"):
        with st.spinner('Researching...'):
            # Step 1: Research
            research_agent = ResearchAgent(company, industry)
            research_data = research_agent.perform_research()

            # Step 2: Market Trends
            standards_agent = MarketStandardsAgent(industry=industry, company=company)
            use_cases = standards_agent.generate_use_cases()

            # Step 3: Resource Collector
            collector_agent = ResourceCollectorAgent(use_cases)
            resources = collector_agent.collect_resources()

            # Show outputs
            st.header("Industry Overview")
            st.write(research_data['industry_overview'])

            st.header("Company Overview")
            st.write(research_data['company_overview'])

            st.header("Market Trends & Use Cases")
            for case in use_cases:
                st.write(f" {case}")

            st.header("Dataset & Tool Links")

            st.subheader("Fraud Detection in Web3 Ecosystem")
            st.markdown("[Web3 Pre-Event Fraud Detection Dataset - Kaggle](https://www.kaggle.com/datasets/rugdox/scam-detection-dataset-v1-2-01-2025-juliusaiprep)")

            st.subheader("AI-Driven Content Analysis in Web3 Publishing")
            st.markdown("[Post3 Mirror Web3 Publishing Dataset - Week 16 2024](https://www.kaggle.com/datasets/marcocavaco/mirrors-week-16-dataset)")

            st.subheader("Smart Contract Analysis and Interaction")
            st.markdown("[web3.py - Python library for Ethereum Blockchain Interaction (GitHub)](https://github.com/ethereum/web3.py)")

            st.subheader("Building Generative AI Models for Web3 Content Understanding")
            st.markdown("[Distilled-AI Web3-Oriented Pretraining Dataset (HuggingFace)](https://huggingface.co/datasets/distilled-ai/web3-oriented-pretraining-data)")

            st.subheader("Benchmarking Language Models for Blockchain Understanding")
            st.markdown("[LLM Blockchain Benchmark Dataset](https://huggingface.co/datasets/revflask/blockchain-benchmark-formatted)")

            st.subheader("AI-Based Crypto Trading Analysis")
            st.markdown("[BTC Price Dataset with Technical Indicators (HuggingFace)](https://huggingface.co/datasets/WinkingFace/CryptoLM-Bitcoin-BTC-USDT)")


if __name__ == "__main__":
    main()
