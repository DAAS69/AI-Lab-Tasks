#lab 10 task 3
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

data = {
    'spending': [200, 500, 1500, 3000, 100, 2500],
    'age': [25, 40, 35, 50, 23, 45],
    'visits': [5, 10, 20, 25, 2, 18],
    'label': [0, 0, 1, 1, 0, 1]
}

df = pd.DataFrame(data)

X = df[['spending', 'age', 'visits']]
y = df['label']

scaler = StandardScaler()
X = scaler.fit_transform(X)

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

model = SVC(kernel='linear')
model.fit(x_train, y_train)

y_pred = model.predict(x_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
