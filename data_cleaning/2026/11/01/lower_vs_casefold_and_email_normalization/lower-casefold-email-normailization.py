data = [
    "Bob@EXAMPLE.YN",
    "bob@example.yn",
    "BOB@EXAMPLE.YN",
    "Болд",
    "болд",
    "БОЛД",
]

print("Unique:", len(set(data)))

lower_set = set(text.lower() for text in data)
casefold_set = set(text.casefold() for text in data)

print("lower:", len(lower_set))
print("Casefold:", len(casefold_set))

print("\n'ß' тэмдэгт дээрх ялгаа:")
print(
    "'STRASSE'.lower() == 'straße'.lower():",
    "STRASSE".lower() == "straße".lower(),
)  # False ('strasse' != 'straße')
print(
    "'STRASSE'.casefold() == 'straße'.casefold():",
    "STRASSE".casefold() == "straße".casefold(),
)  # True ('strasse' == 'strasse')

def normalize_email(email: str) -> str:
    if "@" not in email:
        return email
    username, sep, domain = email.rpartition("@")
    return f"{username}@{domain.lower()}"

print("\nEmail normalization үр дүн:")
emails = ["Bob@EXAMPLE.YN", "bob@example.yn", "BOB@EXAMPLE.YN"]
for email in emails:
    print(f"  {email} -> {normalize_email(email)}")