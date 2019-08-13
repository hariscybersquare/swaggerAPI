import requests

import couchdb

user = "admin"
password = "password"
couchserver = couchdb.Server("http://%s:%s@localhost:5984/" % (user, password))

dbname = "vervproduct"
if dbname in couchserver:
    db = couchserver[dbname]
else:
    db = couchserver.create(dbname)

#Sample data :
doc1 = {
    "_id": "101",
    "pname": "Apple",
    "cateory": "computer",
    "quantity": 100
}

doc2 = {
    "_id": "102",
    "pname": "Apple2",
    "cateory": "computer2",
    "quantity": 200
}

doc3 = {
    "_id": "103",
    "pname": "Apple3",
    "cateory": "computer3",
    "quantity": 300
}
try:
    db.save(doc1)
except Exception as error:
    print("error is ", error)
    print("Mostly this error will happen when the document is already created.")

try:
    db.save(doc2)
except Exception as error:
    print("error is ", error)
    print("Mostly this error will happen when the document is already created.")

try:
    db.save(doc3)
except Exception as error:
    print("error is ", error)
    print("Mostly this error will happen when the document is already created.")
    
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