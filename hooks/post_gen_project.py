import os
import secrets

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def _create_and_set_local_secret_key():
    """Generate and set `SECRET_KEY` for development use."""
    env_path = os.path.join(PROJECT_DIRECTORY, '.env')
    with open(env_path) as f:
        file_ = f.read()

    secret_key = secrets.token_urlsafe(50)

    file_ = file_.replace(
        'DJANGO_SECRET_KEY=',
        f'DJANGO_SECRET_KEY="{secret_key}"'
    )

    with open(env_path, 'w') as f:
        f.write(file_)


def main():
    _create_and_set_local_secret_key()


if __name__ == "__main__":
    main()
