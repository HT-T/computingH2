import pymongo
client=pymongo.MongoClient("127.0.0.1",27017)

'''access'''
#DB name return LIST,fr client
DBname=client.database_names()

#get DB from client
db=client.get_dataase("ent")

#get collection from db
coll=db.get_collection("movie")

#coll name return LIST,fr a specfic db
collNames=db.collection_names("ent")


'''insert'''
#coll insert, take dict
coll.insert_one({"_id":1,"title":"NMSL","yr":2000})


'''query'''
#use cursor, "result" here
result=coll.find({"genre":"action","year":{"$gt":2016}})
result=coll.find({"genre":{"$exists":False}})
result=coll.find({"genre":{"$in":['action','sitcom']}})

#to print, use cursor; 
for document in result:
    print(document.get("title"))
    print(document)

#can count results
print(result.count())


'''update''' # $set  $unset
#you must have a WHERE && CONDITION
search={'year':{'$gt':2016}}
update={'$set':{'year':2015}}
coll.update_many(search,update)

#to delete certain attri
search={'year':{'$gt':2016}}
update={'$unset':{'year':0}}  #still must pass in a para
coll.update_many(search,update)

'''delete'''
coll.delete_many({'year':2000})
db.drop_collection("ent")


'''import'''
import csv
with open('') as csv_file:
    csv_reader = csv.reader(csv_file,delimiter=',')
    for row in csv_reader:
        coll.insert_one("name":row[0],"age":row[1])

#json
import json
with open('data.json') as file:
    data=json.load(file)
client['ent']['moreusers'].insert_many(data)

client.close()
    








