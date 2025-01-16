import subprocess
import time
import csv
from datetime import datetime
import threading

LOG_FILE = "ping_log.txt"
CSV_FILE = "targets.csv"

def log_to_file(message: str):
    """Append a message to the log file with a timestamp."""
    with open(LOG_FILE, 'a') as f:
        f.write(message + "\n")

def monitor_target(ip: str, target_name: str, ping_interval: int):
    """
    Continuously ping the given IP, print and log the reachability status
    with a timestamp every 'ping_interval' seconds.
    """
    while True:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Ping once
        result = subprocess.run(
            ["ping", "-c", "1", ip],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        
        if result.returncode == 0:
            message = f"{now} - {target_name} ({ip}) is reachable."
        else:
            message = f"{now} - {target_name} ({ip}) is NOT reachable! Alert!"
        
        # Print to CLI
        print(message)
        # Log to file
        log_to_file(message)
        
        # Wait for next ping cycle
        time.sleep(ping_interval)

def main():
    threads = []

    # Read targets from CSV
    try:
        with open(CSV_FILE, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                ip = row["IP"].strip()
                target_name = row["TARGET_NAME"].strip()
                ping_interval = int(row["PING_INTERVAL"].strip())
                
                # Start a daemon thread for each target
                t = threading.Thread(
                    target=monitor_target,
                    args=(ip, target_name, ping_interval),
                    daemon=True
                )
                t.start()
                threads.append(t)
    except FileNotFoundError:
        print(f"Error: {CSV_FILE} file not found.")
        return
    except KeyError as e:
        print(f"Error: Missing column in {CSV_FILE}: {e}")
        return
    except ValueError as e:
        print(f"Error: Invalid data in {CSV_FILE}: {e}")
        return

    # Keep main thread alive until Ctrl+C
    print("Monitoring started. Press Ctrl+C to stop.\n")
    try:
        while True:
            time.sleep(1)  # Idle loop
    except KeyboardInterrupt:
        print("\nStopping all monitoring threads. Goodbye!")
        # Daemon threads will terminate when main thread ends.

if __name__ == "__main__":
    main()
