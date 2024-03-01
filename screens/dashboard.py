import flet as ft
from providers.authprovider import AuthProvider
from providers.data_provider import DataProvider
from providers.navigator import Navigator
from routes.routes import Routes


class Dashboard(ft.View):
    def __init__(self, **kwargs):
        super().__init__(route=Routes.DASHBOARD_ROUTE)
        self.appbar = ft.AppBar(
            title=ft.Text("Dashboard"),
            actions=[
                ft.IconButton(
                    icon="logout",
                    on_click=AuthProvider.logout,
                )
            ],
        )

        self.controls = [
            ft.Text("dashboard"),
            ft.ElevatedButton(
                "Settings",
                on_click=lambda _: Navigator.push(Routes.SETTINGS_ROUTE),
            ),
        ]
