#!/usr/bin/env python
# coding: utf-8

# In[5]:


from pymongo import MongoClient
from bson.objectid import ObjectId


class AnimalShelter(object):
        """ CRUD operations for Animal collection in MongoDB"""
        
        def _init_(self):
            USER = 'aacuser'
            PASS = 'animals'
            HOST = 'nv-desktop-services.apporto.com'
            PORT = 31338
            DB = 'aac'
            COL = 'animals'
            
            self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
            self.database = self.client['%s' & (DB)]
            self.collection = self.database['%s' % (COL)]

 # Complete this create method to implement the C in CRUD.           
        def create(self, data):
            if data is not None:
                insertSuccess = self.database.animals.insert(data) #data should be in the dictionary
                #Check insertSuccess for operation
                if insertSuccess !=0:
                    return False
                # default return
                return True
            else:
                raise Exception("Nothing to save, because data parameter is empty")

# Complete this create method to implement the R in CRUD.
        def read(self, searchData):
            if searchData:
                data = self.database.animals.find(searchData, {"_id": False})
            else: 
                data = self.database.animals.find( {}, {"_id": False})
            # Return the dataset else, let the error flow up
            return data

# Complete this create method to implement the U in CRUD.        
        def update(self, searchData, updateData):
            if searchData is not None:
                result = self.database.animals.update_many(searchData, { "$set": updateData})
            else: 
                return "{}"
            # return the dataset else, let the error flow up
            return result.raw_result

# Complete this create method to implement the D in CRUD.
        def delete(self, deleteData):
            if deleteData is not None:
                result = self.database.animals.delete_many(deleteDate)
            else:
                return "{}"
            # Return the dataset els let the error flow up
            return result.raw_result


# In[ ]:




