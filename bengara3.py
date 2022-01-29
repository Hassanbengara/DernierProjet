#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
df=pd.read_csv(r'Desktop\Nouveaudossier/t.csv',sep=';')
df.head(6)


# In[4]:


df.tail()


# In[5]:


df.info()


# In[6]:


df.describe()


# In[7]:


df.isnull().sum()


# In[8]:


df['Age'].fillna(df['Age'].mean(),inplace=True)
df['Age'].isnull().sum()


# In[9]:


number_of_elements=len(df['Cabin'])
print("Number of elements",number_of_elements)
print(df['Embarked'].value_counts())
df['Embarked'].fillna('S',inplace=True)
df['Embarked'].isnull().sum()


# In[10]:


number_of_elements=len(df['Cabin'])
print("Number of elements",number_of_elements)
print(df['Cabin'].value_counts())
df['Cabin'].fillna('G6',inplace=True)
df['Cabin'].isnull().sum()


# In[11]:


df.isnull().sum().sum()


# In[12]:


import matplotlib.pyplot as plt 
df['Age'].plot.hist()


# In[13]:


plt.xlabel("Pclass")
plt.ylabel("Pclasse value count")
plt.title("Bar plot of Pclasses")
vc=df['Pclass'].value_counts()
vc.plot.bar(rot=0)


# In[14]:


import seaborn as sns
grid = sns.FacetGrid(df, row="Survived", size=2.2, aspect=1.6)
grid.map(sns.barplot, "Sex", 'Age', alpha=.5, ci=None)
grid.add_legend()


# In[18]:


grid = sns.FacetGrid(df, row="Survived", size=2.2, aspect=1.6)
grid.map(sns.barplot, "Pclass", "Fare", alpha=.5, ci=None)
grid.add_legend()


# In[17]:


def plot_correlation_map( df ):

    corr = df.corr()

    s , ax = plt.subplots( figsize =( 12 , 10 ) )

    cmap = sns.diverging_palette( 220 , 10 , as_cmap = True )

    s = sns.heatmap(

        corr, 

        cmap = cmap,

        square=True, 

        cbar_kws={ 'shrink' : .9 }, 

        ax=ax, 

        annot = True, 

        annot_kws = { 'fontsize' : 12 }

        )
plot_correlation_map(df)


# The result depicts the correlations between the different columns. Obviously, the coefficient of correlation between a column and itself is equal to one. There are columns that are positively correlated. Others are negatively correlated. For instance, the correlation between Fare and Pclass is -0.55. That means, the more the class is higher in terms of numbers, the higher the fare is. The lowest correlation in module is between PassengerId and Parch. These variables are practically non-correlated and it's irrelevant to associate one variable with another.

# In[20]:


df[["Pclass", "Survived"]].groupby(["Survived"], as_index=True).mean()


# In[32]:


df.drop("Name",axis=1)


# In[ ]:


Title_Dictionary = {

                    "Capt":       "Officer",

                    "Col":        "Officer",

                    "Major":      "Officer",

                      "Dr":         "Officer",

                    "Rev":        "Officer”,

                    "Jonkheer":   "Royalty",

                    "Don":        "Royalty",

                    "Sir" :       "Royalty",

                   "Lady" :      "Royalty"

                  "the Countess": "Royalty",

                    "Dona":       "Royalty”,

                    "Mme":        "Miss",

                    "Mlle":       "Miss",

                    "Miss" :      "Miss",

                    "Ms":         "Mrs",

                    "Mr" :        "Mrs",

                    "Mrs" :       "Mrs

                    "Master" :    "Master"

                    }


# In[35]:


df['FamilySize']=df['SibSp']+df['Parch']
df


# In[36]:


plot_correlation_map(df)


# In[37]:


df[["FamilySize", "Survived"]].groupby(["Survived"], as_index=True).mean()


# This feature is practically not useful. That's because the average family size of people on board is almost one regardless of whether they survived or not

# In[ ]:




