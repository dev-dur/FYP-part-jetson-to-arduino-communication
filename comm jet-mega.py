import serial
import time


arduino_port = '/dev/ttyUSB0'
baud_rate = 9600  # Same baud rate as set in the Arduino code

try:
    arduino = serial.Serial(arduino_port, baud_rate, timeout=1)
    time.sleep(2)  
    print("Connected to Arduino")


    while True:
        command = input("Enter command (1 to turn ON, 0 to turn OFF, q to quit): ")
        if command == 'q':
            print("Exiting program...")
            break
        elif command in ['0', '1']:
            arduino.write(command.encode())  
            print(f"Command '{command}' sent.")
        else:
            print("Invalid command. Please enter '1', '0', or 'q'.")

except serial.SerialException as e:
    print(f"Error: {e}")
except KeyboardInterrupt:
    print("Program interrupted by user.")
finally:
    if 'arduino' in locals() and arduino.is_open:
        arduino.close()
        print("Arduino connection closed.")
