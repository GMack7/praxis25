import json

rocky = {"name": "Rocky", "owner": "Shane", "breed": "Texas Heeler",
         "likes": ["vocalizing", "eating disgusting garbage", "cats"]}
maple = {"name": "Maple", "owner":"Amanda", "breed": "Hound","likes":["zoomies","looking"]}
bofur = {"name": "Bofur", "owner":"Ronda", "breed": "Corgi","likes":["ladies"]}
dogs = [rocky,maple,bofur]

with open('dogs.json', mode="w") as jsonfile:
    jsonfile.write(json.dumps(dogs))

with open('dogs.json', mode="r") as jsonfile:
    dogs_load = json.loads(jsonfile.read())
    for dog in dogs_load:
        print(dog["name"],"and",dog["owner"])