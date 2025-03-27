import os
import dotenv
from pathlib import Path


def load_env(env_param_key: str) -> str:
    project_root = Path(__file__).resolve().parent.parent
    dotenv_path = project_root / ".env"

    try:
        dotenv.load_dotenv(dotenv_path)
        env_param_body = os.environ.get(env_param_key)
        if env_param_body is None:
            print(f"Warning: Environment variable '{env_param_key}' not found")

        return env_param_body

    except FileNotFoundError:
        print(f"Error: .env file not found at {dotenv_path}")
        return None
    except Exception as e:
        print(f"Unexpected error loading environment variables: {e}")
        return None


def set_env(env_param_key: str, env_param_body: str) -> None:
    project_root = Path(__file__).resolve().parent.parent
    dotenv_path = project_root / ".env"

    try:
        dotenv.set_key(str(dotenv_path), env_param_key, env_param_body)
        print(f"Successfully set {env_param_key} in .env file")

    except Exception as e:
        print(f"Error setting environment variable: {e}")
