from tech_stack_lookup import TechStackLookupClient

client = TechStackLookupClient()
rows = client.run({'mode': 'find',
 'technologies': ['Shopify'],
 'country': ['US'],
 'hasEmail': True,
 'maxItems': 100})
print(rows[0] if rows else "No results")
