import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

df = pd.read_csv('/content/Mall_Customers.csv')

df = df.drop('CustomerID', axis=1)

df['Genre'] = df['Genre'].map({'Male':0, 'Female':1})

#case 1
X = df.values

kmeans = KMeans(n_clusters=5, random_state=42)
labels_no_scaling = kmeans.fit_predict(X)

#case 2
scaler = StandardScaler()

X_scaled = X.copy()

X_scaled[:,2:] = scaler.fit_transform(X[:,2:])

kmeans_scaled = KMeans(n_clusters=5, random_state=42)
labels_scaled = kmeans_scaled.fit_predict(X_scaled)
