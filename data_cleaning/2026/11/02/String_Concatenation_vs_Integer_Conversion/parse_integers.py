a = "100"
b = "200"
spaced_val = "  100  "
empty_val = ""

concat_result = a + b
sum_result = int(a) + int(b)
parsed_spaced = int(spaced_val)

try:
    parsed_empty = int(empty_val)
except ValueError as e:
    parsed_empty = f"ValueError: {e}"

print(f"concat: {concat_result} (type: {type(concat_result).__name__})")
print(f"sum:    {sum_result} (type: {type(sum_result).__name__})")
print(f"spaced: {parsed_spaced} (type: {type(parsed_spaced).__name__})")
print(f"empty:  {parsed_empty}")