#!/usr/bin/env python
# coding: utf-8

# ### DCL-160: Python Programming
# 
# Module 01
# 
# December 08, 2020
# 
# Binnur Kurt <binnur.kurt@gmail.com>

# In[1]:


import this


# In[2]:


name = "Jack"


# In[3]:


x = None


# In[4]:


type(x)


# In[5]:


type(name)


# In[6]:


y = "\u20ba"


# In[7]:


y


# In[10]:


z = 3615.73


# In[11]:


type(z)


# In[12]:


u = 42


# In[13]:


type(u)


# In[14]:


v = True


# In[15]:


type(v)


# In[18]:


type("Jack Shephard")


# In[19]:


type(None)


# In[21]:


type(u * u + 2.45)


# In[22]:


v = 2**16


# In[23]:


v


# In[24]:


type(v)


# In[25]:


type( (0.1+0.2)+0.3 == 0.1+(0.2+0.3))


# In[26]:


w = (0.1+0.2)+0.3 == 0.1+(0.2+0.3)


# In[27]:


w


# In[28]:


w = 0.1 + 0.2


# In[29]:


w


# In[32]:


w = 0.1 + ( 0.2 + 0.3 )


# In[33]:


w


# In[34]:


w = ( 0.1 + 0.2 ) + 0.3


# In[39]:


w == 0.6


# In[37]:


100 * 4.35


# In[38]:


2.0 - 1.1


# In[40]:


# CPU (8-10), GPU (1024-2048-4096), TPU(Tensor Processing Unit) -> IEEE-756 v5


# In[41]:


i = 2
j = i ** 100000


# In[42]:


j


# In[43]:


3615 * 4629


# In[44]:


3615.0 * 4629.0


# In[45]:


#TensorRT -> Model -> Integer Model x100


# In[46]:


3 / 2


# In[47]:


4 / 2


# In[48]:


3 // 2


# In[49]:


3 % 2


# In[50]:


2 ** 3


# In[51]:


m = 2 / 0


# In[54]:


m = float('-inf')


# In[55]:


m


# In[56]:


n = float('nan')


# In[57]:


n


# In[59]:


n * 2


# In[60]:


m = float('nan')


# In[61]:


m


# In[62]:


n


# In[63]:


m == n


# In[64]:


x = 42


# In[65]:


x == x


# In[66]:


x = float('nan')


# In[67]:


x == x


# In[68]:


u = "123.45"


# In[69]:


type(u)


# In[70]:


f = float(u)


# In[71]:


f


# In[73]:


g = int(f)


# In[74]:


g


# In[75]:


bool(g)


# In[76]:


bool(0)


# In[77]:


bool(-1)


# In[78]:


bool(+1)


# In[79]:


h = None


# In[80]:


h is None


# In[81]:


h = 42


# In[82]:


h is None


# In[83]:


h is not None


# In[84]:


def add_and_multiple(a,b,c=None):
    result = a + b
    if c is not None:
        result = result * c
    return result    


# In[85]:


x=10
y=20
add_and_multiple(x,y)


# In[86]:


add_and_multiple(x,y,2)


# In[87]:


c1 = complex(2,3) # 2 + 3i


# In[88]:


type(c1)


# In[89]:


c2 = complex(3,2) # 3 + 2i


# In[90]:


c1


# In[91]:


c2


# In[92]:


c1 * c2


# In[93]:


c1.conjugate()


# In[94]:


c1 * c1.conjugate()


# In[95]:


c1.conjugate().real


# In[97]:


c1.conjugate().imag


# In[98]:


fullname = "jack bauer"


# In[99]:


fullname


# In[100]:


fullname = 'jack bauer'


# In[101]:


fullname


# In[102]:


fulltext = """this is first line.
this is the second line.
this is the third line.
"""


# In[104]:


fulltext= "this is first line.\nthis is second line.\nthis is the third line."


# In[105]:


print(fulltext)


# In[106]:


print("""This is the firstline.
This is the second line.
This is the third line.
""")


# In[107]:


print("This" "is" "the" "line")


# In[108]:


print("This","is","the","line")


# In[111]:


print("first name: \"%s\", last name: \"%s\"\nsalary: %8.2f" 
      % ("Jack","Bauer", 123456.789))


# In[114]:


numbers = [4,8,15,16,23,42]
print("Lottery numbers:\t\\%s\\" % numbers)


# In[126]:


from math import pow, sqrt, exp, expm1


# In[127]:


expm1(1e-5)


# In[128]:


pow(10,2.3)


# In[130]:


sqrt(3615.77)


# In[131]:


import math


# In[135]:


math.dist((2,8,1),(-1,-7,8))


# In[136]:


math.degrees(3.1415)


# In[138]:


math.radians(180)


# In[140]:


math.acosh(3.14)


# In[141]:


math.erf(0.9)


# In[142]:


math.e


# In[143]:


math.pi


# In[144]:


math.inf


# In[145]:


math.nan


# In[146]:


4 * math.atan(1)


# In[147]:


math.factorial(20)


# In[148]:


math.gcd(3,5)


# In[149]:


math.fsum([1.1,2.2,3.3,4.4,5.5,6.6,7.7,8.8,9.9])


# In[150]:


math.fsum([0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1])


# In[151]:


sum([0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1])


# In[152]:


max([0.9,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1])


# In[153]:


min([0.9,0.1,0.05,0.1,0.1,0.1,0.1,0.1,0.1,0.1])


# In[154]:


from mpmath import *


# In[155]:


x = 0


# In[156]:


y = 0


# In[157]:


z = x / y


# In[158]:


z = math.nan


# In[160]:


z = float('-inf')


# In[161]:


z


# In[162]:


z = z + 1


# In[163]:


z


# In[164]:


z = math.nan


# In[165]:


z += 1


# In[167]:


z = z + 1


# In[169]:


import this


# In[170]:


z


# In[2]:


get_ipython().system('pip3 install mpmath > requirements.txt')


# In[5]:


from mpmath import *


# In[7]:


mp.dps = 10
mp.pretty = True


# In[8]:


4*atan(1)


# In[9]:


mp.dps = 100
mp.pretty = True


# In[10]:


4*atan(1)


# In[11]:


limit(lambda n: (1+1/n)**n, inf)


# In[ ]:




