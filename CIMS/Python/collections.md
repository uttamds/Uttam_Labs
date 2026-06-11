### List

A list stores multiple values and can be changed.

```python
cities = ["Mumbai", "Pune", "Delhi"]

print(cities)

cities.append("Chennai")
print(cities)

cities.remove("Pune")
print(cities)
```

---

### Tuple

A tuple stores multiple values but cannot be changed.

```python
coordinates = (10, 20)

print(coordinates)
print(coordinates[0])
print(coordinates[1])
```

---

### Dictionary

A dictionary stores data as key-value pairs.

```python
student = {
    "name": "Rahul",
    "course": "Python",
    "marks": 85
}

print(student)

print(student["name"])

student["marks"] = 90
print(student)
```

---

### Quick Comparison

```python
my_list = ["Python", "Java"]
my_tuple = ("Python", "Java")
my_dict = {"course": "Python", "duration": 30}

print(my_list)
print(my_tuple)
print(my_dict)
```

* **List** → Ordered, changeable
* **Tuple** → Ordered, not changeable
* **Dictionary** → Key-value pairs (`key : value`)
