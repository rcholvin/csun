
# coding: utf-8

# In[ ]:


import pymongo

# Connection to Mongo DB
def connectMongo():
    try:
        conn=pymongo.MongoClient()
        print "Connected successfully!!!"
    except pymongo.errors.ConnectionFailure, e:
       print "Could not connect to MongoDB: %s" % e 
    return conn

conn=connectMongo()


                In [6]: conn.database_names()
Out[6]: [u'admin', u'twitter', u'lines', u'local', u'mydb']

                
# In[ ]:

db=conn.twitter


                In [10]: db.collection_names()
Out[10]: [u'lines', u'system.indexes', u'system.users', u'system.profile']
                
# In[ ]:

collection=db.lines


# In[1]:

name_list=['katy perry',
'britney spears',
'taylor swift',
'kim kardashian',
'justin bieber',
'justin timberlake',
 'chris brown',
 'nicki minaj',
 'lady gaga',
 'miley cyrus',
 'beyonce knowles',
 'selena gomez',
 'rihanna',
 'ashton kutcher',
 'ellen gegeneres',
 'cristian oronaldo',
 'oprah winfrey',
 'jennifer lopez',
 'shakira']


# In[17]:

def searchMongo(name,collection, limit=10):
    name=name.split(' ')
    if(len(name)>1):
        first=name[0]
        last=name[1]
    else:
        first=name[0]
        last=''
    line1=r'love.*'+first+' ?'+last
    line2=first+' ?'+last+r'.*love'
    re_exp=re.compile(r'('+line1+r')|('+line2+r')', re.IGNORECASE)
    
    query={'$and':
              [ {'text':re_exp},
                {'text':{'$not':re.compile(r'^.?@'+first+last, re.IGNORECASE)}}]
        }
    
    return list(collection.find(query).limit(limit))


# In[ ]:



