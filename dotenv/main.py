import os

from dotenv import dotenv_values, load_dotenv

load_dotenv(".env")

user_id = os.environ.get("_UID")
base_url = os.environ.get("BASE_URL")

print(user_id)
print(base_url)


env_variables = dotenv_values(".env")
print(env_variables)
print(env_variables["_VERSION"])
