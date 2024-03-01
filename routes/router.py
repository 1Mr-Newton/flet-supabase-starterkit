from routes.routes import Routes
from screens.auth_board import AuthBoard
from screens.auth_home import AuthHome
from screens.dashboard import Dashboard
from screens.login import Login
from screens.settings import Settings
from screens.signup import SignUP


ROUTER = {
    Routes.HOME_ROUTE: AuthHome,
    Routes.SIGNUP_ROUTE: SignUP,
    Routes.LOGIN_ROUTE: Login,
    Routes.DASHBOARD_ROUTE: Dashboard,
    Routes.SETTINGS_ROUTE: Settings,
    Routes.AUTH_BOARD_ROUTE: AuthBoard,
}
