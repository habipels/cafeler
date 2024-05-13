
from sinch import Client

sinch_client = Client(
    key_id="773b13d2-98ad-49c1-8aab-a83597daa0f4",
    key_secret="9sJ1~gw92FFBudICHZPzfdpacT",
    project_id="474594da-b864-491a-91c6-91bbc089b932"
)

send_batch_response = sinch_client.sms.batches.send(
    body="Hello from Sinch!",
    to=["447520662243"],
    from_="+905395154570",
    delivery_report="none"
)

print(send_batch_response)