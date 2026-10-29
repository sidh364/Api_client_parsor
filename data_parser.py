
class UserParser:
    """Validates and cleans user data."""

    def parse(self, data):
        if not isinstance(data, dict):
            raise ValueError("User data must be a dictionary.")

        required_fields = ["id", "name", "username", "email"]

        for field in required_fields:
            if field not in data:
                raise ValueError(f"Missing required field: {field}")

        if not isinstance(data["name"], str) or not data["name"].strip():
            raise ValueError("Name must be a non-empty string.")

        if not isinstance(data["username"], str) or not data["username"].strip():
            raise ValueError("Username must be a non-empty string.")

        if not isinstance(data["email"], str) or not data["email"].strip():
            raise ValueError("Email must be a non-empty string.")

        return {
            "id": data["id"],
            "name": data["name"].strip(),
            "username": data["username"].strip(),
            "email": data["email"].strip().lower()
        }
