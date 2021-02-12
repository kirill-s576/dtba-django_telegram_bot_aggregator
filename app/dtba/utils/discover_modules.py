from ..config import DJANGO_SETTINGS
import os
import importlib
import inspect


def get_bot_interfaces():
    output_modules = []
    dirs = os.listdir(DJANGO_SETTINGS.BASE_DIR)
    for dir in dirs:
        module_path = f"{dir}.tg_bot"
        try:
            module = importlib.import_module(module_path)
            members = inspect.getmembers(module)
            for member in members:
                if member[1].__bases__[0].__name__ == 'BasicBotInterface':
                    output_modules.append(f"{module_path}.{member[1].__name__}")
        except:
            pass
    return output_modules
