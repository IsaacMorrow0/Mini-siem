import requests

def send_slack_alert(ip, count):
    webhook_url = "x"  # Replace x with your slack url

    message = {
        "text": f"🚨 ALERT: {ip} has triggered {count} failed SSH login attempts!"
    }

    response = requests.post(webhook_url, json=message)

    if response.status_code != 200:
        print(f"Failed to send Slack alert: {response.status_code}, {response.text}")

