import subprocess
import time
import csv
from datetime import datetime

# Log file path
log_file = "ping_log.txt"

def ping_ip(ip, target_name, ping_interval):
    while True:
        try:
            # Ping the IP address once
            result = subprocess.run(['ping', '-c', '1', ip],
                                    stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            if result.returncode == 0:
                print(f"{target_name} ({ip}) is reachable.")
                log_to_file(f"{target_name} ({ip}) is reachable.")
            else:
                print(f"{target_name} ({ip}) is not reachable! Alert!")
                log_to_file(f"{target_name} ({ip}) is not reachable!")

            # Sleep for ping interval
            time.sleep(ping_interval)
        
        except KeyboardInterrupt:
            print("\nMonitoring stopped.")
            break
        except Exception as e:
            print(f"Error occurred while pinging {target_name} ({ip}): {str(e)}")

def log_to_file(message):
    with open(log_file, 'a') as f:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"{timestamp} - {message}\n"
        f.write(log_entry)

def start_monitoring():
    try:
        with open('targets.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                ip = row['IP']
                target_name = row['TARGET_NAME']
                ping_interval = int(row['PING_INTERVAL'])
                ping_ip(ip, target_name, ping_interval)
    except FileNotFoundError:
        print("Error: targets.csv file not found.")
    except Exception as e:
        print(f"Error occurred while reading targets.csv: {str(e)}")

if __name__ == "__main__":
    start_monitoring()
