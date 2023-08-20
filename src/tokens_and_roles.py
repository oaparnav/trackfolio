from os import environ as env
from dotenv import find_dotenv, load_dotenv
from flask import request

import requests

from src.models import advisors

ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)

def get_access_token():
    url = "https://dev-d6pchdbvs0cq84vq.us.auth0.com/oauth/token"

    data = {
        "grant_type" : "client_credentials",
        "client_id" : env.get("AUTH0_CLIENT_ID"),
        "client_secret" : env.get("AUTH0_CLIENT_SECRET"),
        "audience" : env.get("AUTH0_AUDIANCE"),
    }
    response = requests.post(url, data= data)

    access_token = response.json()['access_token']
    return access_token

def get_roles(id):
    access_token = get_access_token()
    url = f"https://dev-d6pchdbvs0cq84vq.us.auth0.com/api/v2/users/{id}/roles"
    headers = {
        "Authorization":f"Bearer {access_token}"
    }
    user_roles = requests.get(url, headers=headers)
    return user_roles