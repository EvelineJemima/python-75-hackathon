#!/usr/bin/env python
# coding: utf-8

# In[1]:


#To randomly display numbers between given range
import numpy as np
x = np.random.randint(low=10, high=100, size=6)
print(x)


# In[2]:


#Create an empty tuple 
tuple1 = ()
print(x)
#Create an empty tuple with tuple() function built-in Python
tuple2= tuple()
print(tuplex)


# In[5]:


d = {100:10, 200:20}
print(d)
d.update({300:30})
print(d)


# In[6]:


dic = {'a': 1, 'b': 2}
dic1= {'x': 3, 'y': 2}
d = dic.copy()
d.update(dic1)
print(d)


# In[9]:


set1 = set([0, 1, 3, 4, 5])
set1.pop()
print(set1)
set1.pop()
print(set1)


# In[11]:


import numpy as np
x = np.random.randint(1000,50000,10)
print("1st array:")
print(x)
y = np.random.randint(1000,50000,10)
print("2nd array:")
print(y)
print("Test above two arrays are equal or not!")
check_equal = np.allclose(x, y)
print(array_equal)


# In[13]:



def string_length(str):
    count = 0
    for char in str:
        count += 1
    return count
print(string_length('talent accurate'))


# In[14]:


def add_string(str1):
  length = len(str1)

  if length > 2:
    if str1[-3:] == 'tal':
      str1 += 'ent'
    else:
      str1 += 'accurate'

  return str1
print(add_string('tal'))
print(add_string('talent'))


# In[27]:


def find_longest_element(elements_list):
    element_len = []
    
    for n in elements_list:
        element_len.append((len(n), n))
        print(element_len)
    
    element_len.sort(reverse=True)
    print(element_len)
    
    element_len.sort()
    print(element_len)
    
    return element_len[-1][1]  #returns the 

print(find_longest_element(["HACKATHON", "PYTHON", "75"]))


# In[28]:


# python program to print initials of a name  
def name(s): 
  
    # split the string into a list  
    l = s.split() 
    new = "" 
  
    # traverse in the list  
    for i in range(len(l)-1): 
        s = l[i] 
          
        # adds the capital first character  
        new += (s[0].upper()+'.') 
          
    # l[-1] gives last item of list l. We 
    # use title to print first character in 
    # capital. 
    new += l[-1].title() 
      
    return new  
      
# Driver code             
s ="mohandas karamchand gandhi" 
print(name(s))    


# In[40]:


import csv

f = open(r'C:\Users\Admin\AppData\Roaming\Microsoft\Windows\Network Shortcuts\Data.csv')
csv_f = csv.reader(f)
for row in csv_f:
    print(row)


# In[ ]:




