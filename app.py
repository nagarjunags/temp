from flask import Flask
import serial
import time

app = Flask(__name__)

# Replace 'COM3' with the port where your Arduino is connected
port_name = "COM3"

# Initialize serial connection
serial_port = serial.Serial(port_name, baudrate=9600, timeout=1)

# Path to the text file where you want to store the data
text_file_path = "price.txt"

@app.route("/")
def index():
    # Read data from Arduino serial port
    data_from_arduino = serial_port.readline().decode().strip()

    # Write the data received from Arduino to the text file
    with open(text_file_path, "a") as file:
        file.write(data_from_arduino + "\n")

    return "Data from Arduino written to text file."

if __name__ == "__main__":
    app.run(debug=True)
