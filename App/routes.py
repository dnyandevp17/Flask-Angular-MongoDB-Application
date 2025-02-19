from project1 import app, mongodb_local, cors
from flask import jsonify, request, redirect, url_for
from flask_cors import cross_origin
 
# Retrieve all data
@app.route("/", methods=["GET"])
@cross_origin()
def retrieveData():
    holder = []
    currentCollection = mongodb_local.db.PersonalInfo
    for i in currentCollection.find():
        holder.append({
            "Name": i.get("Name", "N/A"),
            "Company": i.get("Company", "N/A"),
            "Domain": i.get("Domain", "N/A")
        })
    return jsonify(holder)
 
# Retrieve specific data by name
@app.route("/<name>", methods=["GET"])
@cross_origin()
def retrieveFromName(name):
    currentCollection = mongodb_local.db.PersonalInfo
    data = currentCollection.find_one({"Name": name})
    
    if data:
        return jsonify({
            "Name": data.get("Name"),
            "Company": data.get("Company"),
            "Domain": data.get("Domain")
        })
    else:
        return jsonify({"error": "Name not found"})
 
# Insert new data
@app.route("/postData", methods=["POST"])
@cross_origin()
def postData():
    currentCollection = mongodb_local.db.PersonalInfo
    name = request.json.get("Name")
    company = request.json.get("Company")
    domain = request.json.get("Domain")
 
 
    currentCollection.insert_one({
        "Name": name,
        "Company": company,
        "Domain": domain
    })
    return jsonify({
        "Name": name,
        "Company": company,
        "Domain": domain
        })
 
# Delete data by name
@app.route("/deleteData/<name>", methods=["DELETE"])
@cross_origin()
def deleteData(name):
    currentCollection = mongodb_local.db.PersonalInfo
    result = currentCollection.delete_one({"Name": name})
    
    if result.deleted_count > 0:
        return jsonify({"message": "Data deleted successfully"})
    else:
        return jsonify({"error": "Name not found"})
 
# Update data by name
@app.route("/updateData/<name>", methods=["PUT"])
@cross_origin()
def updateData(name):
    currentCollection = mongodb_local.db.PersonalInfo
    updated_name = request.json.get("Name", None)
    
    if not updated_name:
        return jsonify({"error": "New name is required"})
    
    result = currentCollection.update_one({"Name": name}, {"$set": {"Name": updated_name}})
    
    if result.matched_count > 0:
        return jsonify({"message": "Data updated successfully"})
    else:
        return jsonify({"error": "Name not found"})