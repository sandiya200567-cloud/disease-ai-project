import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import joblib

data = {
    "fever": [1,1,0,0],
    "cough": [1,0,1,0],
    "fatigue": [1,1,0,0],
    "disease": ["Flu","Flu","Cold","Healthy"]
}

df = pd.DataFrame(data)

X = df[["fever","cough","fatigue"]]
y = df["disease"]

model = DecisionTreeClassifier()
model.fit(X, y)

joblib.dump(model, "model.pkl")

print("Model trained and saved!")