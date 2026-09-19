from tech_stack_lookup import TechStackLookupClient

for count in (10, 100, 1000):
    print(count, TechStackLookupClient.estimate_cost(count), "USD estimated result charges")
