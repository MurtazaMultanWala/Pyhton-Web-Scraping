from dynaconf import Dynaconf

settings = Dynaconf(load_dotenv=True, envvar_prefix=False)
env_variables = settings.as_dict()


class Config:
    os_type = env_variables.get("OS_TYPE", "Windows")
