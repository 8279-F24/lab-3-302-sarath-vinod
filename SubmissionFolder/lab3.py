

from adafruit_circuitplayground import cp

while True:
    blue = (0, 0, 255)
    
    # Prompt user for the number of LEDs
    try:
        num_leds = int(input("Enter the number of LEDs to switch on (1-10): "))
    except ValueError:
        print('Entered value is not valid.')
        print('do you want to try again')
        continue

    # Check if the number is within the valid range
    if 1 <= num_leds <= 10:
        # Turn off all LEDs first
        for i in range(10):
            cp.pixels[i] = (0, 0, 0)

        # Turn on the specified number of LEDs
        for i in range(num_leds):
            cp.pixels[i] = blue
            print("LED {} is ON".format(i + 1))
    else:
        print("Number out of range. Please enter a number between 1 and 10.")
        continue
    
    # Prompt if user wants to start again
    restart = input("Do you want to start again? (n to stop, any other key to continue): ").lower()
    if restart == 'n':
        print("Program ended.")
        break
