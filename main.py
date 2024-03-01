from urllib.parse import parse_qs, urlparse
import flet as ft
from providers.authprovider import AuthProvider
from providers.navigator import Navigator
from routes.router import ROUTER
from routes.routes import Routes


class Main:
    def __init__(self, page: ft.Page):
        self.page = page
        AuthProvider.update_page(page)
        Navigator.update_page(page)

        self.page.on_route_change = self.route_change
        self.page.on_view_pop = self.view_pop

        self.page.views.clear()
        AuthProvider.is_signed_in()
        # Navigator.push(Routes.AUTH_BOARD_ROUTE)

    def route_change(self, route):
        _route = urlparse(route.route)
        params = parse_qs(_route.query)
        path = _route.path
        new_view = ROUTER.get(path)
        print(path)

        clear = params.get("clear", [False])[0]

        if clear:
            self.page.views.clear()

        if not new_view:
            Navigator.replace(Routes.NOT_FOUND_ROUTE)

        elif len(self.page.views) == 0:
            self.page.views.append(new_view(**params))

        elif self.page.views[-1].route != new_view(**params).route:
            self.page.views.append(new_view(**params))

    def view_pop(self, event):
        self.page.views.pop()
        top_view = self.page.views[-1]
        self.page.go(top_view.route)


ft.app(Main, assets_dir="assets")
