import json

from app.config import BASE_DIR


USERS_FILE = BASE_DIR / "data" / "users.json"


def _load_users() -> list[dict]:
    if not USERS_FILE.exists():
        return []

    with USERS_FILE.open("r", encoding="utf-8") as file:
        data = json.load(file)

    return data.get("users", [])


def _save_users(users: list[dict]) -> None:
    USERS_FILE.parent.mkdir(parents=True, exist_ok=True)

    with USERS_FILE.open("w", encoding="utf-8") as file:
        json.dump(
            {"users": users},
            file,
            ensure_ascii=False,
            indent=4,
        )


def get_user(telegram_id: int) -> dict | None:
    users = _load_users()

    for user in users:
        if user["telegram_id"] == telegram_id:
            return user

    return None


def save_user(user: dict) -> None:
    users = _load_users()

    for index, existing_user in enumerate(users):
        if existing_user["telegram_id"] == user["telegram_id"]:
            users[index] = user
            _save_users(users)
            return

    users.append(user)
    _save_users(users)

def get_managers() -> list[dict]:
    users = _load_users()

    return [
        users
        for user in users
        if user["role"] == "manager"
    ]