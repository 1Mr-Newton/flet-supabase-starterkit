import flet as ft
from providers.authprovider import AuthProvider
from providers.navigator import Navigator
from gotrue.types import Provider
from routes.routes import Routes


class ProviderBtn(ft.Container):
    def __init__(
        self,
        *,
        provider: Provider,
        icon: str,
        isLogin: bool,
        # **kwargs,
    ):
        super().__init__()

        self.isLogin = isLogin
        self.provider: Provider = provider
        self.icon = icon

        self.border = ft.border.all(width=1, color="#D8DADC")
        self.on_click = self.handle_signup
        self.border_radius = 20
        self.bgcolor = "#ffffff"
        self.padding = ft.padding.symmetric(vertical=15, horizontal=20)
        self.alignment = ft.alignment.center

        if self.isLogin:
            self.btn_text = f"Login with {self.provider.title()}"
        else:
            self.btn_text = f"Sign Up with {self.provider.title()}"

        self.content = ft.Row(
            controls=[
                ft.Image(
                    src=self.icon,
                    height=20,
                    width=20,
                    fit=ft.ImageFit.CONTAIN,
                ),
                ft.Text(
                    self.btn_text,
                    color="black",
                    weight=ft.FontWeight.W_500,
                    size=14,
                ),
            ]
        )

    def handle_signup(self, event):
        if self.provider == "email" and not self.isLogin:
            Navigator.push(Routes.SIGNUP_ROUTE)

        elif self.provider == "email" and self.isLogin:
            Navigator.push(Routes.LOGIN_ROUTE)

        else:
            AuthProvider.oauth_login(self.provider)
