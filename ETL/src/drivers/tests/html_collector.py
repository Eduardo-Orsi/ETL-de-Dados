from typing import List, Dict


class HtmlCollectorSpy():
    def __init__(self) -> None:
        self.collect_essential_information_attributes = {}

    def collect_essential_information(self, html: str) -> List[Dict[str, str]]:
        self.collect_essential_information_attributes["html"] = html
        essential_information = []
        essential_information.append({
            "name": "someName",
            "link": "https://google.com.br"
        })

        return essential_information
