from service import *

def print_colored_disk(used_disk):
    if used_disk > 80:
        print('\033[91m', end='')  # สีแดงสำหรับ Disk > 80%
    elif used_disk > 60:
        print('\033[33m', end='')  # สีส้มสำหรับ Disk > 60%
    elif used_disk > 40:
        print('\033[93m', end='')  # สีเหลืองสำหรับ Disk > 40%
    elif used_disk > 20:
        print('\033[92m', end='')  # สีเขียวอ่อนสำหรับ Disk > 20%
    else:
        print('\033[32m', end='')  # สีเขียวแก่สำหรับ Disk <= 20%

    print(f"Used Disk: {used_disk}%", end='')
    print('\033[0m')  # คืนสีเป็นค่าเริ่มต้น

def run_disk():
    while True:
        # รับข้อมูลการใช้พื้นที่บน disk และแสดงผล
        disk = psutil.disk_usage('/')
        total_disk = round(disk.total / (1024 ** 3),2) # หน่วยความจำทั้งหมด
        free_disk = round(disk.free / (1024 ** 3),2)  # หน่วยความจำที่ว่าง
        used_disk = round(disk.used / (1024 ** 3),2)  # หน่วยความจำที่ใช้งาน
        disk_usage = disk.percent  # อัตราส่วนการใช้งานหน่วยความจำ
        used_disk_percent = disk_usage
        # print_colored_disk(used_disk_percent)
        # print("=========== Disk Percent ===========")
        data = {
            "total_disk" : total_disk,
            "free_disk" : free_disk,
            "used_disk" : used_disk,
            "disk_usage" : disk_usage,
        }
        dictToSend = {
                "status": used_disk_percent,
                "data" :data
        }
        requests.post(
            f"{path_system}/api/add/disk", json=dictToSend)
        time.sleep(0.5)

