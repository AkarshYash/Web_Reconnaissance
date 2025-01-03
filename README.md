# Recon Tool

The **Recon Tool** is a web-based application designed for ethical reconnaissance. It helps cybersecurity enthusiasts and professionals perform basic reconnaissance tasks such as Whois lookups and subdomain enumeration for authorized purposes.

---

## Features

### 1. Whois Lookup
- Extracts information about the domain name, registrar, creation date, and expiration date.
- Useful for understanding the ownership and lifecycle of a domain.

### 2. Subdomain Enumeration
- Returns a list of subdomains (currently dummy data for demonstration purposes).
- Can be extended with actual subdomain enumeration logic using tools like `dnspython` or external APIs.

### 3. Simple and Intuitive UI
- Easy-to-use interface for entering URLs and displaying results.
- Includes links to LinkedIn, GitHub, and Portfolio for the developer.

---

## Project Structure

```
Recon-Tool/
├── templates/
│   └── index.html  # HTML template for the web interface
├── static/
│   └── styles.css  # (Optional) Additional CSS styles
├── app.py          # Flask application
├── README.md       # Project documentation
└── requirements.txt # Python dependencies
```

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/recon-tool.git
   cd recon-tool
   ```

2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # For Linux/Mac
   venv\Scripts\activate    # For Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   python app.py
   ```

5. Open your browser and navigate to:
   ```
   http://127.0.0.1:5000
   ```

---

## Usage

1. Enter a website URL in the input field.
2. Click the "Submit" button.
3. View the Whois details and subdomain information.

---

## Technologies Used

- **Frontend:** HTML, CSS
- **Backend:** Python, Flask
- **Tools:** `whois` for Whois lookup


---

## Future Enhancements

- Implement actual subdomain enumeration using `dnspython` or other tools.
- Add support for additional reconnaissance features like IP geolocation.
- Improve UI with animations and more detailed results display.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Developer Info!


**Akarsh Chaturvedi**  
- [LinkedIn](https://www.linkedin.com/in/akarsh-chaturvedi-259271236)
- [GitHub](https://github.com/AkarshYash)
- [Portfolio](https://akarshyash.github.io/Akarsh-potfolio/)
- Kalki !>0
---

## Disclaimer

This tool is intended for ethical use only. Always obtain proper authorization before performing reconnaissance on any website or domain.

## Screenshots

### Homepage
![Screenshot 2025-01-03 235615](https://github.com/user-attachments/assets/3feaaed1-9e66-43a3-8546-fb7fd34750ed)

![Screenshot 2025-01-03 235527](https://github.com/user-attachments/assets/41e4e5f0-56dd-4fbe-9c4d-5179944760f3)
