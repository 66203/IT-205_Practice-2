def count_character_frequency(string):
    frequency = {}

    for char in string:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

    return frequency

def print_character_frequency(frequency):
    print("Character frequency:")
    for char, count in frequency.items():
        print(f"{char}: {count}")

def main():
    user_input = input("Enter a string: ")
    character_frequency = count_character_frequency(user_input)
    print_character_frequency(character_frequency)

if __name__ == "__main__":
    main()
