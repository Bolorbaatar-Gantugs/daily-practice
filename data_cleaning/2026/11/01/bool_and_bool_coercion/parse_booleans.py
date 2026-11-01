records = [
    {"name": "Бат", "active": "true", "age": 25},
    {"name": "Дорж", "active": "True", "age": 0},
    {"name": "Сувд", "active": "1", "age": -5},
    {"name": "Марал", "active": "", "age": 150},
    {"name": "Номин", "active": "false", "age": 30},
]

TRUE_VALUES = {"true", "1", "yes", "y", "тийм"}
FALSE_VALUES = {"0", "false", "no", "n", "үгүй",""}

def parse_booleans(value):
    value = value.strip().lower()
    if value in TRUE_VALUES:
        return True
    if value in FALSE_VALUES:
        return False
    raise ValueError("Invalid boolean value")

for record in records:
    record["active"] = parse_booleans(record["active"])
    record["is_valid"] = 0 <= record["age"] <= 120

    print(record)