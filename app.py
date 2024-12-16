from flask import Flask, request, jsonify
import requests
from datetime import datetime
import uuid

app = Flask(__name__)

# Discord Webhook URL
DISCORD_WEBHOOK_URL = ""

def send_to_discord(user_data):
    """
    Sends the user tracking data to a Discord webhook.
    """
    discord_message = {
        "content": "New Tracking Event",
        "embeds": [
            {
                "title": "User Tracking Data",
                "fields": [
                    {"name": "User ID", "value": user_data["User ID"], "inline": True},
                    {"name": "IP Address", "value": user_data["IP Address"], "inline": True},
                    {"name": "User Agent", "value": user_data["User Agent"], "inline": False},
                    {"name": "Referrer URL", "value": user_data["Referrer URL"] or "None", "inline": False},
                    {"name": "Timestamp", "value": user_data["Timestamp"], "inline": False},
                    {"name": "Behavior", "value": str(user_data["Behavior"]), "inline": False}
                ]
            }
        ]
    }

    try:
        response = requests.post(DISCORD_WEBHOOK_URL, json=discord_message)
        if response.status_code == 204:
            return True
        else:
            return False
    except Exception as e:
        print(f"Error sending to Discord: {e}")
        return False

@app.route('/pixel/<id>', methods=['GET'])
def tracking_pixel_id(id):
    """
    Route for serving a pixel with user tracking based on a unique ID.
    """
    user_ip = request.remote_addr
    user_agent = request.headers.get('User-Agent')
    referrer_url = request.referrer
    timestamp = datetime.now().isoformat()

    # Simulate user behavior
    user_behavior = {
        "page_views": 1,
        "interaction": f"Viewed Tracking Pixel with ID {id}"
    }

    user_data = {
        "User ID": id,
        "IP Address": user_ip,
        "User Agent": user_agent,
        "Referrer URL": referrer_url,
        "Timestamp": timestamp,
        "Behavior": user_behavior
    }

    # Send data to Discord
    if send_to_discord(user_data):
        print("Data sent to Discord successfully.")

    # Return a 1x1 transparent pixel
    pixel = b"\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x80\xff\x00\xff\xff\xff\x00\x00\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02\x4c\x01\x00\x3b"
    return pixel, 200, {'Content-Type': 'image/gif'}

@app.route('/track', methods=['GET'])
def track_user():
    """
    Standalone route for user tracking without a pixel.
    """
    user_ip = request.remote_addr
    user_agent = request.headers.get('User-Agent')
    referrer_url = request.referrer
    timestamp = datetime.now().isoformat()
    user_id = str(uuid.uuid4())  # Generate a unique ID for the user session

    user_behavior = {
        "page_views": 1,
        "interaction": "Viewed Tracking Page"
    }

    user_data = {
        "User ID": user_id,
        "IP Address": user_ip,
        "User Agent": user_agent,
        "Referrer URL": referrer_url,
        "Timestamp": timestamp,
        "Behavior": user_behavior
    }

    # Send data to Discord
    if send_to_discord(user_data):
        return jsonify({"message": "Tracking data sent to Discord."}), 200
    else:
        return jsonify({"error": "Failed to send data to Discord."}), 500

@app.route('/pixel', methods=['GET'])
def serve_pixel():
    """
    Route to serve a tracking pixel without ID-based tracking.
    """
    return tracking_pixel_id(str(uuid.uuid4()))  # Generate a random UUID for the pixel

if __name__ == '__main__':
    app.run(debug=True)
