import pandas as pd
from sklearn.ensemble import IsolationForest
import pickle

data = {
    "packets_per_ip": [10, 12, 9, 11, 13, 8, 7, 10, 9, 50, 60, 70]
}

df = pd.DataFrame(data)

model = IsolationForest(contamination=0.2)
model.fit(df)

with open("ai_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("AI Model Trained & Saved Successfully")
