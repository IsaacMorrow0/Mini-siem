import requests

def send_slack_alert(ip, count):
    webhook_url = "https://hooks.slack.com/services/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"  # Replace with yours

    message = {
        "text": f"🚨 ALERT: {ip} has triggered {count} failed SSH login attempts!"
    }

    response = requests.post(webhook_url, json=message)

    if response.status_code != 200:
        print(f"Failed to send Slack alert: {response.status_code}, {response.text}")

