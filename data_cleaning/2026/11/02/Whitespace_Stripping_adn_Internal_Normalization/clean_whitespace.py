names = ["Бат", " Бат", "Бат ", "  Бат  ", "\tБат", "Бат"]
internal_spaced_name = "Бат   Дорж"

# 1. Анхны өгөгдлийн unique тоо
raw_unique = len(set(names))

# 2. strip, lstrip, rstrip хийсний дараах unique тоо
strip_unique = len({n.strip() for n in names})
lstrip_unique = len({n.lstrip() for n in names})
rstrip_unique = len({n.rstrip() for n in names})

# 3. Үг хоорондын зайг хэвийн болгох
normalized_name = " ".join(internal_spaced_name.split())

# 4. Dictionary үүсгэж хэвлэх
results = {
    "raw_unique": raw_unique,
    "strip_unique": strip_unique,
    "lstrip_unique": lstrip_unique,
    "rstrip_unique": rstrip_unique,
    "normalized_name": normalized_name,
}

print(results)