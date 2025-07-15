import pandas as pd

print("This is testingg purpose")# test_run.py
from src.components.data_ingestion import DataIngestion

print("Starting data ingestion manually")
obj = DataIngestion()
train, test = obj.initiate_data_ingestion()
print("✅ Data ingestion completed")
