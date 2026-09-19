import os
from tech_stack_lookup import TechStackLookupClient

if not os.environ.get("APIFY_API_TOKEN"):
    raise SystemExit("Set APIFY_API_TOKEN before running this example")
client = TechStackLookupClient()
print(client.run_one({'mode': 'find',
 'technologies': ['Shopify'],
 'country': ['US'],
 'hasEmail': True,
 'maxItems': 100}))
