from app.infrastructure.repositories.user_repository import (
    get_user,
    save_user,
    get_managers,
)


def register_user(
    telegram_id: int,
    username: str | None,
    first_name: str | None,
    role: str,
) -> dict:

    existing_user = get_user(telegram_id)

    # Користувач вже існує
    if existing_user:
        # Якщо роль змінилася — оновлюємо її
        if existing_user["role"] != role:
            existing_user["role"] = role
            existing_user["username"] = username
            existing_user["first_name"] = first_name

            save_user(existing_user)

        return existing_user


    user = {
        'telegram_id': telegram_id,
        'username': username,
        'first_name': first_name,
        'role': role,
    }

    save_user(user)

    return user

def get_user_by_id(telegram_id: int) -> dict | None:
    return get_user(telegram_id)

def get_manager_users() -> list[dict]:
    return get_managers()