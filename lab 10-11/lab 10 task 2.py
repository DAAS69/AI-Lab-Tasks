#lab 10 task 2
from sklearn.datasets import fetch_20newsgroups
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

data = [
    ("Free money now!!!", 1),
    ("Hi, how are you?", 0),
    ("Win cash prize", 1),
    ("Meeting tomorrow", 0)
]

df = pd.DataFrame(data, columns=["text", "label"])

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df['text'])
y = df['label']

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

model = SVC()
model.fit(x_train, y_train)

y_pred = model.predict(x_test)

print("Accuracy:", accuracy_score(y_test, y_pred))

new_email = ["my name is saad"]
new_vec = vectorizer.transform(new_email)
print("Prediction (1=Spam):", model.predict(new_vec))
