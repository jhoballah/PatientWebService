from pymodm import connect
from pymodm import MongoModel, fields
from flask import Flask, request, jsonify
app = Flask(__name__)

connect("mongodb://localhost:27017/PatientWebService")


class User(MongoModel):
    name = fields.CharField()
    age = fields.CharField()
    bmi = fields.CharField()

@app.route("/api/new_patient/", methods=['POST'])
def new_patient():

    user_input = request.json

    user_db = User(name=user_input['name'], age=user_input['age'],
                   bmi=user_input['bmi'])
    user_db.save()

    return "i hate myself"


@app.route("/api/average_bmi/<input_age>", methods=['GET'])
def bmi_averaging(input_age):
    bmi_total = 0
    counter = 0
    for user in User.objects.raw({"age": int(input_age)}):

        bmi_total = bmi_total + user.bmi
        counter = counter + 1

    average_bmi = bmi_total / counter

    return jsonify(average_bmi)