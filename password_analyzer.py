import re
import secrets
import string


# Common passwords
COMMON_PASSWORDS = {
    "password",
    "123456",
    "12345678",
    "123456789",
    "qwerty",
    "abc123",
    "password123",
    "admin",
    "welcome",
    "letmein"
}


def check_password(password):

    score = 0
    suggestions = []

    # Length check
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
        suggestions.append("Use 12 or more characters.")
    else:
        suggestions.append("Use at least 8 characters.")

    # Lowercase check
    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Add lowercase letters.")

    # Uppercase check
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("Add uppercase letters.")

    # Number check
    if re.search(r"[0-9]", password):
        score += 1
    else:
        suggestions.append("Add numbers.")

    # Special character check
    if re.search(r"[^A-Za-z0-9]", password):
        score += 1
    else:
        suggestions.append("Add special characters such as @, #, $, !.")

    # Common password check
    if password.lower() in COMMON_PASSWORDS:
        score = 0
        suggestions.append(
            "This is a common password. Choose something unique."
        )

    # Repeated characters check
    if re.search(r"(.)\1\1", password):
        score -= 1
        suggestions.append(
            "Avoid repeating the same character three or more times."
        )

    # Prevent negative score
    if score < 0:
        score = 0

    # Strength rating
    if score <= 2:
        strength = "WEAK"
    elif score <= 4:
        strength = "MEDIUM"
    elif score <= 6:
        strength = "STRONG"
    else:
        strength = "VERY STRONG"

    return score, strength, suggestions


def generate_password(length=16):

    characters = (
        string.ascii_letters +
        string.digits +
        "!@#$%^&*"
    )

    password = ""

    for _ in range(length):
        password += secrets.choice(characters)

    return password


def main():

    print("=" * 50)
    print("       PASSWORD STRENGTH ANALYZER")
    print("=" * 50)

    password = input("Enter your password: ")

    score, strength, suggestions = check_password(password)

    print("\n--- PASSWORD ANALYSIS ---")
    print("Length   :", len(password))
    print("Score    :", score)
    print("Strength :", strength)

    if suggestions:

        print("\nSuggestions:")

        for suggestion in suggestions:
            print("- " + suggestion)

    else:
        print("\nExcellent! Your password passed all checks.")

    print("\n--- STRONG PASSWORD ALTERNATIVE ---")

    alternative = generate_password()

    print("Suggested password:", alternative)


if __name__ == "__main__":
    main()