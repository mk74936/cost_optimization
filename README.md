# Infrastructure Cost Optimization & Monitoring Dashboard

This repository provides a sample implementation of a cost monitoring solution using **Azure Monitor** and **Power BI**. It includes example infrastructure-as-code, scripts for retrieving cost and usage data, and guidance for building an interactive dashboard.

## Project Structure

- `azure/` – Bicep template for deploying a Log Analytics workspace.
- `scripts/` – Example Python scripts to query cost data and Log Analytics metrics.
- `sample_data/` – Small CSV file containing sample cost records used for testing Power BI reports.
- `docs/` – Additional documentation such as dashboard setup instructions.

## Prerequisites

- An Azure subscription with permissions to access Cost Management and Log Analytics.
- Python 3.10 or later with `requests`, `azure-identity`, and `azure-monitor-query` packages.
- Power BI Desktop to build the dashboard.

## Getting Started

1. Deploy a Log Analytics workspace using the Bicep template:
   ```bash
   az deployment group create \
     --resource-group <rg-name> \
     --template-file azure/main.bicep
   ```
2. Configure Azure AD application credentials and set the following environment variables for the scripts:
   - `AZURE_TENANT_ID`
   - `AZURE_CLIENT_ID`
   - `AZURE_CLIENT_SECRET`
   - `AZURE_SUBSCRIPTION_ID`
   - `LOG_ANALYTICS_WORKSPACE_ID`
3. Run `scripts/fetch_cost_data.py` to export cost data to a CSV file.
4. Follow `docs/dashboard_setup.md` to create and publish the Power BI dashboard using the exported data or the sample CSV.

The provided scripts and templates are simplified examples meant to demonstrate the overall approach. You can expand them to suit your environment and incorporate additional automation and monitoring features.
