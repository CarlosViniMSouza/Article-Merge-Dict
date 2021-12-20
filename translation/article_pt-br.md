# Como mesclar dicionários em Python

## Artigo por: Ashutosh Krishna

![Logo_Article](https://www.freecodecamp.org/news/content/images/size/w2000/2021/12/Black-Moon-Blog-Banner--1--1.png)

### Em Python, um dicionário é uma coleção que você usa para armazenar dados em pares `{chave: valor} ({key: value})`. É ordenado e mutável e não pode armazenar dados duplicados.

### Escrevemos um dicionário usando chaves como este:

```python
my_dict = {
    "id": 1,
    "name": "Carlos Souza",
    "skills": ["Python", "DS&A", "Django", "D.S.", "Work with Software Development"]
}
```

### Às vezes, precisamos mesclar dois ou mais dicionários para criar um dicionário maior. Por exemplo:

```python
dict_one = {
    "id": 1,
    "name": "Carlos Souza",
    "skills": ["Python", "DS&A", "Django", "D.S.", "Work with Software Development"]
}

dict_two = {
    "college": "IFAM",
    "city": "Manaus",
    "country": "Brasil"
}

merged_dict = {
    "id": 1,
    "name": "Carlos Souza",
    "skills": ["Python", "DS&A", "Django", "D.S.", "Work with Software Development"],
    "college": "IFAM",
    "city": "Manaus",
    "country": "Brasil"
}
```

### Em `merged_dict`, temos os pares de valores-chave de `dict_one` e `dict_two`. Isso é o que desejamos alcançar programaticamente.

### Existem várias maneiras de fazer isso em Python:

1 - Usando um loop for

2 - Usando o método `dict.update()`

3 - Usando o operador `**`

4 - Usando o `|` Operador (União) (para Python 3.9 e superior)

### Vamos explorar cada caminho um após o outro.

## Como mesclar dicionários em Python usando um loop for:

### Podemos mesclar dois ou mais dicionários usando o loop for como este:

```python
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
Output:

{'id': 1, 'name': 'Carlos Souza', 'skills': ['Python', 'DS&A', 'Django', 'D.S.', 'Work with Software Development'], 'college': 'IFAM', 'city': 'Manaus', 'country': 'Brasil'}
"""
```

### Mas o problema com esse método é que precisamos executar muitos loops para mesclar os dicionários.

### Então, qual é a outra opção?

## Como mesclar dicionários em Python usando o método `dict.update()`:

### Se você explorar a classe `dict`, existem vários métodos dentro dela. Um desses métodos é o método `update()`, que você pode usar para mesclar um dicionário em outro.

```python
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
Output:

{'id': 1, 'name': 'Carlos Souza', 'skills': ['Python', 'DS&A', 'Django', 'D.S.', 'Work with Software Development'], 'college': 'IFAM', 'city': 'Manaus', 'country': 'Brasil'}
"""
```

### Mas o problema quando usamos o método `update()` é que ele modifica um dos dicionários. Se quisermos criar um terceiro dicionário sem modificar nenhum dos outros dicionários, não podemos usar este método.

### Além disso, você só pode usar esse método para mesclar dois dicionários por vez. Se você deseja mesclar três dicionários, primeiro você precisa mesclar os dois primeiros e, em seguida, mesclar o terceiro com o dicionário modificado.

```python
dict_one = {
    "id": 1,
    "name": "Ashutosh",
}

dict_two = {
    "books": ["Python", "DSA"],
    "college": "NSEC",
}

dict_three = {
    "city": "Kolkata",
    "country": "India"
}

dict_one.update(dict_two)
print(dict_one)
# Output: {'id': 1, 'name': 'Carlos Souza', 'skills': ['Python', 'DS&A', 'Django', 'D.S.', 'Work with Software Development'], 'college': 'IFAM'}

dict_one.update(dict_three)
print(dict_one)
# Output: {'id': 1, 'name': 'Carlos Souza', 'skills': ['Python', 'DS&A', 'Django', 'D.S.', 'Work with Software Development'], 'college': 'IFAM', 'city': 'Manaus', 'country': 'Brasil'}
```

### Vamos explorar algumas outras opções.