# IP Ping Monitor

This Python script monitors the reachability of multiple IP addresses, logs the results to a file, and provides alerts in the CLI when an IP becomes unreachable.

## Features

- Pings multiple IP addresses specified in `targets.csv`.
- Logs ping results and timestamps to `ping_log.txt`.
- Alerts in the CLI when an IP address becomes unreachable.
- Runs continuously in a detached `screen` session for background monitoring.

## Requirements

- Python 3.x
- `screen` utility (for running the script in detached mode)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/webdevtodayjason/ping_monitor.git
   cd ping_monitor
   ```
2. No external dependencies beyond Python standard library are required.
## Configuration
1. targets.csv: Edit this file to specify the IP addresses, target names, and ping intervals.

Example format:
   ```bash
  IP,TARGET_NAME,PING_INTERVAL
  104.202.247.86,Server1,5
  192.168.1.1,Router,10
  ```
## Usage
1. Start a screen session to run the monitor script in the background:
  ```bash
screen -S ping_monitor -dm python3 ip_ping_monitor.py
```
This command starts a detached screen session named ping_monitor and runs the monitor.py script, which continuously monitors the IP addresses specified in targets.csv.

2. To view the ping_monitor screen session:
```bash
screen -x ping_monitor
```
Press Ctrl+A followed by Ctrl+D to detach from the screen session without terminating it.

3. To stop the monitor script, reattach to the ping_monitor screen session and press Ctrl+C to interrupt the script execution. Then, you can exit the screen session.

## Logging
The script logs all ping results and timestamps to ping_log.txt in the following format:
```ruby
YYYY-MM-DD HH:MM:SS - <IP or TARGET_NAME> is reachable.
YYYY-MM-DD HH:MM:SS - <IP or TARGET_NAME> is not reachable! Alert!
```
Replace <IP or TARGET_NAME> with the actual IP address or target name being monitored.

## Contributing
Feel free to fork the repository, submit issues, and contribute enhancements. Pull requests are welcome!

## License
This project is licensed under the MIT License - see the LICENSE file for details.


