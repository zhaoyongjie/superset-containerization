import os
from typing import Optional

from cachelib.redis import RedisCache

LOG_FORMAT = "[%(thread)s]:%(asctime)s:%(levelname)s:%(process)d:%(name)s:%(message)s"
LOG_LEVEL = "INFO"


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

# Caching
REDIS_HOST = get_env_variable("REDIS_HOST")
REDIS_PORT = get_env_variable("REDIS_PORT")
REDIS_CELERY_DB = get_env_variable("REDIS_CELERY_DB", "0")
REDIS_RESULTS_DB = get_env_variable("REDIS_RESULTS_DB", "1")

CACHE_CONFIG = {
    "CACHE_TYPE": "redis",
    "CACHE_DEFAULT_TIMEOUT": 60 * 60,  # 1 hour
    "CACHE_KEY_PREFIX": "superset_",
    "CACHE_REDIS_HOST": REDIS_HOST,
    "CACHE_REDIS_PORT": REDIS_PORT,
    "CACHE_REDIS_DB": REDIS_RESULTS_DB,
}
DATA_CACHE_CONFIG = CACHE_CONFIG
FILTER_STATE_CACHE_CONFIG = CACHE_CONFIG
EXPLORE_FORM_DATA_CACHE_CONFIG = CACHE_CONFIG

# Security
SECRET_KEY = get_env_variable("SECRET_KEY")
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

    # Dashboards
    "DASHBOARD_NATIVE_FILTERS": True,
    "DASHBOARD_CROSS_FILTERS": True,
    "DASHBOARD_NATIVE_FILTERS_SET": True,
    "DASHBOARD_RBAC": True,

    # Explore
    "ENABLE_TEMPLATE_PROCESSING": True,
    "UX_BETA": True,
    "GENERIC_CHART_AXES": True,
    "DRILL_TO_DETAIL": True,
    "DATAPANEL_CLOSED_BY_DEFAULT": True,

    "EMBEDDED_SUPERSET": True,

    "GLOBAL_ASYNC_QUERIES": True,
}

# Embedded Dashboards
GUEST_TOKEN_JWT_EXP_SECONDS = 2 * 24 * 60 * 60  # 2 days


# Celery Worker(SQLLab query a database through Celery worker rather than web processing)
class CeleryConfig(object):
    broker_url = f"redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_CELERY_DB}"
    imports = ("superset.sql_lab",)
    result_backend = f"redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_RESULTS_DB}"
    worker_prefetch_multiplier = 1
    task_acks_late = False


CELERY_CONFIG = CeleryConfig
RESULTS_BACKEND = RedisCache(
    host=REDIS_HOST,
    port=REDIS_PORT,
    db=REDIS_RESULTS_DB,
)

# Global async query config
GLOBAL_ASYNC_QUERIES_REDIS_CONFIG = {
    "port": REDIS_PORT,
    "host": REDIS_HOST,
    "db": 2,
}
GLOBAL_ASYNC_QUERIES_JWT_SECRET = get_env_variable("GLOBAL_ASYNC_QUERIES_JWT_SECRET")
