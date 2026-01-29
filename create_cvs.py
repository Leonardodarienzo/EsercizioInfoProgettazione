from fpdf import FPDF

def create_cv(data):
    pdf = FPDF()
    pdf.add_page()
    
    # Intestazione (Nome)
    pdf.set_font("Helvetica", "B", 20)
    pdf.cell(0, 10, data["name"], ln=True, align="C")
    
    # Sede e Ruolo
    pdf.set_font("Helvetica", "I", 12)
    pdf.cell(0, 10, f"Sede: {data['location']} | Ruolo: {data['role']}", ln=True, align="C")
    pdf.ln(10)
    
    # Sezione Competenze Tecniche
    pdf.set_font("Helvetica", "B", 14)
    pdf.cell(0, 10, "Competenze Tecniche", ln=True)
    pdf.set_font("Helvetica", "", 12)
    pdf.multi_cell(0, 10, data["skills"])
    pdf.ln(5)
    
    # Sezione Esperienza
    pdf.set_font("Helvetica", "B", 14)
    pdf.cell(0, 10, "Esperienza Professionale", ln=True)
    pdf.set_font("Helvetica", "", 12)
    pdf.multi_cell(0, 10, data["experience"])
    pdf.ln(5)
    
    # Sezione Competenze Extra (Hidden Talent)
    pdf.set_font("Helvetica", "B", 14)
    pdf.cell(0, 10, "Altre Competenze e Lingue", ln=True)
    pdf.set_font("Helvetica", "I", 12)
    pdf.multi_cell(0, 10, data["hidden"])
    
    # Salva il file
    filename = f"CV_{data['name'].replace(' ', '_')}.pdf"
    pdf.output(filename)
    print(f"Creato: {filename}")

# Dati dei 5 profili
profili = [
    {
        "name": "Mario Rossi",
        "location": "Milano, Italia",
        "role": "Senior Research Scientist",
        "skills": "Sintesi organica avanzata, polimeri plastici, spettroscopia NMR, catalisi industriale.",
        "experience": "10 anni nel laboratorio R&D di Milano. Responsabile della stabilità termica dei reattori chimici e ottimizzazione dei processi di sintesi.",
        "hidden": "Lingue: Italiano (Madrelingua), Tedesco (Livello C2 certificato)."
    },
    {
        "name": "Giulia Bianchi",
        "location": "Singapore",
        "role": "Project Manager & Logistics Lead",
        "skills": "Gestione Supply Chain globale, ottimizzazione magazzino, esperta certificata SAP S/4HANA.",
        "experience": "Coordinamento della distribuzione farmaceutica nel sud-est asiatico. Gestione flussi doganali e logistica integrata.",
        "hidden": "Certificazioni extra: Crisis Management e Business Continuity."
    },
    {
        "name": "Marco Esposito",
        "location": "Londra, UK",
        "role": "Data Scientist",
        "skills": "Python, TensorFlow, PyTorch, Machine Learning applicato alla Drug Discovery.",
        "experience": "Sviluppo di modelli predittivi per analizzare la tossicità dei composti chimici e accelerare la ricerca farmacologica.",
        "hidden": "Competenze database: SQL avanzato, NoSQL (MongoDB) e Data Visualization."
    },
    {
        "name": "Elena Ferrari",
        "location": "New York, USA",
        "role": "Global Brand Manager",
        "skills": "Strategie di lancio prodotti, analisi di mercato USA, conformità FDA (Food and Drug Administration).",
        "experience": "Lancio di 3 farmaci di successo negli Stati Uniti. Gestione budget marketing multi-milionari e relazioni con gli stakeholder.",
        "hidden": "Soft Skills: Public Speaking a conferenze internazionali e leadership di team multiculturali."
    },
    {
        "name": "Alessandro Conti",
        "location": "Milano, Italia",
        "role": "IT Infrastructure Specialist",
        "skills": "Cloud Architecture (AWS/Azure), Cybersecurity, gestione server remoti e virtualizzazione.",
        "experience": "Responsabile della sicurezza informatica e dell'infrastruttura dati dei laboratori di ricerca italiani.",
        "hidden": "Hobby tecnici: Progettazione di micro-elettronica e circuiti stampati (PCB)."
    }
]

# Genera i PDF
for p in profili:
    create_cv(p)