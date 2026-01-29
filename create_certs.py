from fpdf import FPDF

def create_certificate(data):
    pdf = FPDF()
    pdf.add_page()
    
    # Cornice
    pdf.rect(5, 5, 200, 287)
    
    # Titolo
    pdf.set_font("Helvetica", "B", 24)
    pdf.ln(40)
    pdf.cell(0, 10, "CERTIFICATO DI COMPLETAMENTO", ln=True, align="C")
    
    pdf.ln(20)
    pdf.set_font("Helvetica", "", 16)
    pdf.cell(0, 10, "Si attesta che il dipendente", ln=True, align="C")
    
    # Nome Dipendente
    pdf.set_font("Helvetica", "B", 20)
    pdf.cell(0, 15, data["name"], ln=True, align="C")
    
    pdf.ln(10)
    pdf.set_font("Helvetica", "", 16)
    pdf.cell(0, 10, "ha partecipato con successo al corso di aggiornamento in:", ln=True, align="C")
    
    # Titolo Corso
    pdf.set_font("Helvetica", "B", 18)
    pdf.set_text_color(0, 51, 102) # Blu scuro
    pdf.cell(0, 15, data["course_title"], ln=True, align="C")
    
    pdf.ln(10)
    pdf.set_text_color(0, 0, 0)
    pdf.set_font("Helvetica", "I", 12)
    pdf.multi_cell(0, 10, f"Descrizione: {data['description']}", align="C")
    
    # Sede e Data
    pdf.ln(20)
    pdf.set_font("Helvetica", "", 12)
    pdf.cell(0, 10, f"Sede Aziendale: {data['location']} | Data: Gennaio 2026", ln=True, align="C")
    
    # Salva il file
    filename = f"Certificato_{data['name'].replace(' ', '_')}_{data['course_id']}.pdf"
    pdf.output(filename)
    print(f"Creato: {filename}")

# Dati dei corsi
corsi = [
    {
        "name": "Marco Esposito",
        "course_id": "1",
        "course_title": "AI Ethics & Governance",
        "location": "Londra",
        "description": "Analisi dei bias negli algoritmi e regolamentazione AI Act europeo."
    },
    {
        "name": "Marco Esposito",
        "course_id": "2",
        "course_title": "Advanced Cloud Security",
        "location": "Londra",
        "description": "Protezione di architetture serverless e crittografia dati in transito."
    },
    {
        "name": "Giulia Bianchi",
        "course_id": "1",
        "course_title": "Green Logistics & Sustainability",
        "location": "Singapore",
        "description": "Ottimizzazione delle rotte per la riduzione dell'impronta di carbonio."
    },
    {
        "name": "Alessandro Conti",
        "course_id": "1",
        "course_title": "Blockchain for Supply Chain",
        "location": "Milano",
        "description": "Utilizzo di smart contracts per la tracciabilità dei farmaci."
    }
]

for c in corsi:
    create_certificate(c)