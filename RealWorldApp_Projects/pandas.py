import pandas as pd

# # Create a dataframe manually with list of numbers and its columns and idex names:
# df = pd.DataFrame([[2,3,4],[10,20,30]],columns=["price","age","value"],index=["First","Second"])
# print df                # df1 is of the type Dataframe
# print df.mean()         # Calculates the mean of each column and its of type Series
# print df.mean().mean()  # Calculates the mean of means calculated above
# print type(df.price)    # price colunm is of type Series hence DataFrame is made of Series!
# print df.price.max()    # returns the maximum value in price


## Create a dataframe manually with dictionary with name and surname as keys:
# df2 = pd.DataFrame([{"name":"John","surname":"Caralo"},{"name":"Liya","surname":"Rosa"}])
# print df2

## *******************************************************************************************

# # Loading excel files while specifing the sheetname=0 meaning 1st sheet
# df3 = pd.read_excel("C:\Users\DIPESH\supermarkets.xlsx", sheetname=0)
# print df3
#
# # Loading file directly from a url
# df4 = pd.read_csv("http://pythonhow.com/supermarkets.csv")
# print df4

# Loading csv file
df1 = pd.read_csv(r"C:\Users\DIPESH\supermarkets.csv")
#print df1
## Header for the file is set to true by default. if you want to change it then
#df1 =pd.read_csv("C:\Users\DIPESH\supermarkets.csv", header = None)

df1 = df1.set_index('Address')  # Sets the index as address and saves it in df1
print(df1)


##*******************************************************************************************************

## Data slicing from dataframe using loc[] method using labels where upperbound label in inclusive**
#print df1.loc["332 Hill St":"1056 Sanchez St", "City":"Country"]
#print df1.loc["332 Hill St",:"Country"]                          # Gives only 1 row's particular column details

## Dataslicing using iloc[] using position index where upperbound index is exclusive like in list slicing**
#print df1.iloc[2:5,1:4]

## When you want to access columns based on name and not their position, use ix[]
## ix[] can be used for combinations also, like name n postions
## But recommended over loc and iloc. Use only when in specific condition.
#print df1.ix[3:5,"Name"]
#print df1.ix[3,4]

##*******************************************************************************************************
## DELETE
############
##Deleting rows -- .drop() *** use 0 to specify that you have to delete rows
#print (df1.drop("332 Hill St",0))
#print (df1.drop(df1.index[1:3],0))        # will delete 2nd n 3rd row

## Deleting columns -- .drop() ** using 1 to specify that you have to delete columns
#print df1.drop("Country",1)
#print df1.drop(df1.columns[0:3],1)

#print(df1.index)       # Gives a list of index(rows)
#print(df1.columns)     # Gives a list of columns
##*******************************************************************************************************

## ADD
##############
## .shape() used to add rows or columns.....this is an inplace command meaning that after using this command, changes made
## are saved in the dataframe.
#print(df1.shape)                         # Gives the shape of our dataframe in form of tuple(5,6)
                                          # where 5 is no. of rows and 6 is no. of columns
#print df1.shape[0]                            # Gives the no. of rows
#print df1.shape[1]                            # Gives the no. of columns

## TO ADD NEW COLUMN:
## Adds a new column "Continent" and fills it up with "North America" multiplied with the no. of rows to fill up
#df1["Continent"] = df1.shape[0]* ["North America"]
#print df1

## OR

# # To modify and add new column(here no need to use .shape[] since we using an existing column.)
# df1["Continent"] = df1["Country"] + "," + "North America"
# print df1

## TO ADD NEW ROW:
## First need to transpose your data ie to transform rows to columns and columns to rows with .T method
# df1_t = df1.T
# print df1_t
#
# df1_t["My address"]= ["my ID", "My CIty", "My STate", "My COuntry","My Name", "My Employee"]   # adds a new column
# print df1_t                                                                             #can update also in same way
# df1 = df1_t.T                 # convert it back to its original form
# print df1

##**********************************************************************************************************
##**********************************************************************************************************

#print df1.set_index("ID")
#df2 = pd.read_csv("http://pythonhow.com/supermarkets.csv")
#print df2

# df1=df1.drop("City",1)
# print(df1)
# print("***************************************************")
# df2 = df1.T
# print(df2)
# df2["myaddress"] = [7,"mystate","USA","myname",34]
# print("******************************************************************")
# print(df2)
# df2 = df2.T
# print("******************************************************************")
# print(df2)