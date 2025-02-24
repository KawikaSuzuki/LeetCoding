from collections import Counter

def canConstruct(ransomNote: str, magazine: str) -> bool:
    ransom_count = Counter(ransomNote)  # Count letters in ransomNote
    magazine_count = Counter(magazine)  # Count letters in magazine

    for char, count in ransom_count.items():
        # Check if magazine has enough letters like if mag has 2 a's we need to see if it has enough for 2 a's in ransom
        if magazine_count[char] < count:
            return False
    return True

# Example test cases
ransomNote = "aa"
magazine = "aab"

print(canConstruct(ransomNote, magazine))  # Expected output: True

ransomNote = "aaa"
magazine = "aab"

print(canConstruct(ransomNote, magazine))  # Expected output: False
