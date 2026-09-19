from tech_stack_lookup import TechStackLookupClient

client = TechStackLookupClient()
payload = {'mode': 'find',
 'technologies': ['Shopify'],
 'country': ['US'],
 'hasEmail': True,
 'maxItems': 100}
# Add more targets or queries to the list fields supported by this Actor.
rows = client.run(payload)
print(f"Received {len(rows)} rows")
