import flet as ft
from providers.navigator import Navigator

from routes.routes import Routes


class AuthBoardingNavLinks(ft.Container):
    def __init__(self, *, isLogin: bool):
        super().__init__()
        self.isLogin = isLogin
        self.content = ft.Text(
            value="Already have an account?"
            if not self.isLogin
            else "Don't have an account?",
            color="black",
            spans=[
                ft.TextSpan(
                    text="Login" if not self.isLogin else "Sign Up",
                    on_click=lambda _: Navigator.push(
                        Routes.LOGIN_ROUTE if not self.isLogin else Routes.SIGNUP_ROUTE
                    ),
                ),
            ],
        )
