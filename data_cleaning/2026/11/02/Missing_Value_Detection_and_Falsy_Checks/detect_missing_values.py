records = [
    {"name": "Bat", "score": "100"},
    {"name": "Dorj", "score": ""},
    {"name": "Suvd", "score": "0"},
    {"name": "Naran", "score": "   "},
]


def is_missing(value: str) -> bool:
  return value.strip() == ""


for r in records:
  score = r["score"]
  r["is_empty"] = score == ""
  r["is_falsy"] = not score
  r["is_missing"] = is_missing(score)

print(records)