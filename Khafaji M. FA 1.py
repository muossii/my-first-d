#!/usr/bin/env python
# coding: utf-8

# In[6]:


gKM = input("Enter Kilometers:")
KM = float(gKM)
KMpMile = 1.61
Miles = KM / KMpMile
print("There is %.2f miles"%Miles)


# In[15]:


print("Calculate your speed!")

gSec = input("Enter seconds elapsed:")
gMin = input("Enter minutes elapsed:")
gKM = input("Enter Kilometers ran:")

#conversion to float
Sec = int(gSec)
Min = int(gMin)
KM = float(gKM)

#conversion to miles
Miles = KM/1.61

print("\n%.2f Miles in"%Miles)
print("%d Mins"%Min)
print("and %d secs\n\n"%Sec)

#miles per hour
totHour = ((Sec/60)+Min)/60
AveSpeed = Miles/totHour
print("%.2f Miles per hour"%AveSpeed)


# In[ ]:




