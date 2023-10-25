from winreg import QueryInfoKey
import pandas as pd
import re

def dfselect(df,query):
    df1 = df
    lst = df.columns
    lst1 = re.findall('\W', query)
    if len(lst1) == 0:
        return "Error"
    if len(lst1) == 1:
        t = lst1[0]
    if len(lst1) == 2:
        t = lst1[0] + lst1[1]
    print(t) 
    split_query = query.split(t)
    query_var = split_query[0]
    query_val = split_query[1]
    flag = 0
    for cols in lst:
        if query_var == cols:
            flag = 1
            break
        else:
            flag = 0
            continue
    if flag == 0:
        return "Error "
    if len(lst1) == 1:
        if lst1[0] == '=':
            df1 = df1[df1[query_var] == query_val]
        elif lst1[0] == '<':
            df1 = df1[df1[query_var] < query_val]
        elif lst1[0] == '>':
            df1 = df1[df1[query_var] > query_val]

    if len(lst1) == 2:
        if lst1[0] == '!' and lst1[1] == '=':
            df1 = df1[df1[query_var] != query_val]
        elif lst1[0] == '<' and lst1[1] == '=':
            df1 = df1[df1[query_var] <= query_val]
        elif lst1[0] == '>' and lst1[1] == '=':
            df1 = df1[df1[query_var] >= query_val]
    return df1

df14 = pd.read_csv("C:/Users/jeyar/OneDrive/Documents/Arulwork/TestFiles/gapminder.tsv", sep='\t')
print(dfselect(df14, "country<=India"))