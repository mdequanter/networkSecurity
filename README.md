
# 🛜 Fake Wi-Fi Login Portal (Educational Demo)

This project is a **Flask-based fake Wi-Fi login portal** designed purely for **educational purposes** to demonstrate the **risks of using open, unsecured networks**. It mimics the behavior of a captive portal like those found in airports or cafés and captures user-submitted data for awareness training.

---

## ⚠️ Disclaimer

> **This project is for educational use only.**
>
> It is strictly prohibited to deploy this code in any environment where users are not informed or have not given consent. Collecting personal data without permission is illegal and violates privacy laws such as the **GDPR**.

---

## 🎯 Objectives

- Demonstrate how easy it is to create a realistic-looking login form
- Show how personal information can be collected over unsecured networks
- Simulate a captive portal that offers a course download upon "login"
- Teach ethical hacking principles and cybersecurity awareness

---

## 🧱 Features

- Flask server with POST form handling
- Collects:
  - Name, forename, email, password
  - Obfuscated password (30% replaced with `*`)
  - IP address
  - User-Agent (browser & OS info)
  - Screen resolution, timezone, browser language (via JavaScript)
- Saves all data to `logins.csv`
- Displays a thank-you page with a fake course download link

---

## 📁 Project Structure

```
project/
├── app.py
├── logins.csv              # Collected data (for demo only)
├── static/
│   ├── logo.png
│   └── course_materials.pdf
├── templates/
│   ├── login.html
│   └── result.html
└── README.md
```

---

## 🚀 Running the App

1. Create a virtual environment:
   ```
   python -m venv venv
   venv\Scripts\activate       # On Windows
   ```

2. Install Flask:
   ```
   pip install flask
   ```

3. Run the app:
   ```
   python app.py
   ```

4. Open your browser at [http://localhost:8000](http://localhost:80) or the appropriate IP.

---

## ✅ Educational Use Ideas

- Run this in a controlled lab environment
- Set it up on a Raspberry Pi with hostapd to simulate a real open hotspot
- Use Wireshark to show how form data is sent in plain HTTP
- Raise awareness about phishing and man-in-the-middle attacks

---

## 📢 License & Ethics

This code is released under the MIT license, but its **ethical use is mandatory**.

Do not use this software to deceive, manipulate, or harvest real user data without informed consent. It exists to **educate and protect**, not exploit.

---
