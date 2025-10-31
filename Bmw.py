import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
#['3 Series', '5 Series', '7 Series', 'M3', 'M5', 'X1', 'X3', 'X5', 'X6', 'i3', 'i8']
data=pd.read_csv("C:\\EV\\programs\\git try\\bmw\\BMW sales data (2010-2024) (1).csv")
df=pd.DataFrame(data)
Unique_years=sorted(df["Year"].unique())
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
def Series3(df,Unique_years):
    a=df[["Model","Year","Sales_Volume",]]
    b=a[a["Model"]=="3 Series"]
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
    plt.ylabel("Percent of sale for 3 Series")
    plt.title("Bmw 3 Serirs Sales between (2010-2024)")
    plt.show()
def Series5(df,Unique_years):
    a=df[["Model","Year","Sales_Volume",]]
    b=a[a["Model"]=="5 Series"]
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
    plt.ylabel("Percent of sale for 5 Series")
    plt.title("Bmw 5 Serirs Sales between (2010-2024)")
    plt.show()
def Series7(df,Unique_years):
    a=df[["Model","Year","Sales_Volume",]]
    b=a[a["Model"]=="7 Series"]
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
    plt.ylabel("Percent of sale for 7 Series")
    plt.title("Bmw 7 Serirs Sales between (2010-2024)")
    plt.show()
def M3(df,Unique_years):
    a=df[["Model","Year","Sales_Volume",]]
    b=a[a["Model"]=="M3"]
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
    plt.ylabel("Percent of sale for M3")
    plt.title("Bmw M3 Sales between (2010-2024)")
    plt.show()
def X1(df,Unique_years):
    a=df[["Model","Year","Sales_Volume",]]
    b=a[a["Model"]=="X1"]
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
    plt.ylabel("Percent of sale for X1")
    plt.title("Bmw X1 Sales between (2010-2024)")
    plt.show()
def M5(df,Unique_years):
    a=df[["Model","Year","Sales_Volume",]]
    b=a[a["Model"]=="M5"]
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
    plt.ylabel("Percent of sale for M5")
    plt.title("Bmw M5 Sales between (2010-2024)")
    plt.show()
def X3(df,Unique_years):
    a=df[["Model","Year","Sales_Volume",]]
    b=a[a["Model"]=="X3"]
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
    plt.ylabel("Percent of sale for X3")
    plt.title("Bmw X3 Sales between (2010-2024)")
    plt.show()
def X5(df,Unique_years):
    a=df[["Model","Year","Sales_Volume",]]
    b=a[a["Model"]=="X5"]
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
    plt.ylabel("Percent of sale for X5")
    plt.title("Bmw X5 Sales between (2010-2024)")
    plt.show()
def X6(df,Unique_years):
    a=df[["Model","Year","Sales_Volume",]]
    b=a[a["Model"]=="X6"]
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
    plt.ylabel("Percent of sale for X6")
    plt.title("Bmw X6 Sales between (2010-2024)")
    plt.show()
def I3(df,Unique_years):
    a=df[["Model","Year","Sales_Volume",]]
    b=a[a["Model"]=="i3"]
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
    plt.ylabel("Percent of sale for i3")
    plt.title("Bmw i3 Sales between (2010-2024)")
    plt.show()
def I8(df,Unique_years):
    a=df[["Model","Year","Sales_Volume",]]
    b=a[a["Model"]=="i8"]
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
    plt.ylabel("Percent of sale for i8")
    plt.title("Bmw i8 Sales between (2010-2024)")
    plt.show()
#total sales per series between (2010-2024)
def total_series(df):
    series=['3 Series', '5 Series', '7 Series', 'M3', 'M5', 'X1', 'X3', 'X5', 'X6', 'i3', 'i8']
    sales_volume=[]
    di=dict()
    for i in series:
        a=df[df["Model"]==i]
        b=a["Sales_Volume"].sum()
        sales_volume.append(b)
    plt.pie(sales_volume,labels=series,autopct="%d%%")
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
Series3(df,Unique_years)
Series5(df,Unique_years)
Series7(df,Unique_years)
M3(df,Unique_years)
M5(df,Unique_years)
X1(df,Unique_years)
X3(df,Unique_years)
X5(df,Unique_years)
X6(df,Unique_years)
I3(df,Unique_years)
I8(df,Unique_years)
total_series(df)
salesByFueltype(df)






