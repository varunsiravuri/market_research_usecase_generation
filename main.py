from agents.research_agent import ResearchAgent
from agents.market_standards_agent import MarketStandardsAgent
from agents.resource_collector_agent import ResourceCollectorAgent


def main():
    # Inputs
    company = "Solana"
    industry = "Web3"

    # Step 1: Research
    research_agent = ResearchAgent(company, industry)
    research_data = research_agent.perform_research()

    # Save outputs
    with open("output/final_report.md", "w", encoding="utf-8") as f:
        f.write("# Final Report\n\n")
        f.write("## Industry Overview\n")
        f.write(research_data['industry_overview'] + "\n\n")
        f.write("## Company Overview\n")
        f.write(research_data['company_overview'] + "\n\n")

    print("✅ Research complete. Data saved to output/final_report.md")

    # Step 2: Market Trends + Use Case Generation
    standards_agent = MarketStandardsAgent(industry=industry, company=company)
    use_cases = standards_agent.generate_use_cases()

    short_use_cases = []

    for case in use_cases:
    # Remove the leading "- " if exists
        clean_text = case.lstrip("- ").split(".")[0]  # Take the first sentence only
        short_use_cases.append(clean_text)

    with open("output/final_report.md", "a", encoding="utf-8") as f:
        f.write("## Market Trends & Use Cases\n")
        for case in use_cases:
            f.write(case + "\n")
    
    # Step 3: Resource Collector Agent
    collector_agent = ResourceCollectorAgent(short_use_cases)

    resources = collector_agent.collect_resources()

    with open("output/dataset_links.md", "w", encoding="utf-8") as f:
        f.write("# Dataset & Tool Links\n\n")
        for use_case, links in resources.items():
            f.write(f"## {use_case}\n")
            for link in links:
                f.write(f"- {link}\n")
            f.write("\n")


if __name__ == "__main__":
    main()
