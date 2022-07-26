#Advantages of Pandas over excel:
    #more flexible 
    #can handle larger data sets

#LOADING DATA TO PANDAS
import pandas as pd
df = pd.read_csv('pokemon_data.csv')
# print(df.head(3)) # .head(#number of rows) function prints top lines, .tail(#) prints bottom lines

#df_tab_separated= pd.read_csv('pokemon_data.txt', delimiter='\t') #need to introduce tab ('\t) delimiter to change format of txt file 
#print(df_tab_separated.head(3))

#READING HEADERS IN PANDAS

##Read headers
# print(df.columns) 

##Read each column 
# print(df[['Name', 'Type 1', 'Attack']]) #double brackets if printing multiple columns
# print(df['Name']) #single brackets for one column 
#or: print(df.Name)

##Read each row
# print(df.head(4))

#.iloc() function
#print(df.iloc[1])#to print specific row
# print(df.iloc[0:4])#to print specific selection rows

#iterrows() function
# for index, row in df.iterrows():
    # print(index, row['Name']) #to print specific value in each row

# .loc() function
# find data that matches specific values
#print(df.loc[df['Type 1'] == 'Fire'])

#Read a specific location (R:C)
# print(df.iloc[2,1])

#SORTING / DESCRIBING DATA

#print(df.sort_values('Name')) #input as argument column you want to sort, automatically is ascending order
#print(df.sort_values('Name', ascending=False)) #to change to descending order
#print(df.sort_values(['Type 1', 'HP'], ascending = [1,0])) #can combine multiple columns, ascending True or False for both/either) 

#MAKING CHANGES TO THE DATA
#add column that is total of stat columns/rows
#df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed']  #creates new column called Total

#add Total column in more succinct way 
#df['Total'] = df.iloc [:, 4:10].sum(axis = 1) #':' means I want all the rows, from 4th to 9th row (10 - 1, 10th row excluded)
#axis = 1 means that you want to add values horizontally , axis = 0 is adding vertically

#.drop () to drop a column 
#df = df.drop(columns = ['Total'])

#how to move column to different location in dataframe
#to make columns into list to after change their position, use list() function
#cols = list(df.columns.values)
#df = df [cols[0:4 ] + [cols [-1]] +cols[ 4:12]] #places Total column on left 
#print(df.head(5))

# if listing out all columns literally : 
# df = df[['Total ', 'HP', 'Defense']] #"df =" --> to make sure new version saved

#SAVING OUR DATA (.csv, .txt, etc.)

#built in function .to_csv
#df.to_csv('modified.csv', index= False) #index = False -->to remove indexes off data

#built in function to save as excel
#df.to_excel('modified.xlsx', index= False) 

#built in function to save as tab separated file
#df.to_csv('modified.txt', index= False, sep = '\t') 

#FILTERING DATA
new_df = df.loc[(df['Type 1'] == 'Grass' )  & (df['Type 2'] == 'Poison') & (df['HP'] > 70) ]   #in зandas, '&' instead of 'and'
#print(new_df)

new_df.reset_index(drop=True, inplace= True) #to reset index
#print(new_df)

#print(df.loc[(df['Type 1'] == 'Grass' )  | (df['Type 2'] == 'Poison')]) # '|' --> 'or'

#CONDITIONAL CHANGING
#other types of conditions: 

#not allow name to contain 'Mega':
#mega = df.loc[df['Name'].str.contains('Mega')] #columns that inlcude string 'mega'
#no_mega = df.loc[~df['Name'].str.contains('Mega')]# ~ --> excludes columns that inlcude string 'mega'
#print(mega)
#print(no_mega)

#REGEX filtering
#see if Type 1 is Grass or Fire
import re #regex library
fire_grass= df.loc[df['Type 1'].str.contains('Fire|Grass', regex = True)]
print(fire_grass)

#can use  flag to ignore if desired string value is capitalised or not
fire_grass= df.loc[df['Type 1'].str.contains('fire|grass',flags=re.I, regex = True)] 

#want to get all pokemon names that start with 'pi'
#to get name category and just 'pi'
fire_grass= df.loc[df['Name'].str.contains('^pi[a-z]* ',flags=re.I, regex = True)] 

#^pi[a-z]* 
# ^ --> means I need it to start with pi 
# [a-z]*--> I need it to START with pi, but the next set of letters can be anything else in alphabet

#CONDITIONAL CHANGING
#want to change name of Type 1 value Fire to Flamey
flamer = df.loc[df['Type 1']== 'Fire', 'Type 1'] = 'Flamer' 


df.loc[df['Type 1']== 'Fire', 'Type 1'] = 'Flamer' 
flamer = df.loc[df['Type 1']== 'Fire', 'Type 1']

#decide that all flamer pokemon are legendary 
fl_leg = df.loc[df['Type 1']== 'Fire', 'Legendary'] = True 

print(fl_leg)

#change multiple parameters at the same time

#AGGREGATE STATISTICS (Groupby) .mean(), .sum() , .count()
df.groupby(['Type 1']).mean() #aggregate each Type 1 value and work out total mean for each column
df.groupby(['Type 1']).mean().sort_values('Defense', ascending = False) #sort_values - sorts by spec. column

df.groupby(['Type 1']).sum()

df.groupby(['Type 1']).count()
