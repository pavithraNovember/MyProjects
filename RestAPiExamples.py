import requests
import json
api_url = "https://jsonplaceholder.typicode.com/todos/2"
response = requests.get(api_url)

data = response.json()
print(type(data))
#print(type(json_load))
json_load = (json.dumps(response.json(),indent=3))
print(json_load)
#print
print("Writing Indented and Pretty-printed JSON formatted data into a file")

student = {
    "id": 1,
    "name": "Jessa Duggar",
    "class": 9,
    "attendance": 75,
    "subjects": ["English", "Geometry"],
    "email": "jessa@pynative.com"
}

with open("studentWithoutPrettyPrint.json", "w") as write_file:
    json.dump(student, write_file)
print("Done writing JSON data into file without Pretty Printing it")

with open("studentWithPrettyPrint1.json", "w") as write_file:
    json.dump(student, write_file, indent=4)
print("Done writing PrettyPrinted JSON data into file with indent=4")

with open("studentWithPrettyPrint2.json", "w") as write_file:
    json.dump(student, write_file, indent=0)
print("Done writing PrettyPrinted JSON data into file with indent=0")

with open("studentWithPrettyPrint3.json", "w") as write_file:
    json.dump(student, write_file, indent=4, sort_keys=True)
print("Done writing Sorted and PrettyPrinted JSON data into file")
