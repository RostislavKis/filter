#!/usr/bin/env python3
# mmdb_to_lst.py — конвертер GeoLite2-Country.mmdb → geoip-{cc}.lst
# MaxMind GeoLite2 требует бесплатную регистрацию на maxmind.com
#
# Использование:
#   python mmdb_to_lst.py --db GeoLite2-Country.mmdb --country RU
#   python mmdb_to_lst.py --db GeoLite2-Country.mmdb --country RU --output ../geo/geoip-ru.lst
#   python mmdb_to_lst.py --db GeoLite2-Country.mmdb --all  # все страны отдельными файлами

import argparse
import ipaddress
import os
import sys

try:
    import maxminddb
except ImportError:
    print('Установить: pip install maxminddb')
    sys.exit(1)


def mmdb_to_cidr_list(db_path, country_code):
    """Обойти дерево .mmdb, собрать все IPv4 сети для country_code.
    Возвращает список строк "1.2.3.0/24"."""
    cidrs = []
    with maxminddb.open_database(db_path) as reader:
        for ip_network, data in reader:
            if data is None:
                continue
            cc = (data.get('country') or data.get('registered_country') or {})
            iso = cc.get('iso_code', '')
            if iso == country_code:
                net = ipaddress.ip_network(ip_network)
                if net.version == 4:
                    cidrs.append(str(net))
    # Схлопнуть перекрывающиеся сети
    collapsed = list(ipaddress.collapse_addresses(
        ipaddress.ip_network(c) for c in cidrs))
    return [str(n) for n in sorted(collapsed)]


def get_all_countries(db_path):
    """Собрать уникальные ISO коды стран из .mmdb."""
    countries = set()
    with maxminddb.open_database(db_path) as reader:
        for _, data in reader:
            if not data:
                continue
            cc = (data.get('country') or
                  data.get('registered_country') or {}).get('iso_code')
            if cc:
                countries.add(cc)
    return sorted(countries)


def main():
    ap = argparse.ArgumentParser(
        description='MaxMind .mmdb → .lst конвертер для 4eburNet geo')
    ap.add_argument('--db', required=True,
        help='Путь к GeoLite2-Country.mmdb')
    ap.add_argument('--country', default='RU',
        help='ISO код страны (по умолчанию: RU)')
    ap.add_argument('--output',
        help='Выходной файл (по умолчанию: ../geo/geoip-{cc}.lst)')
    ap.add_argument('--all', action='store_true',
        help='Конвертировать все страны в отдельные файлы')
    args = ap.parse_args()

    if not os.path.exists(args.db):
        print(f'Ошибка: файл {args.db!r} не найден')
        sys.exit(1)

    out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'geo')
    out_dir = os.path.abspath(out_dir)
    os.makedirs(out_dir, exist_ok=True)

    if args.all:
        for cc in get_all_countries(args.db):
            cidrs = mmdb_to_cidr_list(args.db, cc)
            if len(cidrs) < 5:
                continue
            out = os.path.join(out_dir, f'geoip-{cc.lower()}.lst')
            tmp = out + '.tmp'
            with open(tmp, 'w') as f:
                f.write('\n'.join(cidrs) + '\n')
            os.replace(tmp, out)
            print(f'[OK] geoip-{cc.lower()}.lst: {len(cidrs)} CIDR')
    else:
        cc = args.country.upper()
        cidrs = mmdb_to_cidr_list(args.db, cc)
        out = args.output or os.path.join(out_dir, f'geoip-{cc.lower()}.lst')
        out = os.path.abspath(out)
        os.makedirs(os.path.dirname(out), exist_ok=True)
        tmp = out + '.tmp'
        with open(tmp, 'w') as f:
            f.write('\n'.join(cidrs) + '\n')
        os.replace(tmp, out)
        print(f'[OK] geoip-{cc.lower()}.lst: {len(cidrs)} CIDR → {out}')


if __name__ == '__main__':
    main()
