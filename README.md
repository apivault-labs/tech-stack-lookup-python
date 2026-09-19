# Tech Stack Lookup — Python SDK

Python client for the [Tech Stack Lookup Apify Actor](https://apify.com/apivault_labs/tech-stack-lookup). Send public Actor inputs, wait for the hosted run, and receive clean Dataset rows without maintaining scraping infrastructure.

[![Apify Actor](https://img.shields.io/badge/Apify-Actor-blue)](https://apify.com/apivault_labs/tech-stack-lookup)
[![Python 3.9+](https://img.shields.io/badge/Python-3.9%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

## Results

- Technology and category targeting
- Country and vertical filters
- Public contact availability filters
- Stable sorting, pagination and count previews

The repository exposes only the Actor's public input and output contract. Data selection and processing remain inside the hosted Actor.

## Install

```bash
pip install git+https://github.com/apivault-labs/tech-stack-lookup-python.git
```

Create an Apify token at [Console → Integrations](https://console.apify.com/account/integrations), then:

```python
from tech_stack_lookup import TechStackLookupClient

client = TechStackLookupClient(api_token="apify_api_xxxxxx")
rows = client.run({'mode': 'find',
 'technologies': ['Shopify'],
 'country': ['US'],
 'hasEmail': True,
 'maxItems': 100})
print(rows[0] if rows else "No results")
```

You can set `APIFY_API_TOKEN` instead of passing the token in code.

## Public input options

| Field | Type | Default | Description |
|---|---|---|---|
| `mode` | `string` | `find` | Find matching websites or inspect supplied domains. |
| `domains` | `array` | `[]` | Domains to inspect in lookup mode. |
| `technologies` | `array` | `[]` | Technology names to include. |
| `matchMode` | `string` | `any` | Match any or all selected technologies. |
| `excludeTechnologies` | `array` | `[]` | Technology names to exclude. |
| `category` | `array` | `[]` | Technology categories to include. |
| `country` | `array` | `[]` | ISO-2 country codes. |
| `vertical` | `array` | `[]` | Business verticals to include. |
| `hasEmail` | `boolean` | `False` | Return records with a public email. |
| `hasPhone` | `boolean` | `False` | Return records with a public phone. |
| `sortBy` | `string` | `` | Public field used to order results. |
| `sortDesc` | `boolean` | `True` | Return highest values first. |
| `dedupeByDomain` | `boolean` | `True` | Return each root domain once. |
| `outputPreset` | `string` | `essential` | Choose a public result layout. |
| `countOnly` | `boolean` | `False` | Return a count preview instead of rows. |
| `maxItems` | `integer` | `100` | Maximum number of returned rows. |
| `offset` | `integer` | `0` | Rows to skip for pagination. |

The complete, versioned schema is also available on the [Actor page](https://apify.com/apivault_labs/tech-stack-lookup).

## Pricing

Pay per delivered result through Apify, starting around **$7/1,000 results** on paid tiers. Free-plan pricing and platform usage can differ; check the Actor page before large runs.

## Examples

- `examples/quickstart.py` — first run
- `examples/bulk_analysis.py` — expand a target list
- `examples/export_csv.py` — save flat result fields
- `examples/save_json.py` — preserve nested output
- `examples/cost_estimate.py` — estimate result-event charges
- `examples/environment_token.py` — keep credentials out of code

## Architecture and privacy

This repository is intentionally a thin API client. Collection, retries, analysis and billing run inside the hosted Apify Actor. No private implementation, credentials, scoring weights or infrastructure configuration are included.

## License

MIT. The hosted Actor is a separate paid service governed by Apify terms.
