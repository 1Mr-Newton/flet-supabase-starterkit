import flet as ft
from providers.authprovider import AuthProvider
from providers.data_provider import DataProvider
from routes.routes import Routes


class Settings(ft.View):
    def __init__(self, **kwargs):
        super().__init__(route=Routes.SETTINGS_ROUTE)
        self.appbar = ft.AppBar(
            title=ft.Text("Settings"),
            actions=[
                ft.IconButton(
                    icon="logout",
                    on_click=AuthProvider.logout,
                )
            ],
        )

        self.controls = [ft.Text("settings")]
