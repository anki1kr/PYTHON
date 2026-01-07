def guessNum(start, end):
    # base case: range khatam
    if start > end:
        return True   # couldn't guess

    mid = (start + end) // 2
    print(f"Is your number {mid}? (Y/N)")
    ans = input().strip().lower()

    if ans == "y": 
        print("🎉 Congratulations! Number guessed correctly.")
        return False

    elif ans == "n":
        print(f"Is your number greater than {mid}? (Y/N):",end=" ")
        ans = input().strip().lower()

        if ans == "y":
            return guessNum(mid + 1, end)
        elif ans == "n":
            return guessNum(start, mid - 1)
        else:
            print("Invalid input. Please enter Y or N.")
            return guessNum(start, end)

    else:
        print("Invalid input. Please enter Y or N.")
        return guessNum(start, end)

print("--- Number Guessing Game ---")
start = int(input("Enter start range = "))
end = int(input("Enter end range = "))

print(f"\nThink of a number between {start} and {end}")
out = guessNum(start, end)

if out:
    print("❌ Couldn't guess it. Are you sure you answered correctly?")
