import requests
parameter = {
    "amount": 10,
    "type": "boolean"
}
req = requests.get("https://opentdb.com/api.php", parameter)
req.raise_for_status()
reponse=req.json()
question_data = reponse['results']