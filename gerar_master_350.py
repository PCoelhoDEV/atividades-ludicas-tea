#!/usr/bin/env python3
import os, sys, json
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable
)
from reportlab.pdfgen import canvas

W, H = A4
OUT_DIR = "/home/pedrocoelho/Downloads/atividades-autismo/materiais_entrega"
os.makedirs(OUT_DIR, exist_ok=True)

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super().showPage()
        super().save()

    def draw_page_decorations(self, total_pages):
        self.saveState()
        if self._pageNumber > 1:
            self.setFont("Helvetica-Bold", 8)
            self.setFillColor(colors.HexColor("#1e3a8a"))
            self.drawString(40, H - 28, "MÉTODO ESTIMULA TEA · PROFª HELENA REZENDE")
            self.setFont("Helvetica", 8)
            self.setFillColor(colors.HexColor("#64748b"))
            self.drawRightString(W - 40, H - 28, "GUIA CLÍNICO E PRÁTICO · +350 DINÂMICAS ADAPTADAS")
            self.setStrokeColor(colors.HexColor("#cbd5e1"))
            self.setLineWidth(0.6)
            self.line(40, H - 32, W - 40, H - 32)

        self.setStrokeColor(colors.HexColor("#cbd5e1"))
        self.setLineWidth(0.6)
        self.line(40, 32, W - 40, 32)
        self.setFont("Helvetica", 8)
        self.setFillColor(colors.HexColor("#64748b"))
        self.drawString(40, 20, "© Portal Estimula TEA · Todos os direitos reservados. Material de uso pessoal e clínico.")
        self.setFont("Helvetica-Bold", 8)
        self.setFillColor(colors.HexColor("#1e3a8a"))
        self.drawRightString(W - 40, 20, f"Página {self._pageNumber} de {total_pages}")
        self.restoreState()

styles = getSampleStyleSheet()

# Custom styles
st_title = ParagraphStyle('T', fontName='Helvetica-Bold', fontSize=24, leading=28, textColor=colors.HexColor('#1e3a8a'), alignment=1, spaceAfter=8)
st_sub = ParagraphStyle('S', fontName='Helvetica', fontSize=12, leading=16, textColor=colors.HexColor('#475569'), alignment=1, spaceAfter=14)
st_intro = ParagraphStyle('I', fontName='Helvetica', fontSize=9.5, leading=14.5, textColor=colors.HexColor('#1e293b'), spaceAfter=8)
st_intro_b = ParagraphStyle('IB', fontName='Helvetica-Bold', fontSize=10, leading=14.5, textColor=colors.HexColor('#0f172a'), spaceAfter=8)

st_cat_h = ParagraphStyle('CH', fontName='Helvetica-Bold', fontSize=15, leading=19, textColor=colors.HexColor('#1e3a8a'), spaceBefore=14, spaceAfter=8, keepWithNext=True)

st_act_title = ParagraphStyle('AT', fontName='Helvetica-Bold', fontSize=11, leading=14, textColor=colors.HexColor('#0f172a'))
st_act_meta = ParagraphStyle('AM', fontName='Helvetica-Bold', fontSize=8, leading=10, textColor=colors.HexColor('#4338ca'))
st_act_obj = ParagraphStyle('AO', fontName='Helvetica', fontSize=8.5, leading=12, textColor=colors.HexColor('#334155'))
st_act_mat = ParagraphStyle('AMAT', fontName='Helvetica-Bold', fontSize=8, leading=11, textColor=colors.HexColor('#047857'))
st_act_step = ParagraphStyle('AS', fontName='Helvetica', fontSize=8.5, leading=12, textColor=colors.HexColor('#1e293b'))
st_act_tip = ParagraphStyle('ATIP', fontName='Helvetica-Oblique', fontSize=8, leading=11, textColor=colors.HexColor('#b45309'))

# Load activities from app
with open('/home/pedrocoelho/Downloads/app-dinamicas-tea/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('const ACTIVITIES =')
end = text.find(';\n', pos)
activities = json.loads(text[pos + len('const ACTIVITIES ='):end])
print(f"Carregadas {len(activities)} dinâmicas com sucesso.")

cat_names = {
    'foco': '1. FOCO, ATENÇÃO SUSTENTADA E CONCENTRAÇÃO',
    'comunicacao': '2. COMUNICAÇÃO, FALA E INTENÇÃO VERBAL',
    'sensorial': '3. INTEGRAÇÃO SENSORIAL E TÁTIL',
    'coordenacao': '4. COORDENAÇÃO MOTORA FINA E GRAFOMOTRICIDADE',
    'regulacao': '5. REGULAÇÃO EMOCIONAL E PREVENÇÃO DE CRISES',
    'social': '6. SOCIALIZAÇÃO, TROCA E CONTATO VISUAL',
    'pratica': '7. AUTONOMIA, ROTINA E VIDA PRÁTICA'
}

cat_colors = {
    'foco': ('#eff6ff', '#bfdbfe', '#1d4ed8'),
    'comunicacao': ('#f0fdf4', '#bbf7d0', '#15803d'),
    'sensorial': ('#fefce8', '#fef08a', '#a16207'),
    'coordenacao': ('#faf5ff', '#e9d5ff', '#7e22ce'),
    'regulacao': ('#fff1f2', '#fecdd3', '#be123c'),
    'social': ('#ecfeff', '#a5f3fc', '#0e7490'),
    'pratica': ('#f8fafc', '#cbd5e1', '#334155')
}

doc = SimpleDocTemplate(
    f"{OUT_DIR}/01_Manual_Oficial_350_Dinamicas_TEA.pdf",
    pagesize=A4,
    leftMargin=36,
    rightMargin=36,
    topMargin=42,
    bottomMargin=42
)

story = []

# CAPA E INTRODUÇÃO
story.append(Spacer(1, 20))
story.append(Paragraph("+350 DINÂMICAS E ATIVIDADES ADAPTADAS", st_title))
story.append(Paragraph("Manual Oficial de Neurodesenvolvimento, Comunicação e Regulação para Crianças no TEA<br/><b>Profª Helena Rezende · Pedagoga e Especialista em Intervenção Precoce</b>", st_sub))
story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor("#1e3a8a"), spaceAfter=16))

story.append(Paragraph("COMO UTILIZAR ESTE MANUAL COM SUA CRIANÇA", st_cat_h))
story.append(Paragraph("Estimada mãe, pai, terapeuta ou educador: O cérebro da criança com Transtorno do Espectro Autista (TEA) aprende com previsibilidade, motivação de interesse restrito e estímulos sensoriais graduados. Este manual reúne <b>todas as 350 dinâmicas práticas</b> do Método Estimula TEA, catalogadas por objetivos clínicos.", st_intro))
story.append(Paragraph("<b>Diretrizes Fundamentais para a Prática Diária:</b><br/>"
"1. <b>Sessões Curtas e Positivas:</b> Pratique de 10 a 15 minutos por vez, sem transformar a brincadeira em cobrança escolar.<br/>"
"2. <b>Respeito ao Limite Sensorial:</b> Se a criança demonstrar sobrecarga (fechar os ouvidos, afastar o corpo, autoestimulação intensa), encerre gentilmente e vá para um momento de descompressão.<br/>"
"3. <b>Adaptação dos Materiais:</b> Quase todas as atividades usam itens que você já tem em casa (prendedores, caixas de ovos, água, grãos, massinha).<br/>"
"4. <b>Celebração de Cada Micro-Avanço:</b> Um olhar de 3 segundos, apontar para um objeto ou tolerar uma nova textura por 10 segundos são vitórias monumentais.", st_intro))

story.append(Spacer(1, 14))

# Agrupar por categorias
grouped = {}
for act in activities:
    cat = act.get('category', 'foco')
    grouped.setdefault(cat, []).append(act)

for cat_code, cat_title in cat_names.items():
    act_list = grouped.get(cat_code, [])
    if not act_list:
        continue

    story.append(PageBreak())
    bg_col, border_col, text_col = cat_colors.get(cat_code, ('#f8fafc', '#cbd5e1', '#334155'))

    # Header da Categoria
    cat_banner = Table(
        [[Paragraph(f"<b>{cat_title}</b> ({len(act_list)} Atividades Prontas)", ParagraphStyle('CB', fontName='Helvetica-Bold', fontSize=12, textColor=colors.HexColor('#ffffff')))]],
        colWidths=[W - 72]
    )
    cat_banner.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor(text_col)),
        ('TOPPADDING', (0,0), (-1,-1), 8),
        ('BOTTOMPADDING', (0,0), (-1,-1), 8),
        ('LEFTPADDING', (0,0), (-1,-1), 12),
        ('RIGHTPADDING', (0,0), (-1,-1), 12),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
    ]))
    story.append(cat_banner)
    story.append(Spacer(1, 10))

    # Adicionar cada atividade em card estilizado
    for a in act_list:
        aid = a.get('id', '')
        title = a.get('title', '')
        age = a.get('age', 'Todas as idades')
        dur = a.get('duration', 10)
        diff = a.get('difficulty', 'fácil').capitalize()
        obj = a.get('objective', a.get('desc', ''))
        mats = ", ".join(a.get('materials', [])) if a.get('materials') else "Itens domésticos comuns"
        steps = a.get('steps', [])
        steps_html = "<br/>".join([f"<b>{i+1}.</b> {s}" for i, s in enumerate(steps)])
        tip = a.get('tip', '')

        card_content = [
            Paragraph(f"<b>#{aid} · {title}</b>", st_act_title),
            Paragraph(f"Idade sugerida: <b>{age} anos</b> | Duração: <b>{dur} min</b> | Dificuldade: <b>{diff}</b>", st_act_meta),
            Spacer(1, 3),
            Paragraph(f"<b>🎯 Objetivo Terapêutico:</b> {obj}", st_act_obj),
            Paragraph(f"<b>📦 Materiais Necessários:</b> {mats}", st_act_mat),
            Spacer(1, 2),
            Paragraph(f"<b>Passo a Passo:</b><br/>{steps_html}", st_act_step),
        ]
        if tip:
            card_content.append(Spacer(1, 2))
            card_content.append(Paragraph(f"💡 <b>Dica da Profª Helena:</b> {tip}", st_act_tip))

        card_table = Table([[card_content]], colWidths=[W - 72])
        card_table.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,-1), colors.HexColor(bg_col)),
            ('BOX', (0,0), (-1,-1), 0.8, colors.HexColor(border_col)),
            ('TOPPADDING', (0,0), (-1,-1), 6),
            ('BOTTOMPADDING', (0,0), (-1,-1), 6),
            ('LEFTPADDING', (0,0), (-1,-1), 10),
            ('RIGHTPADDING', (0,0), (-1,-1), 10),
        ]))

        story.append(KeepTogether([card_table, Spacer(1, 8)]))

doc.build(story, canvasmaker=NumberedCanvas)
print("Sucesso! E-Book Master gerado:", f"{OUT_DIR}/01_Manual_Oficial_350_Dinamicas_TEA.pdf")
