def get_user_filepath(user_id: str) -> str:
    """
    Each user has their own directory to store their data.
    """
    return f"users/{user_id}"
