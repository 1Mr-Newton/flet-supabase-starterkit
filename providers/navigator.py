import flet as ft


class Navigator:
    page: ft.Page | None = None

    @classmethod
    def update_page(cls, page):
        cls.page = page

    @classmethod
    def push(cls, path: str, **params):
        if not cls.page:
            raise Exception("Page attribute for Navigator not initialized")
        cls.page.go(path, **params)

    @classmethod
    def replace(cls, path: str, **params):
        if not cls.page:
            raise Exception("Page attribute for Navigator not initialized")
        cls.page.go(path, clear=True, **params)
