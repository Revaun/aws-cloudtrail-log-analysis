import json

# Load CloudTrail log file
with open("example_cloudtrail_log.json", "r") as f:
    logs = json.load(f)

# Suspicious patterns to check
suspicious_events = []

for record in logs.get("Records", []):
    event_name = record.get("eventName")
    user_identity = record.get("userIdentity", {}).get("type")
    source_ip = record.get("sourceIPAddress")

    # Example checks
    if user_identity == "Root":
        suspicious_events.append(f"Root account used: {event_name}")

    if event_name == "ConsoleLogin" and record.get("responseElements", {}).get("ConsoleLogin") == "Failure":
        suspicious_events.append(f"Failed login attempt from {source_ip}")

    if "Delete" in event_name:
        suspicious_events.append(f"Delete action detected: {event_name}")

# Print results
if suspicious_events:
    print("Suspicious activity detected:")
    for event in suspicious_events:
        print(f"- {event}")
else:
    print("No suspicious activity found.")
