# agents/market_standards_agent.py

from duckduckgo_search import DDGS
import time

class MarketStandardsAgent:
    def __init__(self, industry="Web3", company="Solana"):
        self.industry = industry
        self.company = company

    def search_trends(self):
        query = f"How is AI or GenAI used in {self.industry} industry or in {self.company}?"
        with DDGS() as ddgs:
            results = list(ddgs.text(query, max_results=10))
            time.sleep(1)
            return results

    def extract_trends_and_use_cases(self, results):
        use_cases = []

        for result in results:
            body = result.get("body", "")
            if not body:
                continue

            # Simple logic: look for "AI", "ML", "GenAI", "use case", etc.
            if any(keyword in body.lower() for keyword in ["ai", "ml", "genai", "use case", "automation"]):
                use_cases.append(f"- {body.strip()}")

            if len(use_cases) >= 7:
                break

        return use_cases or ["No trends or use cases found."]

    def generate_use_cases(self):
        print(f"🧠 Searching market trends in {self.industry} for {self.company}...")
        results = self.search_trends()

        print(f"✨ Extracting top trends and relevant use cases...")
        use_cases = self.extract_trends_and_use_cases(results)

        return use_cases
