# pip install apify-client
import os
from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("datagrit/tiktok-top-ads-monitor").call(run_input={
    "countries": [
        "US",
        "GB"
    ],
    "sortBy": [
        "for_you",
        "ctr"
    ],
    "periodDays": "7",
    "includeDetails": True,
    "maxItems": 50
})
items = client.dataset(run["defaultDatasetId"]).list_items().items
print(len(items), "records")
print(items[0] if items else None)
