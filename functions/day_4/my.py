myself = {
    "name": "Tejaswini",
    "age": 19,
    "branch": "AIML",
    "college": "SIMATS",
    "CGPA": 8.62
    }
print(myself)
print(myself["name"])
myself.update({"CGPA": "9.0"})
print(myself)
myself["city"] = "chennai"
print(myself)
print(myself.keys())
print(myself.values())
del myself["age"]
print(myself)