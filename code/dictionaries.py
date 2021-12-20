"""part1

dict_one = {
    "id": 1,
    "name": "Carlos Souza",
}

dict_two = {
    "skills": ["Python", "DS&A", "Django", "D.S.", "Work with Software Development"],
    "college": "IFAM",
}

dict_three = {
    "city": "Manaus",
    "country": "Brasil"
}

merged_dict = dict_one

for key, value in dict_two.items():
    merged_dict[key] = value

for key, value in dict_three.items():
    merged_dict[key] = value

print(merged_dict)
"""

"""part2
dict_one = {
    "id": 1,
    "name": "Carlos Souza",
    "skills": ["Python", "DS&A", "Django", "D.S.", "Work with Software Development"],
}

dict_two = {
    "college": "IFAM",
    "city": "Manaus",
    "country": "Brasil"
}

dict_one.update(dict_two)

print(dict_one)
"""

"""part3
dict_one = {
    "id": 1,
    "name": "Carlos Souza",
}

dict_two = {
    "skills": ["Python", "DS&A", "Django", "D.S.", "Work with Software Development"],
    "college": "IFAM",
}

dict_three = {
    "city": "Manaus",
    "country": "Brasil"
}

dict_one.update(dict_two)
print(dict_one)
# Output: {'id': 1, 'name': 'Carlos Souza', 'skills': ['Python', 'DS&A', 'Django', 'D.S.', 'Work with Software Development'], 'college': 'IFAM'}

dict_one.update(dict_three)
print(dict_one)
# Output: {'id': 1, 'name': 'Carlos Souza', 'skills': ['Python', 'DS&A', 'Django', 'D.S.', 'Work with Software Development'], 'college': 'IFAM', 'city': 'Manaus', 'country': 'Brasil'}
"""

"""part4
dict_one = {
    "id": 1,
    "name": "Carlos Souza",
}

dict_two = {
    "skills": ["Python", "DS&A", "Django", "D.S.", "Work with Software Development"],
    "college": "IFAM",
}

dict_three = {
    "city": "Manaus",
    "country": "Brasil"
}

merged_dict = {**dict_one, **dict_two, **dict_three}
print(merged_dict)

# Output: {'id': 1, 'name': 'Carlos Souza', 'skills': ['Python', 'DS&A', 'Django', 'D.S.', 'Work with Software Development'], 'college': 'IFAM', 'city': 'Manaus', 'country': 'Brasil'}
"""

dict_one = {
    "id": 1,
    "name": "Carlos Souza",
}

dict_two = {
    "skills": ["Python", "DS&A", "Django", "D.S.", "Work with Software Development"],
    "college": "IFAM",
}

dict_three = {
    "city": "Manaus",
    "country": "Brasil"
}

merged_dict = dict_one | dict_two | dict_three
print(merged_dict)
