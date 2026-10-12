import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path

LOG_PATTERN = re.compile(
    r'^(?P<ip>\S+)\s+-\s+-\s+'
    r'\[(?P<time>[^\]]+)\]\s+'
    r'"(?P<request>[^"]*)"\s+'
    r'(?P<status>\d{3})\s+'
    r'(?P<bytes>\S+)\s+'
    r'"(?P<referer>[^"]*)"\s+'
    r'"(?P<user_agent>[^"]*)"\s+'
    r'(?P<duration>\d+)\s*$')

HTTP_METHODS = ["GET", "POST", "PUT", "DELETE", "OPTIONS", "HEAD"]


def parse_line(line: str):
    match = LOG_PATTERN.match(line.strip())
    if match is None:
        return None
    data = match.groupdict()
    request_parts = data["request"].split()
    if len(request_parts) >= 2:
        method = request_parts[0].upper()
        url = request_parts[1]
    elif len(request_parts) == 1:
        method = request_parts[0].upper()
        url = "-"
    else:
        method = "-"
        url = "-"
    return {
        "ip": data["ip"],
        "time": data["time"],
        "method": method,
        "url": url,
        "status": data["status"],
        "bytes": data["bytes"],
        "referer": data["referer"],
        "user_agent": data["user_agent"],
        "duration": int(data["duration"])}


def analyze_log_file(file_path: Path) -> dict:
    total_requests = 0
    method_counter = Counter()
    ip_counter = Counter()
    slow_requests = []
    with open(file_path, "r", encoding="utf-8", errors="replace") as f:
        for line in f:
            if not line.strip():
                continue
            parsed = parse_line(line)
            if parsed is None:
                continue
            total_requests += 1
            method_counter[parsed["method"]] += 1
            ip_counter[parsed["ip"]] += 1
            slow_requests.append({
                "method": parsed["method"],
                "url": parsed["url"],
                "ip": parsed["ip"],
                "duration_ms": parsed["duration"],
                "time": parsed["time"]})

    methods_stats = {m: method_counter.get(m, 0) for m in HTTP_METHODS}

    top_ips = [
        {"ip": ip, "requests": count}
        for ip, count in ip_counter.most_common(3)]

    top_slow = sorted(
        slow_requests, key=lambda x: x["duration_ms"], reverse=True)[:3]

    return {
        "file": str(file_path),
        "total_requests": total_requests,
        "methods": methods_stats,
        "top_ips": top_ips,
        "top_slow_requests": top_slow}


def save_statistics(stats: dict, output_dir: Path) -> Path:
    log_file = Path(stats["file"])
    output_file = output_dir / f"{log_file.stem}_stats.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(stats, f, ensure_ascii=False, indent=4)
    return output_file


def print_statistics(stats: dict) -> None:
    print("=" * 70)
    print(f"Файл: {stats['file']}")
    print("=" * 70)
    print(f"Общее количество запросов: {stats['total_requests']}")
    print()
    print("Количество запросов по HTTP-методам:")
    for method, count in stats["methods"].items():
        print(f"  {method:<8} — {count}")
    print()
    print("Топ-3 IP-адресов по количеству запросов:")
    if stats["top_ips"]:
        for i, item in enumerate(stats["top_ips"], start=1):
            print(f"  {i}. {item['ip']} — {item['requests']} запросов")
    else:
        print("  Нет данных")
    print()
    print("Топ-3 самых долгих запросов:")
    if stats["top_slow_requests"]:
        for i, req in enumerate(stats["top_slow_requests"], start=1):
            print(f"  {i}. Метод: {req['method']}")
            print(f"     URL:          {req['url']}")
            print(f"     IP:           {req['ip']}")
            print(f"     Длительность: {req['duration_ms']} мс")
            print(f"     Дата и время: {req['time']}")
            print()
    else:
        print("  Нет данных")
    print()


def collect_log_files(path: Path):
    if path.is_file():
        return [path]
    if path.is_dir():
        return sorted(
            p for p in path.iterdir() if p.is_file() and p.suffix.lower() == ".log")
    return []


def main():
    parser = argparse.ArgumentParser(
        description="Анализ логов веб-сервера Apache (access.log).")
    parser.add_argument(
        "-p", "--path",
        type=str,
        default=r"D:\Учеба\Python\Log",
        help=r"Путь к директории с логами или к конкретному файлу "
             r"(по умолчанию: D:\Учеба\Python\Log)")
    parser.add_argument("-o", "--output",
                        type=str,
                        default=None,
                        help="Директория для сохранения JSON-файлов со статистикой "
                             "(по умолчанию: рядом с лог-файлами)")
    args = parser.parse_args()
    target_path = Path(args.path)
    if not target_path.exists():
        print(f"[ОШИБКА] Путь не существует: {target_path}", file=sys.stderr)
        sys.exit(1)
    log_files = collect_log_files(target_path)
    if not log_files:
        print(
            f"[ПРЕДУПРЕЖДЕНИЕ] В {target_path} не найдено лог-файлов (*.log)",
            file=sys.stderr)
        sys.exit(0)
    output_dir = Path(args.output) if args.output else (
        target_path if target_path.is_dir() else target_path.parent)
    output_dir.mkdir(parents=True, exist_ok=True)
    print(f"[ИНФО] Найдено лог-файлов: {len(log_files)}\n")
    for log_file in log_files:
        try:
            stats = analyze_log_file(log_file)
        except OSError as e:
            print(f"[ОШИБКА] Не удалось прочитать {log_file}: {e}",
                  file=sys.stderr)
            continue
        print_statistics(stats)
        out = save_statistics(stats, output_dir)
        print(f"[OK] Статистика сохранена: {out}\n")


if __name__ == "__main__":
    main()
