# CTF Builder:A Web Security Learning Environment

This project is a simple, Flask-based web application designed to teach and demonstrate fundamental web security vulnerabilities. It is a hands-on learning tool for aspiring security professionals.

## About The Project

As part of my journey into Cyber Security, I wanted to move beyond just solving challenges and begin building them. This project is the result. By creating these vulnerable scenarios from scratch, I gain a deeper understanding of how exploits work and, more importantly, how to prevent them.
This project currently includes the following challenges:
* Challenge 1: The Hidden Message (HTML Source Code Analysis)
* Challenge 2: The Client is a Liar (Client-Side Validation Bypass)
* Challenge 3: The Predictable Path (Insecure Direct Object Reference - IDOR)
* Challenge 4: The Untrusted Input (Reflected Cross-Site Scripting - XSS)
  
### Built With
* Python
* Flask
* HTML / CSS / JavaScript

## Getting Started
To get a local copy up and running, follow these simple steps.

###  Prerequisites
You must have Python 3 and pip installed on your system.

### Installation
1. Clone the repository:

```bash
git clone https://github.com/your-username/CTF-Builder.git
```

2. Navigate into the project directory:
```bash
cd CTF-Builder
```
3. Install the required Python package:
```bash
pip install Flask markupsafe
```
4. Run the application:
```bash
python app.py
```
Open your browser and navigate to ```http://127.0.0.1:5000```.
