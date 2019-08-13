import requests

import couchdb

user = "admin"
password = "password"
couchserver = couchdb.Server("http://%s:%s@localhost:5984/" % (user, password))

# for dbname in couchserver:
#     print("Db name....vervproduct ")
#     print(dbname)
dbname = "vervproduct"
if dbname in couchserver:
    db = couchserver[dbname]
else:
    db = couchserver.create(dbname)
# for id in db:
#     print("The ids are ")
#     print (id)

# doc = db["101"]
# print(doc)
# Data to serve with our API


class CouchProvider(object):
    
    def read_product(_id):
        """
        This function responds to a request for /v1.0/product/{_id}
        with one matching person from product
        :product id:   id of the product
        :return:        product matching the result. 
        """
        try:
            doc = db[_id]
            if doc['_id'] == _id:
                del doc['_rev']
                return doc
        except couchdb.http.ResourceNotFound as error:
            return {"error" : "Product with the Id {_id} not found".format(_id=_id)}
        except Exception as error:
            print(error)
            print("Some general exception occured. ")
            return {"error" : "Some error in connection to the database. Please try again later."}
        return {"error" : "Product with the Id {_id} not found".format(_id=_id)}