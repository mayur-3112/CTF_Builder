# app.py
# Final version of the CTF Builder with Command Injection Challenge

from flask import Flask, render_template_string, request
import subprocess
import platform

app = Flask(__name__)

@app.route('/')
def index():
    # A simple homepage linking to all challenges
    return """
    <h1>CTF Fortress</h1>
    <p>Welcome to my hands-on cybersecurity training lab.</p>
    <h2>Challenges:</h2>
    <ul>
        <li><a href="/challenge/command_injection">Challenge 1: Command Injection (Reverse Shell)</a></li>
        <!-- You can add links to your other challenges (XSS, IDOR) here -->
    </ul>
    """

# --- NEW CHALLENGE: COMMAND INJECTION ---
@app.route('/challenge/command_injection', methods=['GET', 'POST'])
def command_injection_challenge():
    template = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Challenge: Network Diagnostic Tool</title>
        <style>
            body { font-family: monospace; background-color: #0d1117; color: #c9d1d9; }
            .container { width: 80%; margin: 40px auto; padding: 20px; border: 1px solid #30363d; border-radius: 6px; }
            h1, h2 { color: #58a6ff; }
            input[type=text] { background-color: #010409; color: #c9d1d9; border: 1px solid #30363d; padding: 8px; width: 300px; }
            input[type=submit] { background-color: #238636; color: white; padding: 8px 16px; border: none; border-radius: 6px; cursor: pointer; }
            pre { background-color: #161b22; padding: 15px; border-radius: 6px; white-space: pre-wrap; word-wrap: break-word; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Network Diagnostic Tool</h1>
            <p>Enter an IP address to ping. For example: 8.8.8.8</p>
            <form method="POST">
                <input type="text" name="ip_address" placeholder="8.8.8.8">
                <input type="submit" value="Ping">
            </form>
            
            {% if output %}
            <h2>Ping Results:</h2>
            <pre>{{ output }}</pre>
            {% endif %}

            <!-- The flag is not here. The flag is control. -->
        </div>
    </body>
    </html>
    """

    output = ""
    if request.method == 'POST':
        ip_address = request.form.get('ip_address')
        if ip_address:
            # --- THE VULNERABILITY ---
            # This code is deliberately vulnerable to Command Injection.
            # It detects the OS to use the correct ping command, but the core
            # vulnerability of executing user input via `shell=True` remains.
            if platform.system().lower() == "windows":
                command = f"ping -n 3 {ip_address}"
            else: # For Linux, macOS, etc.
                command = f"ping -c 3 {ip_address}"

            try:
                result = subprocess.run(
                    command,
                    shell=True,
                    capture_output=True,
                    text=True,
                    timeout=15 # Increased timeout for reverse shell stability
                )
                output = result.stdout + result.stderr
            except subprocess.TimeoutExpired:
                output = "Error: The command timed out. (This is expected for a successful reverse shell)."
            except Exception as e:
                output = f"An error occurred: {e}"

    return render_template_string(template, output=output)


if __name__ == '__main__':
    # Running on 0.0.0.0 makes the server accessible on the local network
    app.run(host='0.0.0.0', port=5000, debug=True)



