import subprocess
import sys
from datetime import datetime
from collections import defaultdict


def parse_ps_aux():
    try:
        result = subprocess.run(['ps', 'aux'], capture_output=True, text=True, check=True)
        lines = result.stdout.strip().split('\n')
        if not lines:
            return []
        processes = []
        for line in lines[1:]:
            parts = line.split()
            if len(parts) < 11:
                continue
            process = {
                'user': parts[0],
                'pid': int(parts[1]),
                'cpu': float(parts[2]),
                'mem': float(parts[3]),
                'command': ' '.join(parts[10:])
            }
            processes.append(process)
        return processes
    except subprocess.CalledProcessError as e:
        sys.stderr.write(f"Ошибка при выполнении ps aux: {e}\n")
        return []
    except Exception as e:
        sys.stderr.write(f"Неожиданная ошибка: {e}\n")
        return []


def format_process_name(name, max_length=20):
    if len(name) > max_length:
        return name[:max_length] + '...'
    return name


def generate_report(processes):
    if not processes:
        return "Нет данных о процессах"
    users = sorted(set(p['user'] for p in processes))
    user_process_count = defaultdict(int)
    for p in processes:
        user_process_count[p['user']] += 1
    total_processes = len(processes)
    total_cpu = sum(p['cpu'] for p in processes)
    total_mem = sum(p['mem'] for p in processes)
    max_cpu_process = max(processes, key=lambda p: p['cpu'])
    max_mem_process = max(processes, key=lambda p: p['mem'])
    report_lines = []
    report_lines.append("Отчёт о состоянии системы:")
    report_lines.append(f"Пользователи системы: {', '.join(users)}")
    report_lines.append(f"Процессов запущено: {total_processes}")
    report_lines.append("")
    report_lines.append("Пользовательских процессов:")
    for user in sorted(user_process_count.keys()):
        report_lines.append(f"{user}: {user_process_count[user]}")
    report_lines.append("")
    report_lines.append(f"Всего памяти используется: {total_mem:.1f}%")
    report_lines.append(f"Всего CPU используется: {total_cpu:.1f}%")
    report_lines.append(f"Больше всего памяти использует: {format_process_name(max_mem_process['command'])}")
    report_lines.append(f"Больше всего CPU использует: {format_process_name(max_cpu_process['command'])}")
    return '\n'.join(report_lines)


def save_report(report_content):
    now = datetime.now()
    filename = now.strftime("%d-%m-%Y-%H-%M.txt")
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(report_content)
        sys.stdout.write(f"Отчёт сохранён в файл: {filename}\n")
        return filename
    except Exception as e:
        sys.stderr.write(f"Ошибка при сохранении файла: {e}\n")
        return None


def print_report(report):
    separator = "=" * 50
    sys.stdout.write(f"\n{separator}\n")
    sys.stdout.write(report)
    sys.stdout.write(f"\n{separator}\n\n")


def main():
    sys.stdout.write("Сбор информации о процессах...\n")
    processes = parse_ps_aux()
    if not processes:
        sys.stderr.write("Не удалось получить данные о процессах\n")
        sys.exit(1)
    report = generate_report(processes)
    print_report(report)
    save_report(report)


if __name__ == "__main__":
    main()
