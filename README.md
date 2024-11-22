# Financial Data Engineering Project
Project 1 Notes can be found on my Notion: https://www.notion.so/Project-1-FinForensics-c00d0da1042b4f36ba9516137c680386?pvs=4

## Overview

This project focuses on building a robust data pipeline and analytical platform for **financial analysis**, **fraud detection**, and **AI-powered banking solutions**. The end-to-end workflow incorporates modern data engineering tools and practices to handle raw financial datasets efficiently, transform them into meaningful insights, and make them accessible through an interactive user interface.

## Features

- **Financial Analysis**: Extract, transform, and analyze financial data to derive actionable insights.
- **Fraud Detection**: Design pipelines to detect potential fraudulent activities using advanced data engineering practices.
- **AI-Powered Banking Solutions**: Enable AI models by preparing high-quality datasets for machine learning pipelines.

## Tools and Technologies Used

- **Google Sheets**: Initial data collection and lightweight data exploration.
- **Airbyte**: Extracting data from multiple sources and loading it into Snowflake.
- **Snowflake**: Cloud-based data warehouse for centralized data storage and querying.
- **AWS S3**: Data lake storage for raw and intermediate data files.
- **SODA**: Data quality checks to ensure accuracy, consistency, and completeness of datasets.
- **Apache Airflow**: Orchestrating workflows and managing data pipelines.
- **dbt (Data Build Tool)**: Data transformation and modeling for analytics-ready datasets.
- **Streamlit**: Building an interactive web application to visualize and interact with processed data.

## Workflow

1. **Data Ingestion**: Raw data is sourced using Airbyte from multiple origins and stored in Snowflake.
2. **Data Storage**: Intermediate and raw data are securely stored in AWS S3.
3. **Data Transformation**: dbt models are used to transform raw data into analytics-ready tables.
4. **Orchestration**: Apache Airflow schedules and monitors the pipelines to ensure smooth execution.
5. **Data Quality Assurance**: SODA ensures data quality and consistency at every stage of the pipeline.
6. **Visualization**: Processed data is presented in a user-friendly interface using Streamlit.

## Objectives

- Build a scalable and maintainable data pipeline.
- Ensure high data quality for critical financial decision-making.
- Provide an interactive platform for users to explore and visualize data.
