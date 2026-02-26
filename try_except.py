try:
    num1 = int(input("Enter the number 1: "))
    num2 = int(input("Enter the number 2: "))

    result = num1/num2
    print(f"Result: {result}")

except ValueError:
    print("Error: you must enter a valid number, not text!")

except ZeroDivisionError:
    print("❌ Error: You cannot divide by zero! Math doesn't work like that.")

except Exception as e:
    print(f"❌ An unexpected error occurred: {e}")

finally:
    print("✅ Process finished. Your code is still running!")