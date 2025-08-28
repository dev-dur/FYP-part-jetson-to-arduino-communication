Jetson to Arduino Communication

A simple Python script that allows a **NVIDIA Jetson (or any Linux system)** to communicate with an **Arduino** board over a **serial connection (USB)**.  
This project demonstrates how to send basic commands from the Jetson to the Arduino to control external devices (like LEDs, motors, or relays).

📌 Features
- Serial communication between Jetson (Python) and Arduino  
- Command-based control (`1` = ON, `0` = OFF)  
- Safe exit with quit command (`q`)  
- Error handling for disconnection and interruptions  

🛠 Tech Stack
- **Python**  
- **pySerial** library  
- **Arduino Uno/Nano/Mega** (any board with USB serial)  

📖 Usage
- Enter 1 → turns LED ON
- Enter 0 → turns LED OFF
- Enter q → quits program and closes serial connection

🔮 Future Improvements
- Add bi-directional communication (Arduino sends sensor data back to Jetson)
- Support multiple devices or commands
- Build a GUI interface for easier control
