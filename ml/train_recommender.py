from sklearn.ensemble import RandomForestClassifier
import joblib

X = [[1,1,1,1],[0,1,0,1]]
y = ["Casual","Formal"]

model = RandomForestClassifier()
model.fit(X, y)

joblib.dump(model, "recommender.pkl")
