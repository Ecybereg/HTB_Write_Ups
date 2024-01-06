import os
import pyshark
from datetime import datetime
import sys
import time

def moving_message(message):
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
    time.sleep(0.5)  # Pause after the message

def print_darth_vader():
    darth_vader = r"""
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⣀⣀⣤⢤⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣴⣶⣿⣿⡿⣿⢿⣷⣽⣿⣿⣿⣷⣆⠀⠀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣛⣽⣿⠿⠿⢻⣿⡟⣷⣼⣉⣿⣿⣿⣿⣟⠻⣿⣿⣟⢿⡦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⢏⣤⣶⣿⣿⣿⢹⣿⣿⡟⣿⣿⣿⣿⣿⣷⣄⣈⣻⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣼⠿⣿⣇⣿⣿⣿⣿⣿⣿⣾⣿⣿⡇⣿⣿⣿⣿⣿⣿⣿⣿⡁⢿⣿⣟⢷⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢰⣿⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⣿⣿⣿⣿⣿⣿⣿⣿⣷⢸⣿⣿⠸⣇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⣿⣿⣿⣿⣿⣿⡿⠛⣿⣿⡿⣿⡏⠉⢻⣿⣿⣿⣿⣿⣿⢸⣿⣿⢀⣿⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⣿⣧⠀⢿⣿⣙⣿⣿⡟⠁⠀⠀⢸⠀⠘⠀⠀⠀⣿⣿⣿⣿⣿⣿⢸⣿⡏⢸⣿⡆⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣿⣿⣿⣶⣻⡿⠋⣹⣿⡀⠀⠀⢀⣿⣀⠀⣀⣶⣴⣿⣿⣷⣿⣷⣦⣬⣻⣧⣼⣿⡇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣿⠟⣹⣿⢋⣀⣿⡿⠿⠿⠷⣶⢾⣿⡟⢙⣿⠿⣻⣿⣿⣿⣿⣿⣿⣿⣿⣅⢻⣿⣷⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢣⣾⣿⣿⣿⣿⡿⠿⠿⣿⣶⣦⣼⣿⣧⣤⣾⣿⣿⣛⣛⡛⠿⣿⣿⣿⡍⢿⣿⣟⣿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⠋⠉⢛⣿⣿⣿⣿⣟⣿⣿⣿⣟⢉⣽⣿⣿⣷⣮⣿⣿⣿⣦⡀⣿⣾⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣶⣾⣿⣿⣿⣿⣿⣷⣰⣿⣿⣿⡿⠋⠙⣿⣿⣿⣿⣿⣿⣿⣷⡜⣿⣧⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠟⠁⠀⣿⣿⣯⣼⣿⣿⣿⣷⣀⣀⣈⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⣆⠀⠀⠀⠀⠀
⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣶⣿⣿⣿⡿⣿⣿⣽⣤⣽⣛⣛⣛⣿⣿⣟⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀
⠀⠀⣾⣿⣿⣿⣿⣿⣿⡿⣿⣿⣧⣬⣥⣴⡿⠿⣻⣧⣟⣿⣿⠿⠿⠿⢿⣿⣿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀
⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠉⣹⣿⣿⣿⣾⠋⠉⠹⣿⣿⣷⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡽⣷⠀⠀⠀
⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⢸⣿⣿⣿⣭⣦⣤⣤⣿⣿⡻⣷⣤⣺⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡙⣇⠀⠀
⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡎⣴⢟⣿⡿⢻⣿⣿⣿⣿⣿⣿⣿⣌⣿⣟⢿⣟⡟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡹⡄⠀
⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣧⣿⡿⣳⣿⣿⡟⢻⣿⣿⣿⣿⣿⣟⣿⣧⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⢳⡀
⢿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣷⣿⣿⡿⠇⠸⠿⠸⢿⣟⣿⣿⣮⣱⢿⣿⡋⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⠟⠁
⠀⠉⠙⠛⠛⠛⠛⠛⢛⣿⣿⣿⣀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣅⣸⣿⣷⣎⣿⣿⣯⣁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣿⣿⣿⣿⣿⣷⣦⣀⣀⣠⣠⣤⣤⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣤⡀⠀⠀⠀
⠀⠀⠀⠀⠀⣠⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⠗⠀⠀
⠀⠀⠀⠘⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠉⠀⣠⣾⣿⣿⣿⣿⣿⣿⡿⠋⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠈⠙⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠉⠉⠉⠉⢉⣽⣿⣿⣄⣀⣴⣿⣿⣿⣿⣿⣿⡿⠛⠉⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠿⣿⣿⣿⣿⣿⣿⣶⣦⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠋⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    """
    print(darth_vader)

def check_for_handshakes(tool_directory):
    # Get the current day in the same format as the directory name
    date = datetime.now().strftime("%m-%d-%y").replace('/', '-')

    # Specify the path to the directory containing .cap files
    directory_path = tool_directory.format(date=date)

    files = [file for file in os.listdir(directory_path) if file.endswith(".cap")]

    if not files:
        pikachu = r"""
⢀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⣠⣤⣶⣶
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⢰⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣀⣀⣾⣿⣿⣿⣿
⣿⣿⣿⣿⣿⡏⠉⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿
⣿⣿⣿⣿⣿⣿⠀⠀⠀⠈⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠉⠁⠀⣿
⣿⣿⣿⣿⣿⣿⣧⡀⠀⠀⠀⠀⠙⠿⠿⠿⠻⠿⠿⠟⠿⠛⠉⠀⠀⠀⠀⠀⣸⣿
⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⣴⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⢰⣹⡆⠀⠀⠀⠀⠀⠀⣭⣷⠀⠀⠀⠸⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠈⠉⠀⠀⠤⠄⠀⠀⠀⠉⠁⠀⠀⠀⠀⢿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⢾⣿⣷⠀⠀⠀⠀⡠⠤⢄⠀⠀⠀⠠⣿⣿⣷⠀⢸⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⡀⠉⠀⠀⠀⠀⠀⢄⠀⢀⠀⠀⠀⠀⠉⠉⠁⠀⠀⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿
        """
        print(pikachu)
        print("No .cap files found in the specified directory.")
        return

    print_darth_vader()
    moving_message("Whahahahahaha YOU HAVE CONTROLLED YOUR FEAR. NOW, RELEASE YOUR ANGER. ONLY YOUR HATRED CAN DESTROY ME. ")

    for file in files:
        file_path = os.path.join(directory_path, file)
        try:
            cap = pyshark.FileCapture(file_path)
            handshake_found = False
            pmkid_found = False

            for packet in cap:
                if "EAPOL" in packet:
                    handshake_found = True
                    break
                elif "PMKID" in packet:
                    pmkid_found = True

            if handshake_found or pmkid_found:
                moving_message(f"\nFile: {file} - Handshake Found: {handshake_found} - PMKID Found: {pmkid_found}")

        except pyshark.FileCaptureException:
            print(f"Error reading file: {file_path}")

# Specify the path to the Tool directory
tool_directory_path = "./Tool/{date}"  # Replace with the actual path
check_for_handshakes(tool_directory_path)
