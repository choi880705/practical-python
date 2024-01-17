# Assume some initial values for height, BOUNCE_RATE, and num_bounce
height = 100
BOUNCE_RATE = 0.6
num_bounce = 0


def wloop(height=100):
    print("made with while statement")
    while num_bounce < 10:  # Run 10 times
        height *= BOUNCE_RATE  # BOUNCE height = BOUNCE height * 0.6
        num_bounce += 1  # increase count by 1
        print(
            f"{num_bounce} times: {round(height, 4)}"
        )  # Print the bounce height with 4 decimal places


# Call the function
wloop()
