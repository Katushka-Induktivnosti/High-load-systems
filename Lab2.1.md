Task 1.1
> db.test.insert({"category":"Phone", "model":"iPhone 12", "producer":"Apple", "price":600})
WriteResult({ "nInserted" : 1 })
> db.test.insert({"category":"Phone", "model":"Galaxy Fold", "producer":"Samsung", "price":750})
WriteResult({ "nInserted" : 1 })
> db.test.insert({"category":"TV", "model":"ThinQ", "producer":"LG", "diagonal":55, "price":400})
WriteResult({ "nInserted" : 1 })
> db.test.insert({"category":"TV", "model":"Crystal", "producer":"Samsung", "diagonal":65, "price":550})
WriteResult({ "nInserted" : 1 })
> db.test.insert({"category":"TV", "model":"MotionFlow", "producer":"Sony", "diagonal":50, "price":450})
WriteResult({ "nInserted" : 1 })
> db.test.insert({"category":"Phone", "model":"Redmi Note", "producer":"Xiaomi", "price":300})
WriteResult({ "nInserted" : 1 })
> db.test.insert({"category":"Smart Watch", "model":"Galaxy Watch", "producer":"Samsung", "color":"grey", "price":350})
WriteResult({ "nInserted" : 1 })
> db.test.insert({"category":"Smart Watch", "model":"Series 6", "producer":"Apple", "color":"blue", "price":350})
WriteResult({ "nInserted" : 1 })
> db.test.insert({"category":"Smart Watch", "model":"Fit", "producer":"Huawei", "color":"pink", "price":250})
WriteResult({ "nInserted" : 1 })

Task 1.2

db.test.find().pretty()

{
        "_id" : ObjectId("614718a602fc0aff0ec40ef8"),
        "category" : "Phone",
        "model" : "iPhone 12",
        "producer" : "Apple",
        "price" : 600
}
{
        "_id" : ObjectId("614718c902fc0aff0ec40ef9"),
        "category" : "Phone",
        "model" : "Galaxy Fold",
        "producer" : "Samsung",
        "price" : 750
}
{
        "_id" : ObjectId("61471a2d02fc0aff0ec40efa"),
        "category" : "TV",
        "model" : "ThinQ",
        "producer" : "LG",
        "diagonal" : 55,
        "price" : 400
}
{
        "_id" : ObjectId("61471a7302fc0aff0ec40efb"),
        "category" : "TV",
        "model" : "Crystal",
        "producer" : "Samsung",
        "diagonal" : 65,
        "price" : 550
}
{
        "_id" : ObjectId("61471b1402fc0aff0ec40efc"),
        "category" : "TV",
        "model" : "MotionFlow",
        "producer" : "Sony",
        "diagonal" : 50,
        "price" : 450
}
{
        "_id" : ObjectId("61471b7202fc0aff0ec40efd"),
        "category" : "Phone",
        "model" : "Redmi Note",
        "producer" : "Xiaomi",
        "price" : 300
}
{
        "_id" : ObjectId("61471c0702fc0aff0ec40efe"),
        "category" : "Smart Watch",
        "model" : "Galaxy Watch",
        "producer" : "Samsung",
        "color" : "grey",
        "price" : 350
}
{
        "_id" : ObjectId("61471c3902fc0aff0ec40eff"),
        "category" : "Smart Watch",
        "model" : "Series 6",
        "producer" : "Apple",
        "color" : "blue",
        "price" : 350
}
{
        "_id" : ObjectId("61471c5b02fc0aff0ec40f00"),
        "category" : "Smart Watch",
        "model" : "Fit",
        "producer" : "Huawei",
        "color" : "pink",
        "price" : 250
}

Task 1.3
> db.test.find({"category":"TV"}).count()
3

Task 1.4
> db.getCollection("test").distinct("category").length
3

Task 1.5
> db.test.distinct("producer")
[ "Apple", "Huawei", "LG", "Samsung", "Sony", "Xiaomi" ]

Task 1.6
> db.test.find({$and: [{"category":"Smart Watch"}, {"price":{$gte: 200, $lte: 300}}]})
{ "_id" : ObjectId("61471c5b02fc0aff0ec40f00"), "category" : "Smart Watch", "model" : "Fit", "producer" : "Huawei", "color" : "pink", "price" : 250 }

> db.test.find({$or: [{"model":"Crystal"},{"model":"ThinQ"}]})
{ "_id" : ObjectId("61471a2d02fc0aff0ec40efa"), "category" : "TV", "model" : "ThinQ", "producer" : "LG", "diagonal" : 55, "price" : 400 }
{ "_id" : ObjectId("61471a7302fc0aff0ec40efb"), "category" : "TV", "model" : "Crystal", "producer" : "Samsung", "diagonal" : 65, "price" : 550 }

> db.test.find({"producer": {$in:["Apple", "Samsung"]}})
{ "_id" : ObjectId("614718a602fc0aff0ec40ef8"), "category" : "Phone", "model" : "iPhone 12", "producer" : "Apple", "price" : 600 }
{ "_id" : ObjectId("614718c902fc0aff0ec40ef9"), "category" : "Phone", "model" : "Galaxy Fold", "producer" : "Samsung", "price" : 750 }
{ "_id" : ObjectId("61471a7302fc0aff0ec40efb"), "category" : "TV", "model" : "Crystal", "producer" : "Samsung", "diagonal" : 65, "price" : 550 }
{ "_id" : ObjectId("61471c0702fc0aff0ec40efe"), "category" : "Smart Watch", "model" : "Galaxy Watch", "producer" : "Samsung", "color" : "grey", "price" : 350 }
{ "_id" : ObjectId("61471c3902fc0aff0ec40eff"), "category" : "Smart Watch", "model" : "Series 6", "producer" : "Apple", "color" : "blue", "price" : 350 }

Task 1.7
> db.test.updateMany({"category":"Phone"}, {$set: {"category":"Smartphone"}})
{ "acknowledged" : true, "matchedCount" : 3, "modifiedCount" : 3 }

> db.test.updateMany({"category":"Smartphone"}, {$set: {"diagonal":6}})
{ "acknowledged" : true, "matchedCount" : 3, "modifiedCount" : 3 }

> db.test.find({"category":"Smartphone"})
{ "_id" : ObjectId("614718a602fc0aff0ec40ef8"), "category" : "Smartphone", "model" : "iPhone 12", "producer" : "Apple", "price" : 600, "diagonal" : 6 }
{ "_id" : ObjectId("614718c902fc0aff0ec40ef9"), "category" : "Smartphone", "model" : "Galaxy Fold", "producer" : "Samsung", "price" : 750, "diagonal" : 6 }
{ "_id" : ObjectId("61471b7202fc0aff0ec40efd"), "category" : "Smartphone", "model" : "Redmi Note", "producer" : "Xiaomi", "price" : 300, "diagonal" : 6 }

Task 1.8
> db.test.find({"color":{$exists:true}}).pretty()
{
        "_id" : ObjectId("61471c0702fc0aff0ec40efe"),
        "category" : "Smart Watch",
        "model" : "Galaxy Watch",
        "producer" : "Samsung",
        "color" : "grey",
        "price" : 350
}
{
        "_id" : ObjectId("61471c3902fc0aff0ec40eff"),
        "category" : "Smart Watch",
        "model" : "Series 6",
        "producer" : "Apple",
        "color" : "blue",
        "price" : 350
}
{
        "_id" : ObjectId("61471c5b02fc0aff0ec40f00"),
        "category" : "Smart Watch",
        "model" : "Fit",
        "producer" : "Huawei",
        "color" : "pink",
        "price" : 250
}

Task 1.9
> db.test.updateMany({"color":{$exists:true}}, {$inc: {"price":50}})
{ "acknowledged" : true, "matchedCount" : 3, "modifiedCount" : 3 }

> db.test.find({"color":{$exists:true}}).pretty()
{
        "_id" : ObjectId("61471c0702fc0aff0ec40efe"),
        "category" : "Smart Watch",
        "model" : "Galaxy Watch",
        "producer" : "Samsung",
        "color" : "grey",
        "price" : 400
}
{
        "_id" : ObjectId("61471c3902fc0aff0ec40eff"),
        "category" : "Smart Watch",
        "model" : "Series 6",
        "producer" : "Apple",
        "color" : "blue",
        "price" : 400
}
{
        "_id" : ObjectId("61471c5b02fc0aff0ec40f00"),
        "category" : "Smart Watch",
        "model" : "Fit",
        "producer" : "Huawei",
        "color" : "pink",
        "price" : 300
}
