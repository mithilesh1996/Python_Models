
# coding: utf-8

# In[12]:


stuple=('CSS','CCS','RMS','scrts','PVP')


# In[19]:


print(stuple)


# In[22]:


type(stuple)


# In[29]:


b=list(stuple)


# In[30]:


print(b)


# In[31]:


b[0]="hhhfhfhf"


# In[32]:


print(b)


# In[33]:


stuple


# In[34]:


ls1=[1,5,8,'Mithi','Python','were']


# In[35]:


ls2=ls1


# In[36]:


ls2


# In[37]:


ls1[3]='rahhhh'


# In[38]:


ls1


# In[39]:


ls2


# In[40]:


print(ls1)
print(ls2)


# In[41]:


sort(stuple)


# In[42]:


stuple(sort)


# In[43]:


stuple.sort()


# In[46]:


set1={'css','ccs','rms','scrts','drvts','usdinr','frxfwd','cls','rms'}


# # 

# In[47]:


set1


# In[48]:


print(set1)


# In[49]:


print(set1)


# In[50]:


print(set1)


# In[51]:


print(set1)


# In[52]:


print(set1)


# In[53]:


print(set1)


# In[54]:


ls3=[10,123,13,14,15,12,10,10,12]


# In[55]:


set2=set(ls3)


# In[56]:


set2


# In[57]:


set2


# In[58]:


set2.add('astha')


# In[59]:


set2


# In[60]:


set2.remove('astha')


# In[61]:


set2


# In[62]:


set2.add('astha')


# In[63]:


set2


# In[64]:


set2.remove('assth')


# In[65]:


set3={'mi','srh','dd','csk','kkr','pnjb','rcb'}


# In[66]:


set3


# In[67]:


set3.pop(set3)


# In[68]:


set3.pop('mi')


# In[69]:


set3.pop(3)


# In[75]:


set4={1,7,8,9,5,6}


# In[74]:


set5={2,4,6,7,8,6,3,11,12}


# In[76]:


set6=set4.union(set5)


# In[77]:


print(set6)


# In[78]:


set7=set4.intersection(set5)


# In[79]:


print(set2)


# In[80]:


print(set6)


# In[81]:


print(set7)


# In[82]:


print(set4)
print(set5)


# In[83]:


set4.difference(set5)


# In[84]:


set4.symmetric_difference(set5)


# In[85]:


dict1={'name':'mithi','location':'pune','copany':'Tcs','work':'Majuri','hobby':'sleeping'}


# In[86]:


dict1


# In[88]:


dict2={1:1,2:4,3:9,4:16,5:25,6:36,7:49,8:64}


# In[90]:


dict2


# In[91]:


dict2[2]


# In[92]:


dict2[4]


# In[93]:


dict2[16]


# In[94]:


dict2[9]=81


# In[95]:


dict2


# In[96]:


print(dict2)


# In[99]:


dict2[10]=100


# In[100]:


dict


# In[102]:


dict2


# In[103]:


del dict2[6]


# In[104]:


dict2


# In[107]:


del dict2[7]


# In[108]:


dict2


# In[109]:


del dict2[9]


# In[110]:


dict2


# In[111]:


dict2_items


# In[113]:


dict2.values()


# In[114]:


dict2.keys()


# In[115]:


dict2.keys()

