import requests

def fetch_data():
    try:
        response = requests.get("http://flask_app:5000/api/data")
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}
