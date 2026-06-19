# 基础镜像使用python 
FROM python:3.9-slim

# 设置工作区
WORKDIR /app

# 复制代码到容器
COPY src/main.py /app

# 让 main.py 可运行
RUN chmod +x /app/main.py

# 使用 ENTRYPOINT 固定命令
ENTRYPOINT ["python"]

# 使用CMD接收参数
CMD ["/app/main.py"]




