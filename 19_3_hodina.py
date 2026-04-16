import pandas as pd

df = pd.read_csv("big4_financial_risk_compliance.csv")

print(df.head(0))
print(df.shape)
print(df.dtypes)

#Deskriptívna štatistika
print(df.groupby("Year")["Total_Audit_Engagements"].mean())
print(df.groupby("Year")["Total_Audit_Engagements"].median())
print(df.groupby("Year")["Total_Audit_Engagements"].std())

print(df.isnull().sum())

print(df.groupby("Firm_Name")["AI_Used_for_Auditing"].value_counts())