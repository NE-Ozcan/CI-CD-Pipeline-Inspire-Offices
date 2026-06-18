from flask import Flask

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="nl">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Inspire Offices — Proftaak 2025</title>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=DM+Serif+Display&display=swap" rel="stylesheet" />
  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

    :root {
      --bg: #0d0f14;
      --bg-card: #13161e;
      --bg-subtle: #1a1e28;
      --border: rgba(255,255,255,0.07);
      --text-primary: #f0f2f7;
      --text-secondary: #8b92a8;
      --text-muted: #525a72;
      --accent-blue: #4a90d9;
      --accent-teal: #2fcb96;
      --accent-purple: #9b7cf4;
      --accent-amber: #f0a832;
      --accent-red: #e05a5a;
    }

    html { scroll-behavior: smooth; }

    body {
      font-family: 'Inter', sans-serif;
      background: var(--bg);
      color: var(--text-primary);
      line-height: 1.7;
      font-size: 16px;
    }

    /* ─── Nav ─── */
    nav {
      position: fixed;
      top: 0; left: 0; right: 0;
      z-index: 100;
      background: rgba(13,15,20,0.85);
      backdrop-filter: blur(12px);
      border-bottom: 1px solid var(--border);
      padding: 0 2rem;
      height: 56px;
      display: flex;
      align-items: center;
      justify-content: space-between;
    }
    .nav-logo {
      font-size: 14px;
      font-weight: 600;
      color: var(--text-primary);
      letter-spacing: 0.02em;
    }
    .nav-logo span { color: var(--accent-teal); }
    .nav-links {
      display: flex;
      gap: 1.5rem;
      list-style: none;
    }
    .nav-links a {
      font-size: 13px;
      color: var(--text-secondary);
      text-decoration: none;
      transition: color 0.2s;
    }
    .nav-links a:hover { color: var(--text-primary); }

    /* ─── Hero ─── */
    .hero {
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      text-align: center;
      padding: 6rem 2rem 4rem;
      position: relative;
      overflow: hidden;
    }
    .hero::before {
      content: '';
      position: absolute;
      top: -200px; left: 50%;
      transform: translateX(-50%);
      width: 800px; height: 600px;
      background: radial-gradient(ellipse at center, rgba(74,144,217,0.12) 0%, transparent 70%);
      pointer-events: none;
    }
    .hero-eyebrow {
      font-size: 12px;
      font-weight: 500;
      letter-spacing: 0.1em;
      text-transform: uppercase;
      color: var(--accent-teal);
      margin-bottom: 1.25rem;
    }
    .hero-title {
      font-family: 'DM Serif Display', serif;
      font-size: clamp(2.5rem, 6vw, 4.5rem);
      font-weight: 400;
      line-height: 1.1;
      color: var(--text-primary);
      margin-bottom: 1.5rem;
      max-width: 700px;
    }
    .hero-title em {
      font-style: italic;
      color: var(--accent-blue);
    }
    .hero-sub {
      font-size: 17px;
      color: var(--text-secondary);
      max-width: 560px;
      line-height: 1.75;
      margin-bottom: 2.5rem;
    }
    .hero-meta {
      display: flex;
      gap: 2rem;
      justify-content: center;
      flex-wrap: wrap;
    }
    .meta-item {
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 4px;
    }
    .meta-value {
      font-size: 22px;
      font-weight: 600;
      color: var(--text-primary);
    }
    .meta-label {
      font-size: 12px;
      color: var(--text-muted);
      text-transform: uppercase;
      letter-spacing: 0.07em;
    }
    .meta-divider {
      width: 1px;
      height: 40px;
      background: var(--border);
      align-self: center;
    }

    /* ─── Sections ─── */
    .section {
      max-width: 760px;
      margin: 0 auto;
      padding: 5rem 2rem;
    }
    .section + .section {
      border-top: 1px solid var(--border);
    }

    .section-eyebrow {
      font-size: 11px;
      font-weight: 500;
      letter-spacing: 0.1em;
      text-transform: uppercase;
      margin-bottom: 0.75rem;
    }
    .eyebrow-problem { color: var(--accent-red); }
    .eyebrow-opdracht { color: var(--accent-amber); }
    .eyebrow-fase1 { color: var(--accent-blue); }
    .eyebrow-fase2 { color: var(--accent-teal); }
    .eyebrow-fase3 { color: var(--accent-purple); }
    .eyebrow-result { color: var(--accent-teal); }

    .section-title {
      font-family: 'DM Serif Display', serif;
      font-size: clamp(1.6rem, 3vw, 2.2rem);
      font-weight: 400;
      line-height: 1.25;
      color: var(--text-primary);
      margin-bottom: 1.25rem;
    }
    .section-body {
      font-size: 16px;
      color: var(--text-secondary);
      line-height: 1.8;
    }
    .section-body p + p { margin-top: 1rem; }
    .section-body strong {
      color: var(--text-primary);
      font-weight: 500;
    }

    /* ─── Tags ─── */
    .tag-row {
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      margin-top: 1.5rem;
    }
    .tag {
      font-size: 12px;
      font-weight: 500;
      padding: 5px 13px;
      border-radius: 999px;
      border: 1px solid;
    }
    .tag-red    { color: #f08080; border-color: rgba(224,90,90,0.3); background: rgba(224,90,90,0.08); }
    .tag-blue   { color: #7eb8f0; border-color: rgba(74,144,217,0.3); background: rgba(74,144,217,0.08); }
    .tag-teal   { color: #5ddcb0; border-color: rgba(47,203,150,0.3); background: rgba(47,203,150,0.08); }
    .tag-purple { color: #c4a8f8; border-color: rgba(155,124,244,0.3); background: rgba(155,124,244,0.08); }
    .tag-amber  { color: #f5c36a; border-color: rgba(240,168,50,0.3); background: rgba(240,168,50,0.08); }

    /* ─── Phase card ─── */
    .phase-card {
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: 16px;
      padding: 1.75rem 2rem;
      margin-top: 2rem;
    }
    .phase-card-header {
      display: flex;
      align-items: center;
      gap: 12px;
      margin-bottom: 1rem;
    }
    .phase-dot {
      width: 10px; height: 10px;
      border-radius: 50%;
      flex-shrink: 0;
    }
    .dot-blue   { background: var(--accent-blue); }
    .dot-teal   { background: var(--accent-teal); }
    .dot-purple { background: var(--accent-purple); }
    .phase-card-label {
      font-size: 12px;
      font-weight: 600;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: var(--text-muted);
    }

    /* ─── Result grid ─── */
    .result-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
      gap: 12px;
      margin-top: 1.5rem;
    }
    .result-item {
      background: var(--bg-subtle);
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 1.25rem;
    }
    .result-icon {
      font-size: 22px;
      margin-bottom: 0.5rem;
    }
    .result-name {
      font-size: 14px;
      font-weight: 500;
      color: var(--text-primary);
      margin-bottom: 4px;
    }
    .result-desc {
      font-size: 13px;
      color: var(--text-muted);
      line-height: 1.5;
    }

    /* ─── Timeline connector ─── */
    .timeline {
      display: flex;
      flex-direction: column;
      gap: 0;
      margin-top: 2.5rem;
    }
    .timeline-item {
      display: grid;
      grid-template-columns: 48px 1fr;
      gap: 0 1.25rem;
      position: relative;
    }
    .timeline-left {
      display: flex;
      flex-direction: column;
      align-items: center;
    }
    .timeline-circle {
      width: 36px; height: 36px;
      border-radius: 50%;
      border: 2px solid;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 13px;
      font-weight: 600;
      flex-shrink: 0;
      background: var(--bg);
      position: relative;
      z-index: 1;
    }
    .circle-blue   { border-color: var(--accent-blue);   color: var(--accent-blue); }
    .circle-teal   { border-color: var(--accent-teal);   color: var(--accent-teal); }
    .circle-purple { border-color: var(--accent-purple); color: var(--accent-purple); }
    .timeline-line {
      width: 2px;
      flex: 1;
      background: var(--border);
      margin: 4px 0;
      min-height: 24px;
    }
    .timeline-content {
      padding-bottom: 2.5rem;
    }
    .timeline-phase {
      font-size: 11px;
      font-weight: 600;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      margin-bottom: 0.4rem;
    }
    .tc-blue   { color: var(--accent-blue); }
    .tc-teal   { color: var(--accent-teal); }
    .tc-purple { color: var(--accent-purple); }
    .timeline-heading {
      font-family: 'DM Serif Display', serif;
      font-size: 1.3rem;
      font-weight: 400;
      color: var(--text-primary);
      margin-bottom: 0.6rem;
      line-height: 1.3;
    }
    .timeline-text {
      font-size: 14px;
      color: var(--text-secondary);
      line-height: 1.7;
    }

    /* ─── Final CTA ─── */
    .cta-section {
      text-align: center;
      padding: 6rem 2rem;
      border-top: 1px solid var(--border);
    }
    .cta-title {
      font-family: 'DM Serif Display', serif;
      font-size: clamp(1.8rem, 4vw, 3rem);
      font-weight: 400;
      color: var(--text-primary);
      margin-bottom: 1rem;
    }
    .cta-sub {
      font-size: 16px;
      color: var(--text-secondary);
      max-width: 480px;
      margin: 0 auto 2rem;
    }
    .badge-row {
      display: flex;
      justify-content: center;
      flex-wrap: wrap;
      gap: 10px;
    }
    .badge {
      font-size: 13px;
      font-weight: 500;
      padding: 8px 18px;
      border-radius: 999px;
      border: 1px solid var(--border);
      color: var(--text-secondary);
      background: var(--bg-card);
    }

    /* ─── Footer ─── */
    footer {
      text-align: center;
      padding: 2rem;
      font-size: 13px;
      color: var(--text-muted);
      border-top: 1px solid var(--border);
    }

    /* ─── Responsive ─── */
    @media (max-width: 600px) {
      nav { padding: 0 1rem; }
      .nav-links { display: none; }
      .section { padding: 3.5rem 1.25rem; }
      .hero { padding: 5rem 1.25rem 3rem; }
      .hero-meta { gap: 1rem; }
      .phase-card { padding: 1.25rem; }
    }
  </style>
</head>
<body>

  <nav>
    <div class="nav-logo">Inspire<span>Offices</span></div>
    <ul class="nav-links">
      <li><a href="#probleem">Probleem</a></li>
      <li><a href="#oplossing">Oplossing</a></li>
      <li><a href="#resultaat">Resultaat</a></li>
    </ul>
  </nav>

  <section class="hero">
    <div class="hero-eyebrow">Fontys ICT — Proftaak 2025</div>
    <h1 class="hero-title">Van <em>kwetsbaar netwerk</em> naar Zero Trust infrastructuur</h1>
    <p class="hero-sub">Hoe een team van Fontys ICT-studenten in 15 weken een veilige, schaalbare basis bouwde voor Inspire Offices — van fysiek lab tot cloud.</p>
    <div class="hero-meta">
      <div class="meta-item">
        <span class="meta-value">15</span>
        <span class="meta-label">Weken</span>
      </div>
      <div class="meta-divider"></div>
      <div class="meta-item">
        <span class="meta-value">3</span>
        <span class="meta-label">Fases</span>
      </div>
      <div class="meta-divider"></div>
      <div class="meta-item">
        <span class="meta-value">400+</span>
        <span class="meta-label">Flexplekken</span>
      </div>
      <div class="meta-divider"></div>
      <div class="meta-item">
        <span class="meta-value">6</span>
        <span class="meta-label">Studenten</span>
      </div>
    </div>
  </section>

  <section class="section" id="probleem">
    <div class="section-eyebrow eyebrow-problem">Het probleem</div>
    <h2 class="section-title">Een co-working space met grote ambities — en een kwetsbare basis</h2>
    <div class="section-body">
      <p>Inspire Offices in Tilburg biedt 150 flexplekken aan professionals die direct productief willen zijn. Maar in de praktijk klagen huurders over <strong>onstabiele wifi</strong>, trage verbindingen en printproblemen. Erger nog: niemand kan aantonen dat data van de ene huurder echt gescheiden blijft van de andere.</p>
      <p>Met een tweede locatie in de <strong>Suikerfabriek Zevenbergen</strong> (250+ plekken) in het vooruitzicht — en het cybersecuritybedrijf SecureMeister als eerste grote klant — staat Inspire voor een kritisch moment. SecureMeister stelt hoge eisen: aantoonbare segmentatie, sterke identity, logging en een basis voor incident response. <strong>Geen half werk.</strong></p>
    </div>
    <div class="tag-row">
      <span class="tag tag-red">Onstabiele wifi</span>
      <span class="tag tag-red">Geen netwerksegmentatie</span>
      <span class="tag tag-red">Privacy-risico's</span>
      <span class="tag tag-red">Geen centrale identity</span>
      <span class="tag tag-red">Geen logging</span>
    </div>
  </section>

  <section class="section">
    <div class="section-eyebrow eyebrow-opdracht">De opdracht</div>
    <h2 class="section-title">Bouw het fundament dat Inspire kan laten groeien</h2>
    <div class="section-body">
      <p>Wij kregen de opdracht om in 15 weken — verdeeld over drie fases — een veilige, schaalbare infrastructuur te bouwen. Niet alles in één keer perfect, maar telkens een <strong>werkend, aantoonbaar resultaat</strong> dat als basis dient voor de volgende stap.</p>
      <p>Met elke fase meer complexiteit, meer cloud, en meer security-volwassenheid. Opgeleverd in korte cycli, met bewijs dat het werkt.</p>
    </div>
  </section>

  <section class="section" id="oplossing">
    <div class="section-eyebrow eyebrow-fase1">De oplossing</div>
    <h2 class="section-title">Drie fases, één doorlopend verhaal</h2>

    <div class="timeline">

      <div class="timeline-item">
        <div class="timeline-left">
          <div class="timeline-circle circle-blue">1</div>
          <div class="timeline-line"></div>
        </div>
        <div class="timeline-content">
          <div class="timeline-phase tc-blue">Fase 1 — On-prem fundament</div>
          <div class="timeline-heading">Een veilig netwerk — fysiek, tastbaar, aantoonbaar</div>
          <p class="timeline-text">We begonnen in het Mobile Infra Lab: een fysiek lab dat de situatie op locatie simuleert. Hier bouwden we de basisinfrastructuur die Inspire nodig heeft. Gescheiden netwerken voor gasten, huurders, beheer en IoT. Een toegangscontrole-PoC met passen en scanners. Een veilige printoplossing via pull-print. En een ontwerp voor Single Sign-On dat later kon aansluiten op de cloud.</p>
          <div class="tag-row">
            <span class="tag tag-blue">Netwerksegmentatie</span>
            <span class="tag tag-blue">Toegangscontrole PoC</span>
            <span class="tag tag-blue">Pull-print</span>
            <span class="tag tag-blue">SSO-ontwerp</span>
            <span class="tag tag-blue">Firewallregels + logging</span>
          </div>
        </div>
      </div>

      <div class="timeline-item">
        <div class="timeline-left">
          <div class="timeline-circle circle-teal">2</div>
          <div class="timeline-line"></div>
        </div>
        <div class="timeline-content">
          <div class="timeline-phase tc-teal">Fase 2 — Cloud & hybride koppeling</div>
          <div class="timeline-heading">Azure als ruggengraat — identity die niet gaat zweven</div>
          <p class="timeline-text">Met het fysieke fundament op orde, was de volgende uitdaging: hoe zorgen we dat meerdere locaties niet elk hun eigen ICT-eiland worden? Het antwoord: Azure en Entra ID als centrale verbinding. We richtten een cloud landing zone in met tagging, RBAC en policies. Bouwden hybride connectiviteit. Implementeerden SSO met MFA en Conditional Access. En zetten centrale logging op met aandacht voor AVG/GDPR.</p>
          <div class="tag-row">
            <span class="tag tag-teal">Azure Landing Zone</span>
            <span class="tag tag-teal">Entra ID / SSO</span>
            <span class="tag tag-teal">MFA & Conditional Access</span>
            <span class="tag tag-teal">SIEM-lite logging</span>
            <span class="tag tag-teal">AVG/GDPR compliance</span>
          </div>
        </div>
      </div>

      <div class="timeline-item">
        <div class="timeline-left">
          <div class="timeline-circle circle-purple">3</div>
        </div>
        <div class="timeline-content">
          <div class="timeline-phase tc-purple">Fase 3 — Zero Trust & modernisering</div>
          <div class="timeline-heading">Operationeel volwassen — klaar voor de toekomst</div>
          <p class="timeline-text">In de laatste fase maakten we de omgeving klaar voor de realiteit van een groeiende co-working space. We bouwden een intern selfservice-portaal beveiligd via Entra ID. Containeriseerden componenten met een CI/CD-flow. Hardenden de omgeving op Zero Trust-principes. Werkten een volledig incident response-scenario uit met forensics. En maakten het netwerk toekomstbestendig met IPv6 en DNS-security.</p>
          <div class="tag-row">
            <span class="tag tag-purple">Selfservice portaal</span>
            <span class="tag tag-purple">Containers + CI/CD</span>
            <span class="tag tag-purple">Zero Trust hardening</span>
            <span class="tag tag-purple">Incident response & forensics</span>
            <span class="tag tag-purple">IPv6 + DNS-security</span>
          </div>
        </div>
      </div>

    </div>
  </section>

  <section class="section" id="resultaat">
    <div class="section-eyebrow eyebrow-result">Het resultaat</div>
    <h2 class="section-title">Van klachten naar een blueprint voor groei</h2>
    <div class="section-body">
      <p>Wat begon als een co-working space met wifi-klachten en privacyzorgen, is nu voorzien van een infrastructuur die Inspire Offices in staat stelt om te groeien naar meerdere locaties — zonder dat security, beheer of compliance daarbij achterblijft.</p>
      <p>SecureMeister heeft een omgeving die voldoet aan hun eisen. Inspire heeft een <strong>blueprint voor schaalbare groei</strong>. En wij hebben in 15 weken laten zien hoe je van een probleem naar een werkende, aantoonbare oplossing bouwt.</p>
    </div>
    <div class="result-grid">
      <div class="result-item">
        <div class="result-icon">🔒</div>
        <div class="result-name">Aantoonbare segmentatie</div>
        <div class="result-desc">Gast, huurder, beheer en IoT volledig gescheiden</div>
      </div>
      <div class="result-item">
        <div class="result-icon">☁️</div>
        <div class="result-name">Hybride cloud</div>
        <div class="result-desc">Azure Landing Zone met Entra ID als centrale identity</div>
      </div>
      <div class="result-item">
        <div class="result-icon">🛡️</div>
        <div class="result-name">Zero Trust</div>
        <div class="result-desc">Least privilege, MFA, Conditional Access en logging</div>
      </div>
      <div class="result-item">
        <div class="result-icon">📋</div>
        <div class="result-name">Incident ready</div>
        <div class="result-desc">Forensics, tijdlijn en responsetaken uitgewerkt</div>
      </div>
      <div class="result-item">
        <div class="result-icon">⚙️</div>
        <div class="result-name">Herhaalbaar beheer</div>
        <div class="result-desc">Containers, CI/CD en selfservice-portaal</div>
      </div>
      <div class="result-item">
        <div class="result-icon">📈</div>
        <div class="result-name">Schaalbaar</div>
        <div class="result-desc">Klaar voor derde locatie zonder ICT-eilanden</div>
      </div>
    </div>
  </section>

  <div class="cta-section">
    <h2 class="cta-title">Gebouwd in 15 weken.<br>Ontworpen voor de toekomst.</h2>
    <p class="cta-sub">Een Fontys ICT proftaak door een team van studenten — infra en cybersecurity gecombineerd.</p>
    <div class="badge-row">
      <span class="badge">Fontys ICT</span>
      <span class="badge">Infra & Cyber</span>
      <span class="badge">Cybermeister</span>
      <span class="badge">Azure / Entra ID</span>
      <span class="badge">Zero Trust</span>
    </div>
  </div>

  <footer>
    Inspire Offices — Proftaak 2025 · Fontys ICT
  </footer>

</body>
</html>
"""

@app.route("/")
def home():
    return HTML_TEMPLATE

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)