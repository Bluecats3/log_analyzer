# Import defaultdict from collections
# This lets us create a dictionary that automatically starts values at 0
from collections import defaultdict


# Create a dictionary to store failed login counts for each IP
# Example: {"192.168.1.2": 3}
failed_attempts = defaultdict(int)


# Open the log file in read mode ("r")
with open("log.txt", "r") as file:

    # Go through each line in the file one by one
    for line in file:

        # Check if the line contains the word "failed"
        # This filters only failed login attempts
        if "failed" in line:

            # Split the line at "ip=" to isolate the IP address
            # Example: "Login failed: user=admin ip=192.168.1.2"
            # becomes ["Login failed: user=admin ", "192.168.1.2"]
            parts = line.split("ip=")

            # Take the second part (index 1) and remove extra spaces/newlines
            ip = parts[1].strip()

            # Increase the count for this IP address
            # If IP doesn't exist yet, defaultdict starts it at 0 automatically
            failed_attempts[ip] += 1


# Print report header
print("Suspicious Activity Report")
print("==========================")


# Loop through each IP and its number of failed attempts
for ip, count in failed_attempts.items():

    # If an IP has 3 or more failed attempts, flag it as suspicious
    if count >= 3:

        # Print alert message
        print(f"⚠️ ALERT: {ip} has {count} failed login attempts")