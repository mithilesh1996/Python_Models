
# coding: utf-8

# In[5]:


myfile='C:/Users/admin/Documents/My_Dir_Python/Data1/winequality-white.csv'

import pandas as pd
from sklearn.preprocessing import scale
from sklearn.cluster import KMeans
from sklearn.metrics import  silhouette_score

import matplotlib.pyplot as plt
import numpy as np

get_ipython().run_line_magic('matplotlib', 'inline')

wine=pd.read_csv(myfile,sep=";")


# In[9]:


wine=wine[["sulphates","alcohol"]]


# In[10]:


wine.head(5)


# In[11]:


wine.shape


# In[12]:


wine.describe()


# In[13]:


wine_std=pd.DataFrame(scale(wine),
                      columns=list(wine.columns))


# In[14]:


wine_std.describe()


# In[15]:


range_n_clusters = [2, 3, 4, 5, 6,7,8,9]


# In[17]:


for k in range_n_clusters:
    kmeans=KMeans(n_clusters=k)
    kmeans.fit(wine_std)
    
    print(k,silhouette_score(wine_std,kmeans.labels_))


# In[20]:


print(k)


# In[21]:


k = 3
kmeans = KMeans(n_clusters=k)
kmeans.fit(wine_std)


# In[22]:


labels = kmeans.labels_
wine["cluster"]=labels


# In[23]:


wine['cluster'].value_counts()


# In[24]:


wine.groupby(['cluster']).mean()


# In[25]:


import seaborn as sns


# In[26]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[27]:


sns.lmplot(fit_reg=False,x='sulphates',y='alcohol',data=wine,hue='cluster')


# In[28]:


from sklearn.cluster import AgglomerativeClustering


# In[29]:


for n_clusters in range(2,10):
    cluster_model = AgglomerativeClustering(n_clusters=n_clusters, affinity='euclidean',linkage='ward')
    cluster_labels = cluster_model.fit_predict(wine_std)
    silhouette_avg = silhouette_score(wine_std,cluster_labels,metric='euclidean')
    print("For n_clusters =", n_clusters, 
          "The average silhouette_score is:", silhouette_avg)


# In[30]:


hclus=AgglomerativeClustering(n_clusters=k, affinity='euclidean',linkage='ward')


# In[31]:


labels_hclus=hclus.fit_predict(wine_std)


# In[32]:


wine['cluster_hclus']=labels_hclus


# In[33]:


sns.lmplot(fit_reg=False,x='sulphates',y='alcohol',data=wine,hue='cluster_hclus')


# In[35]:


wine.head(100)


# # DBSCAN

# In[56]:



mydata=pd.read_csv("C:/Users/admin/Documents/My_Dir_Python/Data1/moon_data.csv").iloc[:,1:]
mydata.head()


# In[57]:


mydata.head()

mydata.shape



# In[58]:


sns.lmplot('X','Y',data=mydata,fit_reg=False) 


# In[59]:


kmeans=KMeans(n_clusters=2)
kmeans.fit(mydata)
mydata["cluster"]=kmeans.labels_


# In[60]:


sns.lmplot('X','Y',data=mydata,hue='cluster',fit_reg=False)


# In[61]:


from sklearn.cluster import DBSCAN


# In[62]:


del mydata['cluster']


# In[79]:


db = DBSCAN(eps= 0.1, min_samples=60, metric='euclidean').fit(mydata)
mydata['cluster']=db.labels_
sns.lmplot('X','Y',data=mydata,hue='cluster',fit_reg=False)


# In[34]:


pd.Series(db.labels_).value_counts()


# # anamoly detection with dbscan

# In[86]:


myfile='C:/Users/admin/Documents/My_Dir_Python/Data1/Wholesale customers data.csv'

groc=pd.read_csv(myfile)

groc=groc[["Milk","Grocery"]]

groc_std=pd.DataFrame(scale(groc),columns=list(groc.columns))


# In[87]:


sns.lmplot(x='Milk',y='Grocery',data=groc,fit_reg=False)


# In[88]:


r=np.linspace(0.5,5)
for epsilon in r:
    db = DBSCAN(eps=epsilon, min_samples=20, metric='euclidean').fit(groc_std)
    labels = db.labels_
#     n_clust=len(set(labels))-1
    outlier=np.round((labels == -1).sum()/len(labels)*100,2)
#     print('Estimated number of clusters: %d', n_clust)
    print("For epsilon =", epsilon ,", percentage of outliers is: ",outlier)


# In[92]:


print(db.labels_)


# In[95]:


print(r)


# In[84]:


db = DBSCAN(eps=0.77, min_samples=20, metric='euclidean').fit(groc_std)
groc['cluster']=db.labels_


# In[85]:


sns.lmplot(x='Milk',y='Grocery',data=groc,fit_reg=False,hue='cluster')

