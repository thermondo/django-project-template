import os
import random

try:
    random = random.SystemRandom()
    using_sysrandom = True
except NotImplementedError:
    using_sysrandom = False

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def generate_secret_key():
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'

    if not using_sysrandom:
        print(
            'We could not find a secure pseudo-random number generator on your system. '
            'Please set your SECRET_KEY variable in .env manually.'
        )
        return ''
    return ''.join(random.choice(chars) for _ in range(50))


def _create_secret_key(env_path):
    with open(env_path) as f:
        file_ = f.read()

    secret_key = generate_secret_key()

    file_ = file_.replace(
        'DJANGO_SECRET_KEY=',
        f'DJANGO_SECRET_KEY="{secret_key}"'
    )

    with open(env_path, 'w') as f:
        f.write(file_)


def main():
    env_path = os.path.join(PROJECT_DIRECTORY, '.env')
    _create_secret_key(env_path)


if __name__ == "__main__":
    main()
