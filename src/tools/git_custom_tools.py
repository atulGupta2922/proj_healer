from core import config
from exceptions.tool_exceptions import UnknownAppException


def get_repository_name_by_app_name(app_name: str):
    try:
        return config.app_repo_mapping[app_name]
    except KeyError:
        raise UnknownAppException(f"{app_name} app is not supported.")
    except Exception as e:
        raise e
