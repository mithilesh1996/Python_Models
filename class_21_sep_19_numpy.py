
# coding: utf-8

# In[1]:


import numpy as np


# In[8]:


import math


# In[29]:


b = np.array([[1,2,3],[4,5,7]])


# In[30]:


type(b)


# In[31]:


print(b)


# In[32]:


b.shape


# ###  numpy generally for matrix multiplication
# 

# In[34]:


b[1,1]


# In[35]:


b[0,0]


# In[38]:


b[0,0],b[0,1],b[0,2],b[1,0],b[1,1],b[1,2]


# In[39]:


np.zeros((2,2))


# In[44]:


mt1=np.array([[1,1],[1,1]])


# In[45]:


np.ones((3,3))


# In[59]:


mt1


# In[62]:


mt2=np.array([[2,2],[2,2]])


# In[63]:


print(mt2)


# In[52]:


np.full((4,3),4)


# In[67]:


mt2*mt1


# In[65]:


np.multiply(mt1,mt2)


# In[66]:


np.eye(5)


# In[57]:


np.eye(2)


# In[58]:


np.eye(1)


# In[69]:


np.random.random((4,3))  ##by default value in 0 to 1


# In[72]:


(10-6)*np.random.random()+6


# In[75]:


np.random.random((10,10))


# In[78]:


(60-50)*np.random.random((10,10))+50


# In[87]:


a=np.array([[1,2],[3,4],[5,6]])


# In[88]:


a[0]


# In[89]:


a[1]


# In[83]:


a[2]


# In[93]:


a[0,1][0,1]


# In[99]:


a


# In[125]:


a=np.array([(1,2,3),[4,5,6],[7,8,9],[10,11,12]])


# In[126]:


a


# In[106]:


c


# In[107]:


c1=np.array([0,2,0,1])


# # 

# In[108]:


c1


# In[109]:


d=np.array([1,2,3,4])


# In[116]:


c=np.arange(1,10,2)


# In[117]:


c


# In[ ]:


0


# In[118]:


b=np.array([0,2,0,1])


# In[119]:


b


# In[121]:


c=np.arange(4)


# In[122]:


c


# In[127]:


a[c,b]


# In[128]:


a[c,b]+=10


# In[129]:


a


# In[130]:


a


# In[137]:


a!=17


# In[138]:


(a>2) & (a<10)


# In[144]:


arr1=np.array([[1,1],[1,1]])


# In[145]:


arr2=np.array([[2,2],[2,2]])


# In[146]:


print(arr1)
print(arr2)


# ## 

# In[153]:


arr1+arr2


# In[154]:


arr2-arr1


# In[155]:


np.add(arr1,arr2)


# In[156]:


np.subtract(arr1,arr2)


# In[157]:


np.multiply(arr1,arr2)


# ## np.add(a,b)   a+b
# ## subtract(a,b)  a-b
# 
# ## np.multiply(a*b)  element wise multiplication
# 
# ## np.dot(a*b)     matrix multiplication

# In[159]:


np.dot(arr1,arr2)


# In[160]:


np.divide(arr1,arr2)


# In[164]:


v=np.array([1,2])


# In[165]:


v


# In[166]:


v.shape


# In[167]:


v.ndim


# In[169]:


w=np.array([3,4])


# In[170]:


w.shape


# In[171]:


w.ndim


# In[173]:


np.dot(v,w)


# In[174]:


a


# In[176]:


print('matrix a:',a)
print('transpose of A is :',a.T)


# In[177]:


b=np.array([[1,2],[3,4],[5,6]])


# In[178]:


b


# In[179]:


print(b.T)


# In[180]:


np.sum(b)


# In[183]:


mat=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])


# In[185]:


mat2=np.array([[1],[1],[1],[1]])


# In[187]:


print(mat)
print(mat2)


# In[186]:


np.add(mat,mat2)


# In[188]:


mat3=np.array([[1,2,3],[4,5,6]])


# In[189]:


mat3.shape


# In[196]:


mat4=np.array([[1,1,1]])


# In[197]:


mat4.shape


# In[198]:


print(mat3)
print(mat4)


# In[193]:


np.add(mat3,mat4)


# In[199]:


mat3.reshape


# In[202]:


mat3.reshape(3,2)


# ## pandas data frames

# In[203]:


import pandas as pd


# In[204]:


cities=['mumbai','delhi','pune','banglore']


# In[205]:


code=[1,2,3,4]


# In[206]:


mydata=list(zip(cities,code))


# In[207]:


mydata


# In[212]:


df=pd.DataFrame(mydata,columns=["cities","code"])


# In[210]:


df


# In[214]:


data={'name':["css",'ccs','rms','scrts','drvts','usdinr'],'priority':[1,2,3,4,5,6]}


# In[215]:


df_from_dict=pd.DataFrame(data)


# In[216]:


df_from_dict


# In[282]:


a=[{'a':10,'b':20,'c':30},{'a':100,'d':200,'c':300},{'a':1000,'b':2000,'c':3000}]


# In[31]:


import pandas as pd


# In[284]:


list_to_frame=pd.DataFrame(a)


# In[285]:


list_to_frame


# In[75]:


myfile="C:/Users/admin/Documents/My_Dir_Python/Data/bank-full.csv"

bd=pd.read_csv(myfile,sep=',')

bd.head()


# In[78]:


bd.dtypes


# In[79]:


bd["month"].dtypes


# In[80]:


bd.describe()










# In[81]:


bd["job"].value_counts()


# In[82]:


bd["age"][3]=NA


# In[83]:


bd


# In[60]:


d=0


# In[ ]:


np.fillna()


# In[88]:


for i in bd.columns:
        a=bd[i].isna().sum()
        print("bd [",i,"]:       ",a)
        d=d+a
print("All th sum is ")
print(d)


# In[85]:


mean2=np.mean(bd['balance'])


# In[86]:


mean2


# In[87]:


bd['balance'].fillna(mean2,inplace=True),


# In[95]:


bd['balannce_3']=bd['balance'].fillna(method='ffill')


# In[96]:


bd.head()


# In[62]:


bd.groupby('job')["age"].min()


# ## Group by in Pandas how to Apply

# In[63]:


bd.groupby(['housing','loan']).agg({'age':'mean','duration':'max','balance':'sum'})


# In[7]:


np.linspace(1,50,num=6)


# In[3]:


np.arange(1,5,4)


# In[10]:


np.arange(1,51,5)


# In[18]:


a=[1,2,45,86,54,8,89]


# In[12]:


np.max(a)


# In[13]:


np.argmax(a)


# In[19]:


np.sort(a)


# In[20]:


np.argsort(a)


# In[116]:


myfile="C:/Users/admin/Documents/My_Dir_Python/Data/bank-full.csv"


# In[117]:


bd=pd.read_csv(myfile,sep=',')


# In[118]:


bd.head(100)


# In[140]:


bd_1=bd[(bd['age']!=40) &(bd['marital']=='single') & (bd['balance']>9000)]


# In[144]:


import math


# In[148]:


import statistics


# In[181]:


temp=bd[(bd['age']>40) &(bd['marital']=='married')]


# In[183]:


temp[['balance','housing']]


# In[170]:


np.mean(bd_2['balance'])


# In[168]:


import statistics


# In[169]:


statistics.mean([1,2,3])


# In[135]:


bd[['balance','education'],(bd['balance']>10000)]


# In[141]:


avg(bd_1['balance'])


# ## Aceesing specific number from dataframe in Pandas

# In[184]:


bd.iloc[0,5]


# In[185]:


bd.iloc[0:5,5:7]


# In[189]:


bd.loc[3,'balance']


# In[188]:


bd


# In[204]:


myfile="C:/Users/admin/Documents/My_Dir_Python/Data/bank-full.csv"


# In[205]:


bd_new=pd.read_csv(myfile,index_col=5)


# In[209]:


bd_new.head()


# In[216]:


print(bd.shape)


# In[210]:


gen=np.random.choice([0,1],size=bd.shape[0])


# In[222]:


salary=500*np.random.random([bd.shape[0]])+1000


# In[213]:


salary_df=pd.DataFrame(data=list(zip(gen,salary)),columns=['gender','salary'])


# In[217]:


concat_horiz_df=pd.concat([bd,salary_df],axis=1)


# In[235]:


bd.shape


# In[232]:


print(salary_df.shape)
print(bd.shape)
print(concat_horiz_df.shape)


# In[220]:


concat_horiz_df.head()


# In[236]:


bd_vet_df=bd.head(100)


# In[237]:


bd_vet_df


# In[239]:


concat_vet_df=pd.concat([concat_horiz_df,bd_vet_df],axis=0)


# In[240]:


print(salary_df.shape)
print(bd.shape)
print(concat_horiz_df.shape)
print(concat_vet_df.shape)


# ## Combining data frames using append

# In[241]:


df_add_row=bd.append(bd_vet_df,verify_integrity=True)


# ##  Combining Data frames using Merge statement (it work like join in sql)

# In[242]:


gen=np.array([0,1])


# In[243]:


gen


# In[244]:


fixed_salary=500*np.random.random([2])+1000


# In[247]:


fixed_salary_df=pd.DataFrame(data=list(zip(gen,fixed_salary)),columns=['gender','fixed_salary'])


# In[249]:


fixed_salary_df


# In[250]:


mapped_salary=pd.merge(concat_horiz_df,fixed_salary_df,left_on='gender',right_on='gender',how='left')


# In[251]:


mapped_salary.head()

