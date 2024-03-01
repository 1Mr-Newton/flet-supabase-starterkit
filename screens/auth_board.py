import flet as ft
from components.already_have_account import AuthBoardingNavLinks
from components.ui.provider_btn import ProviderBtn
from constants.assets import Assets
from providers.authprovider import AuthProvider
from providers.data_provider import DataProvider
from providers.navigator import Navigator
from routes.routes import Routes


class AuthBoard(ft.View):
    def __init__(self, **kwargs):
        super().__init__(route=Routes.AUTH_BOARD_ROUTE)

        self.isLogin = kwargs.get("isLogin", ["False"])[0] == "True"

        self.bgcolor = "white"
        self.controls = [
            ft.SafeArea(
                expand=True,
                content=ft.Column(
                    controls=[
                        ft.Container(
                            expand=True,
                            bgcolor="#F0F3FB",
                            border_radius=20,
                            padding=20,
                            content=ft.Column(
                                controls=[
                                    ft.Image(
                                        src=Assets.ILLUSTRATION_DARK,
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
                                    ft.Container(
                                        content=ft.Column(
                                            controls=[
                                                ProviderBtn(
                                                    provider="google",
                                                    icon=Assets.GOOGLE,
                                                    isLogin=self.isLogin,
                                                ),
                                                ProviderBtn(
                                                    provider="github",
                                                    icon=Assets.GITHUB,
                                                    isLogin=self.isLogin,
                                                ),
                                                ProviderBtn(
                                                    provider="email",
                                                    icon=Assets.EMAIL,
                                                    isLogin=self.isLogin,
                                                ),
                                            ],
                                        ),
                                    ),
                                ],
                            ),
                        ),
                        ft.Container(
                            margin=ft.margin.only(top=20),
                            content=ft.Row(
                                spacing=0,
                                controls=[
                                    ft.Text(
                                        "Already have an account?",
                                        color="black",
                                    ),
                                    ft.Text(
                                        "Login",
                                        color="black",
                                    ),
                                ],
                                alignment=ft.MainAxisAlignment.CENTER,
                                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                            ),
                        ),
                        AuthBoardingNavLinks(isLogin=self.isLogin),
                    ],
                ),
            ),
        ]
