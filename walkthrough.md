# Assessment Walkthrough

## Overview

This repository contains my solutions for both assessment tasks: Product Scoping and Pipeline Building.

---

## Task 1: Product Scoping

### Understanding the Problem

The marketing team currently uses multiple platforms such as Google Ads, Meta Ads, and CRM tools to track campaign performance. To answer questions about marketing performance, team members manually collect data from different systems and create reports. This process is time-consuming, inconsistent, and dependent on specific individuals.

### Proposed Solution

I proposed a unified marketing performance dashboard that automatically collects data from existing marketing platforms and presents it in a consistent format.

The tool is designed to:

* Provide a single source of truth for marketing performance
* Reduce manual reporting effort
* Improve consistency of reporting
* Allow both internal teams and clients to view performance metrics

### V1 Scope

For Version 1, I focused on:

* Automated data collection from existing platforms
* Unified reporting of key metrics
* Simple dashboard view
* Basic performance monitoring

### Out of Scope

I intentionally excluded:

* AI recommendations
* Budget optimization
* Predictive analytics
* Campaign creation and editing

These features can be considered for future versions after validating the core reporting workflow.

### Design Decisions

My goal was to keep the solution simple and useful. I prioritized solving the reporting problem first rather than building advanced features that might increase complexity.

---

## Task 2: Data Pipeline

### API Selection

I selected the Open-Meteo API because:

* It is free to use
* No API key is required
* It provides structured weather data suitable for analysis

### Pipeline Flow

1. Fetch weather data from the Open-Meteo API.
2. Convert the API response into a tabular format.
3. Transform the data and create a derived field called `temperature_category`.
4. Load the transformed data into BigQuery.
5. Query the stored data using SQL.

### Transformation Logic

I created a derived field named `temperature_category`:

* Hot: Temperature > 35°C
* Warm: Temperature > 25°C
* Cold: Temperature ≤ 25°C

This adds analytical value beyond the raw API response.

### BigQuery Storage

I created:

* Dataset: `weather_dataset`
* Table: `weather_data`

The transformed data is loaded into BigQuery for querying and analysis.

### SQL Query

I included a SQL query that summarizes the stored data and demonstrates that the data is queryable and useful.

### Production Considerations

If deployed in production, I would:

* Schedule the pipeline using Cloud Scheduler or Airflow
* Add monitoring and alerting for failures
* Store secrets securely using Secret Manager
* Implement retry logic and better error handling
* Partition and optimize BigQuery tables for larger datasets

---

## What I Would Improve With More Time

* Add automated scheduling
* Add data quality validation checks
* Add monitoring dashboards
* Expand the marketing dashboard prototype
* Add AI-powered insights and recommendations

---

## Conclusion

My approach focused on building a simple, reliable, and well-documented solution while clearly defining scope, trade-offs, and future improvements.
