# filter

Коллекция наборов правил для систем проксирования и маршрутизации трафика (Clash, Surge, Shadowrocket, Quantumult X и аналогичных).

## Что это

Правила позволяют настроить умную маршрутизацию: трафик к определённым сервисам направляется через прокси, остальное — напрямую. Используется для обхода блокировок и разделения трафика по категориям.

## Форматы файлов

**YAML** (`*.yaml`) — детальные правила для конкретных сервисов, содержат:

- `DOMAIN-SUFFIX` / `DOMAIN-KEYWORD` — правила по доменам
- `IP-CIDR` / `IP-CIDR6` — правила по IP-адресам
- `IP-ASN` — правила по автономным системам
- `PROCESS-NAME` — правила по имени процесса

**TXT** (`*.txt`) — простые списки доменов/IP для других форматов маршрутизаторов.

## Содержимое

| Файл | Описание |
| ---- | -------- |
| `telegram.yaml` | Telegram и клиенты (Nekogram, Nagram и др.) |
| `youtube.yaml` / `youtube.txt` | YouTube и связанные домены |
| `discord-domain.yaml` / `discord-ip.yaml` | Discord (домены и IP раздельно) |
| `microsoft.yaml` | Сервисы Microsoft |
| `openai.yaml` | OpenAI / ChatGPT |
| `gemini.yaml` | Google Gemini |
| `instagram.yaml` | Instagram |
| `twitter.yaml` | Twitter / X |
| `facebook.yaml` | Facebook / Meta |
| `whatsapp.yaml` | WhatsApp |
| `steam.yaml` | Steam |
| `notion.yaml` | Notion |
| `oracle.yaml` | Oracle Cloud |
| `xiaomi.yaml` | Сервисы Xiaomi |
| `anime-trackers.yaml` | Аниме-торрент-трекеры |
| `ru-blocked.yaml` | Сайты, заблокированные в России (медиа, VPN, торренты и др.) |
| `social.txt` | Социальные сети |
| `video.txt` | Видеосервисы |
| `music.txt` | Музыкальные сервисы |
| `games.txt` | Игровые сервисы |
| `news.txt` | Новостные сайты |
| `anime.txt` | Аниме-сайты |
| `torrent.txt` | Торрент-трекеры |
| `porn.txt` | 18+ контент |
| `casino.txt` | Казино и азартные игры |
| `shop.txt` | Интернет-магазины |
| `education.txt` | Образовательные ресурсы |
| `messengers.txt` | Мессенджеры |
| `art.txt` | Арт-платформы |
| `tools.txt` | Инструменты и утилиты |
| `jetbrains.txt` | Сервисы JetBrains |

## Источники

Часть правил основана на репозитории [blackmatrix7/ios_rule_script](https://github.com/blackmatrix7/ios_rule_script).
