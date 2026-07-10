student = {
    "name": "Tejaswini",
    "age": 18,
    "marks": 92 
}
print(student)
student["city"] = "chennai"
print(student)
student["age"] = 19
print(student.keys())
print(student.values())
student.pop("marks")
print(student)
print(student.get("phone"))
student.update({"branch": "CSE"})
print(student)