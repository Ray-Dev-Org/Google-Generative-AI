import os
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

app = Flask(__name__)
CORS(app)

API_KEY = os.getenv("API_KEY")
genai.configure(api_key=API_KEY)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/api/generate", methods=["POST"])
def generate_content():
    data = request.json
    user_input = data.get("input")

    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 40,
        "max_output_tokens": 500,
        "response_mime_type": "text/plain",
    }

    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        system_instruction="The chatbot should only answer about information assurance and security\n\nFoundational IA&S Concepts: Definitions of confidentiality, integrity, availability, authentication, and non-repudiation.\nRisk Management: Identifying, assessing, and mitigating information security risks.\nSecurity Measures: Firewalls, encryption, antivirus tools, MFA, and secure software development practices.\nIncident Response: Steps to detect, respond to, and recover from security breaches.\nLegal and Compliance Frameworks: Basic knowledge of GDPR, HIPAA, or other regional data protection laws.\nCyber Threats: Common threats (e.g., phishing, ransomware) and how to prevent them.\n\nInformation Assurance and Security (IA&S) in Information Technology\nInformation Assurance and Security (IA&S) are complementary domains within information technology that focus on safeguarding data and ensuring its reliability, availability, and integrity. Below is an overview of each term and their interrelation:\n\n1. Information Assurance (IA)\nDefinition:\nInformation assurance refers to the measures and processes used to protect and manage the risks associated with data and information systems. It ensures that information is accurate, accessible, and reliable for authorized users while minimizing the risk of data breaches or unauthorized access.\n\nCore Objectives (Often Called the \"Five Pillars\" of IA):\n\nConfidentiality - Ensuring sensitive information is accessible only to those authorized.\nIntegrity - Ensuring that information remains accurate and unaltered.\nAvailability - Ensuring timely access to information and resources by authorized individuals.\nAuthentication - Verifying the identity of users and systems.\nNon-repudiation - Ensuring actions or communications cannot be denied by the parties involved.\nExamples of IA:\n\nPolicies for data backup and recovery.\nAccess control and user authentication measures.\nRisk assessments and audits of IT systems.\n2. Information Security (InfoSec)\nDefinition:\nInformation security is a subset of information assurance, focusing specifically on protecting information and IT systems from unauthorized access, disruption, theft, or destruction. It involves both technical and procedural safeguards.\n\nKey Components:\n\nCybersecurity - Protection of digital assets and systems from cyberattacks.\nData Encryption - Encoding data to prevent unauthorized access during transmission or storage.\nFirewalls and Antivirus Software - Preventing malicious attacks on systems.\nIncident Response - Detecting and responding to security breaches effectively.\nExamples of InfoSec:\n\nImplementing multi-factor authentication (MFA).\nSecuring networks with encryption protocols like SSL/TLS.\nMonitoring and mitigating threats through intrusion detection systems (IDS).\nHow IA & InfoSec Work Together\nWhile information security is focused on protecting information from threats, information assurance takes a broader approach, ensuring that risks are managed and the organization can recover from disruptions. Together, they form the foundation for comprehensive IT protection strategies.\n\nExample:\n\nAn organization deploying a firewall (InfoSec) and creating a business continuity plan for data recovery (IA).\nWhy It Matters\nWith increasing reliance on technology, organizations face growing threats like cyberattacks, data breaches, and insider threats. IA&S practices help safeguard critical data, maintain trust, comply with regulations, and ensure business continuity in the digital age.",
    )

    response = model.generate_content(user_input)
    return jsonify({"response": response.text})

if __name__ == "__main__":
    app.run(debug=True)

