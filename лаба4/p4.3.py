import psutil
import sqlite3
from datetime import datetime
import time

DB_NAME = 'system_monitor.db'

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS system_stats (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            cpu_usage REAL,
            memory_usage REAL,
            disk_usage REAL
        )
    ''')
    conn.commit()
    conn.close()

def save_stats(timestamp, cpu, memory, disk):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO system_stats (timestamp, cpu_usage, memory_usage, disk_usage)
        VALUES (?, ?, ?, ?)
    ''', (timestamp, cpu, memory, disk))
    conn.commit()
    conn.close()

def fetch_all_stats():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM system_stats')
    rows = cursor.fetchall()
    conn.close()
    return rows

def get_system_stats():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    return cpu, memory, disk

def main():
    init_db()
    while True:
        print("\n---СИСТЕМНЫЙ_МОНИТОР---")
        print("1. Сделать замер и сохранить")
        print("2. Показать сохраненные данные")
        print("0. Выйти")
        choice = input("Выбор действия: ")

        if choice == '1':
            cpu, memory, disk = get_system_stats()
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            save_stats(timestamp, cpu, memory, disk)
            print(f"[{timestamp}] CPU: {cpu}% | RAM: {memory}% | Disk: {disk}%")

        elif choice == '2':
            rows = fetch_all_stats()
            print("\nСохраненные данные:")
            for row in rows:
                print(f"{row[1]} | CPU: {row[2]}% | RAM: {row[3]}% | Disk: {row[4]}%")

        elif choice == '0':
            print("Все вышел, отстал.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == '__main__':
    main()