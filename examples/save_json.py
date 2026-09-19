import json
from tech_stack_lookup import TechStackLookupClient

rows = TechStackLookupClient().run({'mode': 'find',
 'technologies': ['Shopify'],
 'country': ['US'],
 'hasEmail': True,
 'maxItems': 100})
with open("results.json", "w", encoding="utf-8") as handle:
    json.dump(rows, handle, ensure_ascii=False, indent=2)
