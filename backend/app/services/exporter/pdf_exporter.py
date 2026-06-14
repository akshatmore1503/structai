"""Generate PDF design reports using ReportLab."""
import io
from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
)
from reportlab.lib.enums import TA_LEFT, TA_CENTER


_BRAND = colors.HexColor("#6366f1")  # indigo-500
_DARK = colors.HexColor("#111827")
_GRAY = colors.HexColor("#6b7280")
_LIGHT = colors.HexColor("#f3f4f6")


def _styles():
    s = getSampleStyleSheet()
    s.add(ParagraphStyle("Brand", parent=s["Title"], textColor=_BRAND, fontSize=22, spaceAfter=4))
    s.add(ParagraphStyle("SectionHead", parent=s["Heading1"], textColor=_DARK, fontSize=14, spaceBefore=14, spaceAfter=6))
    s.add(ParagraphStyle("CompHead", parent=s["Heading2"], textColor=_BRAND, fontSize=12, spaceBefore=10, spaceAfter=4))
    s.add(ParagraphStyle("Body", parent=s["Normal"], textColor=_DARK, fontSize=10, leading=14))
    s.add(ParagraphStyle("Meta", parent=s["Normal"], textColor=_GRAY, fontSize=9))
    s.add(ParagraphStyle("Tag", parent=s["Normal"], textColor=_BRAND, fontSize=9, fontName="Helvetica-Bold"))
    return s


def generate_pdf(problem_statement: str, architecture: dict, explanations: dict) -> bytes:
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(
        buffer,
        pagesize=letter,
        leftMargin=0.85 * inch,
        rightMargin=0.85 * inch,
        topMargin=0.85 * inch,
        bottomMargin=0.85 * inch,
    )
    s = _styles()
    story = []

    # ── Header ────────────────────────────────────────────────────────────────
    story.append(Paragraph("StructAI", s["Brand"]))
    story.append(Paragraph("System Design Report", s["SectionHead"]))
    story.append(Paragraph(
        f"Generated {datetime.utcnow().strftime('%B %d, %Y %H:%M UTC')}",
        s["Meta"],
    ))
    story.append(HRFlowable(width="100%", thickness=2, color=_BRAND, spaceAfter=12))

    # ── Problem Statement ─────────────────────────────────────────────────────
    story.append(Paragraph("Problem Statement", s["SectionHead"]))
    story.append(Paragraph(problem_statement, s["Body"]))
    story.append(Spacer(1, 8))

    # ── Summary ───────────────────────────────────────────────────────────────
    summary = architecture.get("summary", "")
    if summary:
        story.append(Paragraph("Architecture Overview", s["SectionHead"]))
        story.append(Paragraph(summary, s["Body"]))
        story.append(Spacer(1, 8))

    # ── Tech Stack ────────────────────────────────────────────────────────────
    tech_stack = architecture.get("tech_stack", [])
    if tech_stack:
        story.append(Paragraph("Tech Stack", s["SectionHead"]))
        tech_data = [[Paragraph(t, s["Body"]) for t in tech_stack[i:i+3]] for i in range(0, len(tech_stack), 3)]
        # Pad last row
        if tech_data and len(tech_data[-1]) < 3:
            tech_data[-1] += [Paragraph("", s["Body"])] * (3 - len(tech_data[-1]))
        t = Table(tech_data, colWidths=[2.1 * inch] * 3)
        t.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, -1), _LIGHT),
            ("GRID", (0, 0), (-1, -1), 0.5, colors.white),
            ("ROWBACKGROUNDS", (0, 0), (-1, -1), [_LIGHT, colors.white]),
            ("LEFTPADDING", (0, 0), (-1, -1), 8),
            ("RIGHTPADDING", (0, 0), (-1, -1), 8),
            ("TOPPADDING", (0, 0), (-1, -1), 6),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ]))
        story.append(t)
        story.append(Spacer(1, 12))

    # ── Components ────────────────────────────────────────────────────────────
    nodes = architecture.get("nodes", [])
    if nodes:
        story.append(Paragraph("Architecture Components", s["SectionHead"]))
        for node in nodes:
            story.append(Paragraph(f"{node['label']}", s["CompHead"]))
            story.append(Paragraph(f"<b>Type:</b> {node['type']}  |  <b>Tech:</b> {node['tech']}", s["Meta"]))
            story.append(Paragraph(node.get("description", ""), s["Body"]))

            exp = explanations.get(node["id"])
            if exp:
                story.append(Spacer(1, 4))
                if exp.get("why"):
                    story.append(Paragraph(f"<b>Why chosen:</b> {exp['why']}", s["Body"]))
                alts = exp.get("alternatives", [])
                if alts:
                    story.append(Paragraph(f"<b>Alternatives:</b> {', '.join(alts)}", s["Body"]))
                if exp.get("trade_offs"):
                    story.append(Paragraph(f"<b>Trade-offs:</b> {exp['trade_offs']}", s["Body"]))

            story.append(Spacer(1, 6))

    # ── Data Flow ─────────────────────────────────────────────────────────────
    edges = architecture.get("edges", [])
    if edges:
        story.append(Paragraph("Data Flow", s["SectionHead"]))
        node_map = {n["id"]: n["label"] for n in nodes}
        flow_data = [
            [
                Paragraph(node_map.get(e["source"], e["source"]), s["Body"]),
                Paragraph("→", s["Body"]),
                Paragraph(node_map.get(e["target"], e["target"]), s["Body"]),
                Paragraph(e.get("label", ""), s["Meta"]),
            ]
            for e in edges
        ]
        ft = Table(flow_data, colWidths=[2.0 * inch, 0.4 * inch, 2.0 * inch, 1.9 * inch])
        ft.setStyle(TableStyle([
            ("ROWBACKGROUNDS", (0, 0), (-1, -1), [colors.white, _LIGHT]),
            ("GRID", (0, 0), (-1, -1), 0.3, colors.HexColor("#e5e7eb")),
            ("LEFTPADDING", (0, 0), (-1, -1), 6),
            ("TOPPADDING", (0, 0), (-1, -1), 4),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ]))
        story.append(ft)

    doc.build(story)
    return buffer.getvalue()
