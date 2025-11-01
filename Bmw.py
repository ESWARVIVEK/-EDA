import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
#['3 Series', '5 Series', '7 Series', 'M3', 'M5', 'X1', 'X3', 'X5', 'X6', 'i3', 'i8']
data=pd.read_csv("C:\\EV\\programs\\git try\\bmw\\BMW sales data (2010-2024) (1).csv")
df=pd.DataFrame(data)
Unique_years=sorted(df["Year"].unique())
models=['3 Series', '5 Series', '7 Series', 'M3', 'M5', 'X1', 'X3', 'X5', 'X6', 'i3', 'i8']
#percentage of sales per year
def Total_sales(df,Unique_years):
    SOTS=(df["Sales_Volume"].sum())
    sales=[]
    print(Unique_years)
    for i in Unique_years:
        a=(df["Year"]==i)
        b=df[a]
        SOS=b["Sales_Volume"].sum()
        sales.append(SOS)
    POS=np.array(sales)
    print(POS)
    x=Unique_years
    y=POS
    plt.plot(x,y,marker="o")
    plt.xlabel("Years")
    plt.ylabel("sale per year in .cr")
    plt.title("Bmw Sales between (2010-2024)")
    plt.yticks()
    plt.show()
def Series(df,Unique_years,model):
    a=df[["Model","Year","Sales_Volume",]]
    b=a[a["Model"]==model]
    new=[]
    SOTS=b["Sales_Volume"].sum()
    print(SOTS)
    for i in Unique_years:
        year=b[b["Year"]==i]
        sale_year=(year["Sales_Volume"].sum()/SOTS)*100
        new.append(sale_year)
    POS=np.array(new)
    x=Unique_years
    y=POS
    plt.plot(x,y,marker="o")
    plt.xlabel("Years")
    plt.ylabel(f"Percent of sale for {model}")
    plt.title(f"Bmw {model} Sales between (2010-2024)")
    plt.show()

#total sales per series between (2010-2024)
def total_series(df,models):
    sales_volume=[]
    di=dict()
    for i in models:
        a=df[df["Model"]==i]
        b=a["Sales_Volume"].sum()
        sales_volume.append(b)
    plt.pie(sales_volume,labels=models,autopct="%d%%")
    plt.title("toyal sales of all series")
    plt.show()
def salesByFueltype(df):
    new=[]
    Fuel_type=df["Fuel_Type"].unique()
    for i in Fuel_type:
        dframe=df[df["Fuel_Type"]==i]
        sales=dframe["Sales_Volume"].sum()
        new.append(sales)
    plt.bar(Fuel_type,np.array(new))
    plt.xlabel("Fuel_Type")
    plt.ylabel("sold units in .cr")
    plt.ylim(62000000,65000000)
    plt.show()

Total_sales(df,Unique_years)
for i in models:
    Series(df,Unique_years,model=i)
total_series(df,models)
salesByFueltype(df)













