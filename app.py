from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
<!DOCTYPE html>
<html lang="nl">
<head>
    <meta charset="UTF-8">
    <title>Inspire Offices</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Segoe UI', sans-serif;
            background: #f0f4f8;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            min-height: 100vh;
            color: #1a202c;
        }
        .card {
            background: red;
            border-radius: 16px;
            padding: 48px 64px;
            box-shadow: 0 4px 24px rgba(0,0,0,0.1);
            text-align: center;
            max-width: 560px;
        }
        .logo {
            font-size: 2.5rem;
            font-weight: 700;
            color: #2563eb;
            margin-bottom: 8px;
        }
        .tagline {
            color: #64748b;
            font-size: 1rem;
            margin-bottom: 32px;
        }
        .version-badge {
            display: inline-block;
            background: #eff6ff;
            color: #2563eb;
            border: 1px solid #bfdbfe;
            border-radius: 999px;
            padding: 4px 16px;
            font-size: 0.85rem;
            font-weight: 600;
            margin-bottom: 24px;
        }
        .status {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
            color: #16a34a;
            font-weight: 500;
        }
        .dot {
            width: 10px; height: 10px;
            background: #16a34a;
            border-radius: 50%;
            animation: pulse 1.5s infinite;
        }
        @keyframes pulse {
            0%, 100% { opacity: 1; }
            50% { opacity: 0.4; }
        }
        .links {
            margin-top: 32px;
            display: flex;
            gap: 12px;
            justify-content: center;
        }
        a {
            padding: 10px 20px;
            border-radius: 8px;
            text-decoration: none;
            font-weight: 500;
            font-size: 0.9rem;
        }
        .btn-primary { background: #2563eb; color: white; }
        .btn-secondary { background: #f1f5f9; color: #475569; }
        .btn-primary:hover { background: #1d4ed8; }
        .btn-secondary:hover { background: #e2e8f0; }
    </style>
</head>
<body>
    <div class="card">
        <div class="logo">🏢 Inspire Offices Beheerders site</div>
        <p class="tagline">Dit is het Inspire Offices Beheerportaal!</p>
        <p style="color:#475569;font-size:0.9rem;margin-bottom:8px;">Gemaakt door:Emir.</p>
        <p style="color:#475569;font-size:0.9rem;margin-bottom:16px;">A.</p>
        <div class="version-badge">Sprint Oplevering — v1.0</div>
        <div class="status">
            <div class="dot"></div>
            Applicatie actief op poort 5000
        </div>
        <div class="links">
            <a href="/health" class="btn-primary">Health Check</a>
            <a href="/info" class="btn-secondary">App Info</a>
        </div>
    </div>
</body>
</html>
"""

@app.route("/health")
def health():
    return {"status": "ok", "message": "Inspire Offices draait correct"}, 200

@app.route("/info")
def info():
    return """
<!DOCTYPE html>
<html lang="nl">
<head>
    <meta charset="UTF-8">
    <title>App Info</title>
    <style>
        body { font-family: 'Segoe UI', sans-serif; background: #f0f4f8; display: flex; justify-content: center; padding: 48px 16px; }
        .card { background: white; border-radius: 16px; padding: 40px; max-width: 480px; width: 100%; box-shadow: 0 4px 24px rgba(0,0,0,0.1); }
        h2 { color: #2563eb; margin-bottom: 24px; }
        table { width: 100%; border-collapse: collapse; }
        td { padding: 10px 0; border-bottom: 1px solid #f1f5f9; font-size: 0.95rem; }
        td:first-child { color: #64748b; font-weight: 500; }
        td:last-child { color: #1a202c; font-weight: 600; }
        a { display: inline-block; margin-top: 24px; color: #2563eb; text-decoration: none; font-weight: 500; }
    </style>
</head>
<body>
    <div class="card">
        <h2>App Info</h2>
        <table>
            <tr><td>Applicatie</td><td>Inspire Offices</td></tr>
            <tr><td>Versie</td><td>v1.0</td></tr>
            <tr><td>Framework</td><td>Flask (Python)</td></tr>
            <tr><td>Poort</td><td>5000</td></tr>
            <tr><td>Status</td><td>✅ Running</td></tr>
        </table>
        <a href="/">← Terug naar home</a>
    </div>
</body>
</html>
"""

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)