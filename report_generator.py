from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def generate_report(blocked_ips, total_packets):
    styles = getSampleStyleSheet()
    report = SimpleDocTemplate("Security_Report.pdf")

    content = []
    content.append(Paragraph("AI Network Breach Containment Report", styles["Title"]))
    content.append(Spacer(1,10))
    content.append(Paragraph(f"Total Packets Analyzed: {total_packets}", styles["BodyText"]))
    content.append(Spacer(1,10))
    content.append(Paragraph("Blocked IP Addresses:", styles["Heading2"]))

    for ip in blocked_ips:
        content.append(Paragraph(ip, styles["BodyText"]))

    report.build(content)
