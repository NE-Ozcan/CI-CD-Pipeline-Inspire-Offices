from flask import Flask

app = Flask(__name__)

# CSS en Styling voor een high-end presentatie (Dark Mode / Cyber thema)
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="nl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Inspire Offices | Proftaak Presentatie</title>
    <style>
        :root {
            --bg-dark: #0f172a;
            --bg-card: #1e293b;
            --primary: #38bdf8;
            --primary-glow: rgba(56, 189, 248, 0.4);
            --text-main: #f8fafc;
            --text-muted: #94a3b8;
            --accent: #10b981;
        }
        
        * { margin: 0; padding: 0; box-sizing: border-box; font-family: 'Segoe UI', system-ui, sans-serif; scroll-behavior: smooth; }
        
        body {
            background-color: var(--bg-dark);
            color: var(--text-main);
            line-height: 1.6;
        }

        /* Navigatie & Logo */
        nav {
            position: fixed;
            top: 0; width: 100%;
            background: rgba(15, 23, 42, 0.9);
            backdrop-filter: blur(10px);
            padding: 20px 5%;
            display: flex;
            justify-content: space-between;
            align-items: center;
            z-index: 1000;
            border-bottom: 1px solid #334155;
        }

        .logo {
            font-size: 1.5rem;
            font-weight: 800;
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .logo span { color: var(--primary); }
        .logo-icon { font-size: 2rem; }

        .nav-links a {
            color: var(--text-main);
            text-decoration: none;
            margin-left: 20px;
            font-weight: 600;
            transition: color 0.3s;
        }
        .nav-links a:hover { color: var(--primary); }

        /* Hero Sectie */
        header {
            padding: 150px 5% 100px;
            text-align: center;
            background: radial-gradient(circle at center, #1e293b 0%, #0f172a 100%);
        }

        .po-badge {
            display: inline-block;
            background: rgba(16, 185, 129, 0.1);
            color: var(--accent);
            padding: 8px 16px;
            border-radius: 20px;
            border: 1px solid var(--accent);
            font-weight: 700;
            margin-bottom: 20px;
            letter-spacing: 1px;
        }

        h1 {
            font-size: 3.5rem;
            margin-bottom: 20px;
            background: -webkit-linear-gradient(45deg, #38bdf8, #818cf8);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .subtitle {
            font-size: 1.2rem;
            color: var(--text-muted);
            max-width: 800px;
            margin: 0 auto;
        }

        /* Secties & Kaarten (Geen bulletpoints!) */
        section { padding: 80px 5%; }
        
        .section-title {
            text-align: center;
            font-size: 2.5rem;
            margin-bottom: 50px;
            color: #ffffff;
        }

        .grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 30px;
            max-width: 1200px;
            margin: 0 auto;
        }

        .card {
            background: var(--bg-card);
            padding: 40px 30px;
            border-radius: 16px;
            border: 1px solid #334155;
            transition: all 0.3s ease;
        }

        .card:hover {
            transform: translateY(-5px);
            border-color: var(--primary);
            box-shadow: 0 10px 30px var(--primary-glow);
        }

        .card-icon {
            font-size: 2.5rem;
            margin-bottom: 20px;
        }

        .card h3 {
            font-size: 1.3rem;
            margin-bottom: 15px;
            color: var(--primary);
        }

        footer {
            text-align: center;
            padding: 40px;
            background: #0b1120;
            color: var(--text-muted);
            border-top: 1px solid #334155;
        }

        /* Systeem status widget */
        .live-status {
            position: fixed;
            bottom: 20px;
            right: 20px;
            background: var(--bg-card);
            padding: 10px 20px;
            border-radius: 50px;
            display: flex;
            align-items: center;
            gap: 10px;
            border: 1px solid #334155;
            box-shadow: 0 4px 15px rgba(0,0,0,0.3);
            z-index: 1000;
        }
        .dot {
            width: 10px; height: 10px;
            background: var(--accent);
            border-radius: 50%;
            animation: blink 2s infinite;
        }
        @keyframes blink { 50% { opacity: 0.4; } }

    </style>
</head>
<body>

    <nav>
        <div class="logo">
            <div class="logo-icon">🛡️</div>
            Inspire<span>Offices</span>
        </div>
        <div class="nav-links">
            <a href="#intro">Overzicht</a>
            <a href="#fase1">Fase 1</a>
            <a href="#fase2">Fase 2</a>
            <a href="#fase3">Fase 3</a>
        </div>
    </nav>

    <header id="intro">
        <div class="po-badge">OPDRACHTGEVER: SECUREMEISTER</div>
        <h1>Proftaak Eindoplevering</h1>
        <p class="subtitle">Een veilige, schaalbare en moderne IT-infrastructuur voor Inspire Offices in de oude Suikerfabriek Zevenbergen, Tilburg. Ontworpen en gebouwd over een periode van 15 weken.</p>
    </header>

    <section id="fase1">
        <h2 class="section-title">Fase 1: Fysiek Fundament (On-Prem)</h2>
        <div class="grid">
            <div class="card">
                <div class="card-icon">🖧</div>
                <h3>Gescheiden Netwerken</h3>
                <p>Gebouwd in het Mobile Infra Lab. Strikte VLAN-scheiding gerealiseerd tussen Gasten, Huurders, Beheer en IoT-apparatuur ter voorkoming van laterale verplaatsing bij incidenten.</p>
            </div>
            <div class="card">
                <div class="card-icon">🪪</div>
                <h3>Toegangscontrole (PoC)</h3>
                <p>Implementatie van een fysieke toegangscontrole Proof of Concept middels passen en scanners om de locatie fysiek te beveiligen.</p>
            </div>
            <div class="card">
                <div class="card-icon">🖨️</div>
                <h3>Veilig Printen</h3>
                <p>Introductie van een pull-print oplossing. Printopdrachten worden pas vrijgegeven wanneer de gebruiker zich fysiek bij de printer authenticeert, wat datalekken voorkomt.</p>
            </div>
        </div>
    </section>

    <section id="fase2" style="background-color: rgba(30, 41, 59, 0.3);">
        <h2 class="section-title">Fase 2: Cloud & Hybride Koppeling</h2>
        <div class="grid">
            <div class="card">
                <div class="card-icon">☁️</div>
                <h3>Azure Landing Zone</h3>
                <p>Een solide cloud-fundament in Microsoft Azure voorzien van RBAC (Role-Based Access Control), strikte policies en tagging voor overzichtelijk beheer.</p>
            </div>
            <div class="card">
                <div class="card-icon">🔐</div>
                <h3>Entra ID & SSO</h3>
                <p>Hybride connectiviteit opgezet met Single Sign-On (SSO). Toegang wordt streng bewaakt met Multi-Factor Authenticatie (MFA) en Conditional Access beleid.</p>
            </div>
            <div class="card">
                <div class="card-icon">📊</div>
                <h3>SIEM-lite & AVG</h3>
                <p>Centrale logging ingericht voor monitoring van toegangs- en printdata. De architectuur is volledig ontworpen met de AVG/GDPR-compliance in het achterhoofd.</p>
            </div>
        </div>
    </section>

    <section id="fase3">
        <h2 class="section-title">Fase 3: Modernisering & Zero Trust</h2>
        <div class="grid">
            <div class="card">
                <div class="card-icon">🚀</div>
                <h3>Containerisatie & CI/CD</h3>
                <p>Applicaties (zoals deze presentatiesite) draaien in gecontaineriseerde omgevingen (Docker). Volledig geautomatiseerde uitrol middels een veilige CI/CD-pipeline.</p>
            </div>
            <div class="card">
                <div class="card-icon">🛡️</div>
                <h3>Zero Trust Hardening</h3>
                <p>Volledige implementatie van het 'Assume Breach' en 'Least Privilege' principe, inclusief een uitgewerkt incident response scenario met digital forensics.</p>
            </div>
            <div class="card">
                <div class="card-icon">🌐</div>
                <h3>Toekomstbestendig Netwerk</h3>
                <p>De netwerkarchitectuur is klaargestoomd voor de toekomst door de implementatie van IPv6 en geavanceerde DNS-security (DoT/DoH en DNSSEC).</p>
            </div>
        </div>
    </section>

    <footer>
        <p>Gemaakt voor de eindoplevering van Inspire Offices. © 2026</p>
    </footer>

    <div class="live-status">
        <div class="dot"></div>
        <span>CI/CD Pipeline Actief</span>
    </div>

</body>
</html>
"""

@app.route("/")
def presentatie():
    return HTML_TEMPLATE

if __name__ == "__main__":
    # Applicatie starten op alle interfaces, poort 5000
    app.run(host="0.0.0.0", port=5000, debug=True)