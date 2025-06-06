"""Fetch Azure cost data using Cost Management API and save to CSV."""
import os
import requests
from datetime import datetime

# Placeholder: replace with actual Azure credentials/environment variables
TENANT_ID = os.environ.get("AZURE_TENANT_ID", "<tenant-id>")
CLIENT_ID = os.environ.get("AZURE_CLIENT_ID", "<client-id>")
CLIENT_SECRET = os.environ.get("AZURE_CLIENT_SECRET", "<client-secret>")
SUBSCRIPTION_ID = os.environ.get("AZURE_SUBSCRIPTION_ID", "<subscription-id>")

# Acquire token from Azure AD
TOKEN_URL = f"https://login.microsoftonline.com/{TENANT_ID}/oauth2/token"
resource = "https://management.azure.com/"

def get_access_token():
    data = {
        'grant_type': 'client_credentials',
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'resource': resource,
    }
    resp = requests.post(TOKEN_URL, data=data)
    resp.raise_for_status()
    return resp.json()['access_token']

def fetch_cost_data(access_token):
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    url = f"https://management.azure.com/subscriptions/{SUBSCRIPTION_ID}/providers/Microsoft.CostManagement/query?api-version=2023-03-01"
    payload = {
        "type": "Usage",
        "timeframe": "BillingMonthToDate",
        "dataset": {
            "granularity": "Daily",
            "aggregation": {
                "totalCost": {"name": "Cost", "function": "Sum"}
            },
            "grouping": [
                {"type": "Dimension", "name": "ResourceGroupName"},
                {"type": "Dimension", "name": "ResourceType"},
                {"type": "Dimension", "name": "ResourceId"}
            ]
        }
    }
    resp = requests.post(url, headers=headers, json=payload)
    resp.raise_for_status()
    return resp.json()

def save_to_csv(data, filename):
    with open(filename, 'w') as f:
        headers = [c['name'] for c in data['columns']]
        f.write(','.join(headers) + '\n')
        for row in data['rows']:
            f.write(','.join(str(r) for r in row) + '\n')

if __name__ == "__main__":
    token = get_access_token()
    result = fetch_cost_data(token)
    date_str = datetime.utcnow().strftime('%Y%m%d')
    output_file = f'cost_data_{date_str}.csv'
    save_to_csv(result, output_file)
    print(f"Saved cost data to {output_file}")
