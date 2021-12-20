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
    "country": "Amazonas"
}

merged_dict = dict_one

for key, value in dict_two.items():
    merged_dict[key] = value

for key, value in dict_three.items():
    merged_dict[key] = value

print(merged_dict)
