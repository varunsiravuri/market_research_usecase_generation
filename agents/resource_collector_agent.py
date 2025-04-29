# agents/resource_collector_agent.py

class ResourceCollectorAgent:
    def __init__(self, use_cases):
        self.use_cases = use_cases

    def collect_resources(self):
        all_links = {}

        for use_case in self.use_cases:
            print(f"🔎 Please search manually for datasets/tools related to: {use_case}")
            all_links[use_case] = ["[Please manually search on Kaggle / HuggingFace / GitHub]"]

        return all_links
