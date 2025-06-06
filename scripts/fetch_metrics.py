"""Query Azure Monitor metrics via Log Analytics."""
import os
from azure.identity import ClientSecretCredential
from azure.monitor.query import LogsQueryClient

TENANT_ID = os.environ.get("AZURE_TENANT_ID", "<tenant-id>")
CLIENT_ID = os.environ.get("AZURE_CLIENT_ID", "<client-id>")
CLIENT_SECRET = os.environ.get("AZURE_CLIENT_SECRET", "<client-secret>")
WORKSPACE_ID = os.environ.get("LOG_ANALYTICS_WORKSPACE_ID", "<workspace-id>")

credential = ClientSecretCredential(TENANT_ID, CLIENT_ID, CLIENT_SECRET)
client = LogsQueryClient(credential)

query = "AzureActivity | summarize count() by bin(TimeGenerated, 1h)"

def main():
    response = client.query_workspace(WORKSPACE_ID, query)
    for table in response.tables:
        for row in table.rows:
            print(row)

if __name__ == "__main__":
    main()
