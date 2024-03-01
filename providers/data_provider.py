import flet as ft


class DataProvider:
    email: str = "test@gmail.com"
    password: str = "123456789"

    @classmethod
    def update(cls, attribute_name, new_value):
        if hasattr(cls, attribute_name):
            setattr(cls, attribute_name, new_value)
        else:
            setattr(cls, attribute_name, new_value)

    @classmethod
    def get(cls, attribute_name):
        if hasattr(cls, attribute_name):
            return getattr(cls, attribute_name)
        else:
            raise AttributeError(
                f"'{cls.__name__}' object has no attribute '{attribute_name}'"
            )

    @classmethod
    def get_all(cls):
        return {
            attr: getattr(cls, attr)
            for attr in dir(cls)
            if not callable(getattr(cls, attr)) and not attr.startswith("__")
        }
