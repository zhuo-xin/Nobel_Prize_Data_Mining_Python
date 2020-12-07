
import json
import pandas as pd
import numpy as np
file_object = open("nobelprizes.json",'r')
nobelprizeDict = json.load(file_object)
year=input("please enter year:")
category=input("please enter category:")
year=int(year)

def get_laureates_and_motivation(nobelprizeDict, year, category):
    file_object = open("nobelprizes.json",'r')
    nobelprizeDict = json.load(file_object)
    file_object.close()
    df = pd.DataFrame(nobelprizeDict)
    df=df.dropna(subset=['laureates'])
    df2=pd.DataFrame(df['laureates'])    
    list_laureates0=df2["laureates"].tolist()               
    list_laureates= [x for x in list_laureates0 if type(x) is list]   
    w=[]
    for n in range(len(list_laureates)):
        w=w+list_laureates[n]                 
    df_laureates=pd.DataFrame(w)                                      
    df_laureates['firstname']=df_laureates['firstname'].astype(str)
    df_laureates['surname']=df_laureates['surname'].astype(str)
    df_laureates['share']=df_laureates['share'].astype(int)
    df_laureates['laureate']=df_laureates['firstname'].str.cat(df_laureates['surname'],sep=' ')
    df_laureates=df_laureates.drop(['firstname','surname'], axis=1)
    df_laureates=df_laureates[['id','laureate','motivation','share']]                                              
    list_category=df['category'].tolist() 
    newlist_category=[]         
    list_year=df['year'].tolist() 
    newlist_year=[]         
    list_overallMotivation=df['overallMotivation'].tolist() 
    newlist_overallMotivation=[]         
    for i in range(597):
        newlist_category=newlist_category+[list_category[i]]*len(list_laureates0[i])
        newlist_year=newlist_year+[list_year[i]]*len(list_laureates0[i])
        newlist_overallMotivation=newlist_overallMotivation+[list_overallMotivation[i]]*len(list_laureates0[i])
    newlist_category = pd.DataFrame(newlist_category,columns=['category'])
    newlist_year = pd.DataFrame(newlist_year,columns=['year'])
    newlist_overallMotivation = pd.DataFrame(newlist_overallMotivation,columns=['overallMotivation'])
    df_new1=pd.concat([newlist_category,newlist_year,newlist_overallMotivation,df_laureates],axis=1)
    df_new1=df_new1.drop(['share'], axis=1)
    df_new1 = df_new1[['category', 'year','id','laureate','motivation','overallMotivation']]
    df_new1=df_new1.rename(columns={'overallMotivation':'overall_motivation'})
    df_new1['category']=df_new1['category'].astype(str)
    df_new1['year']=df_new1['year'].astype(int)
    df_new1['id']=df_new1['id'].astype(int)
    df_new1['laureate']=df_new1['laureate'].astype(str)
    df=df_new1
    df=df_new1[(df['year']==year)&(df['category']==category)]
    return df


import matplotlib.pyplot as plt
from pylab import *
import pandas as pd
import json
import numpy as np
file_object = open("nobelprizes.json",'r')
nobelprizeDict = json.load(file_object)
def plot_freqs(nobelprizeDict):
    file_object = open("nobelprizes.json",'r')
    nobelprizeDict = json.load(file_object)
    file_object.close()
    df = pd.DataFrame(nobelprizeDict)
    df=df.dropna(subset=['laureates'])
    df2=pd.DataFrame(df['laureates'])    
    list_laureates0=df2["laureates"].tolist()               
    list_laureates= [x for x in list_laureates0 if type(x) is list]   
    w=[]
    for n in range(len(list_laureates)):
        w=w+list_laureates[n]                 
    df_laureates=pd.DataFrame(w)                                      
    df_laureates['firstname']=df_laureates['firstname'].astype(str)
    df_laureates['surname']=df_laureates['surname'].astype(str)
    df_laureates['share']=df_laureates['share'].astype(int)
    df_laureates['laureate']=df_laureates['firstname'].str.cat(df_laureates['surname'],sep=' ')
    df_laureates=df_laureates.drop(['firstname','surname'], axis=1)
    df_laureates=df_laureates[['id','laureate','motivation','share']]                                              
    list_category=df['category'].tolist() 
    newlist_category=[]         
    list_year=df['year'].tolist() 
    newlist_year=[]         
    list_overallMotivation=df['overallMotivation'].tolist() 
    newlist_overallMotivation=[]         
    for i in range(597):
        newlist_category=newlist_category+[list_category[i]]*len(list_laureates0[i])
        newlist_year=newlist_year+[list_year[i]]*len(list_laureates0[i])
        newlist_overallMotivation=newlist_overallMotivation+[list_overallMotivation[i]]*len(list_laureates0[i])
    newlist_category = pd.DataFrame(newlist_category,columns=['category'])
    newlist_year = pd.DataFrame(newlist_year,columns=['year'])
    newlist_overallMotivation = pd.DataFrame(newlist_overallMotivation,columns=['overallMotivation'])
    df_new1=pd.concat([newlist_category,newlist_year,newlist_overallMotivation,df_laureates],axis=1)
    df_new1=df_new1.drop(['share'], axis=1)
    df_new1 = df_new1[['category', 'year','id','laureate','motivation','overallMotivation']]
    df_new1=df_new1.rename(columns={'overallMotivation':'overall_motivation'})
    df_new1['category']=df_new1['category'].astype(str)
    df_new1['year']=df_new1['year'].astype(int)
    df_new1['id']=df_new1['id'].astype(int)
    df_new1['laureate']=df_new1['laureate'].astype(str)
    df=df_new1
    df=df.drop(['year','id','laureate','overall_motivation'], axis=1)
    df_given_words= pd.read_csv("whitelist.txt",names=['words'])
    list_given_words=df_given_words['words'].tolist()
    df=df.drop_duplicates(subset=['category','motivation'],keep='first',inplace=False)
    df_chemistry=df[df['category']=='chemistry']              #1.chemistry
    list_chemistry=df_chemistry['motivation'].tolist()
    for i in range(len(list_chemistry)):
        list_chemistry[i]=list_chemistry[i][1:-1]
        list_chemistry[i]
    str_chemistry=' '.join(list_chemistry)
    dict_chemistry_frequency={}
    for i in range(len(list_given_words)):
        dict_chemistry_frequency[list_given_words[i]]=str_chemistry.count(list_given_words[i])
    dict_chemistry_frequency
    s = pd.Series(dict_chemistry_frequency)
    df_chemistry_frequency=pd.DataFrame(s,columns=['frequency'])
    df_chemistry_frequency=df_chemistry_frequency.sort_values(by="frequency",ascending=False)
    df_chemistry_frequency.head()
    y1_chemistry=int(df_chemistry_frequency.iloc[0])
    y10_chemistry=int(df_chemistry_frequency.iloc[9])
    y20_chemistry=int(df_chemistry_frequency.iloc[19])
    y30_chemistry=int(df_chemistry_frequency.iloc[29])
    y40_chemistry=int(df_chemistry_frequency.iloc[39])
    y50_chemistry=int(df_chemistry_frequency.iloc[49])
    list_words_chemistry=df_chemistry_frequency.index.values.tolist()  
    x1_chemistry=list_words_chemistry[0]
    x2_chemistry=list_words_chemistry[9]
    x3_chemistry=list_words_chemistry[19]
    x4_chemistry=list_words_chemistry[29]
    x5_chemistry=list_words_chemistry[39]
    x6_chemistry=list_words_chemistry[49]
    df_economics=df[df['category']=='economics']              #2.economics
    list_economics=df_economics['motivation'].tolist()
    for i in range(len(list_economics)):
        list_economics[i]=list_economics[i][1:-1]
        list_economics[i]
    str_economics=' '.join(list_economics)
    dict_economics_frequency={}
    for i in range(len(list_given_words)):
        dict_economics_frequency[list_given_words[i]]=str_economics.count(list_given_words[i])
    dict_economics_frequency
    s = pd.Series(dict_economics_frequency)
    df_economics_frequency=pd.DataFrame(s,columns=['frequency'])
    df_economics_frequency=df_economics_frequency.sort_values(by="frequency",ascending=False)
    df_economics_frequency.head()
    y1_economics=int(df_economics_frequency.iloc[0])
    y10_economics=int(df_economics_frequency.iloc[9])
    y20_economics=int(df_economics_frequency.iloc[19])
    y30_economics=int(df_economics_frequency.iloc[29])
    y40_economics=int(df_economics_frequency.iloc[39])
    y50_economics=int(df_economics_frequency.iloc[49])                              
    list_words_economics=df_economics_frequency.index.values.tolist()  
    x1_economics=list_words_economics[0]
    x2_economics=list_words_economics[9]
    x3_economics=list_words_economics[19]
    x4_economics=list_words_economics[29]
    x5_economics=list_words_economics[39]
    x6_economics=list_words_economics[49]
    df_literature=df[df['category']=='literature']              #3.literature
    list_literature=df_literature['motivation'].tolist()
    for i in range(len(list_literature)):
        list_literature[i]=list_literature[i][1:-1]
        list_literature[i]
    str_literature=' '.join(list_literature)
    dict_literature_frequency={}
    for i in range(len(list_given_words)):
        dict_literature_frequency[list_given_words[i]]=str_literature.count(list_given_words[i])
    dict_literature_frequency
    s = pd.Series(dict_literature_frequency)
    df_literature_frequency=pd.DataFrame(s,columns=['frequency'])
    df_literature_frequency=df_literature_frequency.sort_values(by="frequency",ascending=False)
    df_literature_frequency.head()
    y1_literature=int(df_literature_frequency.iloc[0])
    y10_literature=int(df_literature_frequency.iloc[9])
    y20_literature=int(df_literature_frequency.iloc[19])
    y30_literature=int(df_literature_frequency.iloc[29])
    y40_literature=int(df_literature_frequency.iloc[39])
    y50_literature=int(df_literature_frequency.iloc[49])
    list_words_literature=df_literature_frequency.index.values.tolist()  
    x1_literature=list_words_literature[0]
    x2_literature=list_words_literature[9]
    x3_literature=list_words_literature[19]
    x4_literature=list_words_literature[29]
    x5_literature=list_words_literature[39]
    x6_literature=list_words_literature[49]
    df_peace=df[df['category']=='peace']              #4.peace
    list_peace=df_peace['motivation'].tolist()
    for i in range(len(list_peace)):
        list_peace[i]=list_peace[i][1:-1]
        list_peace[i]
    str_peace=' '.join(list_peace)
    dict_peace_frequency={}
    for i in range(len(list_given_words)):
        dict_peace_frequency[list_given_words[i]]=str_peace.count(list_given_words[i])
    dict_peace_frequency
    s = pd.Series(dict_peace_frequency)
    df_peace_frequency=pd.DataFrame(s,columns=['frequency'])
    df_peace_frequency=df_peace_frequency.sort_values(by="frequency",ascending=False)
    df_peace_frequency.head()
    y1_peace=int(df_peace_frequency.iloc[0])
    y10_peace=int(df_peace_frequency.iloc[9])
    y20_peace=int(df_peace_frequency.iloc[19])
    y30_peace=int(df_peace_frequency.iloc[29])
    y40_peace=int(df_peace_frequency.iloc[39])
    y50_peace=int(df_peace_frequency.iloc[49])
    list_words_peace=df_peace_frequency.index.values.tolist()  
    x1_peace=list_words_peace[0]
    x2_peace=list_words_peace[9]
    x3_peace=list_words_peace[19]
    x4_peace=list_words_peace[29]
    x5_peace=list_words_peace[39]
    x6_peace=list_words_peace[49]
    df_physics=df[df['category']=='physics']              #5.physics
    list_physics=df_physics['motivation'].tolist()
    for i in range(len(list_physics)):
        list_physics[i]=list_physics[i][1:-1]
        list_physics[i]
    str_physics=' '.join(list_physics)
    dict_physics_frequency={}
    for i in range(len(list_given_words)):
        dict_physics_frequency[list_given_words[i]]=str_physics.count(list_given_words[i])
    dict_physics_frequency
    s = pd.Series(dict_physics_frequency)
    df_physics_frequency=pd.DataFrame(s,columns=['frequency'])
    df_physics_frequency=df_physics_frequency.sort_values(by="frequency",ascending=False)
    df_physics_frequency.head()
    y1_physics=int(df_physics_frequency.iloc[0])
    y10_physics=int(df_physics_frequency.iloc[9])
    y20_physics=int(df_physics_frequency.iloc[19])
    y30_physics=int(df_physics_frequency.iloc[29])
    y40_physics=int(df_physics_frequency.iloc[39])
    y50_physics=int(df_physics_frequency.iloc[49])
    list_words_physics=df_physics_frequency.index.values.tolist()  
    x1_physics=list_words_physics[0]
    x2_physics=list_words_physics[9]
    x3_physics=list_words_physics[19]
    x4_physics=list_words_physics[29]
    x5_physics=list_words_physics[39]
    x6_physics=list_words_physics[49]
    df_medicine=df[df['category']=='medicine']              #6.medicine
    list_medicine=df_medicine['motivation'].tolist()
    for i in range(len(list_medicine)):
        list_medicine[i]=list_medicine[i][1:-1]
        list_medicine[i]
    str_medicine=' '.join(list_medicine)
    dict_medicine_frequency={}
    for i in range(len(list_given_words)):
        dict_medicine_frequency[list_given_words[i]]=str_medicine.count(list_given_words[i])
    dict_medicine_frequency
    s = pd.Series(dict_medicine_frequency)
    df_medicine_frequency=pd.DataFrame(s,columns=['frequency'])
    df_medicine_frequency=df_medicine_frequency.sort_values(by="frequency",ascending=False)
    df_medicine_frequency.head()
    y1_medicine=int(df_medicine_frequency.iloc[0])
    y10_medicine=int(df_medicine_frequency.iloc[9])
    y20_medicine=int(df_medicine_frequency.iloc[19])
    y30_medicine=int(df_medicine_frequency.iloc[29])
    y40_medicine=int(df_medicine_frequency.iloc[39])
    y50_medicine=int(df_medicine_frequency.iloc[49])
    list_words_medicine=df_medicine_frequency.index.values.tolist()  
    x1_medicine=list_words_medicine[0]
    x2_medicine=list_words_medicine[9]
    x3_medicine=list_words_medicine[19]
    x4_medicine=list_words_medicine[29]
    x5_medicine=list_words_medicine[39]
    x6_medicine=list_words_medicine[49]
    fig = plt.figure(figsize=(15,15))
    ax1 = fig.add_subplot(321)
    plt.subplots_adjust(wspace =0.5, hspace =0.5)
    ax1.set_title('chemistry')
    plt.plot([1, 2, 3, 4, 5, 6], [y1_chemistry, y10_chemistry, y20_chemistry, y30_chemistry, y40_chemistry, y50_chemistry], 'or',mfc='none')
    plt.xticks([1,2,3,4,5,6],[x1_chemistry, x2_chemistry, x3_chemistry, x4_chemistry, x5_chemistry, x6_chemistry])
    plt.ylabel('frequency')
    plt.legend(labels = ['chemistry'], loc = 'best')
    ax2 = fig.add_subplot(322)
    ax2.title.set_text('economics')
    plt.plot([1, 2, 3, 4, 5, 6], [y1_economics, y10_economics, y20_economics, y30_economics, y40_economics, y50_economics], 'ob',mfc='none')
    plt.xticks([1,2,3,4,5,6],[x1_economics, x2_economics, x3_economics, x4_economics, x5_economics, x6_economics])
    plt.ylabel('frequency')
    plt.legend(labels = ['economics'], loc = 'best')
    ax3 = fig.add_subplot(323)
    ax3.title.set_text('literature')
    plt.plot([1, 2, 3, 4, 5, 6], [y1_literature, y10_literature, y20_literature, y30_literature, y40_literature, y50_literature], 'og',mfc='none')
    plt.xticks([1,2,3,4,5,6],[x1_literature, x2_literature, x3_literature, x4_literature, x5_literature, x6_literature])
    plt.ylabel('frequency')
    plt.legend(labels = ['literature'], loc = 'best')
    ax4 = fig.add_subplot(324)
    ax4.title.set_text('peace')
    plt.plot([1, 2, 3, 4, 5, 6], [y1_peace, y10_peace, y20_peace, y30_peace, y40_peace, y50_peace], 'oc',mfc='none')
    plt.xticks([1,2,3,4,5,6],[x1_peace, x2_peace, x3_peace, x4_peace, x5_peace, x6_peace])
    plt.ylabel('frequency')
    plt.legend(labels = ['peace'], loc = 'best')
    ax5 = fig.add_subplot(325)
    ax5.title.set_text('physics')
    plt.plot([1, 2, 3, 4, 5, 6], [y1_physics, y10_physics, y20_physics, y30_physics, y40_physics, y50_physics], 'oy',mfc='none')
    plt.xticks([1,2,3,4,5,6],[x1_physics, x2_physics, x3_physics, x4_physics, x5_physics, x6_physics])
    plt.ylabel('frequency')
    plt.legend(labels = ['physics'], loc = 'best')
    ax6 = fig.add_subplot(326)
    ax6.title.set_text('medicine')
    plt.plot([1, 2, 3, 4, 5, 6], [y1_medicine, y10_medicine, y20_medicine, y30_medicine, y40_medicine, y50_medicine], 'ok',mfc='none')
    plt.xticks([1,2,3,4,5,6],[x1_medicine, x2_medicine, x3_medicine, x4_medicine, x5_medicine, x6_medicine])
    plt.ylabel('frequency')
    plt.legend(labels = ['medicine'], loc = 'best')
    plt.show()
