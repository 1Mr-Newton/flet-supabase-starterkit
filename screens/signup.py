import flet as ft
from components.already_have_account import AuthBoardingNavLinks
from components.ui.action_button import ActionButton
from components.ui.text_input import TextInput
from constants.assets import Assets
from constants.colors import Colors
from providers.authprovider import AuthProvider
from providers.data_provider import DataProvider
from routes.routes import Routes


class SignUP(ft.View):
    def __init__(self, **kwargs):
        super().__init__(route=Routes.SIGNUP_ROUTE)
        self.bgcolor = "white"
        self.controls = [
            ft.SafeArea(
                expand=True,
                content=ft.Container(
                    expand=True,
                    bgcolor=Colors.BACKGROUND,
                    border_radius=20,
                    padding=15,
                    content=ft.Column(
                        alignment=ft.MainAxisAlignment.SPACE_AROUND,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            ft.Image(
                                Assets.ILLUSTRATION_DARK,
                            ),
                            ft.Text(
                                "Create Account",
                                size=30,
                                weight=ft.FontWeight.W_900,
                                color="black",
                                text_align=ft.TextAlign.CENTER,
                            ),
                            ft.Container(
                                ft.Column(
                                    controls=[
                                        TextInput(
                                            type_="email",
                                            placeholder="Email",
                                        ),
                                        TextInput(
                                            type_="password",
                                            placeholder="Password",
                                        ),
                                        TextInput(
                                            type_="password",
                                            placeholder="Confirm Password",
                                        ),
                                    ]
                                )
                            ),
                            ActionButton(
                                text="Create Account",
                                variant="filled",
                                action="login",
                            ),
                            AuthBoardingNavLinks(isLogin=False),
                        ],
                        scroll=ft.ScrollMode.AUTO,
                    ),
                    alignment=ft.alignment.center,
                ),
            ),
        ]
