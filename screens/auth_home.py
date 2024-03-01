import flet as ft
from components.ui.navigation_button import NavigationButton
from constants.assets import Assets
from providers.authprovider import AuthProvider
from providers.data_provider import DataProvider
from routes.routes import Routes


class AuthHome(ft.View):
    def __init__(self, **kwargs):
        super().__init__(route=Routes.HOME_ROUTE)

        # print("Auth Home params", kwargs)

        self.controls = [ft.Text("Auth Home")]

        self.bgcolor = "white"

        self.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.spacing = 0
        self.expand = True

        self.controls = [
            ft.SafeArea(
                expand=True,
                content=ft.Column(
                    scroll=ft.ScrollMode.AUTO,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    alignment=ft.MainAxisAlignment.SPACE_AROUND,
                    controls=[
                        ft.Container(
                            content=ft.Image(
                                src=Assets.ILLUSTRATION_DARK,
                                width=200,
                            ),
                        ),
                        ft.Column(
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            controls=[
                                ft.Text(
                                    "Explore the app",
                                    size=30,
                                    weight=ft.FontWeight.W_900,
                                    color="black",
                                ),
                                ft.Text(
                                    "Now your finances are in one place and always under control",
                                    size=20,
                                    color="black",
                                    text_align=ft.TextAlign.CENTER,
                                    opacity=0.7,
                                ),
                            ],
                        ),
                        ft.Column(
                            controls=[
                                NavigationButton(
                                    text="Login",
                                    path=Routes.AUTH_BOARD_ROUTE,
                                    variant="filled",
                                    isLogin=True,
                                ),
                                NavigationButton(
                                    text="Create Account",
                                    path=Routes.AUTH_BOARD_ROUTE,
                                    variant="outlined",
                                    isLogin=False,
                                ),
                            ],
                        ),
                    ],
                ),
            )
        ]
