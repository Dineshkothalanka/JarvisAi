"""
Module for basic task automation.
"""

import os
import subprocess
import platform

class TaskAutomation:
    def __init__(self):
        pass

    def open_application(self, app_path):
        try:
            if platform.system() == "Windows":
                os.startfile(app_path)
            elif platform.system() == "Darwin":
                subprocess.call(["open", app_path])
            else:
                subprocess.call([app_path])
            return f"Opened application: {app_path}"
        except Exception as e:
            return f"Error opening application: {str(e)}"

    def run_command(self, command):
        try:
            result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
            return result
        except subprocess.CalledProcessError as e:
            return f"Command failed: {e.output}"

    def set_reminder(self, message, delay_seconds):
        # Simple reminder using sleep and print (can be improved with notifications)
        import threading
        def reminder():
            import time
            time.sleep(delay_seconds)
            print(f"Reminder: {message}")
        threading.Thread(target=reminder).start()
        return f"Reminder set for {delay_seconds} seconds from now."
