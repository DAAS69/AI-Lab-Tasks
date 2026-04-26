#lab 11 task 2

import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

data = {
 'vehicle_serial_no': [5,3,8,2,4,7,6,10,1,9],
 'mileage': [150000,120000,250000,80000,100000,220000,180000,300000,75000,280000],
 'fuel_efficiency': [15,18,10,22,20,12,16,8,24,9],
 'maintenance_cost': [5000,4000,7000,2000,3000,6500,5500,8000,1500,7500],
 'vehicle_type': ['SUV','Sedan','Truck','Hatchback','Sedan','Truck','SUV','Truck','Hatchback','SUV']
}

df = pd.DataFrame(data)

print("Original Data:\n", df)

df['vehicle_type'] = df['vehicle_type'].map({
    'SUV':0,
    'Sedan':1,
    'Truck':2,
    'Hatchback':3
})

X = df.values

kmeans = KMeans(n_clusters=3, random_state=42)
labels_no_scaling = kmeans.fit_predict(X)

df['Cluster_No_Scaling'] = labels_no_scaling

scaler = StandardScaler()

X_scaled = X.copy()

X_scaled[:,:-1] = scaler.fit_transform(X[:,:-1])

kmeans_scaled = KMeans(n_clusters=3, random_state=42)
labels_scaled = kmeans_scaled.fit_predict(X_scaled)

df['Cluster_With_Scaling'] = labels_scaled

print("\nFinal Data with Clusters:\n", df)
