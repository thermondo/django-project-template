#!/usr/bin/env bash

set -eo pipefail

BIN_DIR=$(cd "$(dirname "$0")"; pwd)
PYTHON=$(which python3)
DISABLE_RELEASE=${DISABLE_RELEASE:-"0"}
DISABLE_MIGRATIONS=${DISABLE_MIGRATIONS:-"0"}


source "$BIN_DIR/utils.sh"

if [ "$DISABLE_RELEASE" -ne "0" ]; then
    puts-warn "Skipping release because \$DISABLE_RELEASE is set."
    puts-step "Done!"
    exit 0
fi

if [ "$DISABLE_MIGRATIONS" -eq "0" ]; then
    puts-step "Running migrations"
    ${PYTHON} manage.py migrate --no-input | indent
else
    puts-warn "Skipping migrations because \$DISABLE_MIGRATIONS is set."
fi

puts-step "Done!"
