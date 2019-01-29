import os
import secrets

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def _create_and_set_local_secret_key():
    """Generate and set `SECRET_KEY` for development use."""
    with open(os.path.join(PROJECT_DIRECTORY, '.env'), 'a') as fs:
        fs.write(f'DJANGO_SECRET_KEY={secrets.token_urlsafe(50)}\n')


def main():
    _create_and_set_local_secret_key()


if __name__ == "__main__":
    main()
