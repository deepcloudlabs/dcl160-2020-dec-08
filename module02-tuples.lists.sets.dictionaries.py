#!/usr/bin/env python
# coding: utf-8

# ### DCL-160: Python Programming
# 
# Module 02
# 
# December 08, 2020
# 
# Binnur Kurt <binnur.kurt@gmail.com>

# In[1]:


names = ("jack","kate","ben","sun","jin","james") # tuple -> immutable


# In[2]:


names[0]


# In[3]:


names[3]


# In[4]:


names[3] = "sunny"


# In[5]:


print(names)


# In[7]:


type(names)


# In[8]:


len(names)


# In[9]:


type(names[0])


# In[10]:


len(names)


# In[11]:


len(names[0])


# In[12]:


x= 3.1415
str(x)


# In[13]:


str(names)


# In[14]:


sales = ("jack", "james")
it = ("jin", "ben", "hugo")
hr = ("sun")
finance = ("kate", "ben")


# In[15]:


employees = (sales, it, hr, finance)


# In[16]:


employees


# In[17]:


len(employees)


# In[18]:


employees[0]


# In[19]:


len(employees[0])


# In[20]:


numbers = (4,8,15,16,23,42)


# In[21]:


numbers[0]


# In[22]:


numbers[len(numbers)-1]


# In[24]:


numbers[-2]


# In[26]:


numbers[-6]


# In[27]:


numbers[0]


# In[28]:


numbers[-7]


# In[29]:


numbers[6]


# In[30]:


numbers = [4,8,15,16,23,42] # list


# In[31]:


numbers[0]


# In[32]:


numbers[-1]


# In[33]:


numbers[0] = numbers[0] + 10


# In[34]:


len(numbers)


# In[35]:


numbers.append(108)


# In[36]:


len(numbers)


# In[37]:


numbers


# In[39]:


names = ["jack", "james", "jin"]


# In[40]:


len(names)


# In[41]:


names[0]


# In[42]:


names[0] = "ben" 


# In[43]:


names


# In[44]:


names.append("kim")


# In[45]:


names


# In[46]:


employees = [('jack','bauer', 10000),('kate','austen',20000)]


# In[48]:


salary = employees[1][2]


# In[49]:


employees[1] = ('kate','austen', salary * 1.10 )


# In[50]:


employees


# In[51]:


employees.append(("ben","linus",50000))


# In[52]:


employees


# In[53]:


employees = [['jack','bauer', 10000],['kate','austen',20000]]


# In[54]:


employees = [[('jack','bauer'), 10000],[('kate','austen'),20000]]


# In[55]:


employees[0]


# In[56]:


employees[-1]


# In[59]:


employees.extend([[('jin','kwon'), 20000],[('sun','kwon'),40000]])


# In[60]:


employees


# In[62]:


jack = ("jack", "bauer", 1956, 25000, True)


# In[63]:


first_name = jack[0]
last_name = jack[1]
birth_year = jack[2]
salary = jack[3]
fulltime = jack[-1]


# In[64]:


first_name, last_name, birth_year, salary , fulltime = jack


# In[65]:


first_name


# In[66]:


fulltime


# In[67]:


x = 3
y = 5


# In[68]:


y , x = (x, y)


# In[69]:


y


# In[70]:


x


# In[71]:


meyveler = ["elma", "armut", "kavun", "karpuz", "muz"]


# In[73]:


meyveler[-6]


# In[75]:


list(enumerate(meyveler))


# In[76]:


tuple(enumerate(meyveler))


# In[78]:


for t in enumerate(meyveler):
    index = t[0]
    meyve = t[1]
    print(f"{index} -> {meyve}")


# In[79]:


for t in enumerate(meyveler):
    print(f"{t[0]} -> {t[1]}")


# In[80]:


for index, meyve in enumerate(meyveler):
    print(f"{index} -> {meyve}")


# In[81]:


for index, meyve in enumerate(meyveler):
    print("%d -> %s" % (index,meyve) )


# In[82]:


meyveler[0:3]


# In[83]:


meyveler[:2]


# In[84]:


meyveler[3:]


# In[85]:


meyveler[:]


# In[87]:


numbers = [0,1,2,3,4,5,6,7,8,9,10]


# In[88]:


numbers[4:8]


# In[89]:


numbers[:8]


# In[91]:


numbers[4::2]


# In[101]:


numbers[::-5]


# In[97]:


numbers[0:10:-1]


# In[96]:


numbers[10:0:-1]


# In[104]:


numbers[7:3:-1]


# In[106]:


numbers[7:3:1]


# In[107]:


numbers[3:7] = [6,5,4,3]


# In[108]:


numbers


# In[109]:


numbers[3:7] = []


# In[110]:


numbers


# In[111]:


numbers[:] = []


# In[113]:


numbers


# In[114]:


numbers = list(range(20))


# In[115]:


numbers


# In[116]:


numbers.pop(5)


# In[117]:


numbers


# In[119]:


numbers.pop(-1)


# In[120]:


numbers.pop(100)


# In[130]:


names = ["jack", "kate" ,"james", "jin","hugo", "james"]


# In[124]:


names.remove("james")


# In[125]:


names


# In[127]:


names.remove("james")


# In[128]:


names.clear()


# In[129]:


names


# In[135]:


names = ["jack", "kate" ,"james", "jin","hugo", "sun"]


# In[136]:


del names[-1]


# In[137]:


names


# In[138]:


del names[-1]


# In[140]:


names


# In[142]:


del names[:2]


# In[143]:


names


# In[144]:


del names[:]


# In[145]:


names


# In[146]:


# how to modify/remove list: clear(), pop(index), remove(element), del


# In[147]:


names = ["jack", "kate" ,"james", "jin","hugo", "sun"]


# In[148]:


names.sort()


# In[149]:


names


# In[150]:


names.sort(reverse=True)


# In[151]:


names


# In[155]:


numbers = [42,8,15,16,23,4]


# In[156]:


numbers.sort()


# In[157]:


numbers


# In[158]:


numbers.sort(reverse=True)


# In[159]:


numbers


# In[160]:


numbers_asc = sorted(numbers)


# In[161]:


numbers_asc


# In[162]:


numbers


# In[166]:


names = ["jack", "kate" ,"james", "Jin","Hugo", "Sun"]


# In[167]:


names


# In[168]:


sorted(names)


# In[169]:


sorted(names, key= str.lower)


# In[176]:


stocks = [('msft', 100., 500), ('ibm', 90.0, 1000), ('gogle', 220., 10)]


# In[171]:


sorted(stocks)


# In[172]:


def get_price(stock):
    return stock[1]


# In[173]:


sorted(stocks, key= get_price, reverse=True)


# In[174]:


def get_volume(stock):
    return stock[1]*stock[2]


# In[177]:


sorted(stocks, key= get_volume, reverse=True)


# In[178]:


sorted(stocks, key= lambda stock: stock[1]*stock[2], reverse=True)


# In[179]:


get_volume2 = lambda stock: stock[1]*stock[2]


# In[180]:


sorted(stocks, key= get_volume2, reverse=True)


# In[ ]:




