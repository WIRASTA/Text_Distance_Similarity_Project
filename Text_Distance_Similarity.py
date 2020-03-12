#!/usr/bin/env python
# coding: utf-8

# In[1]:


# pip install textdistance


# ## Example Methode

# # Hamming
# 
# https://github.com/life4/textdistance

# In[2]:


import textdistance


# In[3]:


textdistance.hamming('test', 'text')


# In[4]:


textdistance.hamming.distance('test', 'text')


# In[5]:


textdistance.hamming.similarity('test', 'text')


# In[6]:


textdistance.hamming.normalized_distance('test', 'text')


# In[7]:


textdistance.hamming.normalized_similarity('test', 'text')


# In[8]:


textdistance.Hamming(qval=2).distance('test', 'text')


# In[9]:


hamming = textdistance.Hamming(external=False)
hamming('text', 'testit')


# # Levenshtein
# 
# https://itnext.io/string-similarity-the-basic-know-your-algorithms-guide-3de3d7346227

# In[10]:


textdistance.levenshtein('arrow', 'arow')


# In[11]:


textdistance.levenshtein.normalized_similarity('arrow', 'arow')


# # Jaro Winkler
# 
# https://itnext.io/string-similarity-the-basic-know-your-algorithms-guide-3de3d7346227

# In[12]:


textdistance.jaro_winkler("mes", "messi")


# In[13]:


textdistance.jaro_winkler("crate", "crat")


# In[14]:


textdistance.jaro_winkler("crate", "atcr")


# # Jaccard Index

# In[15]:


tokens_1 = "hello world".split()
tokens_2 = "world hello".split()
textdistance.jaccard(tokens_1 , tokens_2)


# In[16]:


tokens_1 = "hello new world".split()
tokens_2 = "hello world".split()
textdistance.jaccard(tokens_1 , tokens_2)


# ##  Metaphone

# In[18]:


pip install Metaphone


# In[19]:


from metaphone import doublemetaphone


# In[21]:


text1 = input ("enter your first word : ")
text2 = input ("enter your second word : ")

def sim_text(text1,text2):
    print("hamming = "+str(textdistance.hamming.normalized_similarity(text1, text2)))
    #a=textdistance.hamming.normalized_similarity(text1, text2)
    print("lavenshtein ="+str(textdistance.levenshtein.normalized_similarity(text1, text2)))
    #b=textdistance.levenshtein.normalized_similarity(text1, text2)
    print("jaro = "+str(textdistance.jaro.normalized_similarity(text1, text2)))
    #c=textdistance.jaro.normalized_similarity(text1, text2)

def meta_style(text1,text2):
    an = doublemetaphone(text1)
    x = an[0]
    bn= doublemetaphone(text2)
    y = bn[0]
    c = sim_text(x,y)

print("================================================================")
print("without metaphone")
sim_text(text1,text2)
print("================================================================")
print("with metaphone")
meta_style(text1,text2)

