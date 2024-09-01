import re

def assess_password_strength(password):
    # Criteria for password strength
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    number_criteria = re.search(r'[0-9]', password) is not None
    special_char_criteria = re.search(r'[\W_]', password) is not None
    
    # Calculate the score
    score = sum([length_criteria, uppercase_criteria, lowercase_criteria, number_criteria, special_char_criteria])
    
    # Determine strength level
    if score == 5:
        strength = "Very Strong"
    elif score == 4:
        strength = "Strong"
    elif score == 3:
        strength = "Moderate"
    elif score == 2:
        strength = "Weak"
    else:
        strength = "Very Weak"
    
    return {
        "length_criteria": length_criteria,
        "uppercase_criteria": uppercase_criteria,
        "lowercase_criteria": lowercase_criteria,
        "number_criteria": number_criteria,
        "special_char_criteria": special_char_criteria,
        "score": score,
        "strength": strength
    }

# Example usage
password = "Password123!"
result = assess_password_strength(password)
print(f"Password: {password}")
print(f"Strength: {result['strength']}")
print("Criteria met:")
print(f"  Length >= 8: {result['length_criteria']}")
print(f"  Uppercase letter: {result['uppercase_criteria']}")
print(f"  Lowercase letter: {result['lowercase_criteria']}")
print(f"  Number: {result['number_criteria']}")
print(f"  Special character: {result['special_char_criteria']}")
