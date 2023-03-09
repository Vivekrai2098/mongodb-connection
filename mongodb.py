import pymongo
if __name__=="__main__":
    print("welcome\n")
    client=pymongo.MongoClient("mongodb://localhost:27017")
    database=client["python_dbs"]
    collection=database["pytable"]



# this is single inseretion in mongodb
    distionary={"name":"rahul","age":23,"address":"new delhi india"}
    val=collection.insert_one(distionary)

# this is many insertion data in one time in mongodb
    data=[
        {"name":"sanju","age":12},
        {"name": "mohan", "age": 55},
        {"name": "sumit", "age": 36},
        {"name": "parmod", "age": 90},
        {"name": "sanjeev", "age": 67}
        ]
    collection.insert_many(data)


# also alloacte your own primary key data in mongo db
    distionary={"_id":1,"name":"one","age":23,"address":"new one street one id delhi india"}
    val=collection.insert_one(distionary)
#
# also alloacte your many own primary key data in mongo db id
    data = [
            {"_id":2,"two":"sanju","age":12},
            {"_id":3,"three": "mohan", "age": 55},
            {"_id":4,"four": "sumit", "age": 36},
            {"_id":5,"five": "parmod", "age": 90},
            {"_id":6,"six": "sanjeev", "age": 67}
            ]
    collection.insert_many(data)


# find all the data in django data base
    one=collection.find()
    a=0
    for i in one:
        a=a+1
        print(i)
    print("the total row in database is ",a)

#show all the database in mongodb
    alldatabase=client.list_database_names()
    print(alldatabase)



# show all database collection/table in mongodb
    print(database.list_collection_names())



# update the data on database
    ch={"_id":6}
    nextt={"$set":{"age":70}}
    collection.update_one(ch,nextt)


#this is the delete the data in database
    data1={"name":"rahul"}
    collection.delete_many(data1)




#this is the condition check the data insert or not in mongodb
    if(bool(val)==True):
        print("insert succefully")
    else:
        print("this not add ")

