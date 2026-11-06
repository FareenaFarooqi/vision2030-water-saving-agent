
"""Vision 2030 Water-Saving Assistant."""

def water_saving_advice(daily_liters):
    """Give simple water-saving advice based on daily water use."""
    if daily_liters <= 100:
        return "Great! Keep saving water and maintain your good habits."
    elif daily_liters <= 200:
        return "Good start! Try shorter showers and turn off taps when not needed."
    else:
        return "Your water use is high. Check for leaks and reduce unnecessary water use."


def main():
    print("=" * 45)
    print("VISION 2030 WATER-SAVING ASSISTANT")
    print("Supporting Saudi Vision 2030 and SDG 6")
    print("=" * 45)

    try:
        liters = float(input("Enter daily water use in liters: "))

        if liters < 0:
            print("Please enter a positive number.")
            return

        print("\nYour Water-Saving Report")
        print("-" * 25)
        print(f"Daily water use: {liters:g} liters")
        print("Recommendation:", water_saving_advice(liters))
        print("\nGoal: Use water responsibly and reduce waste.")

    except ValueError:
        print("Invalid input. Please enter a number.")


if __name__ == "__main__":
    main()
