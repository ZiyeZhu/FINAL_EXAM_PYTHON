# Task 3: Count vowels in a given string
def count_vowels(text):
    print("\nTask 3: Count Vowels")
    vowels = "aeiou"
    count_dict = {v: 0 for v in vowels}
    total = 0
    for char in text.lower():
        if char in count_dict:
            count_dict[char] += 1
            total += 1
    print(f"Total vowels: {total}")
    for v in vowels:
        print(f"{v}: {count_dict[v]}")

sample_text = "Data is the new oil."  # Clive Humby
count_vowels(sample_text)