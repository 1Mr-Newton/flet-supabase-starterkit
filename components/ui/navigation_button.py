import flet as ft
from providers.authprovider import AuthProvider
from providers.navigator import Navigator

from routes.routes import Routes


class NavigationButton(ft.Container):
    def __init__(
        self,
        *,
        path: str,
        text: str,
        variant: str | None = None,
        isLogin: bool,
        # **kwargs
    ):
        super().__init__()
        self.text = text
        self.path = path
        self.isLogin = isLogin

        self.variant = variant

        self.alignment = ft.alignment.center
        self.content = ft.Text(
            value=self.text,
            color="white" if self.variant == "filled" else "black",
        )
        self.padding = ft.padding.symmetric(vertical=15, horizontal=20)
        self.border_radius = 10
        self.border = ft.border.all(color="black", width=0.5)
        self.margin = ft.margin.only(top=10)
        self.bgcolor = "black" if variant == "filled" else None
        self.on_click = lambda e: Navigator.push(self.path, isLogin=self.isLogin)
