import requests
from config import BASE_URL


def get_post(post_id):
    response = requests.get(f"{BASE_URL}/posts/{post_id}")
    return response
