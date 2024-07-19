import pymongo
from datetime import datetime

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["trading"]
collection = db["signals"]

# Sample data to insert
sample_data = [
    {
        "signal_id": "S001",
        "date_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "symbol": "AAPL",
        "signal_type": "Buy",
        "price": 150.25,
        "volume": 100,
        "confidence_level": 0.95,
        "strategy": "Mean Reversion",
        "stop_loss": 145.00,
        "take_profit": 155.00,
        "duration": "1 Day",
        "comments": "Strong buy signal based on recent dip."
    },
    {
        "signal_id": "S002",
        "date_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "symbol": "GOOGL",
        "signal_type": "Sell",
        "price": 2750.50,
        "volume": 50,
        "confidence_level": 0.85,
        "strategy": "Momentum",
        "stop_loss": 2800.00,
        "take_profit": 2700.00,
        "duration": "1 Week",
        "comments": "Sell signal due to overbought condition."
    }
    # Add more sample data if needed
]

# Insert sample data into the collection
collection.insert_many(sample_data)

print("Sample data inserted into MongoDB.")
