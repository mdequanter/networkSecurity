from flask import Flask, render_template, request
import csv
import os
import random
from datetime import datetime

app = Flask(__name__)
CSV_FILE = 'logins.csv'

def mask_password(password, mask_ratio=0.3):
    """Replace ~30% of the characters in the password with '*'."""
    if not password:
        return ''
    
    length = len(password)
    num_to_mask = max(1, int(length * mask_ratio))
    indices = random.sample(range(length), num_to_mask)

    masked = list(password)
    for i in indices:
        masked[i] = '*'
    
    return ''.join(masked)

# Create CSV with headers if it doesn't exist
if not os.path.isfile(CSV_FILE):
    with open(CSV_FILE, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Timestamp', 'IP Address', 'Forename', 'Name', 'Email', 'Obfuscated Password'])

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        forename = request.form.get('forename')
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ip_address = request.remote_addr
        masked_password = mask_password(password)

        # Print to console
        print(f"[{timestamp}] Login attempt from {ip_address}")
        print(f"Name: {forename} {name}")
        print(f"Email: {email}")
        print(f"Obfuscated Password: {masked_password}")

        # Append to CSV
        with open(CSV_FILE, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([timestamp, ip_address, forename, name, email, masked_password])

        return render_template('result.html', forename=forename, name=name, email=email, masked_password=masked_password)

    return render_template('login.html')

if __name__ == '__main__':
    app.run(host='192.168.1.75', port=8000, debug=True)
