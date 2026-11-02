names = [
    "бат дорж",
    "СҮРЭН МАМБЕКОВ",
    "оюун-эрдэнэ цэцэг",
    "mcdonald o'brien",
    "дэлгэр  дорж",
]
result = []
for name in names:
    title_name = name.title()
    cap_name = " ".join(word.capitalize() for word in name.split())
    result.append({
        "orignal" : name,
        "title" : title_name,
        "capitalized": cap_name,
        "is_match": title_name == cap_name,
    })

print(result)
