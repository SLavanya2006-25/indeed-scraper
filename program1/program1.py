import pandas as pd
from apify_client import ApifyClient

# Initialize the ApifyClient with your API token
client = ApifyClient("apify_api_tb5ERlPewV1SBmTej8Fblh7QjgMFqS4jobPc")

# Prepare the Actor input

run_input = {
    "position": "social media",
    "country": "IN",
    "location": "TAMILNADU",
    "maxItems": 10,
    "parseCompanyDetails": True,
    "saveOnlyUniqueItems": True,
    "followApplyRedirects": True,
}

# Run the Actor and wait for it to finish
run = client.actor("hMvNSpz3JnHgl5jkh").call(run_input=run_input)

# Fetch and print Actor results from the run's dataset (if there are any)
items =list(client.dataset(run["defaultDatasetId"]).iterate_items())


#convert the data to a pandas datafram
df=pd.DataFrame(items)

#export the dataframe to an excel file
df.to_excel("indeed scraper.xlsx",index=False)

print("Data exported to indeed scraper.xlsx")