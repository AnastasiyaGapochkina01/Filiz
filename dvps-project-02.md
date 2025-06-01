1) В директории `/var/www` создать директорию `dvps-02`
2) В директории `dvps-02` создать файл `main.py` с содержимым
```
from fastapi import FastAPI, Request
import getpass
import platform
import logging
import uvicorn
from datetime import datetime
import time

app = FastAPI()

logging.basicConfig(
    filename='info_app.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger("fastapi")

@app.middleware("http")
async def log_requests(request: Request, call_next):
    """Middleware for incoming requests"""
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    
    log_data = {
        "timestamp": datetime.now().isoformat(),
        "method": request.method,
        "path": request.url.path,
        "client_ip": request.client.host,
        "status_code": response.status_code,
        "process_time": round(process_time, 4)
    }
    
    logger.info(f"{log_data['method']} {log_data['path']} from {log_data['client_ip']} "
                f"- Status: {log_data['status_code']} - {log_data['process_time']}s")
    
    return response

@app.get("/")
async def get_system_info():
    """Return username and OS version"""
    return {
        "username": getpass.getuser(),
        "os_version": platform.platform()
    }

if __name__ == "__main__":
    config = uvicorn.Config(
        app,
        host="0.0.0.0",
        port=9100,
        log_level="info",
        access_log=True
    )
    server = uvicorn.Server(config)
    
    server.run()
```
3) Запустить приложение командой `python3 main.py`; выяснить
- на каком порту запустилось приложение
- создался ли файл `info_app.log`
- PID процесса, в котором запущено приложение
4) Проверить работу приложения запросами
```
$ curl 127.0.0.1:9100
$ curl 127.0.0.1:9100/docs
$ curl http://localhost:9100/redoc
```
5) Посмотреть содержимое файла `info_app.log`. Что это за файл?
6) В директории `dvps-02` создать файл `load_test.py` с содержимым
```
import asyncio
import random
import aiohttp
import time
import argparse
import sys
from datetime import datetime

def generate_random_data():
    return {
        "data": ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=20)),
        "value": random.randint(1, 1000),
        "timestamp": datetime.now().isoformat()
    }

async def send_request(session, url, method="GET", data=None):
    start_time = time.monotonic()
    try:
        if method == "GET":
            async with session.get(url) as response:
                status = response.status
                if status == 200:
                    await response.text()
        elif method == "POST":
            async with session.post(url, json=data) as response:
                status = response.status
        elif method == "PUT":
            async with session.put(url, json=data) as response:
                status = response.status
        elif method == "DELETE":
            async with session.delete(url) as response:
                status = response.status
                
        duration = time.monotonic() - start_time
        return {"status": "success", "code": status, "duration": duration}
        
    except Exception as e:
        duration = time.monotonic() - start_time
        return {"status": "error", "message": str(e), "duration": duration}

async def load_test(target_url, num_requests, concurrent_workers):
    endpoints = ["/", "/redoc", "/docs", "/user/profile"]
    connector = aiohttp.TCPConnector(limit=0) 
    async with aiohttp.ClientSession(connector=connector) as session:
        tasks = []
        request_counter = 0
        success_count = 0
        error_count = 0
        total_duration = 0
        
        while request_counter < num_requests:
            method = random.choices(
                ["GET", "POST", "PUT", "DELETE"],
                weights=[0.5, 0.3, 0.15, 0.05] 
            )[0]

            endpoint = random.choices(endpoints,
                weights=[0.5, 0.3, 0.15, 0.05] 
            )[0]

            full_url = f"{target_url}{endpoint}"
            
            data = generate_random_data() if method in ["POST", "PUT"] else None
            
            task = asyncio.create_task(
                send_request(session, full_url, method, data)
            )
            tasks.append(task)
            request_counter += 1
            
            if len(tasks) >= concurrent_workers:
                done, pending = await asyncio.wait(
                    tasks, 
                    return_when=asyncio.FIRST_COMPLETED
                )
                
                for task in done:
                    result = task.result()
                    total_duration += result["duration"]
                    if result["status"] == "success":
                        success_count += 1
                    else:
                        error_count += 1
                
                tasks = list(pending)
                
                sys.stdout.flush()
        
        if tasks:
            results = await asyncio.gather(*tasks)
            for result in results:
                total_duration += result["duration"]
                if result["status"] == "success":
                    success_count += 1
                else:
                    error_count += 1
    print("\n\n📊 Load testing results:")
    print(f"✅ Successful requests: {success_count} ({success_count/num_requests:.1%})")
    print(f"❌ Failure requests: {error_count} ({error_count/num_requests:.1%})")
    print(f"⏱️ Total time: {total_duration:.2f} s")
    print(f"⚡ Requests per second: {num_requests/total_duration:.2f}")
    print(f"⏳ Average response time: {total_duration/num_requests:.4f} s")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('url', type=str, help='Target URL (for example: http://localhost:9100)')
    parser.add_argument('-r', '--requests', type=int, default=100, 
                        help='Total requests (default: 100)')
    parser.add_argument('-c', '--concurrency', type=int, default=10,
                        help='Count of simultaneous requests (default: 10)')
    
    args = parser.parse_args()
    print()
    print("=" * 50)
    print(f"🛠️ Settings:")
    print(f"  Target URL: {args.url}")
    print(f"  Total requests: {args.requests}")
    print(f"  Parallel requests: {args.concurrency}")
    print("=" * 50)
    
    start_time = time.monotonic()
    asyncio.run(load_test(args.url, args.requests, args.concurrency))
    print(f"\n🕒 Total test execution time: {time.monotonic() - start_time:.2f} s")
```
7) Запустить скрипт командой `python3 info_gen_load.py http://localhost:9100 -r 1000 -c 50`
8) Посмотреть содержимое файла `info_app.log`; найти в этом файле
- все записи с методом DELETE
- все записи с методом PUT и посчитать их количество
- все записи со статусом 405 и выяснить методы, которые использовались в таких запросах
- все записи со статусом 404 и выяснить их endpoint
- все записи об endpoint `/redoc` и для них выяснить сколько было кодов ответа 200
9) Убить процесс приложения
10) Написать bash-скрипт для автоматизации развертывания этого приложения; в скрипте должна быть возможность задав аргумент gen_load  запускать скрипт `info_gen_load.py`
