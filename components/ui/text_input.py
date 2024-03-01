import flet as ft
from constants.assets import Assets
from constants.colors import Colors
from providers.authprovider import AuthProvider
from providers.data_provider import DataProvider


class TextInput(ft.Container):
    def __init__(self, *, type_: str, placeholder: str, **kwargs):
        super().__init__()
        self.height = 50

        self.hideShowRef = ft.Ref()
        self.inputRef = ft.Ref()

        self.bgcolor = "white"
        self.placeholder = placeholder
        self.type_ = type_
        self.border_radius = 10

        self.padding = ft.padding.only(right=10) if self.type_ == "password" else None
        self.border = ft.border.all(
            width=1,
            color=Colors.OUTLINE,
        )
        self.alignment = ft.alignment.center
        self.content = ft.Row(
            spacing=0,
            expand=True,
            controls=[
                ft.TextField(
                    expand=True,
                    hint_text=self.placeholder,
                    hint_style=ft.TextStyle(
                        color=Colors.HINT_TEXT,
                        weight=ft.FontWeight.W_400,
                    ),
                    keyboard_type=ft.KeyboardType.EMAIL
                    if self.type_ == "email"
                    else ft.KeyboardType.TEXT,
                    content_padding=ft.padding.symmetric(horizontal=10),
                    text_style=ft.TextStyle(
                        size=16,
                        color=Colors.BLACK,
                    ),
                    border=ft.InputBorder.NONE,
                    focused_bgcolor=ft.colors.TRANSPARENT,
                    focused_border_color=ft.colors.TRANSPARENT,
                    focused_border_width=0,
                    border_width=0,
                    ref=self.inputRef,
                    password=False if self.type_ == "email" else True,
                    autofocus=True,
                    on_blur=self.on_blur,
                    on_change=self.on_change,
                ),
                ft.Container(
                    content=ft.Image(
                        src=Assets.SHOW,
                        width=20,
                        height=20,
                        ref=self.hideShowRef,
                    ),
                    on_click=self.toggleShowHidePassword,
                )
                if self.type_ == "password"
                else ft.Container(),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        )

    def toggleShowHidePassword(self, e):
        if self.inputRef.current.password:
            self.inputRef.current.password = False
            self.hideShowRef.current.src = Assets.HIDE
        else:
            self.inputRef.current.password = True
            self.hideShowRef.current.src = Assets.SHOW

        self.inputRef.current.update()
        self.hideShowRef.current.update()

    def on_change(self, event):
        if self.type_ == "email":
            DataProvider.update("email", self.inputRef.current.value)

    def on_blur(self, e):
        if self.type_ == "email":
            DataProvider.update("email", self.inputRef.current.value)
            # self.auth.email = self.inputRef.current.value
        elif self.type_ == "password":
            pass
            # self.auth.password = self.inputRef.current.value
