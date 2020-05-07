import re
import os
import string
import pandas as pd
import numpy as np
import sqlite3 as sq
import json
from datetime import *
import requests
from bs4 import BeautifulSoup
import bs4


list=os.listdir("csv_files")
list.sort()
list.reverse()


l=[]

for i in range(0,len(list)):
    
    temp_df=pd.read_csv( 'csv_files/'+list[i] )       
    l.append(temp_df)
#     print(list[i],temp_df.shape)
    
#    df.append(temp_df)
# print(len(l))

df=pd.concat(l)

df.to_csv('final_csv/final.csv') 

df.iloc[:,41].fillna(0,inplace=True)
df.iloc[:,42].fillna(0,inplace=True)
df.iloc[:,43].fillna(0,inplace=True)


df_T=df.T
# df.iloc[:,212]
d1= date(2000, 5, 1)
df.iloc[:,212] = df.iloc[:,212].fillna(value = str(d1))
df.iloc[:,212]


d = date(2018, 5, 1)


data=df.to_numpy()

scores_array=[]

for i in range(df.shape[0]):
    
    dict={}
    dict[43]=0
    dict[44]=0
    dict[52]=0
    dict["EBRW"]=0
    dict["MATH"]=0
    
    j=0
    col=212
    while(j<6):
        var=data[:,212][i]
        date_object = datetime.strptime(var, '%Y-%m-%d').date()
        if(date_object>d):
            
            col+=3
                
            if(dict.get(data[i][col])!=None):
                dict[data[i][col]]=max(data[i][col+1],dict[data[i][col]])

            col+=5
            if(dict.get(data[i][col])!=None):
                dict[data[i][col]]=max(data[i][col+1],dict[data[i][col]])    
        
            col+=5
            if(dict.get(data[i][col])!=None):
                dict[data[i][col]]=max(data[i][col+1],dict[data[i][col]])
            
            col+=5
        else:
            col+=18
        j+=1
        
    dict["EBRW"]=max(data[i][42],data[i][71],data[i][100],data[i][129],data[i][158],data[i][187],dict["EBRW"])
    dict["MATH"]=max(data[i][43],data[i][72],data[i][101],data[i][130],data[i][159],data[i][188],dict["MATH"])        
    
    scores_array.append(dict)
    
# for i in range(len(scores_array)):
#     print(i,scores_array[i])


list_43=[]
list_44=[]
list_52=[]
list_EBRW=[]
list_MATH=[]

for itr in scores_array:
    
    list_43.append(itr[43])
    list_44.append(itr[44])
    list_52.append(itr[52])
    list_EBRW.append(itr["EBRW"])
    list_MATH.append(itr["MATH"])

list_43=np.array(list_43)
list_44=np.array(list_44)
list_52=np.array(list_52)
list_EBRW=np.array(list_EBRW)
list_MATH=np.array(list_MATH)


final_list=[]
final_dict={}

# print(data[:,21])
for i in range(data.shape[0]):
    flag=1
#     print(data[i])
    if(data[i,21] in final_dict):
        flag=0
        tem=final_dict[data[i,21]]
#         print(final_dict[data[i,21]])
#         print('.............................................................')
        

        
        
    details={"Last_Name":data[i,1],
                "First_Name":data[i,2],
                "Birth_date":data[i,19],
                "SAT_score":data[i,41],
                "EBRW_score":list_EBRW[i],
                "Math_score":list_MATH[i],
                "Chemistry":list_43[i],
                "Physics":list_44[i],   
                "Math_2":list_52[i]
                
                }
    
    temp_dict={}
    temp_dict[data[i,21]]=details
    final_dict[data[i,21]]=details
    if(flag==0): 
        final_dict[data[i,21]]["SAT_score"]=max(final_dict[data[i,21]]["SAT_score"],tem["SAT_score"])
        final_dict[data[i,21]]["EBRW_score"]=max(final_dict[data[i,21]]["EBRW_score"],tem["EBRW_score"])
        final_dict[data[i,21]]["Math_score"]=max(final_dict[data[i,21]]["Math_score"],tem["Math_score"])
        final_dict[data[i,21]]["Chemistry"]=max(final_dict[data[i,21]]["Chemistry"],tem["Chemistry"])
        final_dict[data[i,21]]["Physics"]=max(final_dict[data[i,21]]["Physics"],tem["Physics"])
        final_dict[data[i,21]]["Math_2"]=max(final_dict[data[i,21]]["Math_2"],tem["Math_2"])
        
        temp_dict[data[i,21]]=final_dict[data[i,21]]
#         print(temp_dict[data[i,21]])
#         print('.....................................................')
#         print(final_dict[data[i,21]])
    
    
for i in final_dict:
    final_list.append({i:final_dict[i]})

print(len(final_list))





ini_string = json.dumps(final_list,indent = 4)

with open("sample.html", "w") as outfile: 
	outfile.write("<pre>\n")
	outfile.write(ini_string)
	outfile.write("\n</pre>") 
    
    

bs4.BeautifulSoup


Valid_Ids=[] 
URL = "http://ims.iiit.ac.in/dasa_score_validations.php?requesttype=getdata&acadyear=2020-21&semester=monsoon"
r = requests.get(URL)
soup=bs4.BeautifulSoup(r.text,'html5lib')

page = soup.getText()
#print(page,type(page))
page=page.split(')')
print(page)
json_object = json.loads(page[1])

c=0
for items in json_object:
        if(json_object[items]["valid_marks"]==True):
            Valid_Ids.append(items)
#             print(items)
# print(len(Valid_Ids))

valid_id_details=[]

for i in Valid_Ids:
    cb_id=int(i)
#     print(final_dict[cb_id])
    temp=[]
    valid_id_details.append([final_dict[cb_id]['EBRW_score']+final_dict[cb_id]['Math_score'],
                             final_dict[cb_id]['EBRW_score'],
                             final_dict[cb_id]['Math_score'],
                             cb_id])

valid_id_details.sort(reverse=True)

print("valid id:- ",len(valid_id_details))

final_dict={}
i=1
for lst in valid_id_details:
	details={"SAT_TOTAL":lst[0],
			 "EBRW":lst[1],
			 "MATH":lst[2],
			 "rank":i
			}
	i+=1
	final_dict[lst[3]]=details
print(final_dict)

ini_string = json.dumps(final_dict,indent = 4)

with open("rank.html", "w") as outfile:
	outfile.write("<pre>\n")
	outfile.write(ini_string)
	outfile.write("\n</pre>")
