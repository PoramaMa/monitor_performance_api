from service import *

def print_colored_ram(used_ram):
    if used_ram > 80:
        print('\033[91m', end='')  # สีแดงสำหรับ RAM > 80%
    elif used_ram > 60:
        print('\033[33m', end='')  # สีส้มสำหรับ RAM > 60%
    elif used_ram > 40:
        print('\033[93m', end='')  # สีเหลืองสำหรับ RAM > 40%
    elif used_ram > 20:
        print('\033[92m', end='')  # สีเขียวอ่อนสำหรับ RAM > 20%
    else:
        print('\033[32m', end='')  # สีเขียวแก่สำหรับ RAM <= 20%

    print(f"Used RAM: {used_ram}%", end='')
    print('\033[0m')

def run_ram():
    while True:
        ram = psutil.virtual_memory()
        total_ram = round(ram.total / (1024 ** 3),2) # หน่วยความจำทั้งหมด
        free_ram = round(ram.available / (1024 ** 3),2)  # หน่วยความจำที่ว่าง
        used_ram = round(total_ram-free_ram,2)  # หน่วยความจำที่ใช้งาน
        ram_usage = ram.percent  # อัตราส่วนการใช้งานหน่วยความจำ
        used_ram_percent = ram_usage
        # print_colored_ram(used_ram_percent)
        # print("=========== RAM Percent ===========")
        # print(f"Used RAM Average: {used_ram_percent}%")
        # print(f"=========== RAM {ram} ===========")
        data = {
            "total_ram" : total_ram,
            "free_ram" : free_ram,
            "used_ram" : used_ram,
            "ram_usage" : ram_usage,
        }
        dictToSend = {
                "status": used_ram_percent,
                "data" : data
        }
        requests.post(
            f"{path_system}/api/add/ram", json=dictToSend)
        time.sleep(0.5)

