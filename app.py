import whois
from flask import Flask, render_template, request

app = Flask(__name__)

# Perform Recon Logic
def perform_recon(url):
    result = {}
    try:
        # Whois Lookup
        w = whois.whois(url)
        result['whois'] = {
            'domain_name': w.domain_name,
            'registrar': w.registrar,
            'creation_date': w.creation_date,
            'expiration_date': w.expiration_date
        }

        # Subdomain Enumeration (Dummy Example for Demo)
        result['subdomains'] = ['sub1.example.com', 'sub2.example.com']

        # Add more recon functionality as needed
    except Exception as e:
        result['error'] = str(e)
    return result

@app.route('/')
def home():
    return render_template('index.html', result=None, error=None)

@app.route('/recon', methods=['POST'])
def recon():
    url = request.form.get('url')
    if not url:
        return render_template('index.html', result=None, error="URL is required!")
    report = perform_recon(url)
    return render_template('index.html', result=report, error=None)
