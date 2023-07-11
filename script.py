import psutil 
import time 
    
def get_cpu_usuage():
    cpu_percent = psutil.cpu_percent(interval=0.2)
    return cpu_percent

def get_memory_usuage():
    memory= psutil.virtual_memory()
    memory_percent = memory.percent
    return memory_percent 

while True:
    cpu = get_cpu_usuage()
    memory_usuage = get_memory_usuage()

    print(f"CPU Usuage: {cpu:.1f}%", end=" | ")
    print(f"Memory Usuage: {memory_usuage:.1f}%", end="\r")
    time.sleep(1)

