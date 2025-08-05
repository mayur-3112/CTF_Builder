# CTF Builder Dojo 🥋

Welcome to the CTF Builder Dojo, a hands-on cybersecurity training lab built with Python and Flask. This project is designed not just to be a collection of challenges, but a personal training ground to practice and master the art of web application exploitation.

## The Training Rooms (Challenges)

This lab currently features several training rooms, each focused on a critical web vulnerability from the OWASP Top 10.

### 1. Command Injection (The Master's Challenge)

* **Scenario:** A "Network Diagnostic Tool" page allows users to ping an IP address.
* **Vulnerability:** The user's input is passed directly to the system's command line, allowing an attacker to inject their own commands.
* **Ultimate Goal:** This challenge is designed to be exploited to gain full **Remote Code Execution (RCE)**. This can be achieved by injecting a payload to start a **reverse shell**, such as a PowerShell or Netcat-based shell, giving the attacker full control over the server.

### 2. Cross-Site Scripting (XSS)

* **Scenario:** A guestbook or comment section where user input is displayed back to the page.
* **Vulnerability:** The application does not properly sanitize user input, allowing an attacker to inject malicious JavaScript code.

### 3. Insecure Direct Object References (IDOR)

* **Scenario:** A user profile page that is accessed via a URL parameter (e.g., `/profile?id=123`).
* **Vulnerability:** The application does not properly check if the logged-in user is authorized to view the requested profile ID, allowing an attacker to cycle through IDs and view other users' private information.

### 4. Client-Side Validation Bypass

* **Scenario:** A form that uses JavaScript to prevent the user from submitting certain values (e.g., ordering more than 10 items).
* **Vulnerability:** The validation is only happening in the user's browser (client-side), not on the server. An attacker can use a tool like Burp Suite to intercept the request and change the values *after* they pass the JavaScript check, but *before* they reach the server.

## Technologies Used

* **Backend:** Python 3, Flask
* **Frontend:** HTML, CSS, JavaScript
* **Core Concepts:** This project is a practical application of understanding and exploiting common security vulnerabilities.

## Setup & Usage

### Prerequisites

* Python 3
* pip

### Installation

1.  Clone the repository:
    ```bash
    git clone [https://github.com/mayur-3112/CTF_Builder.git](https://github.com/mayur-3112/CTF_Builder.git)
    cd CTF_Builder
    ```
2.  (Recommended) Create and activate a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
3.  Install the required libraries:
    ```bash
    pip install Flask
    ```

### Running the Lab

To start the web server and begin training, run the following command:
```bash
python3 app.py
```

The application will be accessible at http://localhost:5000. To practice the reverse shell, run the server on host='0.0.0.0' and access it from your attack machine (e.g., a Kali VM in Bridged mode).

### Disclaimer
This project is a deliberately vulnerable application created for educational purposes only. It is designed to be a safe and legal environment to learn and practice ethical hacking skills. Do not deploy this application in a production environment.
