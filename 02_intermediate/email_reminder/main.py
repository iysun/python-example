"""
定时邮件提醒脚本
练习点：smtplib、email 模块、schedule 库、环境变量（.env）
"""
import os
import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path

import schedule
from dotenv import load_dotenv

load_dotenv(Path(__file__).parent / ".env")

SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 587
SENDER = os.getenv("EMAIL_SENDER", "")
PASSWORD = os.getenv("EMAIL_PASSWORD", "")
RECEIVER = os.getenv("EMAIL_RECEIVER", "")


def build_email(subject: str, body: str) -> MIMEMultipart:
    """构建邮件对象。"""
    msg = MIMEMultipart()
    msg["From"] = SENDER
    msg["To"] = RECEIVER
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain", "utf-8"))
    return msg


def send_email(subject: str, body: str) -> bool:
    """发送邮件，返回是否成功。"""
    # TODO: 用 smtplib.SMTP(SMTP_HOST, SMTP_PORT) 连接
    # TODO: 调用 server.starttls() 加密
    # TODO: 调用 server.login(SENDER, PASSWORD) 登录
    # TODO: 用 server.send_message() 发送，捕获异常返回 False
    raise NotImplementedError


def daily_reminder():
    """每日提醒任务函数。"""
    subject = "每日提醒"
    body = "这是你的每日提醒邮件，记得完成今天的计划！"
    ok = send_email(subject, body)
    print(f"邮件发送{'成功' if ok else '失败'}")


def main():
    if not all([SENDER, PASSWORD, RECEIVER]):
        print("请在 .env 文件中配置 EMAIL_SENDER / EMAIL_PASSWORD / EMAIL_RECEIVER")
        return

    # TODO: 用 schedule.every().day.at("09:00").do(daily_reminder) 设定定时
    # TODO: 在 while True 循环中调用 schedule.run_pending() + time.sleep(60)
    raise NotImplementedError


if __name__ == "__main__":
    main()
