#!/usr/bin/env python
# coding: utf-8

# In[16]:


gKM = input("Enter Kilometers:")
KM = float(gKM)
KMpMile = 1.61
Miles = KM / KMpMile
print("There is %.2f miles"%Miles)


# In[23]:


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

totMins=Min+(Sec/60)
paceTime = totMins/Miles

paceMin = round(paceTime)
paceSec = (paceTime-paceMin)*60
print("\nPace is %.2f mins and"%paceMin)
print("\b%.2f secs"%paceSec)
#miles per hour
totHour = ((Sec/60)+Min)/60
AveSpeed = Miles/totHour
print("\nAve speed is %.2f Miles per hour"%AveSpeed)


# In[ ]:




