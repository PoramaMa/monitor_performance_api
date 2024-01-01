#!/bin/bash

# หยุด container
docker stop monitor_performance_api

# ลบ container
docker rm monitor_performance_api

# ลบ Docker image
docker rmi monitor_performance_api

# สร้าง Docker image จาก Dockerfile ที่อยู่ในไดเรกทอรีปัจจุบัน
docker image build -t monitor_performance_api ./

# รัน container จาก image ใหม่ที่สร้างขึ้น
docker run --name monitor_performance_api -d -p 6111:5000 monitor_performance_api

# สั่ง container รีสตาทอัตโนมัติทุกครั้ง
docker update --restart always monitor_performance_api