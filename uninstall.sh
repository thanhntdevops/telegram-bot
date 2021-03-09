#!/bin/bash

systemctl stop telegram-bot.service
systemctl disable telegram-bot.service
rm -rf /srv/telegrambot/
rm /etc/systemd/system/telegram-bot.service
