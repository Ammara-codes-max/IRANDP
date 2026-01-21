import os
from datetime import datetime
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

LOG_FILE = "incidents.log"

def generate_report():
    if not os.path.exists(LOG_FILE):
        print("❌ incidents.log not found")
        return None

    styles = getSampleStyleSheet()
    filename = f"Incident_Report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
    doc = SimpleDocTemplate(filename)

    story = []
    story.append(Paragraph("SentinelX – Network Intrusion Forensic Report", styles["Title"]))
    story.append(Spacer(1,10))
    story.append(Paragraph(f"Generated at: {datetime.now()}", styles["Normal"]))
    story.append(PageBreak())

    table_data = [["Time","IP Address","Packets","Risk Level","Details"]]

    total_alerts = 0
    high_risk = 0

    with open(LOG_FILE, "r") as f:
        for line in f:
            parts = [p.strip() for p in line.split("|")]
            if len(parts) < 4:
                continue

            time = parts[0]
            ip = parts[1].replace("IP:","")
            packets = parts[2].replace("Packets:","")
            risk = parts[3].replace("Risk:","")
            details = parts[4] if len(parts) > 4 else "N/A"

            table_data.append([time, ip, packets, risk, details])

            total_alerts += 1
            if risk.upper() == "HIGH":
                high_risk += 1

    story.append(Paragraph("Incident Timeline", styles["Heading2"]))
    table = Table(table_data, repeatRows=1)

    table.setStyle(TableStyle([
        ('BACKGROUND',(0,0),(-1,0),colors.darkblue),
        ('TEXTCOLOR',(0,0),(-1,0),colors.whitesmoke),
        ('GRID',(0,0),(-1,-1),0.5,colors.black),
        ('BACKGROUND',(0,1),(-1,-1),colors.beige),
        ('ALIGN',(2,1),(2,-1),'CENTER'),
    ]))

    story.append(table)
    story.append(PageBreak())

    story.append(Paragraph("Summary", styles["Heading2"]))
    story.append(Paragraph(f"Total Incidents Detected: {total_alerts}", styles["Normal"]))
    story.append(Paragraph(f"High Risk Events: {high_risk}", styles["Normal"]))

    doc.build(story)
    print(f"✅ {filename} generated successfully")
    return filename
