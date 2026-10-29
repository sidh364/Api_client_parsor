import requests

class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url.rstrip("/")
        self.session = requests.Session()

    def fetch_user(self, user_id=1):
        """Fetch a user by ID."""
        url = f"{self.base_url}/users/{user_id}"

        response = self.session.get(url, timeout=10)
        response.raise_for_status()

        return response.json()
    