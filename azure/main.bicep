// Deploy a Log Analytics workspace for Azure Monitor
param location string = resourceGroup().location
param workspaceName string = 'log-workspace'

resource workspace 'Microsoft.OperationalInsights/workspaces@2022-10-01' = {
  name: workspaceName
  location: location
  properties: {
    retentionInDays: 30
  }
}

output workspaceId string = workspace.id
