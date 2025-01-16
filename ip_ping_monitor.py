import subprocess
import time
import csv
from datetime import datetime

# Log file path
log_file = "ping_log.txt"

def ping_ip(ip, target_name, ping_interval):
    while True:
        # Ping the IP address once
        result = subprocess.run(['ping', '-c', '1', ip],
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if result.returncode == 0:
            print(f"{target_name} ({ip}) is reachable.")
            log_to_file(f"{target_name} ({ip}) is reachable.")
        else:
            print(f"{target_name} ({ip}) is not reachable! Alert!")
            log_to_file(f"{target_name} ({ip}) is not reachable!")

        # Sleep for ping_interval seconds
        time.sleep(ping_interval)

def log_to_file(message):
    with open(log_file, 'a') as f:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"{timestamp} - {message}\n"
        f.write(log_entry)

def start_screen_session():
    screen_cmd = f"screen -dmS ping_monitor python3 {__file__}"
    subprocess.run(screen_cmd, shell=True)

if __name__ == "__main__":
    # Start a screen session for continuous monitoring
    start_screen_session()

    # Read targets from targets.csv
    with open('targets.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            ip_address = row['IP']
            target_name = row['TARGET_NAME']
            ping_interval = int(row['PING_INTERVAL'])

            # Start pinging for each target in a separate thread or process
            ping_ip(ip_address, target_name, ping_interval)
