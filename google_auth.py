"""
google_auth.py - Simplified Google OAuth helper for sign-in only.
Only needs openid/email/profile scopes. No token refresh or revocation.
"""

from urllib.parse import urlencode
import requests
from flask import current_app


class GoogleOAuthError(Exception):
    pass


class GoogleOAuthManager:
    AUTH_URI = 'https://accounts.google.com/o/oauth2/v2/auth'
    TOKEN_URI = 'https://oauth2.googleapis.com/token'
    USERINFO_URI = 'https://www.googleapis.com/oauth2/v3/userinfo'
    SCOPES = ['openid', 'email', 'profile']

    def __init__(self):
        self.client_id = current_app.config['GOOGLE_CLIENT_ID']
        self.client_secret = current_app.config['GOOGLE_CLIENT_SECRET']
        self.redirect_uri = current_app.config['GOOGLE_REDIRECT_URI']

    def get_authorization_url(self, state=None):
        params = {
            'client_id': self.client_id,
            'redirect_uri': self.redirect_uri,
            'response_type': 'code',
            'scope': ' '.join(self.SCOPES),
            'access_type': 'online',
            'prompt': 'select_account',
        }
        if state:
            params['state'] = state
        return f"{self.AUTH_URI}?{urlencode(params)}"

    def exchange_code_for_tokens(self, authorization_code):
        data = {
            'code': authorization_code,
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'redirect_uri': self.redirect_uri,
            'grant_type': 'authorization_code',
        }
        response = requests.post(self.TOKEN_URI, data=data, timeout=20)
        response.raise_for_status()
        return response.json()

    def get_user_info(self, access_token):
        response = requests.get(
            self.USERINFO_URI,
            headers={'Authorization': f'Bearer {access_token}'},
            timeout=20,
        )
        response.raise_for_status()
        return response.json()
