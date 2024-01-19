#!/usr/bin/env python3
import sys
import json
import requests
import argparse

def format_json_as_markdown(json_data):
    def format_dict(d, indent=0):
        markdown = ""
        for key, value in d.items():
            markdown += " " * indent + f"- **{key}**: "
            if isinstance(value, dict):
                markdown += "\n" + format_dict(value, indent + 2)
            elif isinstance(value, list):
                markdown += "\n" + format_list(value, indent + 2)
            else:
                markdown += f"{value}\n"
        return markdown

    def format_list(lst, indent=0):
        markdown = ""
        for item in lst:
            if isinstance(item, dict):
                markdown += format_dict(item, indent + 2)
            elif isinstance(item, list):
                markdown += format_list(item, indent + 2)
            else:
                markdown += " " * indent + f"- {item}\n"
        return markdown

    return format_dict(json_data)

alert_file = sys.argv[1]
hook_url = sys.argv[3]
# Read the alert file
try:
    with open(alert_file, 'r') as file:
        alert_json = json.load(file)
except IOError:
    print("Error: Unable to read the alert file.")
    exit(1)

# Extract issue fields
alert_level = alert_json['rule']['level']
agentname = alert_json['agent']['name']
description = alert_json['rule']['description']

# Prepare the request data
issue_data = {
    "message": format_json_as_markdown(alert_json),
    "priority": alert_level,
    "title": agentname + " " + description,
}

# Send the request
try:
    response = requests.post(hook_url, json=issue_data)
    response.raise_for_status()
except requests.RequestException as e:
    print(f"Error sending notification: {e}")
    exit(1)
