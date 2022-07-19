import json

with open ('tdata.json', 'r') as f:
    tdata = json.load(f)
    
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data_path = 'Desktop/ITMGT/ITMGT25/tdata.json'
tdata
type(tdata)

tdict = dict(enumerate(tdata))

type(tdict)

df = pd.DataFrame.from_records(tdata)

#Fix the grain of items
split_items_df =(df.set_index(['address','birthdate','mail','name','sex','username','transaction_value','transaction_date'])
.apply(lambda x: x.str.split(';').explode())
.reset_index())

split_items_df2=split_items_df.replace("HealthyKid 3+",'THREE',regex=True)

split_items_df2['transaction_quantity']=split_items_df2['transaction_items'].astype('str').str.extractall('(\d+)').unstack().fillna('').sum(axis=1).astype(int)

splitems_df=split_items_df2.replace('THREE+','HealthyKid 3',regex=True)

#Extract months from dates
numbered_months = splitems_df["transaction_month"] = [x[7][6] for x in np.array(splitems_df)]

def spell_month(numbered_months):
    if numbered_months == '1':
        return 'January'
    elif numbered_months == '2':
        return 'February'
    elif numbered_months == '3':
        return 'March'
    elif numbered_months == '4':
        return 'April'
    elif numbered_months == '5':
        return 'May'
    else:
        return 'June'
    
splitems_df['transaction_month'] = splitems_df['transaction_month'].apply(spell_month)

itemslist = ['Beef Chicharon', 'Kimchi and Seaweed', 'Nutrional Milk', 'Gummy Vitamins', 'Yummy Vegetables','Orange Beans','Gummy Worms']

#Make a T/F table for each item's transactions
for item in itemslist:
    splitems_df[item] = splitems_df['transaction_items'].str.contains(item)

#Get number of transactions for each item per month)
print(splitems_df.loc[(splitems_df['Beef Chicharon']==True)&(splitems_df['transaction_month']=='January'),'transaction_quantity'].sum())
print(splitems_df.loc[(splitems_df['Beef Chicharon']==True)&(splitems_df['transaction_month']=='February'),'transaction_quantity'].sum())
print(splitems_df.loc[(splitems_df['Beef Chicharon']==True)&(splitems_df['transaction_month']=='March'),'transaction_quantity'].sum())
print(splitems_df.loc[(splitems_df['Beef Chicharon']==True)&(splitems_df['transaction_month']=='April'),'transaction_quantity'].sum())
print(splitems_df.loc[(splitems_df['Beef Chicharon']==True)&(splitems_df['transaction_month']=='May'),'transaction_quantity'].sum())
print(splitems_df.loc[(splitems_df['Beef Chicharon']==True)&(splitems_df['transaction_month']=='June'),'transaction_quantity'].sum())
print("")
print(splitems_df.loc[(splitems_df['Kimchi and Seaweed']==True)&(splitems_df['transaction_month']=='January'),'transaction_quantity'].sum())
print(splitems_df.loc[(splitems_df['Kimchi and Seaweed']==True)&(splitems_df['transaction_month']=='February'),'transaction_quantity'].sum())
print(splitems_df.loc[(splitems_df['Kimchi and Seaweed']==True)&(splitems_df['transaction_month']=='March'),'transaction_quantity'].sum())
print(splitems_df.loc[(splitems_df['Kimchi and Seaweed']==True)&(splitems_df['transaction_month']=='April'),'transaction_quantity'].sum())
print(splitems_df.loc[(splitems_df['Kimchi and Seaweed']==True)&(splitems_df['transaction_month']=='May'),'transaction_quantity'].sum())
print(splitems_df.loc[(splitems_df['Kimchi and Seaweed']==True)&(splitems_df['transaction_month']=='June'),'transaction_quantity'].sum())
print("")
print(splitems_df.loc[(splitems_df['Nutrional Milk']==True)&(splitems_df['transaction_month']=='January'),'transaction_quantity'].sum())
print(splitems_df.loc[(splitems_df['Nutrional Milk']==True)&(splitems_df['transaction_month']=='February'),'transaction_quantity'].sum())
print(splitems_df.loc[(splitems_df['Nutrional Milk']==True)&(splitems_df['transaction_month']=='March'),'transaction_quantity'].sum())
print(splitems_df.loc[(splitems_df['Nutrional Milk']==True)&(splitems_df['transaction_month']=='April'),'transaction_quantity'].sum())
print(splitems_df.loc[(splitems_df['Nutrional Milk']==True)&(splitems_df['transaction_month']=='May'),'transaction_quantity'].sum())
print(splitems_df.loc[(splitems_df['Nutrional Milk']==True)&(splitems_df['transaction_month']=='June'),'transaction_quantity'].sum())
print("")
print(splitems_df.loc[(splitems_df['Gummy Vitamins']==True)&(splitems_df['transaction_month']=='January'),'transaction_quantity'].sum())
print(splitems_df.loc[(splitems_df['Gummy Vitamins']==True)&(splitems_df['transaction_month']=='February'),'transaction_quantity'].sum())
print(splitems_df.loc[(splitems_df['Gummy Vitamins']==True)&(splitems_df['transaction_month']=='March'),'transaction_quantity'].sum())
print(splitems_df.loc[(splitems_df['Gummy Vitamins']==True)&(splitems_df['transaction_month']=='April'),'transaction_quantity'].sum())
print(splitems_df.loc[(splitems_df['Gummy Vitamins']==True)&(splitems_df['transaction_month']=='May'),'transaction_quantity'].sum())
print(splitems_df.loc[(splitems_df['Gummy Vitamins']==True)&(splitems_df['transaction_month']=='June'),'transaction_quantity'].sum())
print("")
print(splitems_df.loc[(splitems_df['Yummy Vegetables']==True)&(splitems_df['transaction_month']=='January'),'transaction_quantity'].sum())
print(splitems_df.loc[(splitems_df['Yummy Vegetables']==True)&(splitems_df['transaction_month']=='February'),'transaction_quantity'].sum())
print(splitems_df.loc[(splitems_df['Yummy Vegetables']==True)&(splitems_df['transaction_month']=='March'),'transaction_quantity'].sum())
print(splitems_df.loc[(splitems_df['Yummy Vegetables']==True)&(splitems_df['transaction_month']=='April'),'transaction_quantity'].sum())
print(splitems_df.loc[(splitems_df['Yummy Vegetables']==True)&(splitems_df['transaction_month']=='May'),'transaction_quantity'].sum())
print(splitems_df.loc[(splitems_df['Yummy Vegetables']==True)&(splitems_df['transaction_month']=='June'),'transaction_quantity'].sum())
print("")
print(splitems_df.loc[(splitems_df['Orange Beans']==True)&(splitems_df['transaction_month']=='January'),'transaction_quantity'].sum())
print(splitems_df.loc[(splitems_df['Orange Beans']==True)&(splitems_df['transaction_month']=='February'),'transaction_quantity'].sum())
print(splitems_df.loc[(splitems_df['Orange Beans']==True)&(splitems_df['transaction_month']=='March'),'transaction_quantity'].sum())
print(splitems_df.loc[(splitems_df['Orange Beans']==True)&(splitems_df['transaction_month']=='April'),'transaction_quantity'].sum())
print(splitems_df.loc[(splitems_df['Orange Beans']==True)&(splitems_df['transaction_month']=='May'),'transaction_quantity'].sum())
print(splitems_df.loc[(splitems_df['Orange Beans']==True)&(splitems_df['transaction_month']=='June'),'transaction_quantity'].sum())
print("")
print(splitems_df.loc[(splitems_df['Gummy Worms']==True)&(splitems_df['transaction_month']=='January'),'transaction_quantity'].sum())
print(splitems_df.loc[(splitems_df['Gummy Worms']==True)&(splitems_df['transaction_month']=='February'),'transaction_quantity'].sum())
print(splitems_df.loc[(splitems_df['Gummy Worms']==True)&(splitems_df['transaction_month']=='March'),'transaction_quantity'].sum())
print(splitems_df.loc[(splitems_df['Gummy Worms']==True)&(splitems_df['transaction_month']=='April'),'transaction_quantity'].sum())
print(splitems_df.loc[(splitems_df['Gummy Worms']==True)&(splitems_df['transaction_month']=='May'),'transaction_quantity'].sum())
print(splitems_df.loc[(splitems_df['Gummy Worms']==True)&(splitems_df['transaction_month']=='June'),'transaction_quantity'].sum())

#Total quantity of transactions per item from January to June
print(splitems_df.loc[splitems_df['Beef Chicharon']==True, 'transaction_quantity'].sum())
print(splitems_df.loc[splitems_df['Kimchi and Seaweed']==True, 'transaction_quantity'].sum())
print(splitems_df.loc[splitems_df['Nutrional Milk']==True, 'transaction_quantity'].sum())
print(splitems_df.loc[splitems_df['Gummy Vitamins']==True, 'transaction_quantity'].sum())
print(splitems_df.loc[splitems_df['Yummy Vegetables']==True, 'transaction_quantity'].sum())
print(splitems_df.loc[splitems_df['Orange Beans']==True, 'transaction_quantity'].sum())
print(splitems_df.loc[splitems_df['Gummy Worms']==True, 'transaction_quantity'].sum())

EEBC_transactions = [9665,10001,9816,9890,10028,9902,59302]
EEKS_transactions = [9676,9949,9967,9921,9773,10104,59390]
HKNM_transactions = [9727,9691,9876,9786,9881,9767,58728]
HKGV_transactions = [9681,9980,10145,9842,9948,9980,59576]
HKYV_transactions = [9959,10256,9896,9861,9735,9722,59429]
CCOB_transactions = [9774,10037,9611,9914,9964,10106,59406]
CCGW_transactions = [9559,9996,9986,10043,9801,9934,59319]

#Create a monthly transactions df
monthly_transactions_df = pd.DataFrame(
    {'EEBC_SQ':EEBC_transactions,
     'EEKS_SQ':EEKS_transactions,
     'HKNM_SQ':HKNM_transactions,
     'HKGV_SQ':HKGV_transactions,
     'HKYV_SQ':HKYV_transactions,
     'CCOB_SQ':CCOB_transactions,
     'CCGW_SQ':CCGW_transactions
    }, index = pd.Index(['January','February','March','April','May','June','Total']))

#price of each item (manually retrieved)
EEBCp = 1299
EEKSp = 799
HKNMp = 1990
HKGVp = 1500
HKYVp = 500
CCOBp = 199
CCGWp = 150

monthly_transactions_df.insert(1,'EEBC_SV','')
monthly_transactions_df.insert(3,'EEKS_SV','')
monthly_transactions_df.insert(5,'HKNM_SV','')
monthly_transactions_df.insert(7,'HKGV_SV','')
monthly_transactions_df.insert(9,'HKYV_SV','')
monthly_transactions_df.insert(11,'CCOB_SV','')
monthly_transactions_df.insert(13,'CCGW_SV','')
monthly_transactions_df.insert(14,'Total','')

#Monthly revenue of EEBC
EEBC_SQ = monthly_transactions_df['EEBC_SV'] = [x[0] for x in np.array(monthly_transactions_df)]

def get_EEBC_revenue(EEBC_SQ):
    if EEBC_SQ == 0:
        return 0
    else:
        return EEBCp*EEBC_SQ

monthly_transactions_df['EEBC_SV'] = monthly_transactions_df['EEBC_SV'].apply(get_EEBC_revenue)

#Monthly revenue of EEKS
EEKS_SQ = monthly_transactions_df['EEKS_SV'] = [x[2] for x in np.array(monthly_transactions_df)]

def get_EEKS_revenue(EEKS_SQ):
    if EEKS_SQ == 0:
        return 0
    else:
        return EEKSp*EEKS_SQ 

monthly_transactions_df['EEKS_SV'] = monthly_transactions_df['EEKS_SV'].apply(get_EEKS_revenue)

#Monthly revenue of HKNM
HKNM_SQ = monthly_transactions_df['HKNM_SV'] = [x[4] for x in np.array(monthly_transactions_df)]

def get_HKNM_revenue(HKNM_SQ):
    if HKNM_SQ == 0:
        return 0
    else:
        return HKNMp*HKNM_SQ 

monthly_transactions_df['HKNM_SV'] = monthly_transactions_df['HKNM_SV'].apply(get_HKNM_revenue)

#Monthly revenue of HKGV
HKGV_SQ = monthly_transactions_df['HKGV_SV'] = [x[6] for x in np.array(monthly_transactions_df)]

def get_HKGV_revenue(HKGV_SQ):
    if HKGV_SQ == 0:
        return 0
    else:
        return HKGVp*HKGV_SQ 

monthly_transactions_df['HKGV_SV'] = monthly_transactions_df['HKGV_SV'].apply(get_HKGV_revenue)

#Monthly revenue of HKYV
HKYV_SQ = monthly_transactions_df['HKYV_SV'] = [x[8] for x in np.array(monthly_transactions_df)]

def get_HKYV_revenue(HKYV_SQ):
    if HKYV_SQ == 0:
        return 0
    else:
        return HKYVp*HKYV_SQ 

monthly_transactions_df['HKYV_SV'] = monthly_transactions_df['HKYV_SV'].apply(get_HKYV_revenue)

#Monthly revenue of CCOB
CCOB_SQ = monthly_transactions_df['CCOB_SV'] = [x[10] for x in np.array(monthly_transactions_df)]

def get_CCOB_revenue(CCOB_SQ):
    if CCOB_SQ == 0:
        return 0
    else:
        return CCOBp*CCOB_SQ 

monthly_transactions_df['CCOB_SV'] = monthly_transactions_df['CCOB_SV'].apply(get_CCOB_revenue)

#Monthly revenue of CCGW
CCGW_SQ = monthly_transactions_df['CCGW_SV'] = [x[12] for x in np.array(monthly_transactions_df)]

def get_CCGW_revenue(CCGW_SQ):
    if CCGW_SQ == 0:
        return 0
    else:
        return CCGWp*CCGW_SQ 

monthly_transactions_df['CCGW_SV'] = monthly_transactions_df['CCGW_SV'].apply(get_CCGW_revenue)

monthly_transactions_df["Total"] = monthly_transactions_df.sum(axis=1, numeric_only=True)
monthly_transactions_df.drop(['Total'],inplace=True,axis=1)
monthslist = ['January','February','March','April','May','June']

#Obtain a df with just the customers' names and months they transacted
customer_df = splitems_df.groupby(['name','transaction_month'],as_index=False).first()
customer_df.drop(['address','birthdate','mail','sex','username','transaction_value','transaction_date','transaction_items','transaction_quantity','Beef Chicharon','Kimchi and Seaweed','Nutrional Milk','Gummy Vitamins','Yummy Vegetables','Orange Beans','Gummy Worms'], inplace=True, axis=1)

#Get all the months a single customer made a purchase
array_agg = lambda x: '/'.join(x.astype(str))
new_customer_df = customer_df.groupby(['name'], as_index=False).agg({'transaction_month':array_agg})
new_customer_df

#Make a true/false columns for transacted months
for month in monthslist:
    new_customer_df[month]=new_customer_df['transaction_month'].str.contains(month)

#Convert to 0 and 1 T/F table
user_types_df = new_customer_df.loc[:,monthslist[0]:monthslist[len(monthslist)-1]]
user_types_df = user_types_df*1

#Add names back
Extracted_Names = new_customer_df['name']
user_types_df = user_types_df.join(Extracted_Names)

#Re-order columns
user_types_df[['name','January','February','March','April','May','June']]

#Solve for repeaters, inactive, and engaged users
for x, month in enumerate(monthslist):
    if x == 0:
        repeaters = 0
        inactive = 0
    else:
        #Repeaters
        user_repeaters = user_types_df[(user_types_df[monthslist[x-1]] == 1) & (user_types_df[monthslist[x]] == 1)]
        repeaters = len(user_repeaters.index)
        
        #Inactive
        user_inactive = user_types_df.loc[:,monthslist[0]:month]
        user_inactive = user_inactive[(user_inactive[monthslist[x]] == 0)]
        
        user_inactive2 = user_inactive.sum(axis=1)
        user_inactive2 = user_inactive2.tolist()
        inactive = np.count_nonzero(user_inactive2)
        
    #Engaged    
    user_engaged = user_types_df.loc[:, monthslist[0]:month]
    user_engaged2 = user_engaged.sum(axis=1)
    user_engaged2 = user_engaged2.tolist()
    engaged = user_engaged2.count(x+1)
    print(month, ":\t", repeaters, "repeaters\t", inactive, "inactive\t", engaged, "engaged")    
    
#Creating RIE DF
user_data = [[0,5172,5216,5154,5110,5193],[0,1416,1747,1909,1917,1835],[6588,5172,4126,3289,2667,2190]]
RIE_users_df = pd.DataFrame(user_data,columns = ['January','February','March','April','May','June'], index = pd.Index(['Repeaters',"Inactive",'Engaged']))

#Getting sum of total customers for each month
new_customer_df['January'].values.sum()
new_customer_df['February'].values.sum()
new_customer_df['March'].values.sum()
new_customer_df['April'].values.sum()
new_customer_df['May'].values.sum()
new_customer_df['June'].values.sum()

monthlycustomers = [6588,6631,6622,6556,6568,6652]

monthly_customers_df = pd.DataFrame(monthlycustomers, index = pd.Index(monthslist))
monthly_customers_df.columns = ['Total Customers']

#DF of sales quantity
sales_quantity = ['EEBC_SQ','EEKS_SQ','HKNM_SQ','HKGV_SQ','HKYV_SQ','CCOB_SQ','CCGW_SQ']
sales_quantity_df = monthly_transactions_df[sales_quantity]
sales_quantity_df

#Setting defaults for matplotlib graphs/tables
plt.rcParams['figure.dpi'] = 300
plt.rcParams['savefig.dpi'] = 300

#Graph the df in matplotlib table
fig, ax = plt.subplots()
fig.patch.set_visible(False)
ax.axis('off')
ax.axis('tight')
ax.set_title('Sales Quantity')
plt.subplots_adjust(bottom=0.54)
table = ax.table(cellText=sales_quantity_df.values, colLabels=sales_quantity_df.columns,rowLabels=sales_quantity_df.index,loc='center')
fig.tight_layout()
plt.show()
fig.savefig('sales_quantity_df.png', dpi=300)

#DF of sales quantity without Total
quantity_df = sales_quantity_df.drop(sales_quantity_df.index[6])
quantity_df 

#Getting bar graph of total quantity of items sold per month
monthly_quantity_graph = quantity_df.plot(kind='bar',figsize=(25,8)).legend(loc='best')
plt.xlabel("Months")
plt.ylabel("Quantity")
plt.title("Monthly Quantity per Item")
monthly_quantity_graph.figure.savefig('monthly_quantity_graph.png',dpi=300)

#DF of the total quantity of items sold from January to June
totalquantity_df = sales_quantity_df.drop(sales_quantity_df.index[0:6])
totalquantity_df 

#Total quantity for all products during the period of January to June
total_quantities = [59302,59390,58728,59576,59429,59406,59319]
items = ['EEBC','EEKS','HKNM','HKGV','HKYV','CCOB','CCGW']

fig = plt.figure(figsize=(8,4),dpi=200)
plt.plot(items, total_quantities,marker='o')
plt.title('Total Quantity of Items from January to June')
plt.xlabel('Items')
plt.ylabel('Total Quantities')
plt.show()
fig.savefig('TotalQuantity_line.png', dpi=300)

#Each item's quantity per month
EEBC_quantity = [9665,10001,9816,9890,10028,9902]
EEKS_quantity = [9676,9949,9967,9921,9773,10104]
HKNM_quantity = [9727,9691,9876,9786,9881,9767]
HKGV_quantity = [9681,9980,10145,9842,9948,9980]
HKYV_quantity = [9959,10256,9896,9861,9735,9722]
CCOB_quantity = [9774,10037,9611,9914,9964,10106]
CCGW_quantity = [9559,9996,9986,10043,9801,9934]

fig = plt.figure(figsize=(12,8),dpi=200)
plt.plot(monthslist,EEBC_quantity, label = 'EEBC Quantity')
plt.plot(monthslist,EEKS_quantity, label = 'EEKS Quantity')
plt.plot(monthslist,HKNM_quantity, label = 'HKNM Quantity')
plt.plot(monthslist,HKGV_quantity, label = 'HKGV Quantity')
plt.plot(monthslist,HKYV_quantity, label = 'HKYV Quantity')
plt.plot(monthslist,CCOB_quantity, label = 'CCOB Quantity')
plt.plot(monthslist,CCGW_quantity, label = 'CCGW Quantity')
plt.legend(loc=1, prop={'size':8})
plt.title('Item Quantity per Month')
plt.xlabel('Month')
plt.ylabel('Item Quantity')
plt.show()
fig.savefig('ItemQuantityPerMonth.png', dpi=300)

#DF of sale values
sales_value = ['EEBC_SV','EEKS_SV','HKNM_SV','HKGV_SV','HKYV_SV','CCOB_SV','CCGW_SV']
sales_value_df = monthly_transactions_df[sales_value]
sales_value_df

#Making the sales value DF into a matplotlib table
fig, ax = plt.subplots()
fig.patch.set_visible(False)
ax.axis('off')
ax.axis('tight')
ax.set_title('Sales Value (Revenue)')
plt.subplots_adjust(bottom=0.54)
table = ax.table(cellText=sales_value_df.values, colLabels=sales_value_df.columns,rowLabels=sales_value_df.index,loc='center')
fig.tight_layout()
plt.show()
fig.savefig('sales_value_table.png', dpi=300)

#DF of sales values without the total
value_df = sales_value_df.drop(sales_value_df.index[6])
value_df

#Getting bar graph of total sales value (revenue) of items sold per month
monthly_value_graph = value_df.plot(kind='bar',figsize=(22,8)).legend(loc='best')
plt.xlabel("Months")
plt.ylabel("Sales Value")
plt.title("Monthly Sales Value per Item")
monthly_value_graph.figure.savefig('monthly_value_graph.png',dpi=300)

#DF of the total sales value (revenue) of items sold from January to June
totalvalue_df = sales_value_df.drop(sales_quantity_df.index[0:6])
totalvalue_df

#Total sales value (revenue) for all products during the period of January to June
total_salesvalue = [77033298,47452610,116868720,89364000,29714500,11821794,8897850]
items = ['EEBC','EEKS','HKNM','HKGV','HKYV','CCOB','CCGW']

fig = plt.figure(figsize=(8,4),dpi=200)
plt.plot(items, total_salesvalue,marker='o')
plt.title('Total Sales Value (Revenue) of Items')
plt.xlabel('Items')
plt.ylabel('Total Sales Value (Revenue)')
plt.show()
fig.savefig('TotalSalesValue_line.png', dpi=300)

#Each item's sales value (revenue) per month
EEBC_salesvalue = [12554825,12991299,12750984,12847110,13026372,12862698]
EEKS_salesvalue = [7731124,7949251,7963633,7926879,7808627,8073096]
HKNM_salesvalue = [19356730,19285090,19653240,19474140,19663190,19436330]
HKGV_salesvalue = [14521500,14970000,15217500,14763000,14922000,14970000]
HKYV_salesvalue = [4979500,5128000,4948000,4930500,4867500,4861000]
CCOB_salesvalue = [1945026,1997363,1912589,1972886,1982836,2011094]
CCGW_salesvalue = [1433850,1499400,1497900,1506450,1470150,1490100]

fig = plt.figure(figsize=(12,8),dpi=200)
plt.plot(monthslist,EEBC_salesvalue, label = 'EEBC Revenue')
plt.plot(monthslist,EEKS_salesvalue, label = 'EEKS Revenue')
plt.plot(monthslist,HKNM_salesvalue, label = 'HKNM Revenue')
plt.plot(monthslist,HKGV_salesvalue, label = 'HKGV Revenue')
plt.plot(monthslist,HKYV_salesvalue, label = 'HKYV Revenue')
plt.plot(monthslist,CCOB_salesvalue, label = 'CCOB Revenue')
plt.plot(monthslist,CCGW_salesvalue, label = 'CCGW Revenue')
plt.legend(loc=1, prop={'size':8})
plt.title('Item Revenue per Month')
plt.xlabel('Month')
plt.ylabel('Item Revenue')
plt.show()
fig.savefig('ItemRevenuePerMonth.png', dpi=300)

#Monthly customers matplotlib table
fig, ax = plt.subplots()
fig.patch.set_visible(False)
ax.axis('off')
ax.axis('tight')
ax.set_title('Monthly Customers')
plt.subplots_adjust(bottom=0.5)
table = ax.table(cellText=monthly_customers_df.values, colLabels=monthly_customers_df.columns,rowLabels=monthly_customers_df.index,loc='center')
fig.tight_layout()
plt.show()
fig.savefig('monthly_customers_table.png', dpi=300)

#Graph of total customers during each month from January to June
total_customers = [6588,6631,6622,6556,6568,6652]

fig = plt.figure(figsize=(8,4),dpi=200)
plt.plot(monthslist, total_customers,marker='o')
plt.title('Monthly Customers')
plt.xlabel('Months')
plt.ylabel('Total Customers')
plt.show()
fig.savefig('TotalCustomers_line.png', dpi=300)

#Testing table of RIE_users_data
fig, ax = plt.subplots()
fig.patch.set_visible(False)
ax.axis('off')
ax.axis('tight')
ax.set_title('Types of Users per month')
plt.subplots_adjust(bottom=0.7)
table = ax.table(cellText=RIE_users_df.values, colLabels=RIE_users_df.columns,rowLabels=RIE_users_df.index,loc='center')
fig.tight_layout()
plt.show()
fig.savefig('RIE_users_table.png', dpi=300)

#Creating a line chart and table for RIE_users_data
repeaters = [0,5172,5216,5154,5110,5193]
inactive = [0,1416,1747,1909,1917,1835]
engaged = [6588,5172,4126,3289,2667,2190]

columns = monthslist
rows = ['Repeaters','Inactive','Engaged']

n_rows = len(RIE_data)

index = np.arange(len(columns))+0.3
bar_width = 0.6

y_offset = np.zeros(len(columns))

plt.plot(monthslist,repeaters, label = 'Repeaters',marker='o')
plt.plot(monthslist,inactive, label = 'Inactive',marker='o')
plt.plot(monthslist,engaged, label = 'Engaged',marker='o')




RIE_table = plt.table(cellText=cell_text,
                      rowLabels=rows,
                      colLabels=columns,
                      loc='bottom')

plt.subplots_adjust(left=0.2,bottom=0.2)
plt.legend(loc=1, prop={'size':8})
plt.ylabel('Count of User Types')
plt.xticks([])
plt.title('Count of the Types of Users per month')
plt.show()

customer_sex_df = pd.DataFrame(columns=['F','M'])

#T/F column of customers' sex
customer_sex_df['F']=df['sex'].str.contains('F')
customer_sex_df['M']=df['sex'].str.contains('M')
customer_sex_df

#Sum of F/M customers
customer_sex_df['F'].values.sum()
customer_sex_df['M'].values.sum()

#Sorting DF with sex
customer_sex_per_month_df = splitems_df.groupby(['sex','transaction_month','Beef Chicharon','Kimchi and Seaweed','Nutrional Milk', 'Gummy Vitamins', 'Yummy Vegetables', 'Orange Beans', 'Gummy Worms'], as_index=False).first()
customer_sex_per_month_df.drop(['address','birthdate','mail','username','transaction_value','transaction_date','transaction_items','transaction_quantity'],inplace=True,axis=1)
customer_sex_per_month_df

#Number of Male and Female Customers per month
print("F per month:")
print(splitems_df.loc[(splitems_df['sex']=='F')&(splitems_df['transaction_month']=='January'),'name'].count())
print(splitems_df.loc[(splitems_df['sex']=='F')&(splitems_df['transaction_month']=='February'),'name'].count())
print(splitems_df.loc[(splitems_df['sex']=='F')&(splitems_df['transaction_month']=='March'),'name'].count())
print(splitems_df.loc[(splitems_df['sex']=='F')&(splitems_df['transaction_month']=='April'),'name'].count())
print(splitems_df.loc[(splitems_df['sex']=='F')&(splitems_df['transaction_month']=='May'),'name'].count())
print(splitems_df.loc[(splitems_df['sex']=='F')&(splitems_df['transaction_month']=='June'),'name'].count())
print("")
print("Total F:")
print(splitems_df.loc[(splitems_df['sex']=='F'),'name'].count())
print("")
print("M per month:")
print(splitems_df.loc[(splitems_df['sex']=='M')&(splitems_df['transaction_month']=='January'),'name'].count())
print(splitems_df.loc[(splitems_df['sex']=='M')&(splitems_df['transaction_month']=='February'),'name'].count())
print(splitems_df.loc[(splitems_df['sex']=='M')&(splitems_df['transaction_month']=='March'),'name'].count())
print(splitems_df.loc[(splitems_df['sex']=='M')&(splitems_df['transaction_month']=='April'),'name'].count())
print(splitems_df.loc[(splitems_df['sex']=='M')&(splitems_df['transaction_month']=='May'),'name'].count())
print(splitems_df.loc[(splitems_df['sex']=='M')&(splitems_df['transaction_month']=='June'),'name'].count())
print("")
print("Total M:")
print(splitems_df.loc[(splitems_df['sex']=='M'),'name'].count())

#Number of Male and Female Customers Lists
F_customers = [13449,13989,13727,13797,13688,13750,82400]
M_customers = [13679,13986,14123,13965,14015,13951,83719]
monthslistotal = ['January','February','March','April','May','June','Total']
total_FM_df= pd.DataFrame([F_customers,M_customers], columns=monthslistotal, index=['F_customers','M_customers'])
total_FM_df

#Table of total_FM_df
fig, ax = plt.subplots()
fig.patch.set_visible(False)
ax.axis('off')
ax.axis('tight')
ax.set_title('Total No. of Female and Male Customers from January to June')
plt.subplots_adjust(bottom=0.75)
table = ax.table(cellText=total_FM_df.values, colLabels=total_FM_df.columns,rowLabels=total_FM_df.index,loc='center')
fig.tight_layout()
plt.show()
fig.savefig('total_FM_df_table', dpi=300)

#Total Female/Male customers per month
F_customers_mon =[13449,13989,13727,13797,13688,13750]
M_customers_mon = [13679,13986,14123,13965,14015,13951]

fig = plt.figure(figsize=(12,8),dpi=200)
plt.plot(monthslist,F_customers_mon, label = 'F customers',marker = "o", color = 'purple')
plt.plot(monthslist,M_customers_mon, label = 'M customers',marker = "o", color = 'red')
plt.legend(loc=1, prop={'size':8})

plt.title('Total No. of Female and Male Customers per Month (January to June)')
plt.xlabel('Month')
plt.ylabel('No. of Customers')
plt.show()
fig.savefig('total_FM_line',dpi=300)

#Total Female/Male customers per month
F_customers_mon =[13449,13989,13727,13797,13688,13750]
M_customers_mon = [13679,13986,14123,13965,14015,13951]

X = monthslist
X_axis = np.arange(len(X))

plt.bar(X_axis - 0.2, F_customers_mon, 0.4, label = 'F customers', color = 'purple')
plt.bar(X_axis + 0.2, M_customers_mon, 0.4, label = 'M customers', color = 'red')
plt.xticks(X_axis,X)
plt.legend(loc=4, prop={'size':8})
plt.title('Total No. of Female and Male Customers')
plt.xlabel('Month')
plt.ylabel('No. of Customers')
plt.show()
fig.savefig('total_FM_bar', dpi=200)

#Number of Female Customers per Item per Month
print("EEBC F:")
print("")
print(splitems_df.loc[(splitems_df['sex']=='F')&(splitems_df['transaction_month']=='January')&(splitems_df['Beef Chicharon']==True),'name'].count())
print(splitems_df.loc[(splitems_df['sex']=='F')&(splitems_df['transaction_month']=='February')&(splitems_df['Beef Chicharon']==True),'name'].count())
print(splitems_df.loc[(splitems_df['sex']=='F')&(splitems_df['transaction_month']=='March')&(splitems_df['Beef Chicharon']==True),'name'].count())
print(splitems_df.loc[(splitems_df['sex']=='F')&(splitems_df['transaction_month']=='April')&(splitems_df['Beef Chicharon']==True),'name'].count())
print(splitems_df.loc[(splitems_df['sex']=='F')&(splitems_df['transaction_month']=='May')&(splitems_df['Beef Chicharon']==True),'name'].count())
print(splitems_df.loc[(splitems_df['sex']=='F')&(splitems_df['transaction_month']=='June')&(splitems_df['Beef Chicharon']==True),'name'].count())
print("")
print("Total EEBC F:")
print(splitems_df.loc[(splitems_df['sex']=='F')&(splitems_df['Beef Chicharon']==True),'name'].count())
print("")
print("EEKS F:")
print(splitems_df.loc[(splitems_df['sex']=='F')&(splitems_df['transaction_month']=='January')&(splitems_df['Kimchi and Seaweed']==True),'name'].count())
print(splitems_df.loc[(splitems_df['sex']=='F')&(splitems_df['transaction_month']=='February')&(splitems_df['Kimchi and Seaweed']==True),'name'].count())
print(splitems_df.loc[(splitems_df['sex']=='F')&(splitems_df['transaction_month']=='March')&(splitems_df['Kimchi and Seaweed']==True),'name'].count())
print(splitems_df.loc[(splitems_df['sex']=='F')&(splitems_df['transaction_month']=='April')&(splitems_df['Kimchi and Seaweed']==True),'name'].count())
print(splitems_df.loc[(splitems_df['sex']=='F')&(splitems_df['transaction_month']=='May')&(splitems_df['Kimchi and Seaweed']==True),'name'].count())
print(splitems_df.loc[(splitems_df['sex']=='F')&(splitems_df['transaction_month']=='June')&(splitems_df['Kimchi and Seaweed']==True),'name'].count())
print("")
print("Total EEKS F:")
print(splitems_df.loc[(splitems_df['sex']=='F')&(splitems_df['Kimchi and Seaweed']==True),'name'].count())
print("")
print("HKNM F:")
print(splitems_df.loc[(splitems_df['sex']=='F')&(splitems_df['transaction_month']=='January')&(splitems_df['Nutrional Milk']==True),'name'].count())
print(splitems_df.loc[(splitems_df['sex']=='F')&(splitems_df['transaction_month']=='February')&(splitems_df['Nutrional Milk']==True),'name'].count())
print(splitems_df.loc[(splitems_df['sex']=='F')&(splitems_df['transaction_month']=='March')&(splitems_df['Nutrional Milk']==True),'name'].count())
print(splitems_df.loc[(splitems_df['sex']=='F')&(splitems_df['transaction_month']=='April')&(splitems_df['Nutrional Milk']==True),'name'].count())
print(splitems_df.loc[(splitems_df['sex']=='F')&(splitems_df['transaction_month']=='May')&(splitems_df['Nutrional Milk']==True),'name'].count())
print(splitems_df.loc[(splitems_df['sex']=='F')&(splitems_df['transaction_month']=='June')&(splitems_df['Nutrional Milk']==True),'name'].count())
print("")
print("Total HKNM F:")
print(splitems_df.loc[(splitems_df['sex']=='F')&(splitems_df['Nutrional Milk']==True),'name'].count())
print("")
print("HKGV F:")
print(splitems_df.loc[(splitems_df['sex']=='F')&(splitems_df['transaction_month']=='January')&(splitems_df['Gummy Vitamins']==True),'name'].count())
print(splitems_df.loc[(splitems_df['sex']=='F')&(splitems_df['transaction_month']=='February')&(splitems_df['Gummy Vitamins']==True),'name'].count())
print(splitems_df.loc[(splitems_df['sex']=='F')&(splitems_df['transaction_month']=='March')&(splitems_df['Gummy Vitamins']==True),'name'].count())
print(splitems_df.loc[(splitems_df['sex']=='F')&(splitems_df['transaction_month']=='April')&(splitems_df['Gummy Vitamins']==True),'name'].count())
print(splitems_df.loc[(splitems_df['sex']=='F')&(splitems_df['transaction_month']=='May')&(splitems_df['Gummy Vitamins']==True),'name'].count())
print(splitems_df.loc[(splitems_df['sex']=='F')&(splitems_df['transaction_month']=='June')&(splitems_df['Gummy Vitamins']==True),'name'].count())
print("")
print("Total HKGV F:")
print(splitems_df.loc[(splitems_df['sex']=='F')&(splitems_df['Gummy Vitamins']==True),'name'].count())
print("")
print("HKYV F:")
print(splitems_df.loc[(splitems_df['sex']=='F')&(splitems_df['transaction_month']=='January')&(splitems_df['Yummy Vegetables']==True),'name'].count())
print(splitems_df.loc[(splitems_df['sex']=='F')&(splitems_df['transaction_month']=='February')&(splitems_df['Yummy Vegetables']==True),'name'].count())
print(splitems_df.loc[(splitems_df['sex']=='F')&(splitems_df['transaction_month']=='March')&(splitems_df['Yummy Vegetables']==True),'name'].count())
print(splitems_df.loc[(splitems_df['sex']=='F')&(splitems_df['transaction_month']=='April')&(splitems_df['Yummy Vegetables']==True),'name'].count())
print(splitems_df.loc[(splitems_df['sex']=='F')&(splitems_df['transaction_month']=='May')&(splitems_df['Yummy Vegetables']==True),'name'].count())
print(splitems_df.loc[(splitems_df['sex']=='F')&(splitems_df['transaction_month']=='June')&(splitems_df['Yummy Vegetables']==True),'name'].count())
print("")
print("Total HKYV F:")
print(splitems_df.loc[(splitems_df['sex']=='F')&(splitems_df['Yummy Vegetables']==True),'name'].count())
print("")
print("CCOB F:")
print(splitems_df.loc[(splitems_df['sex']=='F')&(splitems_df['transaction_month']=='January')&(splitems_df['Orange Beans']==True),'name'].count())
print(splitems_df.loc[(splitems_df['sex']=='F')&(splitems_df['transaction_month']=='February')&(splitems_df['Orange Beans']==True),'name'].count())
print(splitems_df.loc[(splitems_df['sex']=='F')&(splitems_df['transaction_month']=='March')&(splitems_df['Orange Beans']==True),'name'].count())
print(splitems_df.loc[(splitems_df['sex']=='F')&(splitems_df['transaction_month']=='April')&(splitems_df['Orange Beans']==True),'name'].count())
print(splitems_df.loc[(splitems_df['sex']=='F')&(splitems_df['transaction_month']=='May')&(splitems_df['Orange Beans']==True),'name'].count())
print(splitems_df.loc[(splitems_df['sex']=='F')&(splitems_df['transaction_month']=='June')&(splitems_df['Orange Beans']==True),'name'].count())
print("")
print("Total CCOB F:")
print(splitems_df.loc[(splitems_df['sex']=='F')&(splitems_df['Orange Beans']==True),'name'].count())
print("")
print("CCGW F:")
print(splitems_df.loc[(splitems_df['sex']=='F')&(splitems_df['transaction_month']=='January')&(splitems_df['Gummy Worms']==True),'name'].count())
print(splitems_df.loc[(splitems_df['sex']=='F')&(splitems_df['transaction_month']=='February')&(splitems_df['Gummy Worms']==True),'name'].count())
print(splitems_df.loc[(splitems_df['sex']=='F')&(splitems_df['transaction_month']=='March')&(splitems_df['Gummy Worms']==True),'name'].count())
print(splitems_df.loc[(splitems_df['sex']=='F')&(splitems_df['transaction_month']=='April')&(splitems_df['Gummy Worms']==True),'name'].count())
print(splitems_df.loc[(splitems_df['sex']=='F')&(splitems_df['transaction_month']=='May')&(splitems_df['Gummy Worms']==True),'name'].count())
print(splitems_df.loc[(splitems_df['sex']=='F')&(splitems_df['transaction_month']=='June')&(splitems_df['Gummy Worms']==True),'name'].count())
print("")
print("Total CCGW F:")
print(splitems_df.loc[(splitems_df['sex']=='F')&(splitems_df['Gummy Worms']==True),'name'].count())
print("")

#Number of Male Customers per Item per Month
print("")
print("EEBC M:")
print(splitems_df.loc[(splitems_df['sex']=='M')&(splitems_df['transaction_month']=='January')&(splitems_df['Beef Chicharon']==True),'name'].count())
print(splitems_df.loc[(splitems_df['sex']=='M')&(splitems_df['transaction_month']=='February')&(splitems_df['Beef Chicharon']==True),'name'].count())
print(splitems_df.loc[(splitems_df['sex']=='M')&(splitems_df['transaction_month']=='March')&(splitems_df['Beef Chicharon']==True),'name'].count())
print(splitems_df.loc[(splitems_df['sex']=='M')&(splitems_df['transaction_month']=='April')&(splitems_df['Beef Chicharon']==True),'name'].count())
print(splitems_df.loc[(splitems_df['sex']=='M')&(splitems_df['transaction_month']=='May')&(splitems_df['Beef Chicharon']==True),'name'].count())
print(splitems_df.loc[(splitems_df['sex']=='M')&(splitems_df['transaction_month']=='June')&(splitems_df['Beef Chicharon']==True),'name'].count())
print("")
print("Total EEBC M:")
print(splitems_df.loc[(splitems_df['sex']=='M')&(splitems_df['Beef Chicharon']==True),'name'].count())
print("")
print("EEKS M:")
print(splitems_df.loc[(splitems_df['sex']=='M')&(splitems_df['transaction_month']=='January')&(splitems_df['Kimchi and Seaweed']==True),'name'].count())
print(splitems_df.loc[(splitems_df['sex']=='M')&(splitems_df['transaction_month']=='February')&(splitems_df['Kimchi and Seaweed']==True),'name'].count())
print(splitems_df.loc[(splitems_df['sex']=='M')&(splitems_df['transaction_month']=='March')&(splitems_df['Kimchi and Seaweed']==True),'name'].count())
print(splitems_df.loc[(splitems_df['sex']=='M')&(splitems_df['transaction_month']=='April')&(splitems_df['Kimchi and Seaweed']==True),'name'].count())
print(splitems_df.loc[(splitems_df['sex']=='M')&(splitems_df['transaction_month']=='May')&(splitems_df['Kimchi and Seaweed']==True),'name'].count())
print(splitems_df.loc[(splitems_df['sex']=='M')&(splitems_df['transaction_month']=='June')&(splitems_df['Kimchi and Seaweed']==True),'name'].count())
print("")
print("Total EEKS M:")
print(splitems_df.loc[(splitems_df['sex']=='M')&(splitems_df['Kimchi and Seaweed']==True),'name'].count())
print("")
print("HKNM M:")
print(splitems_df.loc[(splitems_df['sex']=='M')&(splitems_df['transaction_month']=='January')&(splitems_df['Nutrional Milk']==True),'name'].count())
print(splitems_df.loc[(splitems_df['sex']=='M')&(splitems_df['transaction_month']=='February')&(splitems_df['Nutrional Milk']==True),'name'].count())
print(splitems_df.loc[(splitems_df['sex']=='M')&(splitems_df['transaction_month']=='March')&(splitems_df['Nutrional Milk']==True),'name'].count())
print(splitems_df.loc[(splitems_df['sex']=='M')&(splitems_df['transaction_month']=='April')&(splitems_df['Nutrional Milk']==True),'name'].count())
print(splitems_df.loc[(splitems_df['sex']=='M')&(splitems_df['transaction_month']=='May')&(splitems_df['Nutrional Milk']==True),'name'].count())
print(splitems_df.loc[(splitems_df['sex']=='M')&(splitems_df['transaction_month']=='June')&(splitems_df['Nutrional Milk']==True),'name'].count())
print("")
print("Total HKNM M:")
print(splitems_df.loc[(splitems_df['sex']=='M')&(splitems_df['Nutrional Milk']==True),'name'].count())
print("")
print("HKGV M:")
print(splitems_df.loc[(splitems_df['sex']=='M')&(splitems_df['transaction_month']=='January')&(splitems_df['Gummy Vitamins']==True),'name'].count())
print(splitems_df.loc[(splitems_df['sex']=='M')&(splitems_df['transaction_month']=='February')&(splitems_df['Gummy Vitamins']==True),'name'].count())
print(splitems_df.loc[(splitems_df['sex']=='M')&(splitems_df['transaction_month']=='March')&(splitems_df['Gummy Vitamins']==True),'name'].count())
print(splitems_df.loc[(splitems_df['sex']=='M')&(splitems_df['transaction_month']=='April')&(splitems_df['Gummy Vitamins']==True),'name'].count())
print(splitems_df.loc[(splitems_df['sex']=='M')&(splitems_df['transaction_month']=='May')&(splitems_df['Gummy Vitamins']==True),'name'].count())
print(splitems_df.loc[(splitems_df['sex']=='M')&(splitems_df['transaction_month']=='June')&(splitems_df['Gummy Vitamins']==True),'name'].count())
print("")
print("Total HKGV M:")
print(splitems_df.loc[(splitems_df['sex']=='M')&(splitems_df['Gummy Vitamins']==True),'name'].count())
print("")
print("HKYV M:")
print(splitems_df.loc[(splitems_df['sex']=='M')&(splitems_df['transaction_month']=='January')&(splitems_df['Yummy Vegetables']==True),'name'].count())
print(splitems_df.loc[(splitems_df['sex']=='M')&(splitems_df['transaction_month']=='February')&(splitems_df['Yummy Vegetables']==True),'name'].count())
print(splitems_df.loc[(splitems_df['sex']=='M')&(splitems_df['transaction_month']=='March')&(splitems_df['Yummy Vegetables']==True),'name'].count())
print(splitems_df.loc[(splitems_df['sex']=='M')&(splitems_df['transaction_month']=='April')&(splitems_df['Yummy Vegetables']==True),'name'].count())
print(splitems_df.loc[(splitems_df['sex']=='M')&(splitems_df['transaction_month']=='May')&(splitems_df['Yummy Vegetables']==True),'name'].count())
print(splitems_df.loc[(splitems_df['sex']=='M')&(splitems_df['transaction_month']=='June')&(splitems_df['Yummy Vegetables']==True),'name'].count())
print("")
print("Total HKYV M:")
print(splitems_df.loc[(splitems_df['sex']=='M')&(splitems_df['Yummy Vegetables']==True),'name'].count())
print("")
print("CCOB M:")
print(splitems_df.loc[(splitems_df['sex']=='M')&(splitems_df['transaction_month']=='January')&(splitems_df['Orange Beans']==True),'name'].count())
print(splitems_df.loc[(splitems_df['sex']=='M')&(splitems_df['transaction_month']=='February')&(splitems_df['Orange Beans']==True),'name'].count())
print(splitems_df.loc[(splitems_df['sex']=='M')&(splitems_df['transaction_month']=='March')&(splitems_df['Orange Beans']==True),'name'].count())
print(splitems_df.loc[(splitems_df['sex']=='M')&(splitems_df['transaction_month']=='April')&(splitems_df['Orange Beans']==True),'name'].count())
print(splitems_df.loc[(splitems_df['sex']=='M')&(splitems_df['transaction_month']=='May')&(splitems_df['Orange Beans']==True),'name'].count())
print(splitems_df.loc[(splitems_df['sex']=='M')&(splitems_df['transaction_month']=='June')&(splitems_df['Orange Beans']==True),'name'].count())
print("")
print("Total CCOB M:")
print(splitems_df.loc[(splitems_df['sex']=='M')&(splitems_df['Orange Beans']==True),'name'].count())
print("")
print("CCGW M:")
print(splitems_df.loc[(splitems_df['sex']=='M')&(splitems_df['transaction_month']=='January')&(splitems_df['Gummy Worms']==True),'name'].count())
print(splitems_df.loc[(splitems_df['sex']=='M')&(splitems_df['transaction_month']=='February')&(splitems_df['Gummy Worms']==True),'name'].count())
print(splitems_df.loc[(splitems_df['sex']=='M')&(splitems_df['transaction_month']=='March')&(splitems_df['Gummy Worms']==True),'name'].count())
print(splitems_df.loc[(splitems_df['sex']=='M')&(splitems_df['transaction_month']=='April')&(splitems_df['Gummy Worms']==True),'name'].count())
print(splitems_df.loc[(splitems_df['sex']=='M')&(splitems_df['transaction_month']=='May')&(splitems_df['Gummy Worms']==True),'name'].count())
print(splitems_df.loc[(splitems_df['sex']=='M')&(splitems_df['transaction_month']=='June')&(splitems_df['Gummy Worms']==True),'name'].count())
print("")
print("Total CCGW M:")
print(splitems_df.loc[(splitems_df['sex']=='M')&(splitems_df['Gummy Worms']==True),'name'].count())

#Number of Female/Male customers per item per month
F_items_jan = [1938,1897,1933,1921,1964,1900,1896]
F_items_feb = [2015,2036,1935,1970,2008,1996,2029]
F_items_mar = [1959,1927,1945,1970,2027,1929,1970]
F_items_apr = [1968,2009,1914,1906,2022,1966,2012]
F_items_may = [1935,1984,1970,1964,1961,1969,1905]
F_items_jun = [1981,2004,1882,1981,1904,2050,1948]
F_items_tot = [11796,11857,11579,11712,11886,11810,11760]

M_items_jan = [1919,2016,1939,1939,2012,1948,1906]
M_items_feb = [1989,1978,1964,2020,2064,1972,1999]
M_items_mar = [2012,2062,2017,2082,1961,1979,2010]
M_items_apr = [2024,1940,2038,2020,1953,2004,1987]
M_items_may = [2053,1953,2027,2005,1954,2006,2017]
M_items_jun = [1992,2015,1968,2016,2002,1979,1979]
M_items_tot = [11989,11964,11953,12082,11946,11887,11898]

F_items_month_df = pd.DataFrame([F_items_jan,F_items_feb,F_items_mar,F_items_apr,F_items_may,F_items_jun],columns=['EEBC_F','EEKS_F','HKNM_F','HKGV_F','HKYV_F','CCOB_F','CCGW_F'],index=monthslist)
F_items_montht_df = pd.DataFrame([F_items_jan,F_items_feb,F_items_mar,F_items_apr,F_items_may,F_items_jun,F_items_tot],columns=['EEBC_F','EEKS_F','HKNM_F','HKGV_F','HKYV_F','CCOB_F','CCGW_F'],index=monthslistotal)
M_items_month_df = pd.DataFrame([M_items_jan,M_items_feb,M_items_mar,M_items_apr,M_items_may,M_items_jun],columns=['EEBC_M','EEKS_M','HKNM_M','HKGV_M','HKYV_M','CCOB_M','CCGW_M'],index=monthslist)
M_items_montht_df = pd.DataFrame([M_items_jan,M_items_feb,M_items_mar,M_items_apr,M_items_may,M_items_jun,M_items_tot],columns=['EEBC_M','EEKS_M','HKNM_M','HKGV_M','HKYV_M','CCOB_M','CCGW_M'],index=monthslistotal)

#Table of F_items_montht_df
fig, ax = plt.subplots()
fig.patch.set_visible(False)
ax.axis('off')
ax.axis('tight')
ax.set_title('Total No. of Female Customers per Item')
plt.subplots_adjust(bottom=0.53)
table = ax.table(cellText=F_items_montht_df.values, colLabels=F_items_montht_df.columns,rowLabels=F_items_montht_df.index,loc='center')
fig.tight_layout()
plt.show()
fig.savefig('F_items_montht_df_table', dpi=200)

#Table of M_items_montht_df
fig, ax = plt.subplots()
fig.patch.set_visible(False)
ax.axis('off')
ax.axis('tight')
ax.set_title('Total No. of Male Customers per Item')
plt.subplots_adjust(bottom=0.53)
table = ax.table(cellText=M_items_montht_df.values, colLabels=M_items_montht_df.columns,rowLabels=M_items_montht_df.index,loc='center')
fig.tight_layout()
plt.show()
fig.savefig('M_items_montht_df_table', dpi=200)

M_mitems_graph = M_items_month_df.plot(kind='bar',figsize=(22,8)).legend(loc='best')
plt.ylabel('Months')
plt.xlabel('Items (M)')
plt.title('Number of Male customers per item per month')
M_mitems_graph.figure.savefig('M_mitems_bar.png')

F_mitems_graph = F_items_month_df.plot(kind='bar',figsize=(22,8)).legend(loc='best')
plt.ylabel('Months')
plt.xlabel('Items (F)')
plt.title('Number of Female customers per item per month')
F_mitems_graph.figure.savefig('F_mitems_bar.png')

#Total Female/Male customers per item
F_per_item = [11796,11857,11579,11712,11886,11810,11760]
M_per_item = [11989,11964,11953,12082,11946,11887,11898]

fig = plt.figure(figsize=(12,8),dpi=200)
plt.plot(itemslist,F_per_item, label = 'F customers', marker = "o")
plt.plot(itemslist,M_per_item, label = 'M customers', marker = "o")
plt.legend(loc=1, prop={'size':8})

plt.title('Total Female/Male Customers per item')
plt.xlabel('Items')
plt.ylabel('No. of Customers')
plt.show()
fig.savefig('total_FM_item_line',dpi=200)

#Unqiue Customers DF
unique_customers_df = splitems_df.groupby(['name'],as_index=False).first()
unique_customers_df

#Number of Unique Male and Female Customers per month
print("Unique F per Month:")
print(unique_customers_df.loc[(unique_customers_df['sex']=='F')&(unique_customers_df['transaction_month']=='January'),'name'].count())
print(unique_customers_df.loc[(unique_customers_df['sex']=='F')&(unique_customers_df['transaction_month']=='February'),'name'].count())
print(unique_customers_df.loc[(unique_customers_df['sex']=='F')&(unique_customers_df['transaction_month']=='March'),'name'].count())
print(unique_customers_df.loc[(unique_customers_df['sex']=='F')&(unique_customers_df['transaction_month']=='April'),'name'].count())
print(unique_customers_df.loc[(unique_customers_df['sex']=='F')&(unique_customers_df['transaction_month']=='May'),'name'].count())
print(unique_customers_df.loc[(unique_customers_df['sex']=='F')&(unique_customers_df['transaction_month']=='June'),'name'].count())
print("")
print("Total Unique F:")
print(unique_customers_df.loc[(unique_customers_df['sex']=='F'),'name'].count())
print("")
print("Unique M per Month:")
print(unique_customers_df.loc[(unique_customers_df['sex']=='M')&(unique_customers_df['transaction_month']=='January'),'name'].count())
print(unique_customers_df.loc[(unique_customers_df['sex']=='M')&(unique_customers_df['transaction_month']=='February'),'name'].count())
print(unique_customers_df.loc[(unique_customers_df['sex']=='M')&(unique_customers_df['transaction_month']=='March'),'name'].count())
print(unique_customers_df.loc[(unique_customers_df['sex']=='M')&(unique_customers_df['transaction_month']=='April'),'name'].count())
print(unique_customers_df.loc[(unique_customers_df['sex']=='M')&(unique_customers_df['transaction_month']=='May'),'name'].count())
print(unique_customers_df.loc[(unique_customers_df['sex']=='M')&(unique_customers_df['transaction_month']=='June'),'name'].count())
print("")
print("Total Unique M:")
print(unique_customers_df.loc[(unique_customers_df['sex']=='M'),'name'].count())

#Number of Unique Male and Female Customers
F_customers_unique = [3301,752,163,50,10,2,4278]
M_customers_unique = [3287,707,159,46,10,0,4209]
FM_Totals_unique = [4278,4209]
total_UFM_df = pd.DataFrame([F_customers_unique,M_customers_unique],columns=monthslistotal,index=['F_customers_unique','M_customers_unique'])
total_UFM_df

#Table of total_UFM_df
fig, ax = plt.subplots()
fig.patch.set_visible(False)
ax.axis('off')
ax.axis('tight')
ax.set_title('Total No. of Unique Female and Male Customers from January to June')
plt.subplots_adjust(bottom=0.75)
table = ax.table(cellText=total_UFM_df.values, colLabels=total_UFM_df.columns,rowLabels=total_UFM_df.index,loc='center')
fig.tight_layout()
plt.show()
fig.savefig('total_UFM_df_table', dpi=200)

#Total Unique Female/Male customers per month
UF_customers_mon = [3301,752,163,50,10,2]
UM_customers_mon = [3287,707,159,46,10,0]
X = monthslist
X_axis = np.arange(len(X))

plt.bar(X_axis - 0.2, UF_customers_mon, 0.4, label = 'UF customers', color = 'purple')
plt.bar(X_axis + 0.2, UM_customers_mon, 0.4, label = 'UM customers', color = 'red')
plt.xticks(X_axis,X)
plt.legend(loc=1, prop={'size':8})
plt.title('Total No. of Unique Female and Male Customers')
plt.xlabel('Month')
plt.ylabel('No. of Customers')
plt.show()
fig.savefig('total_UFM_bar', dpi=200)

#Total Unique Female/Male customers per month
UF_customers_mon = [3301,752,163,50,10,2]
UM_customers_mon = [3287,707,159,46,10,0]

fig = plt.figure(figsize=(12,8),dpi=200)
plt.plot(monthslist,UF_customers_mon, label = 'UF customers',color='purple')
plt.plot(monthslist,UM_customers_mon, label = 'UM customers',color='red')
plt.legend(loc=1, prop={'size':8})

plt.title('Total No. of Unique Female and Male Customers')
plt.xlabel('Month')
plt.ylabel('No. of Customers')
plt.show()
fig.savefig('total_UFM_line', dpi=200)

#Number of Unique Female Customers per Item per Month
print("Unique EEBC F")
print("")
print(unique_customers_df.loc[(unique_customers_df['sex']=='F')&(unique_customers_df['transaction_month']=='January')&(unique_customers_df['Beef Chicharon']==True),'name'].count())
print(unique_customers_df.loc[(unique_customers_df['sex']=='F')&(unique_customers_df['transaction_month']=='February')&(unique_customers_df['Beef Chicharon']==True),'name'].count())
print(unique_customers_df.loc[(unique_customers_df['sex']=='F')&(unique_customers_df['transaction_month']=='March')&(unique_customers_df['Beef Chicharon']==True),'name'].count())
print(unique_customers_df.loc[(unique_customers_df['sex']=='F')&(unique_customers_df['transaction_month']=='April')&(unique_customers_df['Beef Chicharon']==True),'name'].count())
print(unique_customers_df.loc[(unique_customers_df['sex']=='F')&(unique_customers_df['transaction_month']=='May')&(unique_customers_df['Beef Chicharon']==True),'name'].count())
print(unique_customers_df.loc[(unique_customers_df['sex']=='F')&(unique_customers_df['transaction_month']=='June')&(unique_customers_df['Beef Chicharon']==True),'name'].count())
print("")
print("Unique EEBC F Total")
print(unique_customers_df.loc[(unique_customers_df['sex']=='F')&(unique_customers_df['Beef Chicharon']==True),'name'].count())
print("")
print("Unique EEKS F")
print("")
print(unique_customers_df.loc[(unique_customers_df['sex']=='F')&(unique_customers_df['transaction_month']=='January')&(unique_customers_df['Kimchi and Seaweed']==True),'name'].count())
print(unique_customers_df.loc[(unique_customers_df['sex']=='F')&(unique_customers_df['transaction_month']=='February')&(unique_customers_df['Kimchi and Seaweed']==True),'name'].count())
print(unique_customers_df.loc[(unique_customers_df['sex']=='F')&(unique_customers_df['transaction_month']=='March')&(unique_customers_df['Kimchi and Seaweed']==True),'name'].count())
print(unique_customers_df.loc[(unique_customers_df['sex']=='F')&(unique_customers_df['transaction_month']=='April')&(unique_customers_df['Kimchi and Seaweed']==True),'name'].count())
print(unique_customers_df.loc[(unique_customers_df['sex']=='F')&(unique_customers_df['transaction_month']=='May')&(unique_customers_df['Kimchi and Seaweed']==True),'name'].count())
print(unique_customers_df.loc[(unique_customers_df['sex']=='F')&(unique_customers_df['transaction_month']=='June')&(unique_customers_df['Kimchi and Seaweed']==True),'name'].count())
print("")
print("Unique EEKS F Total")
print(unique_customers_df.loc[(unique_customers_df['sex']=='F')&(unique_customers_df['Kimchi and Seaweed']==True),'name'].count())
print("")
print("Unique HKNM F")
print("")
print(unique_customers_df.loc[(unique_customers_df['sex']=='F')&(unique_customers_df['transaction_month']=='January')&(unique_customers_df['Nutrional Milk']==True),'name'].count())
print(unique_customers_df.loc[(unique_customers_df['sex']=='F')&(unique_customers_df['transaction_month']=='February')&(unique_customers_df['Nutrional Milk']==True),'name'].count())
print(unique_customers_df.loc[(unique_customers_df['sex']=='F')&(unique_customers_df['transaction_month']=='March')&(unique_customers_df['Nutrional Milk']==True),'name'].count())
print(unique_customers_df.loc[(unique_customers_df['sex']=='F')&(unique_customers_df['transaction_month']=='April')&(unique_customers_df['Nutrional Milk']==True),'name'].count())
print(unique_customers_df.loc[(unique_customers_df['sex']=='F')&(unique_customers_df['transaction_month']=='May')&(unique_customers_df['Nutrional Milk']==True),'name'].count())
print(unique_customers_df.loc[(unique_customers_df['sex']=='F')&(unique_customers_df['transaction_month']=='June')&(unique_customers_df['Nutrional Milk']==True),'name'].count())
print("")
print("Unique HKNM F Total")
print(unique_customers_df.loc[(unique_customers_df['sex']=='F')&(unique_customers_df['Nutrional Milk']==True),'name'].count())
print("")
print("Unique HKGV F")
print("")
print(unique_customers_df.loc[(unique_customers_df['sex']=='F')&(unique_customers_df['transaction_month']=='January')&(unique_customers_df['Gummy Vitamins']==True),'name'].count())
print(unique_customers_df.loc[(unique_customers_df['sex']=='F')&(unique_customers_df['transaction_month']=='February')&(unique_customers_df['Gummy Vitamins']==True),'name'].count())
print(unique_customers_df.loc[(unique_customers_df['sex']=='F')&(unique_customers_df['transaction_month']=='March')&(unique_customers_df['Gummy Vitamins']==True),'name'].count())
print(unique_customers_df.loc[(unique_customers_df['sex']=='F')&(unique_customers_df['transaction_month']=='April')&(unique_customers_df['Gummy Vitamins']==True),'name'].count())
print(unique_customers_df.loc[(unique_customers_df['sex']=='F')&(unique_customers_df['transaction_month']=='May')&(unique_customers_df['Gummy Vitamins']==True),'name'].count())
print(unique_customers_df.loc[(unique_customers_df['sex']=='F')&(unique_customers_df['transaction_month']=='June')&(unique_customers_df['Gummy Vitamins']==True),'name'].count())
print("")
print("Unique HKGV F Total")
print(unique_customers_df.loc[(unique_customers_df['sex']=='F')&(unique_customers_df['Gummy Vitamins']==True),'name'].count())
print("")
print("Unique HKYV F")
print("")
print(unique_customers_df.loc[(unique_customers_df['sex']=='F')&(unique_customers_df['transaction_month']=='January')&(unique_customers_df['Yummy Vegetables']==True),'name'].count())
print(unique_customers_df.loc[(unique_customers_df['sex']=='F')&(unique_customers_df['transaction_month']=='February')&(unique_customers_df['Yummy Vegetables']==True),'name'].count())
print(unique_customers_df.loc[(unique_customers_df['sex']=='F')&(unique_customers_df['transaction_month']=='March')&(unique_customers_df['Yummy Vegetables']==True),'name'].count())
print(unique_customers_df.loc[(unique_customers_df['sex']=='F')&(unique_customers_df['transaction_month']=='April')&(unique_customers_df['Yummy Vegetables']==True),'name'].count())
print(unique_customers_df.loc[(unique_customers_df['sex']=='F')&(unique_customers_df['transaction_month']=='May')&(unique_customers_df['Yummy Vegetables']==True),'name'].count())
print(unique_customers_df.loc[(unique_customers_df['sex']=='F')&(unique_customers_df['transaction_month']=='June')&(unique_customers_df['Yummy Vegetables']==True),'name'].count())
print("")
print("Unique HKYV F Total")
print(unique_customers_df.loc[(unique_customers_df['sex']=='F')&(unique_customers_df['Yummy Vegetables']==True),'name'].count())
print("")
print("Unique CCOB F")
print("")
print(unique_customers_df.loc[(unique_customers_df['sex']=='F')&(unique_customers_df['transaction_month']=='January')&(unique_customers_df['Orange Beans']==True),'name'].count())
print(unique_customers_df.loc[(unique_customers_df['sex']=='F')&(unique_customers_df['transaction_month']=='February')&(unique_customers_df['Orange Beans']==True),'name'].count())
print(unique_customers_df.loc[(unique_customers_df['sex']=='F')&(unique_customers_df['transaction_month']=='March')&(unique_customers_df['Orange Beans']==True),'name'].count())
print(unique_customers_df.loc[(unique_customers_df['sex']=='F')&(unique_customers_df['transaction_month']=='April')&(unique_customers_df['Orange Beans']==True),'name'].count())
print(unique_customers_df.loc[(unique_customers_df['sex']=='F')&(unique_customers_df['transaction_month']=='May')&(unique_customers_df['Orange Beans']==True),'name'].count())
print(unique_customers_df.loc[(unique_customers_df['sex']=='F')&(unique_customers_df['transaction_month']=='June')&(unique_customers_df['Orange Beans']==True),'name'].count())
print("")
print("Unique CCOB F Total")
print(unique_customers_df.loc[(unique_customers_df['sex']=='F')&(unique_customers_df['Orange Beans']==True),'name'].count())
print("")
print("Unique CCGW F")
print("")
print(unique_customers_df.loc[(unique_customers_df['sex']=='F')&(unique_customers_df['transaction_month']=='January')&(unique_customers_df['Gummy Worms']==True),'name'].count())
print(unique_customers_df.loc[(unique_customers_df['sex']=='F')&(unique_customers_df['transaction_month']=='February')&(unique_customers_df['Gummy Worms']==True),'name'].count())
print(unique_customers_df.loc[(unique_customers_df['sex']=='F')&(unique_customers_df['transaction_month']=='March')&(unique_customers_df['Gummy Worms']==True),'name'].count())
print(unique_customers_df.loc[(unique_customers_df['sex']=='F')&(unique_customers_df['transaction_month']=='April')&(unique_customers_df['Gummy Worms']==True),'name'].count())
print(unique_customers_df.loc[(unique_customers_df['sex']=='F')&(unique_customers_df['transaction_month']=='May')&(unique_customers_df['Gummy Worms']==True),'name'].count())
print(unique_customers_df.loc[(unique_customers_df['sex']=='F')&(unique_customers_df['transaction_month']=='June')&(unique_customers_df['Gummy Worms']==True),'name'].count())
print("")
print("Unique CCGW F Total")
print(unique_customers_df.loc[(unique_customers_df['sex']=='F')&(unique_customers_df['Gummy Worms']==True),'name'].count())

#Number of Unique Male Customers per Item per Month
print("Unique EEBC M")
print("")
print(unique_customers_df.loc[(unique_customers_df['sex']=='M')&(unique_customers_df['transaction_month']=='January')&(unique_customers_df['Beef Chicharon']==True),'name'].count())
print(unique_customers_df.loc[(unique_customers_df['sex']=='M')&(unique_customers_df['transaction_month']=='February')&(unique_customers_df['Beef Chicharon']==True),'name'].count())
print(unique_customers_df.loc[(unique_customers_df['sex']=='M')&(unique_customers_df['transaction_month']=='March')&(unique_customers_df['Beef Chicharon']==True),'name'].count())
print(unique_customers_df.loc[(unique_customers_df['sex']=='M')&(unique_customers_df['transaction_month']=='April')&(unique_customers_df['Beef Chicharon']==True),'name'].count())
print(unique_customers_df.loc[(unique_customers_df['sex']=='M')&(unique_customers_df['transaction_month']=='May')&(unique_customers_df['Beef Chicharon']==True),'name'].count())
print(unique_customers_df.loc[(unique_customers_df['sex']=='M')&(unique_customers_df['transaction_month']=='June')&(unique_customers_df['Beef Chicharon']==True),'name'].count())
print("")
print("Unique EEBC M Total")
print(unique_customers_df.loc[(unique_customers_df['sex']=='M')&(unique_customers_df['Beef Chicharon']==True),'name'].count())
print("")
print("Unique EEKS M")
print("")
print(unique_customers_df.loc[(unique_customers_df['sex']=='M')&(unique_customers_df['transaction_month']=='January')&(unique_customers_df['Kimchi and Seaweed']==True),'name'].count())
print(unique_customers_df.loc[(unique_customers_df['sex']=='M')&(unique_customers_df['transaction_month']=='February')&(unique_customers_df['Kimchi and Seaweed']==True),'name'].count())
print(unique_customers_df.loc[(unique_customers_df['sex']=='M')&(unique_customers_df['transaction_month']=='March')&(unique_customers_df['Kimchi and Seaweed']==True),'name'].count())
print(unique_customers_df.loc[(unique_customers_df['sex']=='M')&(unique_customers_df['transaction_month']=='April')&(unique_customers_df['Kimchi and Seaweed']==True),'name'].count())
print(unique_customers_df.loc[(unique_customers_df['sex']=='M')&(unique_customers_df['transaction_month']=='May')&(unique_customers_df['Kimchi and Seaweed']==True),'name'].count())
print(unique_customers_df.loc[(unique_customers_df['sex']=='M')&(unique_customers_df['transaction_month']=='June')&(unique_customers_df['Kimchi and Seaweed']==True),'name'].count())
print("")
print("Unique EEKS M Total")
print(unique_customers_df.loc[(unique_customers_df['sex']=='M')&(unique_customers_df['Kimchi and Seaweed']==True),'name'].count())
print("")
print("Unique HKNM M")
print("")
print(unique_customers_df.loc[(unique_customers_df['sex']=='M')&(unique_customers_df['transaction_month']=='January')&(unique_customers_df['Nutrional Milk']==True),'name'].count())
print(unique_customers_df.loc[(unique_customers_df['sex']=='M')&(unique_customers_df['transaction_month']=='February')&(unique_customers_df['Nutrional Milk']==True),'name'].count())
print(unique_customers_df.loc[(unique_customers_df['sex']=='M')&(unique_customers_df['transaction_month']=='March')&(unique_customers_df['Nutrional Milk']==True),'name'].count())
print(unique_customers_df.loc[(unique_customers_df['sex']=='M')&(unique_customers_df['transaction_month']=='April')&(unique_customers_df['Nutrional Milk']==True),'name'].count())
print(unique_customers_df.loc[(unique_customers_df['sex']=='M')&(unique_customers_df['transaction_month']=='May')&(unique_customers_df['Nutrional Milk']==True),'name'].count())
print(unique_customers_df.loc[(unique_customers_df['sex']=='M')&(unique_customers_df['transaction_month']=='June')&(unique_customers_df['Nutrional Milk']==True),'name'].count())
print("")
print("Unique HKNM M Total")
print(unique_customers_df.loc[(unique_customers_df['sex']=='M')&(unique_customers_df['Nutrional Milk']==True),'name'].count())
print("")
print("Unique HKGV M")
print("")
print(unique_customers_df.loc[(unique_customers_df['sex']=='M')&(unique_customers_df['transaction_month']=='January')&(unique_customers_df['Gummy Vitamins']==True),'name'].count())
print(unique_customers_df.loc[(unique_customers_df['sex']=='M')&(unique_customers_df['transaction_month']=='February')&(unique_customers_df['Gummy Vitamins']==True),'name'].count())
print(unique_customers_df.loc[(unique_customers_df['sex']=='M')&(unique_customers_df['transaction_month']=='March')&(unique_customers_df['Gummy Vitamins']==True),'name'].count())
print(unique_customers_df.loc[(unique_customers_df['sex']=='M')&(unique_customers_df['transaction_month']=='April')&(unique_customers_df['Gummy Vitamins']==True),'name'].count())
print(unique_customers_df.loc[(unique_customers_df['sex']=='M')&(unique_customers_df['transaction_month']=='May')&(unique_customers_df['Gummy Vitamins']==True),'name'].count())
print(unique_customers_df.loc[(unique_customers_df['sex']=='M')&(unique_customers_df['transaction_month']=='June')&(unique_customers_df['Gummy Vitamins']==True),'name'].count())
print("")
print("Unique HKGV M Total")
print(unique_customers_df.loc[(unique_customers_df['sex']=='M')&(unique_customers_df['Gummy Vitamins']==True),'name'].count())
print("")
print("Unique HKYV M")
print("")
print(unique_customers_df.loc[(unique_customers_df['sex']=='M')&(unique_customers_df['transaction_month']=='January')&(unique_customers_df['Yummy Vegetables']==True),'name'].count())
print(unique_customers_df.loc[(unique_customers_df['sex']=='M')&(unique_customers_df['transaction_month']=='February')&(unique_customers_df['Yummy Vegetables']==True),'name'].count())
print(unique_customers_df.loc[(unique_customers_df['sex']=='M')&(unique_customers_df['transaction_month']=='March')&(unique_customers_df['Yummy Vegetables']==True),'name'].count())
print(unique_customers_df.loc[(unique_customers_df['sex']=='M')&(unique_customers_df['transaction_month']=='April')&(unique_customers_df['Yummy Vegetables']==True),'name'].count())
print(unique_customers_df.loc[(unique_customers_df['sex']=='M')&(unique_customers_df['transaction_month']=='May')&(unique_customers_df['Yummy Vegetables']==True),'name'].count())
print(unique_customers_df.loc[(unique_customers_df['sex']=='M')&(unique_customers_df['transaction_month']=='June')&(unique_customers_df['Yummy Vegetables']==True),'name'].count())
print("")
print("Unique HKYV M Total")
print(unique_customers_df.loc[(unique_customers_df['sex']=='M')&(unique_customers_df['Yummy Vegetables']==True),'name'].count())
print("")
print("Unique CCOB M")
print("")
print(unique_customers_df.loc[(unique_customers_df['sex']=='M')&(unique_customers_df['transaction_month']=='January')&(unique_customers_df['Orange Beans']==True),'name'].count())
print(unique_customers_df.loc[(unique_customers_df['sex']=='M')&(unique_customers_df['transaction_month']=='February')&(unique_customers_df['Orange Beans']==True),'name'].count())
print(unique_customers_df.loc[(unique_customers_df['sex']=='M')&(unique_customers_df['transaction_month']=='March')&(unique_customers_df['Orange Beans']==True),'name'].count())
print(unique_customers_df.loc[(unique_customers_df['sex']=='M')&(unique_customers_df['transaction_month']=='April')&(unique_customers_df['Orange Beans']==True),'name'].count())
print(unique_customers_df.loc[(unique_customers_df['sex']=='M')&(unique_customers_df['transaction_month']=='May')&(unique_customers_df['Orange Beans']==True),'name'].count())
print(unique_customers_df.loc[(unique_customers_df['sex']=='M')&(unique_customers_df['transaction_month']=='June')&(unique_customers_df['Orange Beans']==True),'name'].count())
print("")
print("Unique CCOB M Total")
print(unique_customers_df.loc[(unique_customers_df['sex']=='M')&(unique_customers_df['Orange Beans']==True),'name'].count())
print("")
print("Unique CCGW M")
print("")
print(unique_customers_df.loc[(unique_customers_df['sex']=='M')&(unique_customers_df['transaction_month']=='January')&(unique_customers_df['Gummy Worms']==True),'name'].count())
print(unique_customers_df.loc[(unique_customers_df['sex']=='M')&(unique_customers_df['transaction_month']=='February')&(unique_customers_df['Gummy Worms']==True),'name'].count())
print(unique_customers_df.loc[(unique_customers_df['sex']=='M')&(unique_customers_df['transaction_month']=='March')&(unique_customers_df['Gummy Worms']==True),'name'].count())
print(unique_customers_df.loc[(unique_customers_df['sex']=='M')&(unique_customers_df['transaction_month']=='April')&(unique_customers_df['Gummy Worms']==True),'name'].count())
print(unique_customers_df.loc[(unique_customers_df['sex']=='M')&(unique_customers_df['transaction_month']=='May')&(unique_customers_df['Gummy Worms']==True),'name'].count())
print(unique_customers_df.loc[(unique_customers_df['sex']=='M')&(unique_customers_df['transaction_month']=='June')&(unique_customers_df['Gummy Worms']==True),'name'].count())
print("")
print("Unique CCGW F Total")
print(unique_customers_df.loc[(unique_customers_df['sex']=='M')&(unique_customers_df['Gummy Worms']==True),'name'].count())

#Number of Unique Female/Male customers per month
UF_items_jan = [495,459,457,461,494,487,448]
UF_items_feb = [104,100,108,111,101,111,117]
UF_items_mar = [30,22,19,28,23,22,19]
UF_items_apr = [6,10,11,3,5,9,6]
UF_items_may = [3,0,1,0,1,1,4]
UF_items_jun = [0,0,0,0,0,0,2]
UF_items_tot = [638,591,596,603,624,630,596]

UM_items_jan = [481,447,467,456,487,474,475]
UM_items_feb = [113,99,96,110,91,101,97]
UM_items_mar = [17,18,11,31,19,27,36]
UM_items_apr = [5,5,8,3,9,9,7]
UM_items_may = [4,2,1,1,1,0,1]
UM_items_jun = [0,0,0,0,0,0,0]
UM_items_tot = [620,571,583,601,607,611,616]

UF_items_month_df = pd.DataFrame([UF_items_jan,UF_items_feb,UF_items_mar,UF_items_apr,UF_items_may,UF_items_jun],columns=['EEBC_F','EEKS_F','HKNM_F','HKGV_F','HKYV_F','CCOB_F','CCGW_F'],index=monthslist)  
UF_items_montht_df = pd.DataFrame([UF_items_jan,UF_items_feb,UF_items_mar,UF_items_apr,UF_items_may,UF_items_jun,UF_items_tot],columns=['EEBC_F','EEKS_F','HKNM_F','HKGV_F','HKYV_F','CCOB_F','CCGW_F'],index=monthslistotal)
UM_items_month_df = pd.DataFrame([UM_items_jan,UM_items_feb,UM_items_mar,UM_items_apr,UM_items_may,UM_items_jun],columns=['EEBC_M','EEKS_M','HKNM_M','HKGV_M','HKYV_M','CCOB_M','CCGW_M'],index=monthslist)
UM_items_montht_df = pd.DataFrame([UM_items_jan,UM_items_feb,UM_items_mar,UM_items_apr,UM_items_may,UM_items_jun,UM_items_tot],columns=['EEBC_M','EEKS_M','HKNM_M','HKGV_M','HKYV_M','CCOB_M','CCGW_M'],index=monthslistotal)

#Table of UF_items_montht_df
fig, ax = plt.subplots()
fig.patch.set_visible(False)
ax.axis('off')
ax.axis('tight')
ax.set_title('Total No. of Unique Female Customers per item')
plt.subplots_adjust(bottom=0.53)
table = ax.table(cellText=UF_items_montht_df.values, colLabels=UF_items_montht_df.columns,rowLabels=UF_items_montht_df.index,loc='center')
fig.tight_layout()
plt.show()
fig.savefig('UF_items_montht_df_table', dpi=200)

#Table of UM_items_montht_df
fig, ax = plt.subplots()
fig.patch.set_visible(False)
ax.axis('off')
ax.axis('tight')
ax.set_title('Total No. of Unique Male and Male Customers per item')
plt.subplots_adjust(bottom=0.53)
table = ax.table(cellText=UM_items_montht_df.values, colLabels=UM_items_montht_df.columns,rowLabels=UM_items_montht_df.index,loc='center')
fig.tight_layout()
plt.show()
fig.savefig('UM_items_montht_df_table', dpi=200)

UF_mitems_graph = UF_items_month_df.plot(kind='bar',figsize=(22,8)).legend(loc='best')
plt.ylabel('Months')
plt.xlabel('Items (F)')
plt.title('Number of Unique Female customers per item per month')
UF_mitems_graph.figure.savefig('UF_umitems_bar.png')

UM_mitems_graph = UM_items_month_df.plot(kind='bar',figsize=(22,8)).legend(loc='best')
plt.ylabel('Months')
plt.xlabel('Items (M)')
plt.title('Number of Unique Male customers per item per month')
UM_mitems_graph.figure.savefig('UM_umitems_bar.png')

#Number of Male and Female Customers per Item
print("Total Unique F per Item")
print(unique_customers_df.loc[(unique_customers_df['sex']=='F')&(unique_customers_df['Beef Chicharon']==True),'name'].count())
print(unique_customers_df.loc[(unique_customers_df['sex']=='F')&(unique_customers_df['Kimchi and Seaweed']==True),'name'].count())
print(unique_customers_df.loc[(unique_customers_df['sex']=='F')&(unique_customers_df['Nutrional Milk']==True),'name'].count())
print(unique_customers_df.loc[(unique_customers_df['sex']=='F')&(unique_customers_df['Gummy Vitamins']==True),'name'].count())
print(unique_customers_df.loc[(unique_customers_df['sex']=='F')&(unique_customers_df['Yummy Vegetables']==True),'name'].count())
print(unique_customers_df.loc[(unique_customers_df['sex']=='F')&(unique_customers_df['Orange Beans']==True),'name'].count())
print(unique_customers_df.loc[(unique_customers_df['sex']=='F')&(unique_customers_df['Gummy Worms']==True),'name'].count())
print("")
print("Total Unique M per Item")
print(unique_customers_df.loc[(unique_customers_df['sex']=='M')&(unique_customers_df['Beef Chicharon']==True),'name'].count())
print(unique_customers_df.loc[(unique_customers_df['sex']=='M')&(unique_customers_df['Kimchi and Seaweed']==True),'name'].count())
print(unique_customers_df.loc[(unique_customers_df['sex']=='M')&(unique_customers_df['Nutrional Milk']==True),'name'].count())
print(unique_customers_df.loc[(unique_customers_df['sex']=='M')&(unique_customers_df['Gummy Vitamins']==True),'name'].count())
print(unique_customers_df.loc[(unique_customers_df['sex']=='M')&(unique_customers_df['Yummy Vegetables']==True),'name'].count())
print(unique_customers_df.loc[(unique_customers_df['sex']=='M')&(unique_customers_df['Orange Beans']==True),'name'].count())
print(unique_customers_df.loc[(unique_customers_df['sex']=='M')&(unique_customers_df['Gummy Worms']==True),'name'].count())

#Number of Unique Male and Female Customers per Item
UF_per_item = [638,591,596,603,624,630,596]
UM_per_item = [620,571,583,601,607,611,616]

#Total Female/Male customers per item
fig = plt.figure(figsize=(12,8),dpi=200)
plt.plot(itemslist,UF_per_item, label = 'UF customers',marker = 'o')
plt.plot(itemslist,UM_per_item, label = 'UM customers', marker='o')
plt.legend(loc=1, prop={'size':8})

plt.title('Total Unique Female/Male Customers per item')
plt.xlabel('Items')
plt.ylabel('No. of Customers')
plt.show()
fig.savefig('total_UFM_item_line',dpi=200)
