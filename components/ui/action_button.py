import flet as ft
from providers.authprovider import AuthProvider


from routes.routes import Routes


class ActionButton(ft.Container):
    def __init__(
        self,
        *,
        text: str,
        action: str,
        variant: str | None = None,
        **kwargs,
    ):
        super().__init__()

        self.text = text
        self.variant = variant
        self.action = action

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
        self.on_click = self.perform_action

    def perform_action(self, e):
        if self.action == "login":
            print("login")
            AuthProvider.email_login(e)

        elif self.action == "signup":
            pass
