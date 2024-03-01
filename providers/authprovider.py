import json
from supabase.client import ClientOptions, create_client
from config.config import Config
import flet as ft
from flet.security import decrypt, encrypt
from providers.data_provider import DataProvider
from providers.navigator import Navigator
from routes.routes import Routes
from gotrue.types import Session, AuthChangeEvent, AuthResponse, Provider


class AuthProvider:
    supabaseClient = create_client(
        Config.SUPABASE_URL,
        Config.SUPABASE_KEY,
        # options=ClientOptions(auto_refresh_token=True),
    )

    page = None

    @classmethod
    def update_page(cls, page):
        cls.page = page

    @classmethod
    def email_login(cls, ev):
        if not cls.page:
            raise Exception("AuthProvider.page is not set")
        try:
            auth: AuthResponse = cls.supabaseClient.auth.sign_in_with_password(
                {
                    "email": DataProvider.get("email"),
                    "password": DataProvider.get("password"),
                }
            )

            encrypted_token = encrypt(auth.model_dump_json(), Config.SECRET_KEY)

            cls.page.client_storage.set(Config.SESSION_KEY, encrypted_token)
            print("Token saved to client storage")

        except Exception as e:
            print(e)

    @classmethod
    def logout(cls, e):
        try:
            cls.supabaseClient.auth.sign_out()

            if cls.page and cls.page.client_storage:
                cls.page.client_storage.remove(Config.SESSION_KEY)

        except Exception as e:
            print(e)

    @classmethod
    def signup(cls, e):
        if not cls.page:
            raise Exception("AuthProvider.page is not set")
        try:
            auth = cls.supabaseClient.auth.sign_up(
                credentials={
                    "email": DataProvider.get("email"),
                    "password": DataProvider.get("password"),
                }
            )
            encrypted_token = encrypt(auth.model_dump_json(), Config.SECRET_KEY)

            cls.page.client_storage.set(Config.SESSION_KEY, encrypted_token)
            print("Token saved to client storage")

            return auth
        except Exception as e:
            print(e)
            return False

    @classmethod
    def get_user(cls):
        user = cls.supabaseClient.auth.get_user()
        print("User: ", user)
        return user

    @classmethod
    def get_session(cls):
        try:
            session = cls.supabaseClient.auth.get_session()
            return session
        except Exception as e:
            # print(e)
            return False

    @classmethod
    def is_signed_in(cls):
        if not cls.page:
            raise Exception("AuthProvider.page is not set")

        else:
            token = cls.page.client_storage.get(Config.SESSION_KEY)
            if not token:
                Navigator.replace(Routes.HOME_ROUTE)
            else:
                try:
                    decrypted_token = json.loads(
                        decrypt(
                            token,
                            Config.SECRET_KEY,
                        )
                    )
                    refresh_token = decrypted_token["session"]["refresh_token"]
                    cls.supabaseClient.auth.refresh_session(refresh_token)
                    Navigator.replace(Routes.DASHBOARD_ROUTE)

                except Exception as e:
                    print("Exception: ", e)
                    Navigator.replace(Routes.HOME_ROUTE)

    @classmethod
    def oauth_login(cls, provider: Provider):
        if not cls.page:
            raise Exception("AuthProvider.page is not set")
        try:
            signin_url = cls.supabaseClient.auth.sign_in_with_oauth(
                {"provider": provider}
            ).url
            cls.page.launch_url(signin_url)

        except:
            print("Error")
            return False


def handle_auth_change(event: AuthChangeEvent, session: Session | None):
    if event == "SIGNED_IN" or event == "TOKEN_REFRESHED":
        # if session:
        #     print("Session: ", session.model_dump_json())
        # print("Session type:", type(session))
        # encrypted_token = encrypt(session.model_dump_json(), Config.SECRET_KEY)
        # if AuthProvider.page and AuthProvider.page.client_storage:
        #     AuthProvider.page.client_storage.set(Config.SESSION_KEY, encrypted_token)

        Navigator.replace(Routes.DASHBOARD_ROUTE)

    elif event == "SIGNED_OUT" or event == "USER_DELETED":
        Navigator.replace(Routes.HOME_ROUTE)


AuthProvider.supabaseClient.auth.on_auth_state_change(handle_auth_change)
