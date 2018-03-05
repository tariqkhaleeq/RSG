
# coding: utf-8

# In[11]:

from bs4 import BeautifulSoup
import urllib2
import pandas as pd


# In[2]:

#Should find URL from src of iframe.
iframe_url='https://www.iscb.org/cms_addon/events/display.php?t=all'
page = urllib2.urlopen(iframe_url)
soupthis= BeautifulSoup(page,"html.parser")


# In[40]:

print(soupthis.prettify())


# In[26]:

# Using pandas to convert table into dataframe
# Works for looking but no link!
tableInIframe=pd.read_html(iframe_url)[0]


# In[33]:

#tableInIframe[tableInIframe.Country!="United States"]


# In[81]:

#print soupthis.a['href']
hrefLinks=[]
for ahref in soupthis.find_all('a', href=True):
    #print "Found the URL:", ahref['href']
    hrefLinks.append(ahref['href'])

#print pd.DataFrame(hrefLinks)
#print tableInIframe.shape

# merge both
tableInIframe["Links"]=hrefLinks


# In[82]:

tableInIframe


# In[83]:

# TODO: add it to HTML code


# In[ ]:
