from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD OPERATIONS FOR MONGODB"""
    def __init__(self, username, password):
        
        # init to connect to mongodb without authentication
        #self.client = MongoClient('mongodb://localhost:46602')
        
        # init to connect with authentication
        self.client = MongoClient('mongodb://%s:%s@localhost:46602/?authMechanism=DEFAULT&authSource=AAC'%(username,password))
        self.database = self.client['AAC']
       
                                  
    # create method                              
    def create(self,data):
        if data is not None:
            self.database.animals.insert(data)
        else:
            raise Exception("Nothing to save")
                            
    # read method                       
    def read_all(self,data):
        cursor = self.database.animals.find(data, {'_id':False})
        return cursor               
        
    def read(self,data):
        return self.database.animals.find_one(data) #returns item as a py dictionary                    