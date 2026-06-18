from flask import Flask

app = Flask(__name__)

# Gedeelde CSS voor een strakke, consistente look
SHARED_CSS = """
    <style>
        :root {
            --primary: #0f172a;
            --accent: #3b82f6;
            --bg: #f8fafc;
            --text: #334155;
            --card-bg: #ffffff;
        }
        * { margin: 0; padding: 0; box-sizing: border-box; font-family: 'Segoe UI', system-ui, sans-serif; }
        body {
            background-color: var(--bg);
            color: var(--text);
            display: flex;
            flex-direction: column;
            align-items: center;
            min-height: 100vh;
            padding: 40px 20px;
        }
        .container {
            max-width: 900px;
            width: 100%;
        }
        .header {
            text-align: center;
            margin-bottom: 40px;
        }
        .header h1 {
            color: var(--primary);
            font-size: 2.5rem;
            font-weight: 800;
            margin-bottom: 10px;
            letter-spacing: -0.5px;
        }
        .header p {
            color: #64748b;
            font-size: 1.1rem;
        }
        .badge {
            display: inline-block;
            background: #dbeafe;
            color: var(--accent);
            padding: 6px 16px;
            border-radius: 999px;
            font-size: 0.85rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 1px;
            margin-bottom: 20px;
        }
        .btn {
            display: inline-block;
            background: var(--accent);
            color: white;
            padding: 12px 28px;
            border-radius: 8px;
            text-decoration: none;
            font-weight: 600;
            transition: all 0.2s ease;
            box-shadow: 0 4px 6px -1px rgba(59, 130, 246, 0.3);
            margin: 10px;
        }
        .btn:hover {
            background: #2563eb;
            transform: translateY(-2px);
        }
        .btn-outline {
            background: transparent;
            color: var(--primary);
            border: 2px solid #e2e8f0;
            box-shadow: none;
        }
        .btn-outline:hover {
            background: #f1f5f9;
            border-color: #cbd5e1;
        }
    </style>
"""

@app.route("/")
def home():
    return f"""
<!DOCTYPE html>
<html lang="nl">
<head>
    <meta charset="UTF-8">
    <title>Inspire Offices | Beheerportaal</title>
    {SHARED_CSS}
    <style>
        .hero-card {{
            background: var(--card-bg);
            border-radius: 20px;
            padding: 60px 40px;
            text-align: center;
            box-shadow: 0 10px 30px -5px rgba(0,0,0,0.05);
            border: 1px solid #e2e8f0;
        }}
        .status-indicator {{
            display: inline-flex;
            align-items: center;
            gap: 8px;
            color: #059669;
            font-weight: 600;
            background: #d1fae5;
            padding: 8px 20px;
            border-radius: 12px;
            margin-top: 30px;
        }}
        .pulse {{
            width: 12px; height: 12px;
            background: #10b981;
            border-radius: 50%;
            animation: pulse 2s infinite;
        }}
        @keyframes pulse {{
            0% {{ box-shadow: 0 0 0 0 rgba(16, 185, 129, 0.4); }}
            70% {{ box-shadow: 0 0 0 10px rgba(16, 185, 129, 0); }}
            100% {{ box-shadow: 0 0 0 0 rgba(16, 185, 129, 0); }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="hero-card">
            <span class="badge">Oplevering Sprint 1</span>
            <div class="header">
                <h1>🏢 Inspire Offices Beheerportaal</h1>
                <p>Centraal overzicht van onze vernieuwde, geautomatiseerde IT-infrastructuur.</p>
            </div>
            
            <div style="margin: 40px 0;">
                <a href="/project" class="btn">Bekijk Project Architectuur</a>
                <a href="/health" class="btn btn-outline">Systeem Health Check</a>
            </div>

            <div class="status-indicator">
                <div class="pulse"></div>
                Systeem Actief & Verbonden (Poort 5000)
            </div>
        </div>
    </div>
</body>
</html>
"""

@app.route("/project")
def project():
    return f"""
<!DOCTYPE html>
<html lang="nl">
<head>
    <meta charset="UTF-8">
    <title>Project Architectuur | Inspire Offices</title>
    {SHARED_CSS}
    <style>
        .grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
            gap: 24px;
            margin-top: 30px;
        }}
        .feature-card {{
            background: var(--card-bg);
            padding: 32px;
            border-radius: 16px;
            box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);
            border: 1px solid #e2e8f0;
            transition: transform 0.2s ease;
        }}
        .feature-card:hover {{
            transform: translateY(-4px);
            border-color: #cbd5e1;
        }}
        .icon {{
            font-size: 2rem;
            margin-bottom: 16px;
        }}
        .feature-card h3 {{
            color: var(--primary);
            font-size: 1.25rem;
            margin-bottom: 12px;
        }}
        .feature-card p {{
            color: #64748b;
            line-height: 1.6;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <span class="badge">Infrastructuur Overzicht</span>
            <h1>Architectuur & Requirements</h1>
            <p>De fundamenten van de nieuwe IT-omgeving van Inspire Offices.</p>
        </div>

        <div class="grid">
            <div class="feature-card">
                <div class="icon">🖧</div>
                <h3>Gesegmenteerd Netwerk (VLAN)</h3>
                <p>Het bedrijfsnetwerk is strikt gescheiden in logische VLANs (o.a. Management, Gasten, en Werkplekken). Dit verhoogt de netwerkprestaties en isoleert eventuele beveiligingsrisico's direct bij de bron.</p>
            </div>

            <div class="feature-card">
                <div class="icon">🔐</div>
                <h3>Active Directory & OU Structuur</h3>
                <p>Lokaal identiteitsbeheer is strak georganiseerd via Windows Server Active Directory. Door gebruik te maken van logische Organizational Units (OU's) kunnen we groepsbeleid (GPO) per afdeling feilloos uitrollen.</p>
            </div>

            <div class="feature-card">
                <div class="icon">☁️</div>
                <h3>Entra ID (Cloud Authenticatie)</h3>
                <p>De lokale Active Directory is veilig gekoppeld met Microsoft Entra ID. Hierdoor profiteren medewerkers van Single Sign-On (SSO) en Multi-Factor Authenticatie (MFA) voor alle moderne cloud-applicaties.</p>
            </div>

            <div class="feature-card">
                <div class="icon">📋</div>
                <h3>Compliancy & Requirements</h3>
                <p>De volledige infrastructuur is ontworpen conform de strenge security-eisen van de directie. Dankzij CI/CD-automatisering en containerisatie is de uitrol nu voorspelbaar, schaalbaar en 100% reproduceerbaar.</p>
            </div>
        </div>

        <div style="text-align: center; margin-top: 40px;">
            <a href="/" class="btn btn-outline">← Terug naar Dashboard</a>
        </div>
    </div>
</body>
</html>
"""

@app.route("/health")
def health():
    return {"status": "ok", "message": "Alle microservices van Inspire Offices functioneren naar behoren."}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)