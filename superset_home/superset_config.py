import logging
import os
from typing import Optional

logger = logging.getLogger()
LOG_FORMAT = "[%(thread)s]:%(asctime)s:%(levelname)s:%(process)d:%(name)s:%(message)s"


def get_env_variable(var_name: str, default: Optional[str] = None) -> str:
    """Get the environment variable or raise exception."""
    try:
        return os.environ[var_name]
    except KeyError:
        if default is not None:
            return default
        else:
            error_msg = "The environment variable {} was missing, abort...".format(
                var_name
            )
            raise EnvironmentError(error_msg)


DATABASE_DIALECT = get_env_variable("DATABASE_DIALECT")
DATABASE_USER = get_env_variable("DATABASE_USER")
DATABASE_PASSWORD = get_env_variable("DATABASE_PASSWORD")
DATABASE_HOST = get_env_variable("DATABASE_HOST")
DATABASE_PORT = get_env_variable("DATABASE_PORT")
DATABASE_DB = get_env_variable("DATABASE_DB")

# The SQLAlchemy connection string.
SQLALCHEMY_DATABASE_URI = "%s://%s:%s@%s:%s/%s" % (
    DATABASE_DIALECT,
    DATABASE_USER,
    DATABASE_PASSWORD,
    DATABASE_HOST,
    DATABASE_PORT,
    DATABASE_DB,
)

REDIS_HOST = get_env_variable("REDIS_HOST")
REDIS_PORT = get_env_variable("REDIS_PORT")

CACHE_CONFIG = {
    "CACHE_TYPE": "redis",
    "CACHE_DEFAULT_TIMEOUT": 300,
    "CACHE_KEY_PREFIX": "superset_",
    "CACHE_REDIS_HOST": REDIS_HOST,
    "CACHE_REDIS_PORT": REDIS_PORT,
}
DATA_CACHE_CONFIG = CACHE_CONFIG
FILTER_STATE_CACHE_CONFIG = CACHE_CONFIG
EXPLORE_FORM_DATA_CACHE_CONFIG = CACHE_CONFIG

# Security
SECRET_KEY = "HbJUf96F9swUYq5YCBOUZ3clkYQFqSTm6AJbL97T9ZVkSAO+XzVuZae2"
CONTENT_SECURITY_POLICY_WARNING = False
ENABLE_CORS = True
CORS_OPTIONS = {
    'supports_credentials': True,
    'allow_headers': ['*'],
    'resources': ['*'],
    'origins': ['*']
}
AUTH_ROLE_PUBLIC = "Gamma"

# Feature Flags
FEATURE_FLAGS = {
    "DISABLE_LEGACY_DATASOURCE_EDITOR": False,

    "DASHBOARD_NATIVE_FILTERS": True,
    "DASHBOARD_CROSS_FILTERS": True,
    "DASHBOARD_NATIVE_FILTERS_SET": True,
    "DASHBOARD_RBAC": True,

    "ENABLE_TEMPLATE_PROCESSING": True,
    "UX_BETA": True,
    "GENERIC_CHART_AXES": True,
    "DRILL_TO_DETAIL": True,
    "DATAPANEL_CLOSED_BY_DEFAULT": True,

    "EMBEDDED_SUPERSET": True,
}

GUEST_TOKEN_JWT_EXP_SECONDS = 2 * 24 * 60 * 60  # 2 days
