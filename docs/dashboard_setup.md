# Power BI Dashboard Setup

This guide describes how to configure the Infrastructure Cost Optimization & Monitoring Dashboard using Power BI.

1. **Install Power BI Desktop** if you haven't already.
2. **Load data**:
   - From `sample_data/cost_data_sample.csv` to simulate cost data.
   - Use the Power BI `Azure Log Analytics` connector to query metrics from your Log Analytics workspace.
3. **Create visuals**:
   - Line charts for monthly spend trends.
   - Bar charts for cost by resource group and service.
   - KPIs to track total spend against budget.
4. **Publish the report** to the Power BI Service to share with your team.
5. **Set up scheduled refresh** to keep the dashboard up to date once you have real data sources connected.
