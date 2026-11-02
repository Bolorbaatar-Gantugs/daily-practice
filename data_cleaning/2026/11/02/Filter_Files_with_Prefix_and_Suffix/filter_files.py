files = [
    "tailan_2024.csv",
    "tailan_2024.csv.bak",
    "TAILAN_2023.CSV",
    "salbar_tailan.csv",
    "tailan.csv",
    "tailan_2024",
]


# 1. Байрлал ба үсгийн том жижгийг шалгах функц
def is_valid_report(filename: str) -> bool:
  name = filename.lower()
  return name.startswith("tailan") and name.endswith(".csv")


# 2. Шалгуурт нийцсэн жинхэнэ тайлангууд
valid_files = [f for f in files if is_valid_report(f)]

# 3. in операторын хуурамч илэрцийг тооцоолох
in_matches = [f for f in files if "tailan" in f.lower() and ".csv" in f.lower()]
false_positives = [f for f in in_matches if f not in valid_files]

# 4. Үр дүнг хэвлэх
print("Зөв тайлангууд:", valid_files)
print("Хуурамч илэрцүүд (False Positives):", false_positives)