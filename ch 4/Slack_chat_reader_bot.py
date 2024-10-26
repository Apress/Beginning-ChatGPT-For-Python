from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from datetime import datetime, timezone

# Define your Slack API token
SLACK_BOT_TOKEN = "YOUR_SLACK_API_TOKEN"

# Initialize a WebClient instance
client = WebClient(token=SLACK_BOT_TOKEN)

# Define your channel ID
channel_id = "CHANNEL-ID-HERE"

# Define start and end time in UTC
start_time_utc = datetime(2023, 8, 3, 10, 0, tzinfo=timezone.utc)
end_time_utc = datetime(2023, 8, 12, 15, 0, tzinfo=timezone.utc)

# Convert start and end time to Unix timestamps
start_time_unix = int(start_time_utc.timestamp())
end_time_unix = int(end_time_utc.timestamp())

try:
    # Call the conversations.history method using WebClient
    response = client.conversations_history(
        channel=channel_id,
        oldest=start_time_unix,
        latest=end_time_unix,
    )

    # Check if the API call was successful
    if response["ok"]:
        # Reverse the messages list to get them in chronological order
        messages = reversed(response["messages"])
        for message in messages:
            user_id = message.get("user")
            timestamp = datetime.fromtimestamp(float(message.get("ts")), tz=timezone.utc)
            user_info_response = client.users_info(user=user_id)
            if user_info_response["ok"]:
                user_name = user_info_response["user"]["name"]
                print("User:", user_name)
                print("Timestamp:", timestamp)
                print("Message:", message.get("text"))
                print()
            else:
                print("Failed to fetch user info:", user_info_response["error"])
    else:
        print("Failed to fetch messages:", response["error"])

except SlackApiError as e:
    print(f"Error: {e.response['error']}")
