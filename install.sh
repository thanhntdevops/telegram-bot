#!/bin/bash
set -e
SHELL_DIR="$(cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
#echo $SHELL_DIR
mkdir /srv/telegrambot/
cp $SHELL_DIR/private-variable /srv/telegrambot/
cp $SHELL_DIR/requirements.txt /srv/telegrambot/
cp $SHELL_DIR/telegram-bot.py /srv/telegrambot/
cp $SHELL_DIR/telegram-bot.service /etc/systemd/system/
cd /srv/telegrambot/
python3 -m venv .venv
.venv/bin/pip3 install -r requirements.txt
systemctl daemon-reload
systemctl start telegram-bot.service
systemctl enable telegram-bot.service
