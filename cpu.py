from service import *

def get_color(cpu_percent):
    if cpu_percent > 50:
        return '\033[91m'  # สีแดง
    elif cpu_percent > 40:
        return '\033[33m'  # สีส้ม
    elif cpu_percent > 30:
        return '\033[93m'  # สีเหลือง
    elif cpu_percent > 20:
        return '\033[92m'  # สีเขียวอ่อน
    else:
        return '\033[32m'  # สีเขียวแก่
    
def print_colored_cpu(cpu_percent):
    for i, percent in enumerate(cpu_percent):
        color = get_color(percent)
        end_color = '\033[0m'
        print(f"CPU {i+1} Usage: {color}{percent}%{end_color}")

def run_cpu():
    while True:
        cpu_percent = psutil.cpu_percent(interval=1, percpu=True)
        # print_colored_cpu(cpu_percent)
        # print("=========== CPU Percent ===========")
        data = []
        for i in cpu_percent:
            data.append(i)
        total_cpu_avg = sum(cpu_percent) / len(cpu_percent)
        # print(f"Total CPU Average: {total_cpu_avg}%")
        dictToSend = {
                "status": total_cpu_avg,
                "data" : data
        }
        requests.post(
            f"{path_system}/api/add/cpu", json=dictToSend)
        time.sleep(0.5)



