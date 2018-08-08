
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')


# In[2]:


import seaborn as sns
sns.set_style('whitegrid')


# In[3]:


data=pd.read_csv(r'C:\Users\naveen chauhan\Desktop\mldata\mlp\Turkiye Student Evaluation\train.csv')


# In[4]:


data.head()


# In[5]:


data['nb.repeat'].hist(bins=50)


# In[6]:


data.describe()


# In[7]:


data.isnull().sum()


# In[8]:


plt.figure(figsize=(20,4))
sns.countplot(x='class',data=data)


# In[9]:


plt.figure(figsize=(20,20))
sns.boxplot(data=data.iloc[:,5:31])


# In[12]:


questionmeans=[]
classlist=[]
questions=[]
totalplotdata=pd.DataFrame(list(zip(classlist,questions,questionmeans)),columns=['class','questions','mean'])
for class_num in range(1,13):
    class_data=data[(data['class']==class_num)]
    questionmeans=[]
    classlist=[]
    questions=[]
    for num in range(1,13):
        questions.append(num)
    for col in range(5,17):
        questionmeans.append(class_data.iloc[:,col].mean())
    classlist+=12*[class_num]
    print(classlist)
    plot_data=pd.DataFrame(list(zip(classlist,questions,questionmeans)),columns=['class','questions','mean'])
    totalplotdata=totalplotdata.append(plot_data,ignore_index=True)


# In[15]:


plt.figure(figsize=(20,10))
sns.pointplot(x='questions',y='mean',data=totalplotdata,hue='class')


# In[21]:


questionmeans=[]
inslist=[]
questions=[]
totalplotdata=pd.DataFrame(list(zip(inslist,questions,questionmeans)),columns=['ins','questions','mean'])
for ins_num in range(1,4):
    ins_data=data[(data['instr']==ins_num)]
    questionmeans=[]
    inslist=[]
    questions=[]
    for num in range(13,29):
        questions.append(num)
    for col in range(17,33):
        questionmeans.append(ins_data.iloc[:,col].mean())
    inslist+=16*[ins_num]
    print(inslist)
    plotdata=pd.DataFrame(list(zip(inslist,questions,questionmeans)),columns=['ins','questions','mean'])
    totalplotdata=totalplotdata.append(plotdata)


# In[25]:


plt.figure(figsize=(20,5))
sns.pointplot(x='questions',y='mean',data=totalplotdata,hue='ins')


# In[29]:


#calculate mean for intructor 
dataset_inst3=data[(data['instr']==3)]
class_array_for_inst3=dataset_inst3['class'].unique().tolist()
questionmeans=[]
classlist=[]
questions=[]
totalplotdata=pd.DataFrame(list(zip(classlist,questions,questionmeans)),columns=['class','questions','mean'])
for class_num in class_array_for_inst3:
    class_data=dataset_inst3[(dataset_inst3['class']==class_num)]
    questionmeans=[]
    classlist=[]
    questions=[]
    for num in range(1,13):
        questions.append(num)
    for col in range(5,17):
        questionmeans.append(class_data.iloc[:,col].mean())
    classlist+=12*[class_num]
    plotdata=pd.DataFrame(list(zip(classlist,questions,questionmeans)),columns=['class','questions','mean'])
    totalplotdata=totalplotdata.append(plotdata)


# In[30]:


totalplotdata


# In[31]:


plt.figure(figsize=(20,10))
sns.pointplot(x='questions',y='mean',data=totalplotdata,hue='class')


# In[32]:


#lets begin cluster the students on the basis of questionaire
dataset_question=data.iloc[:,5:33]


# In[33]:


dataset_question.head()


# In[34]:


#lets do pca for feature dimensional reduction
from sklearn.decomposition import PCA
pca=PCA(n_components=2)
dataset_questions_pca=pca.fit_transform(dataset_question)


# In[37]:


dataset_questions_pca


# In[38]:


from sklearn.cluster import KMeans
wcss=[]
for i in range(1,7):
    kmeans=KMeans(n_clusters=i,init='k-means++',random_state=42)
    kmeans.fit(dataset_questions_pca)
    wcss.append(kmeans.inertia_)
plt.plot(range(1,7),wcss)
plt.title('the elbow method')
plt.xlabel('number of clusters')
plt.ylabel('WCSS')
plt.show()


# In[39]:


kmeans=KMeans(n_clusters=3,init='k-means++')
y_kmeans=kmeans.fit_predict(dataset_questions_pca)


# In[41]:


plt.scatter(dataset_questions_pca[y_kmeans==0,0],dataset_questions_pca[y_kmeans==0,1],s=100,c='yellow',label='cluster1')
plt.scatter(dataset_questions_pca[y_kmeans==1,0],dataset_questions_pca[y_kmeans==1,1],s=100,c='green',label='cluster2')
plt.scatter(dataset_questions_pca[y_kmeans==2,0],dataset_questions_pca[y_kmeans==2,1],s=100,c='red',label='cluster3')
plt.scatter(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,1],s=300,c='blue',label='Centroids')
plt.title('cluster of students')
plt.xlabel('PCA 1')
plt.ylabel('PCA 2')
plt.legend()
plt.show()


# In[63]:


import collections
collections.Counter(y_kmeans)


# In[64]:


#using demogram to find the optimal number of cluster
import scipy.cluster.hierarchy as sch


# In[66]:


dendrogram=sch.dendrogram(sch.linkage(dataset_questions_pca,method='ward'))
plt.title('Dendrogram')
plt.xlabel('questions')
plt.ylabel('Euclidean Distances')
plt.show()


# In[67]:


#fitting hierarchical cluster to dataset
from sklearn.cluster import AgglomerativeClustering
hc=AgglomerativeClustering(n_clusters=2,affinity='euclidean',linkage='ward')
y_hc=hc.fit_predict(dataset_questions_pca)
X=dataset_questions_pca
#visualizing the cluster
plt.scatter(X[y_hc == 0, 0], X[y_hc == 0, 1], s = 100, c = 'yellow', label = 'Cluster 1')
plt.scatter(X[y_hc == 1, 0], X[y_hc == 1, 1], s = 100, c = 'red', label = 'Cluster 2')
plt.title('Clusters of STUDENTS')
plt.xlabel('PCA 1')
plt.ylabel('PCA 2')
plt.legend()
plt.show()


# In[68]:


import collections
collections.Counter(y_hc)

