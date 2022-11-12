#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# In[2]:


movies_data = pd.read_csv('movies.csv')


# In[3]:


movies_data.head()


# In[4]:


movies_data.shape


# In[5]:


selected_features = ['genres','keywords','tagline','cast','director']
print(selected_features)


# In[6]:


for feature in selected_features:
    movies_data[feature] = movies_data[feature].fillna('')


# In[7]:


combined_features = movies_data['genres']+' '+movies_data['keywords']+' '+movies_data['tagline']+' '+movies_data['cast']+' '+movies_data['director']


# In[8]:


print(combined_features)


# In[9]:


vectorizer = TfidfVectorizer()


# In[10]:


feature_vectors = vectorizer.fit_transform(combined_features)


# In[11]:


print(feature_vectors)


# In[12]:


similarity = cosine_similarity(feature_vectors)


# In[13]:


print(similarity)


# In[14]:


print(similarity.shape)


# In[15]:


movie_name = input(' Enter your favourite movie name : ')


# In[16]:


list_of_all_titles = movies_data['title'].tolist()
print(list_of_all_titles)


# In[17]:


find_close_match = difflib.get_close_matches(movie_name, list_of_all_titles)
print(find_close_match)


# In[18]:


close_match = find_close_match[0]
print(close_match)


# In[19]:


index_of_the_movie = movies_data[movies_data.title == close_match]['index'].values[0]
print(index_of_the_movie)


# In[20]:


similarity_score = list(enumerate(similarity[index_of_the_movie]))
print(similarity_score)


# In[21]:


len(similarity_score)


# In[22]:


sorted_similar_movies = sorted(similarity_score, key = lambda x:x[1], reverse = True) 
print(sorted_similar_movies)


# In[24]:


print('Movies suggested for you : \n')

i = 1

for movie in sorted_similar_movies:
    index = movie[0]
    title_from_index = movies_data[movies_data.index==index]['title'].values[0]
    if (i<30):
        print(i, '.',title_from_index)
        i+=1


# In[ ]:





# In[ ]:




