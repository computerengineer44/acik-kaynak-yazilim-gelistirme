from flask import Flask, request, jsonify
from flask_restful import Api, Resource
import pandas as pd

app = Flask(__name__)
api = Api(app)

class Missiles(Resource):
    def get(self):
        data = pd.read_csv('Missiles by country.csv')
        data = data.to_dict('records')
        return {'data': data}, 200

    def post(self):
        req_data = request.get_json()

        missile_name = req_data.get('missile_name')
        country = req_data.get('country')
        distance = req_data.get('distance')

        if not all([missile_name, country, distance]):
            return {'message': 'Incomplete data'}, 400

        new_missile = pd.DataFrame({
            'missile_name': [missile_name],
            'country': [country],
            'distance': [distance]
        })

        try:
            data = pd.read_csv('Missiles by country.csv')
            data = data.append(new_missile, ignore_index=True)
            data.to_csv('Missiles by country.csv', index=False)
            return {'message': 'Record successfully added.'}, 200
        except Exception as e:
            return {'message': str(e)}, 500

api.add_resource(Missiles, '/missiles')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=6767)
