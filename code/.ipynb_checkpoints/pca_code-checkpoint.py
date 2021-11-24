#!/usr/bin/env python
# coding: utf-8

# In[88]:


import pandas as pd 
import numpy as np
import pandas as pd 
X = [[7,8,9,10],[45,67,56,57],[34,23,56,78],[68,78,89,90],[1,2,3,4],[2,3,4,5],[8,9,10,11]]

X     


# In[89]:


from sklearn.decomposition import PCA


pca = PCA(n_components = 2)
pc= pca.fit(X) 
print(pc.transform(X))
pc.transform([X[1]])


# In[90]:


from sklearn.decomposition import PCA
import pickle as pk
pca = PCA(n_components=2)
result = pca.fit_transform(X)    
pk.dump(pca, open("pca.pkl","wb"))


pca_reload = pk.load(open("pca.pkl",'rb'))
result_new = pca_reload .transform(X)
import pickle as pk
pca = PCA(n_components=2)
result = pca.fit_transform(X) # Assume X is having more than 2 dimensions    
pk.dump(pca, open("pca.pkl","wb"))

# later reload the pickle file
pca_reload = pk.load(open("pca.pkl",'rb'))
result_new = pca_reload .transform([X[0]])
print(result_new)

