from duckduckgo_search import DDGS
import time

class ResearchAgent:
    def __init__(self, company, industry):
        self.company = company
        self.industry = industry

    def search_web(self, query):
        with DDGS() as ddgs:
            results = list(ddgs.text(query, max_results=5))
            time.sleep(1)
            return results

    def get_industry_overview(self):
        query = f"What is {self.industry} industry?"
        results = self.search_web(query)
        if results:
            return results[0]['body']
        return "No industry overview found."

    def get_company_overview(self):
        query = f"What is {self.company} in {self.industry} industry?"
        results = self.search_web(query)
        if results:
            return results[0]['body']
        return "No company overview found."

    def perform_research(self):
        print(f"🔎 Researching Industry: {self.industry}")
        industry_info = self.get_industry_overview()

        print(f"🔎 Researching Company: {self.company}")
        company_info = self.get_company_overview()

        return {
            "industry_overview": industry_info,
            "company_overview": company_info
        }
