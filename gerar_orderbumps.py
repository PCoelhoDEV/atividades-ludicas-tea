#!/usr/bin/env python3
"""
GERADOR DOS 6 ORDER BUMPS DE ELITE - PORTAL ESTIMULA TEA
"""
import os, sys
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
            self.drawString(36, H - 28, "MÉTODO ESTIMULA TEA · PROFª HELENA REZENDE")
            self.setFont("Helvetica", 8)
            self.setFillColor(colors.HexColor("#64748b"))
            self.drawRightString(W - 36, H - 28, "KIT OFICIAL DE SUPORTE CLÍNICO E FAMILIAR")
            self.setStrokeColor(colors.HexColor("#cbd5e1"))
            self.setLineWidth(0.6)
            self.line(36, H - 32, W - 36, H - 32)

        self.setStrokeColor(colors.HexColor("#cbd5e1"))
        self.setLineWidth(0.6)
        self.line(36, 30, W - 36, 30)
        self.setFont("Helvetica", 8)
        self.setFillColor(colors.HexColor("#64748b"))
        self.drawString(36, 18, "© Portal Estimula TEA · Todos os direitos reservados. Material de uso pessoal e clínico.")
        self.setFont("Helvetica-Bold", 8)
        self.setFillColor(colors.HexColor("#1e3a8a"))
        self.drawRightString(W - 36, 18, f"Página {self._pageNumber} de {total_pages}")
        self.restoreState()

styles = getSampleStyleSheet()

# Estilos universais
st_title = ParagraphStyle('T', fontName='Helvetica-Bold', fontSize=22, leading=26, textColor=colors.HexColor('#1e3a8a'), alignment=1, spaceAfter=6)
st_sub = ParagraphStyle('S', fontName='Helvetica', fontSize=11, leading=15, textColor=colors.HexColor('#475569'), alignment=1, spaceAfter=14)
st_h1 = ParagraphStyle('H1', fontName='Helvetica-Bold', fontSize=14, leading=18, textColor=colors.HexColor('#1e3a8a'), spaceBefore=12, spaceAfter=6, keepWithNext=True)
st_h2 = ParagraphStyle('H2', fontName='Helvetica-Bold', fontSize=11, leading=15, textColor=colors.HexColor('#0f766e'), spaceBefore=8, spaceAfter=4, keepWithNext=True)
st_body = ParagraphStyle('B', fontName='Helvetica', fontSize=9, leading=13.5, textColor=colors.HexColor('#1e293b'), spaceAfter=5)
st_body_bold = ParagraphStyle('BB', fontName='Helvetica-Bold', fontSize=9, leading=13.5, textColor=colors.HexColor('#0f172a'), spaceAfter=4)
st_box = ParagraphStyle('BX', fontName='Helvetica', fontSize=8.5, leading=12.5, textColor=colors.HexColor('#334155'))

st_card_title = ParagraphStyle('CT', fontName='Helvetica-Bold', fontSize=9, leading=11, textColor=colors.HexColor('#0f172a'), alignment=1)
st_card_sub = ParagraphStyle('CS', fontName='Helvetica-Bold', fontSize=7, leading=9, textColor=colors.HexColor('#64748b'), alignment=1)
st_card_tag = ParagraphStyle('CTG', fontName='Helvetica-Bold', fontSize=6.5, leading=8, textColor=colors.HexColor('#ffffff'), alignment=1)

def make_callout(title, text, bg="#f8fafc", border="#cbd5e1", title_color="#0f766e"):
    p_t = Paragraph(f"<b>{title}</b>", ParagraphStyle('CallT', fontName='Helvetica-Bold', fontSize=10, textColor=colors.HexColor(title_color), spaceAfter=3))
    p_b = Paragraph(text, st_box)
    t = Table([[ [p_t, p_b] ]], colWidths=[W - 72])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor(bg)),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor(border)),
        ('TOPPADDING', (0,0), (-1,-1), 7),
        ('BOTTOMPADDING', (0,0), (-1,-1), 7),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
    ]))
    return t

# ==========================================
# 1. OB 1: KIT DE ROTINA VISUAL (132 CARTÕES)
# ==========================================
def build_ob1_rotina():
    doc = SimpleDocTemplate(f"{OUT_DIR}/02_Kit_Rotina_Visual_132_Cartoes_e_Pranchas.pdf", pagesize=A4, leftMargin=28, rightMargin=28, topMargin=36, bottomMargin=36)
    story = []

    # Capa & Instruções
    story.append(Paragraph("KIT DE ROTINA VISUAL E PREVISIBILIDADE", st_title))
    story.append(Paragraph("132 Cartões Ilustrados Prontos para Imprimir, Plastificar e Recortar + 3 Pranchas Estruturadas<br/><b>Método TEACCH Adaptado · Profª Helena Rezende</b>", st_sub))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor("#1e3a8a"), spaceAfter=12))

    story.append(make_callout(
        "COMO PREPARAR E USAR SEUS CARTÕES DE ROTINA",
        "<b>1. Impressão:</b> Imprima preferencialmente em papel sulfite 120g ou papel fotográfico fosco para maior durabilidade.<br/>"
        "<b>2. Plastificação:</b> Plastifique com folhas de polaseal (ou passe fita adesiva transparente grossa nas duas faces).<br/>"
        "<b>3. Montagem com Velcro:</b> Cole um pedaço de velcro adesivo no verso de cada cartão e nas pranchas (páginas finais).<br/>"
        "<b>4. O Segredo da Transição:</b> Sempre aponte para o cartão 5 minutos antes de mudar de atividade dizendo: <i>'Acabou o brincar, agora é banho'</i>. Isso elimina 90% das crises de transição!",
        bg="#eff6ff", border="#93c5fd", title_color="#1d4ed8"
    ))
    story.append(Spacer(1, 14))

    # Lista dos 132 cartões
    cards_data = [
        # Manhã (24)
        ("Acordar", "MANHÃ", "🌅", "#1e40af", "#eff6ff"),
        ("Tirar o Pijama", "MANHÃ", "👕", "#1e40af", "#eff6ff"),
        ("Ir ao Banheiro", "MANHÃ", "🚽", "#1e40af", "#eff6ff"),
        ("Fazer Xixi", "MANHÃ", "💧", "#1e40af", "#eff6ff"),
        ("Lavar o Rosto", "MANHÃ", "🧼", "#1e40af", "#eff6ff"),
        ("Escovar os Dentes", "MANHÃ", "🪥", "#1e40af", "#eff6ff"),
        ("Pentear o Cabelo", "MANHÃ", "🪮", "#1e40af", "#eff6ff"),
        ("Tomar Café", "MANHÃ", "🥛", "#1e40af", "#eff6ff"),
        ("Comer Fruta", "MANHÃ", "🍎", "#1e40af", "#eff6ff"),
        ("Tomar Remédio", "MANHÃ", "💊", "#1e40af", "#eff6ff"),
        ("Colocar a Roupa", "MANHÃ", "🧦", "#1e40af", "#eff6ff"),
        ("Calçar as Meias", "MANHÃ", "🧦", "#1e40af", "#eff6ff"),
        ("Calçar o Tênis", "MANHÃ", "👟", "#1e40af", "#eff6ff"),
        ("Passar Protetor", "MANHÃ", "🧴", "#1e40af", "#eff6ff"),
        ("Pegar a Mochila", "MANHÃ", "🎒", "#1e40af", "#eff6ff"),
        ("Entrar no Carro", "MANHÃ", "🚗", "#1e40af", "#eff6ff"),
        ("Entrar na Van/Ônibus", "MANHÃ", "🚌", "#1e40af", "#eff6ff"),
        ("Andar a Pé", "MANHÃ", "🚶", "#1e40af", "#eff6ff"),
        ("Chegar na Escola", "MANHÃ", "🏫", "#1e40af", "#eff6ff"),
        ("Dar Tchau pra Mamãe", "MANHÃ", "👋", "#1e40af", "#eff6ff"),
        ("Guardar a Mochila", "MANHÃ", "🎒", "#1e40af", "#eff6ff"),
        ("Sentar na Roda", "MANHÃ", "⭕", "#1e40af", "#eff6ff"),
        ("Ouvir a Professora", "MANHÃ", "👩‍🏫", "#1e40af", "#eff6ff"),
        ("Hora da Atividade", "MANHÃ", "✏️", "#1e40af", "#eff6ff"),

        # Escola & Aprendizado (24)
        ("Pintar com Lápis", "ESCOLA", "🎨", "#b45309", "#fffbeb"),
        ("Cortar com Tesoura", "ESCOLA", "✂️", "#b45309", "#fffbeb"),
        ("Usar Cola", "ESCOLA", "🧴", "#b45309", "#fffbeb"),
        ("Brincar de Massinha", "ESCOLA", "🟢", "#b45309", "#fffbeb"),
        ("Hora da Leitura", "ESCOLA", "📖", "#b45309", "#fffbeb"),
        ("Lanche da Escola", "ESCOLA", "🥪", "#b45309", "#fffbeb"),
        ("Beber Água", "ESCOLA", "🥤", "#b45309", "#fffbeb"),
        ("Lavar as Mãos", "ESCOLA", "🧼", "#b45309", "#fffbeb"),
        ("Hora do Recreio", "ESCOLA", "🛝", "#b45309", "#fffbeb"),
        ("Brincar no Pátio", "ESCOLA", "🏃", "#b45309", "#fffbeb"),
        ("Esperar na Fila", "ESCOLA", "🚶‍♂️", "#b45309", "#fffbeb"),
        ("Dividir o Brinquedo", "ESCOLA", "🤝", "#b45309", "#fffbeb"),
        ("Educação Física", "ESCOLA", "⚽", "#b45309", "#fffbeb"),
        ("Hora da Música", "ESCOLA", "🎵", "#b45309", "#fffbeb"),
        ("Guardar o Material", "ESCOLA", "📦", "#b45309", "#fffbeb"),
        ("Saída da Escola", "ESCOLA", "🚪", "#b45309", "#fffbeb"),
        ("Encontrar a Mamãe", "ESCOLA", "👩‍👦", "#b45309", "#fffbeb"),
        ("Terapia ABA", "ESCOLA", "🧩", "#b45309", "#fffbeb"),
        ("Fonoaudióloga", "ESCOLA", "🗣️", "#b45309", "#fffbeb"),
        ("Terapeuta Ocupacional", "ESCOLA", "🖐️", "#b45309", "#fffbeb"),
        ("Psicóloga", "ESCOLA", "🧠", "#b45309", "#fffbeb"),
        ("Fisioterapia", "ESCOLA", "🤸", "#b45309", "#fffbeb"),
        ("Natação", "ESCOLA", "🏊", "#b45309", "#fffbeb"),
        ("Musicoterapia", "ESCOLA", "🥁", "#b45309", "#fffbeb"),

        # Tarde & Lazer (24)
        ("Almoçar", "TARDE", "🍽️", "#15803d", "#f0fdf4"),
        ("Comer Salada", "TARDE", "🥗", "#15803d", "#f0fdf4"),
        ("Comer Carninha", "TARDE", "🍗", "#15803d", "#f0fdf4"),
        ("Comer Arroz e Feijão", "TARDE", "🍚", "#15803d", "#f0fdf4"),
        ("Limpar a Boca", "TARDE", "🧻", "#15803d", "#f0fdf4"),
        ("Descanso / Soneca", "TARDE", "🛋️", "#15803d", "#f0fdf4"),
        ("Fazer Lição de Casa", "TARDE", "📝", "#15803d", "#f0fdf4"),
        ("Brincar Livre", "TARDE", "🧸", "#15803d", "#f0fdf4"),
        ("Montar Quebra-Cabeça", "TARDE", "🧩", "#15803d", "#f0fdf4"),
        ("Brincar com Carrinhos", "TARDE", "🏎️", "#15803d", "#f0fdf4"),
        ("Brincar com Bonecos", "TARDE", "🦸", "#15803d", "#f0fdf4"),
        ("Blocos de Encaixar", "TARDE", "🧱", "#15803d", "#f0fdf4"),
        ("Hora do Tablet / TV", "TARDE", "📺", "#15803d", "#f0fdf4"),
        ("Timer do Tablet Apitou", "TARDE", "⏰", "#15803d", "#f0fdf4"),
        ("Desligar o Tablet", "TARDE", "📴", "#15803d", "#f0fdf4"),
        ("Guardar os Brinquedos", "TARDE", "🧺", "#15803d", "#f0fdf4"),
        ("Lanche da Tarde", "TARDE", "🍌", "#15803d", "#f0fdf4"),
        ("Passear no Parque", "TARDE", "🌳", "#15803d", "#f0fdf4"),
        ("Andar de Bicicleta", "TARDE", "🚲", "#15803d", "#f0fdf4"),
        ("Brincar com o Cachorro", "TARDE", "🐕", "#15803d", "#f0fdf4"),
        ("Tomar Banho de Mangueira", "TARDE", "💦", "#15803d", "#f0fdf4"),
        ("Pular Cama Elástica", "TARDE", "🦘", "#15803d", "#f0fdf4"),
        ("Visitar a Vovó", "TARDE", "👵", "#15803d", "#f0fdf4"),
        ("Ir ao Supermercado", "TARDE", "🛒", "#15803d", "#f0fdf4"),

        # Noite & Higiene (24)
        ("Jantar em Família", "NOITE", "🍲", "#7e22ce", "#faf5ff"),
        ("Ajudar a Tirar a Mesa", "NOITE", "🍽️", "#7e22ce", "#faf5ff"),
        ("Hora do Banho", "NOITE", "🛁", "#7e22ce", "#faf5ff"),
        ("Tirar a Roupa Suja", "NOITE", "🧺", "#7e22ce", "#faf5ff"),
        ("Lavar o Cabelo", "NOITE", "🧴", "#7e22ce", "#faf5ff"),
        ("Enxaguar o Corpo", "NOITE", "🚿", "#7e22ce", "#faf5ff"),
        ("Secar com a Toalha", "NOITE", "🧖", "#7e22ce", "#faf5ff"),
        ("Vestir o Pijama", "NOITE", "👕", "#7e22ce", "#faf5ff"),
        ("Cortar a Unha", "NOITE", "💅", "#7e22ce", "#faf5ff"),
        ("Limpar o Ouvido", "NOITE", "👂", "#7e22ce", "#faf5ff"),
        ("Escovar os Dentes", "NOITE", "🪥", "#7e22ce", "#faf5ff"),
        ("Fazer Xixi Antes de Deitar", "NOITE", "🚽", "#7e22ce", "#faf5ff"),
        ("Passar Hidratante", "NOITE", "🧴", "#7e22ce", "#faf5ff"),
        ("Massagem Relaxante", "NOITE", "💆", "#7e22ce", "#faf5ff"),
        ("Ouvir História", "NOITE", "📚", "#7e22ce", "#faf5ff"),
        ("Ouvir Ruído Branco / Som", "NOITE", "🎶", "#7e22ce", "#faf5ff"),
        ("Abraço de Boa Noite", "NOITE", "🤗", "#7e22ce", "#faf5ff"),
        ("Beijo do Papai e Mamãe", "NOITE", "😘", "#7e22ce", "#faf5ff"),
        ("Deitar na Cama", "NOITE", "🛏️", "#7e22ce", "#faf5ff"),
        ("Puxar o Cobertor Pesado", "NOITE", "🛌", "#7e22ce", "#faf5ff"),
        ("Luz Fraca / Abajur", "NOITE", "💡", "#7e22ce", "#faf5ff"),
        ("Apagar a Luz", "NOITE", "🌑", "#7e22ce", "#faf5ff"),
        ("Ficar no Quarto", "NOITE", "🚪", "#7e22ce", "#faf5ff"),
        ("Dormir a Noite Toda", "NOITE", "💤", "#7e22ce", "#faf5ff"),

        # Emoções, Regulação & Transição (36)
        ("Estou Feliz", "EMOÇÕES", "😊", "#be123c", "#fff1f2"),
        ("Estou Triste", "EMOÇÕES", "😢", "#be123c", "#fff1f2"),
        ("Estou Bravo / Irritado", "EMOÇÕES", "😠", "#be123c", "#fff1f2"),
        ("Estou Cansado", "EMOÇÕES", "🥱", "#be123c", "#fff1f2"),
        ("Estou com Medo", "EMOÇÕES", "😨", "#be123c", "#fff1f2"),
        ("Estou Assustado", "EMOÇÕES", "😱", "#be123c", "#fff1f2"),
        ("Barulho Muito Alto", "EMOÇÕES", "🙉", "#be123c", "#fff1f2"),
        ("Colocar Abafador de Ruído", "EMOÇÕES", "🎧", "#be123c", "#fff1f2"),
        ("Luz Muito Forte", "EMOÇÕES", "🕶️", "#be123c", "#fff1f2"),
        ("Quero Silêncio", "EMOÇÕES", "🤫", "#be123c", "#fff1f2"),
        ("Preciso de um Abraço", "EMOÇÕES", "🫂", "#be123c", "#fff1f2"),
        ("Quero Colo", "EMOÇÕES", "🤱", "#be123c", "#fff1f2"),
        ("Respira Fundo (Cheira Flor)", "EMOÇÕES", "🌸", "#be123c", "#fff1f2"),
        ("Assopra a Vela", "EMOÇÕES", "🎂", "#be123c", "#fff1f2"),
        ("Ir para o Cantinho da Calma", "EMOÇÕES", "🏕️", "#be123c", "#fff1f2"),
        ("Apertar a Bolinha", "EMOÇÕES", "🟢", "#be123c", "#fff1f2"),
        ("Olhar a Garrafa da Calma", "EMOÇÕES", "✨", "#be123c", "#fff1f2"),
        ("Mordedor Sensorial", "EMOÇÕES", "🦷", "#be123c", "#fff1f2"),
        ("Quero Ficar Sozinho", "EMOÇÕES", "🧘", "#be123c", "#fff1f2"),
        ("Estou Calmo Agora", "EMOÇÕES", "😌", "#be123c", "#fff1f2"),
        ("Primeiro", "TRANSIÇÃO", "1️⃣", "#0e7490", "#ecfeff"),
        ("Depois", "TRANSIÇÃO", "2️⃣", "#0e7490", "#ecfeff"),
        ("Agora", "TRANSIÇÃO", "⏰", "#0e7490", "#ecfeff"),
        ("Próximo", "TRANSIÇÃO", "➡️", "#0e7490", "#ecfeff"),
        ("Acabou / Fim", "TRANSIÇÃO", "🛑", "#0e7490", "#ecfeff"),
        ("Esperar 1 Minuto", "TRANSIÇÃO", "⏳", "#0e7490", "#ecfeff"),
        ("Mais Um Pouco", "TRANSIÇÃO", "➕", "#0e7490", "#ecfeff"),
        ("Trocar de Roupa", "TRANSIÇÃO", "👚", "#0e7490", "#ecfeff"),
        ("Guardar Tudo", "TRANSIÇÃO", "📦", "#0e7490", "#ecfeff"),
        ("Parabéns! Conseguiu!", "REFORÇO", "⭐", "#0e7490", "#ecfeff"),
        ("Ganhou uma Estrelinha", "REFORÇO", "🌟", "#0e7490", "#ecfeff"),
        ("Muito Orgulho de Você!", "REFORÇO", "🏆", "#0e7490", "#ecfeff"),
        ("Bate Aqui! (High Five)", "REFORÇO", "✋", "#0e7490", "#ecfeff"),
        ("Hora do Abraço Gostoso", "REFORÇO", "❤️", "#0e7490", "#ecfeff"),
        ("Brincadeira Favorita", "REFORÇO", "🎮", "#0e7490", "#ecfeff"),
        ("Passeio Especial", "REFORÇO", "🍦", "#0e7490", "#ecfeff"),
    ]

    # Renderizar em páginas de 12 cartões (3 colunas x 4 linhas)
    col_w = (W - 56) / 3
    card_h = 160

    for page_idx in range(0, len(cards_data), 12):
        story.append(PageBreak())
        batch = cards_data[page_idx:page_idx+12]
        table_matrix = []
        for r in range(4):
            row_cells = []
            for c in range(3):
                idx = r * 3 + c
                if idx < len(batch):
                    title, cat, icon, color_hex, bg_hex = batch[idx]
                    cell_flow = [
                        Table([[Paragraph(cat, ParagraphStyle('TC', fontName='Helvetica-Bold', fontSize=7, textColor=colors.HexColor('#ffffff'), alignment=1))]],
                              colWidths=[col_w - 24], rowHeights=[14]),
                        Spacer(1, 4),
                        Paragraph(f"<font size=24>{icon}</font>", ParagraphStyle('ICO', alignment=1)),
                        Spacer(1, 4),
                        Paragraph(f"<b>{title}</b>", st_card_title),
                        Spacer(1, 3),
                        Paragraph("✂️ recorte na linha pontilhada", st_card_sub)
                    ]
                    # style table tag
                    cell_flow[0].setStyle(TableStyle([
                        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor(color_hex)),
                        ('TOPPADDING', (0,0), (-1,-1), 1),
                        ('BOTTOMPADDING', (0,0), (-1,-1), 1),
                        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
                    ]))

                    card_box = Table([[cell_flow]], colWidths=[col_w - 12], rowHeights=[card_h])
                    card_box.setStyle(TableStyle([
                        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor(bg_hex)),
                        ('BOX', (0,0), (-1,-1), 1, colors.HexColor(color_hex)),
                        ('TOPPADDING', (0,0), (-1,-1), 6),
                        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
                        ('LEFTPADDING', (0,0), (-1,-1), 6),
                        ('RIGHTPADDING', (0,0), (-1,-1), 6),
                        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
                    ]))
                    row_cells.append(card_box)
                else:
                    row_cells.append("")
            table_matrix.append(row_cells)

        grid_table = Table(table_matrix, colWidths=[col_w, col_w, col_w])
        grid_table.setStyle(TableStyle([
            ('ALIGN', (0,0), (-1,-1), 'CENTER'),
            ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
            ('BOTTOMPADDING', (0,0), (-1,-1), 10),
            ('TOPPADDING', (0,0), (-1,-1), 10),
        ]))
        story.append(grid_table)

    # PRANCHA 1: PRIMEIRO / DEPOIS
    story.append(PageBreak())
    story.append(Paragraph("PRANCHA ESTRUTURADA: PRIMEIRO E DEPOIS", st_title))
    story.append(Paragraph("Cole o velcro nos retângulos abaixo para organizar transições e evitar sobrecargas.", st_sub))
    story.append(Spacer(1, 15))

    p1_box = Table([
        [
            Table([
                [Paragraph("<b>1. PRIMEIRO</b>", ParagraphStyle('P1', fontName='Helvetica-Bold', fontSize=18, textColor=colors.HexColor('#1e40af'), alignment=1))],
                [Spacer(1, 30)],
                [Paragraph("<font size=11 color='#64748b'>[ Cole o Cartão Aqui com Velcro ]</font>", ParagraphStyle('C1', alignment=1))],
                [Spacer(1, 30)]
            ], colWidths=[(W-90)/2], rowHeights=[35, 30, 80, 30]),
            Table([
                [Paragraph("<b>2. DEPOIS</b>", ParagraphStyle('P2', fontName='Helvetica-Bold', fontSize=18, textColor=colors.HexColor('#15803d'), alignment=1))],
                [Spacer(1, 30)],
                [Paragraph("<font size=11 color='#64748b'>[ Cole o Cartão da Recompensa ]</font>", ParagraphStyle('C2', alignment=1))],
                [Spacer(1, 30)]
            ], colWidths=[(W-90)/2], rowHeights=[35, 30, 80, 30])
        ]
    ], colWidths=[(W-72)/2, (W-72)/2])
    p1_box.setStyle(TableStyle([
        ('BOX', (0,0), (0,0), 2, colors.HexColor('#2563eb')),
        ('BACKGROUND', (0,0), (0,0), colors.HexColor('#eff6ff')),
        ('BOX', (1,0), (1,0), 2, colors.HexColor('#16a34a')),
        ('BACKGROUND', (1,0), (1,0), colors.HexColor('#f0fdf4')),
        ('TOPPADDING', (0,0), (-1,-1), 14),
        ('BOTTOMPADDING', (0,0), (-1,-1), 14),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
    ]))
    story.append(p1_box)
    story.append(Spacer(1, 20))
    story.append(make_callout(
        "COMO USAR ESTA PRANCHA NO DIA A DIA",
        "Quando a criança recusar uma atividade essencial (ex: tomar banho, guardar os brinquedos, almoçar):<br/>"
        "1. No quadro <b>PRIMEIRO</b>, coloque o cartão da tarefa necessária (ex: Guardar os Brinquedos).<br/>"
        "2. No quadro <b>DEPOIS</b>, coloque o cartão de algo altamente motivador (ex: Parque, Massinha ou Tablet).<br/>"
        "3. Aponte calmamente e diga apenas: <i>'Primeiro guardar, depois parque.'</i> Não entre em debate. A previsibilidade visual reduz a ansiedade imediatamente.",
        bg="#fefce8", border="#fde047", title_color="#854d0e"
    ))

    # PRANCHA 2: MINHA ROTINA DIÁRIA (Manhã, Tarde e Noite)
    story.append(PageBreak())
    story.append(Paragraph("PRANCHA COMPLETA: MINHA ROTINA DO DIA", st_title))
    story.append(Paragraph("Monte a sequência de 5 cartões para cada período do dia.", st_sub))
    story.append(Spacer(1, 10))

    def make_period_row(title, color_hex, bg_hex):
        cells = [Paragraph(f"<b>{title}</b>", ParagraphStyle('PER', fontName='Helvetica-Bold', fontSize=12, textColor=colors.HexColor('#ffffff'), alignment=1))]
        for i in range(5):
            slot = Table([[Paragraph(f"<font size=8 color='#64748b'>Passo {i+1}<br/>[Velcro]</font>", ParagraphStyle('SL', alignment=1))]],
                         colWidths=[(W-140)/5], rowHeights=[70])
            slot.setStyle(TableStyle([
                ('BOX', (0,0), (-1,-1), 1, colors.HexColor(color_hex)),
                ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#ffffff')),
                ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
            ]))
            cells.append(slot)
        t = Table([[cells[0], cells[1], cells[2], cells[3], cells[4], cells[5]]],
                  colWidths=[65, (W-140)/5, (W-140)/5, (W-140)/5, (W-140)/5, (W-140)/5])
        t.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (0,0), colors.HexColor(color_hex)),
            ('BOX', (0,0), (-1,-1), 1.5, colors.HexColor(color_hex)),
            ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
            ('ALIGN', (0,0), (-1,-1), 'CENTER'),
            ('TOPPADDING', (0,0), (-1,-1), 6),
            ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ]))
        return t

    story.append(make_period_row("MANHÃ", "#1d4ed8", "#eff6ff"))
    story.append(Spacer(1, 16))
    story.append(make_period_row("TARDE", "#15803d", "#f0fdf4"))
    story.append(Spacer(1, 16))
    story.append(make_period_row("NOITE", "#7e22ce", "#faf5ff"))
    story.append(Spacer(1, 20))
    story.append(make_callout(
        "REGRAS DE OURO DA ROTINA VISUAL",
        "• Nunca mude a rotina sem avisar com pelo menos 10 minutos de antecedência.<br/>"
        "• Quando a criança concluir um passo, ensine-a a tirar o cartão e colocar em uma caixinha de 'CONCLUÍDO'. Essa ação física ativa o sistema de dopamina e sensação de dever cumprido!",
        bg="#f0fdf4", border="#86efac", title_color="#166534"
    ))

    doc.build(story, canvasmaker=NumberedCanvas)
    print("OB 1 gerado: 02_Kit_Rotina_Visual_132_Cartoes_e_Pranchas.pdf")

build_ob1_rotina()

# ==========================================
# 2. OB 2: CARTÕES DE COMUNICAÇÃO ALTERNATIVA (120 CARTÕES + 2 PRANCHAS)
# ==========================================
def build_ob2_comunicacao():
    doc = SimpleDocTemplate(f"{OUT_DIR}/03_Cartoes_Comunicacao_Alternativa_PECS_120_Cartoes.pdf", pagesize=A4, leftMargin=28, rightMargin=28, topMargin=36, bottomMargin=36)
    story = []

    # Capa & Instruções
    story.append(Paragraph("CARTÕES DE COMUNICAÇÃO ALTERNATIVA E AUMENTATIVA (CAA / PECS)", st_title))
    story.append(Paragraph("120 Cartões Ilustrados Prontos para Uso Imediato + 2 Pranchas de Comunicação Funcional<br/><b>Para Crianças Não Verbais ou com Pouca Fala · Profª Helena Rezende</b>", st_sub))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor("#1e3a8a"), spaceAfter=12))

    story.append(make_callout(
        "COMO USAR A COMUNICAÇÃO ALTERNATIVA SEM TRAVAR A FALA NATURAL",
        "<b>Mito comum:</b> <i>'Usar cartões vai fazer meu filho ficar preguiçoso e não falar?'</i><br/>"
        "<b>Evidência Científica:</b> Não! A comunicação visual reduz a frustração extrema e a sobrecarga cerebral. Quando a criança percebe o poder de se comunicar através do cartão, as vias de fala no cérebro são <b>desbloqueadas</b> mais rápido.<br/><br/>"
        "<b>Passo 1 (Troca Física Simples):</b> Quando a criança apontar ou chorar por algo (ex: água), coloque o cartão de ÁGUA na mão dela e ajude-a a te entregar.<br/>"
        "<b>Passo 2 (Reforço Imediato):</b> Entregue o copo de água no mesmo segundo dizendo pausadamente: <i>'Á-GUA. Muito bem!'</i>.",
        bg="#f0fdf4", border="#86efac", title_color="#15803d"
    ))
    story.append(Spacer(1, 14))

    pecs_data = [
        # Necessidades & Fisiologia (24)
        ("Água", "NECESSIDADE", "💧", "#0284c7", "#f0f9ff"),
        ("Xixi", "NECESSIDADE", "🚽", "#0284c7", "#f0f9ff"),
        ("Cocô", "NECESSIDADE", "🧻", "#0284c7", "#f0f9ff"),
        ("Fome / Comer", "NECESSIDADE", "🍽️", "#0284c7", "#f0f9ff"),
        ("Sede / Beber", "NECESSIDADE", "🥤", "#0284c7", "#f0f9ff"),
        ("Estou com Calor", "NECESSIDADE", "🥵", "#0284c7", "#f0f9ff"),
        ("Estou com Frio", "NECESSIDADE", "🥶", "#0284c7", "#f0f9ff"),
        ("Sono / Cansado", "NECESSIDADE", "🥱", "#0284c7", "#f0f9ff"),
        ("Dor de Cabeça", "CORPO & DOR", "🤕", "#e11d48", "#fff1f2"),
        ("Dor de Barriga", "CORPO & DOR", "🤢", "#e11d48", "#fff1f2"),
        ("Machucado", "CORPO & DOR", "🩹", "#e11d48", "#fff1f2"),
        ("Coceira", "CORPO & DOR", "🦟", "#e11d48", "#fff1f2"),
        ("Tomar Banho", "HIGIENE", "🛁", "#0284c7", "#f0f9ff"),
        ("Lavar as Mãos", "HIGIENE", "🧼", "#0284c7", "#f0f9ff"),
        ("Escovar Dente", "HIGIENE", "🪥", "#0284c7", "#f0f9ff"),
        ("Trocar Fralda", "HIGIENE", "🧷", "#0284c7", "#f0f9ff"),
        ("Tirar Sapato", "CONFORTO", "👞", "#0284c7", "#f0f9ff"),
        ("Tirar a Roupa", "CONFORTO", "👕", "#0284c7", "#f0f9ff"),
        ("Cobertor", "CONFORTO", "🛌", "#0284c7", "#f0f9ff"),
        ("Travesseiro", "CONFORTO", "🛋️", "#0284c7", "#f0f9ff"),
        ("Luz Apagada", "CONFORTO", "🌑", "#0284c7", "#f0f9ff"),
        ("Silêncio", "CONFORTO", "🤫", "#0284c7", "#f0f9ff"),
        ("Abafador de Som", "CONFORTO", "🎧", "#0284c7", "#f0f9ff"),
        ("Meu Mordedor", "CONFORTO", "🦷", "#0284c7", "#f0f9ff"),

        # Expressões de Controle & Verbos (24)
        ("Eu Quero", "AÇÃO", "👉", "#16a34a", "#f0fdf4"),
        ("Eu Não Quero", "AÇÃO", "🙅", "#dc2626", "#fef2f2"),
        ("Ajuda / Me Ajuda", "URGENTE", "🆘", "#dc2626", "#fef2f2"),
        ("Mais", "PEDIDO", "➕", "#16a34a", "#f0fdf4"),
        ("Chega / Parar", "PEDIDO", "🛑", "#dc2626", "#fef2f2"),
        ("Esperar", "PEDIDO", "⏳", "#d97706", "#fffbeb"),
        ("Sim", "RESPOSTA", "✅", "#16a34a", "#f0fdf4"),
        ("Não", "RESPOSTA", "❌", "#dc2626", "#fef2f2"),
        ("Obrigado", "SOCIAL", "🙏", "#2563eb", "#eff6ff"),
        ("Por Favor", "SOCIAL", "🤝", "#2563eb", "#eff6ff"),
        ("Minha Vez", "SOCIAL", "🙋", "#2563eb", "#eff6ff"),
        ("Sua Vez", "SOCIAL", "👉", "#2563eb", "#eff6ff"),
        ("Olha Isso!", "ATENÇÃO", "👀", "#7c3aed", "#faf5ff"),
        ("Escuta", "ATENÇÃO", "👂", "#7c3aed", "#faf5ff"),
        ("Gostei", "OPINIÃO", "👍", "#16a34a", "#f0fdf4"),
        ("Não Gostei", "OPINIÃO", "👎", "#dc2626", "#fef2f2"),
        ("Vem Comigo", "AÇÃO", "🏃", "#16a34a", "#f0fdf4"),
        ("Me Dá", "PEDIDO", "🤲", "#16a34a", "#f0fdf4"),
        ("Guardar", "AÇÃO", "📦", "#d97706", "#fffbeb"),
        ("Abrir", "AÇÃO", "🔓", "#16a34a", "#f0fdf4"),
        ("Fechar", "AÇÃO", "🔒", "#dc2626", "#fef2f2"),
        ("Subir", "AÇÃO", "⬆️", "#2563eb", "#eff6ff"),
        ("Descer", "AÇÃO", "⬇️", "#2563eb", "#eff6ff"),
        ("Acabou", "AÇÃO", "🏁", "#64748b", "#f8fafc"),

        # Sentimentos & Estados (24)
        ("Estou Feliz", "EMOÇÃO", "😊", "#059669", "#ecfdf5"),
        ("Estou Triste", "EMOÇÃO", "😢", "#0284c7", "#f0f9ff"),
        ("Estou Bravo", "EMOÇÃO", "😠", "#dc2626", "#fef2f2"),
        ("Estou Assustado", "EMOÇÃO", "😨", "#ea580c", "#fff7ed"),
        ("Muito Barulho", "SOBRECARGA", "🔊", "#ea580c", "#fff7ed"),
        ("Luz Muito Clara", "SOBRECARGA", "☀️", "#ea580c", "#fff7ed"),
        ("Cheiro Ruim", "SOBRECARGA", "👃", "#ea580c", "#fff7ed"),
        ("Roupa Incomodando", "SOBRECARGA", "🏷️", "#ea580c", "#fff7ed"),
        ("Quero Colo", "AFETO", "🤱", "#db2777", "#fdf2f8"),
        ("Quero um Abraço", "AFETO", "🫂", "#db2777", "#fdf2f8"),
        ("Quero um Beijo", "AFETO", "😘", "#db2777", "#fdf2f8"),
        ("Quero Minha Mamãe", "PESSOAS", "👩", "#db2777", "#fdf2f8"),
        ("Quero Meu Papai", "PESSOAS", "👨", "#2563eb", "#eff6ff"),
        ("Quero Meu Irmão/ã", "PESSOAS", "👧", "#7c3aed", "#faf5ff"),
        ("Quero a Vovó", "PESSOAS", "👵", "#059669", "#ecfdf5"),
        ("Quero o Vovô", "PESSOAS", "👴", "#059669", "#ecfdf5"),
        ("Minha Professora", "PESSOAS", "👩‍🏫", "#d97706", "#fffbeb"),
        ("Minha Terapeuta", "PESSOAS", "👩‍⚕️", "#0284c7", "#f0f9ff"),
        ("Meu Amigo", "PESSOAS", "🧒", "#2563eb", "#eff6ff"),
        ("Meu Cachorrinho", "ANIMAIS", "🐶", "#78350f", "#fefce8"),
        ("Meu Gatinho", "ANIMAIS", "🐱", "#78350f", "#fefce8"),
        ("Quero Ficar Sozinho", "CALMA", "🧘", "#475569", "#f8fafc"),
        ("Cantinho da Calma", "CALMA", "🏕️", "#475569", "#f8fafc"),
        ("Estou Bem Agora", "CALMA", "😌", "#059669", "#ecfdf5"),

        # Alimentos & Lanches (24)
        ("Água Gelada", "BEBIDAS", "🥛", "#0284c7", "#f0f9ff"),
        ("Leite", "BEBIDAS", "🥛", "#0284c7", "#f0f9ff"),
        ("Suco de Fruta", "BEBIDAS", "🧃", "#d97706", "#fffbeb"),
        ("Iogurte", "LANCHE", "🥣", "#db2777", "#fdf2f8"),
        ("Maçã", "FRUTAS", "🍎", "#dc2626", "#fef2f2"),
        ("Banana", "FRUTAS", "🍌", "#eab308", "#fefce8"),
        ("Uva", "FRUTAS", "🍇", "#7c3aed", "#faf5ff"),
        ("Morango", "FRUTAS", "🍓", "#dc2626", "#fef2f2"),
        ("Laranja", "FRUTAS", "🍊", "#ea580c", "#fff7ed"),
        ("Pão", "LANCHE", "🍞", "#b45309", "#fffbeb"),
        ("Biscoito / Bolacha", "LANCHE", "🍪", "#b45309", "#fffbeb"),
        ("Torrada", "LANCHE", "🥪", "#b45309", "#fffbeb"),
        ("Bolo", "LANCHE", "🍰", "#db2777", "#fdf2f8"),
        ("Pipoca", "LANCHE", "🍿", "#eab308", "#fefce8"),
        ("Arroz", "ALMOÇO", "🍚", "#475569", "#f8fafc"),
        ("Feijão", "ALMOÇO", "🍲", "#78350f", "#fefce8"),
        ("Macarrão", "ALMOÇO", "🍝", "#ea580c", "#fff7ed"),
        ("Batata", "ALMOÇO", "🥔", "#b45309", "#fffbeb"),
        ("Carninha", "ALMOÇO", "🥩", "#991b1b", "#fef2f2"),
        ("Frango", "ALMOÇO", "🍗", "#b45309", "#fffbeb"),
        ("Ovo", "ALMOÇO", "🍳", "#eab308", "#fefce8"),
        ("Queijo", "LANCHE", "🧀", "#eab308", "#fefce8"),
        ("Picolé / Sorvete", "DOCE", "🍦", "#0284c7", "#f0f9ff"),
        ("Chocolate", "DOCE", "🍫", "#78350f", "#fefce8"),

        # Brincadeiras & Lugares (24)
        ("Tablet / Desenho", "LAZER", "📺", "#7c3aed", "#faf5ff"),
        ("Celular", "LAZER", "📱", "#7c3aed", "#faf5ff"),
        ("Música Favorita", "LAZER", "🎵", "#7c3aed", "#faf5ff"),
        ("Massinha", "BRINQUEDO", "🟢", "#059669", "#ecfdf5"),
        ("Bolhas de Sabão", "BRINQUEDO", "🫧", "#0284c7", "#f0f9ff"),
        ("Carrinhos", "BRINQUEDO", "🏎️", "#dc2626", "#fef2f2"),
        ("Bonecos / Heróis", "BRINQUEDO", "🦸", "#2563eb", "#eff6ff"),
        ("Blocos / Lego", "BRINQUEDO", "🧱", "#eab308", "#fefce8"),
        ("Quebra-Cabeça", "BRINQUEDO", "🧩", "#059669", "#ecfdf5"),
        ("Desenhar / Giz", "BRINQUEDO", "🖍️", "#ea580c", "#fff7ed"),
        ("Livro com Figuras", "BRINQUEDO", "📚", "#2563eb", "#eff6ff"),
        ("Pular / Cama Elástica", "MOTOR", "🦘", "#059669", "#ecfdf5"),
        ("Balanço", "MOTOR", "🎪", "#d97706", "#fffbeb"),
        ("Escorregador", "MOTOR", "🛝", "#2563eb", "#eff6ff"),
        ("Bola de Futebol", "MOTOR", "⚽", "#475569", "#f8fafc"),
        ("Bicicleta / Velotrol", "MOTOR", "🚲", "#059669", "#ecfdf5"),
        ("Piscina / Banho", "MOTOR", "🏊", "#0284c7", "#f0f9ff"),
        ("Ir ao Parque", "LUGARES", "🌳", "#15803d", "#f0fdf4"),
        ("Passear de Carro", "LUGARES", "🚗", "#2563eb", "#eff6ff"),
        ("Ir para a Escola", "LUGARES", "🏫", "#d97706", "#fffbeb"),
        ("Ir para a Terapia", "LUGARES", "🏥", "#0284c7", "#f0f9ff"),
        ("Ir para Casa", "LUGARES", "🏠", "#15803d", "#f0fdf4"),
        ("Shopping / Loja", "LUGARES", "🛍️", "#7c3aed", "#faf5ff"),
        ("Médico / Dentista", "LUGARES", "🩺", "#dc2626", "#fef2f2"),
    ]

    col_w = (W - 56) / 3
    card_h = 160

    for page_idx in range(0, len(pecs_data), 12):
        story.append(PageBreak())
        batch = pecs_data[page_idx:page_idx+12]
        table_matrix = []
        for r in range(4):
            row_cells = []
            for c in range(3):
                idx = r * 3 + c
                if idx < len(batch):
                    title, cat, icon, color_hex, bg_hex = batch[idx]
                    cell_flow = [
                        Table([[Paragraph(cat, ParagraphStyle('TC', fontName='Helvetica-Bold', fontSize=7, textColor=colors.HexColor('#ffffff'), alignment=1))]],
                              colWidths=[col_w - 24], rowHeights=[14]),
                        Spacer(1, 4),
                        Paragraph(f"<font size=24>{icon}</font>", ParagraphStyle('ICO', alignment=1)),
                        Spacer(1, 4),
                        Paragraph(f"<b>{title}</b>", st_card_title),
                        Spacer(1, 3),
                        Paragraph("✂️ recorte na linha pontilhada", st_card_sub)
                    ]
                    cell_flow[0].setStyle(TableStyle([
                        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor(color_hex)),
                        ('TOPPADDING', (0,0), (-1,-1), 1),
                        ('BOTTOMPADDING', (0,0), (-1,-1), 1),
                        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
                    ]))
                    card_box = Table([[cell_flow]], colWidths=[col_w - 12], rowHeights=[card_h])
                    card_box.setStyle(TableStyle([
                        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor(bg_hex)),
                        ('BOX', (0,0), (-1,-1), 1, colors.HexColor(color_hex)),
                        ('TOPPADDING', (0,0), (-1,-1), 6),
                        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
                        ('LEFTPADDING', (0,0), (-1,-1), 6),
                        ('RIGHTPADDING', (0,0), (-1,-1), 6),
                        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
                    ]))
                    row_cells.append(card_box)
                else:
                    row_cells.append("")
            table_matrix.append(row_cells)

        grid_table = Table(table_matrix, colWidths=[col_w, col_w, col_w])
        grid_table.setStyle(TableStyle([
            ('ALIGN', (0,0), (-1,-1), 'CENTER'),
            ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
            ('BOTTOMPADDING', (0,0), (-1,-1), 10),
            ('TOPPADDING', (0,0), (-1,-1), 10),
        ]))
        story.append(grid_table)

    # PRANCHA 1 DE COMUNICAÇÃO: EU QUERO...
    story.append(PageBreak())
    story.append(Paragraph("PRANCHA DE COMUNICAÇÃO: 'EU QUERO...'", st_title))
    story.append(Paragraph("Tira de sentença para a criança montar o pedido e entregar ao adulto.", st_sub))
    story.append(Spacer(1, 20))

    strip1 = Table([
        [
            Table([[Paragraph("<b>EU QUERO</b><br/><font size=7 color='#64748b'>[Cartão Fixo]</font>", ParagraphStyle('EQ', fontName='Helvetica-Bold', fontSize=14, textColor=colors.HexColor('#16a34a'), alignment=1))]],
                  colWidths=[120], rowHeights=[90]),
            Table([[Paragraph("<font size=28 color='#16a34a'>+</font>", ParagraphStyle('PLUS', alignment=1))]],
                  colWidths=[40], rowHeights=[90]),
            Table([[Paragraph("<font size=10 color='#64748b'>[ Cole o Cartão do Pedido com Velcro ]<br/>Ex: Água, Pão, Tablet, Brinquedo</font>", ParagraphStyle('SOLO', alignment=1))]],
                  colWidths=[W - 240], rowHeights=[90])
        ]
    ], colWidths=[120, 40, W - 232])
    strip1.setStyle(TableStyle([
        ('BOX', (0,0), (-1,-1), 2, colors.HexColor('#16a34a')),
        ('BACKGROUND', (0,0), (0,0), colors.HexColor('#f0fdf4')),
        ('BACKGROUND', (2,0), (2,0), colors.HexColor('#ffffff')),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
    ]))
    story.append(strip1)
    story.append(Spacer(1, 30))

    # PRANCHA 2 DE COMUNICAÇÃO: EU SINTO...
    story.append(Paragraph("PRANCHA DE EXPRESSÃO EMOCIONAL: 'EU SINTO...'", st_title))
    story.append(Paragraph("Ajuda a criança a identificar e expressar desregulações antes do meltdown.", st_sub))
    story.append(Spacer(1, 20))

    strip2 = Table([
        [
            Table([[Paragraph("<b>EU SINTO</b><br/><font size=7 color='#64748b'>[Cartão Fixo]</font>", ParagraphStyle('ES', fontName='Helvetica-Bold', fontSize=14, textColor=colors.HexColor('#2563eb'), alignment=1))]],
                  colWidths=[120], rowHeights=[90]),
            Table([[Paragraph("<font size=28 color='#2563eb'>+</font>", ParagraphStyle('PLUS', alignment=1))]],
                  colWidths=[40], rowHeights=[90]),
            Table([[Paragraph("<font size=10 color='#64748b'>[ Cole o Cartão do Sentimento ou Sensação ]<br/>Ex: Barulho Alto, Calor, Dor de Barriga, Raiva</font>", ParagraphStyle('SOLO', alignment=1))]],
                  colWidths=[W - 240], rowHeights=[90])
        ]
    ], colWidths=[120, 40, W - 232])
    strip2.setStyle(TableStyle([
        ('BOX', (0,0), (-1,-1), 2, colors.HexColor('#2563eb')),
        ('BACKGROUND', (0,0), (0,0), colors.HexColor('#eff6ff')),
        ('BACKGROUND', (2,0), (2,0), colors.HexColor('#ffffff')),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
    ]))
    story.append(strip2)

    doc.build(story, canvasmaker=NumberedCanvas)
    print("OB 2 gerado: 03_Cartoes_Comunicacao_Alternativa_PECS_120_Cartoes.pdf")

build_ob2_comunicacao()

# ==========================================
# 3. OB 3: MANUAL ANTI-CRISE (5 PRIMEIROS MINUTOS)
# ==========================================
def build_ob3_anticrise():
    doc = SimpleDocTemplate(f"{OUT_DIR}/04_Manual_Anti_Crise_Sensorial_5_Minutos.pdf", pagesize=A4, leftMargin=36, rightMargin=36, topMargin=42, bottomMargin=42)
    story = []

    story.append(Paragraph("MANUAL ANTI-CRISE: OS 5 PRIMEIROS MINUTOS", st_title))
    story.append(Paragraph("Guia Prático de Intervenção Imediata, Descompressão Sensorial e Co-Regulação no TEA<br/><b>Profª Helena Rezende · Neurodesenvolvimento e Terapia Comportamental</b>", st_sub))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor("#1e3a8a"), spaceAfter=14))

    story.append(Paragraph("CAPÍTULO 1: MELTDOWN SENSORIAL VS. BIRRA COMUM", st_h1))
    story.append(Paragraph("O maior erro que pais e educadores cometem é tratar um <b>Meltdown Sensorial</b> como se fosse uma simples birra infantil. Enquanto a birra tem um objetivo operante e para quando o desejo é atendido, o meltdown é uma <b>tempestade neurológica involuntária</b> provocada por sobrecarga sensorial ou exaustão cognitiva.", st_body))

    # Tabela comparativa
    t_comp = Table([
        [
            Paragraph("<b>CARACTERÍSTICA</b>", ParagraphStyle('THC', fontName='Helvetica-Bold', fontSize=8, textColor=colors.HexColor('#ffffff'), alignment=1)),
            Paragraph("<b>BIRRA COMUM (COMPORTAMENTAL)</b>", ParagraphStyle('THB', fontName='Helvetica-Bold', fontSize=8, textColor=colors.HexColor('#ffffff'), alignment=1)),
            Paragraph("<b>MELTDOWN SENSORIAL (TEA)</b>", ParagraphStyle('THM', fontName='Helvetica-Bold', fontSize=8, textColor=colors.HexColor('#ffffff'), alignment=1))
        ],
        [
            Paragraph("<b>Objetivo / Gatilho</b>", st_box),
            Paragraph("Quer algo específico (brinquedo, doce, atenção).", st_box),
            Paragraph("Sobrecarga do sistema nervoso (ruído, luz, cansaço, dor).", st_box)
        ],
        [
            Paragraph("<b>Consciência Social</b>", st_box),
            Paragraph("A criança olha para ver se o adulto está prestando atenção.", st_box),
            Paragraph("Sem controle social; não se importa com quem está em volta.", st_box)
        ],
        [
            Paragraph("<b>Segurança Pessoal</b>", st_box),
            Paragraph("Raramente se machuca intencionalmente.", st_box),
            Paragraph("Risco real de bater a cabeça, morder-se ou se atirar no chão.", st_box)
        ],
        [
            Paragraph("<b>Resolução</b>", st_box),
            Paragraph("Cessa quando ganha o que queria ou cansa da negociação.", st_box),
            Paragraph("Só cessa quando o sistema neurológico despressuriza e esgota.", st_box)
        ],
    ], colWidths=[110, (W-182)/2, (W-182)/2])
    t_comp.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (0,0), colors.HexColor('#1e3a8a')),
        ('BACKGROUND', (1,0), (1,0), colors.HexColor('#d97706')),
        ('BACKGROUND', (2,0), (2,0), colors.HexColor('#dc2626')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#cbd5e1')),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#cbd5e1')),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(t_comp)
    story.append(Spacer(1, 14))

    story.append(Paragraph("CAPÍTULO 2: PROTOCOLO DOS 5 PRIMEIROS MINUTOS", st_h1))
    story.append(Paragraph("Quando a crise estoura, o cérebro pensante (córtex pré-frontal) está desligado. Entrar em debate, brigar ou gritar só adiciona mais decibéis e estímulo sonoro ao cérebro em chamas.", st_body))

    story.append(make_callout(
        "MINUTO 0 A 1: SEGURANÇA IMEDIATA E CORTE DE ESTÍMULOS",
        "• <b>Afaste objetos perigosos:</b> Tire de perto cadeiras pontiagudas, quinas, vidros ou qualquer item que a criança possa arremessar.<br/>"
        "• <b>Corte a luz e o som:</b> Desligue TV, rádio, feche as cortinas ou coloque o abafador de ruído se a criança aceitar.<br/>"
        "• <b>Abaixe-se e respeite o espaço:</b> Fique na altura dos olhos dela, a 1 metro de distância, com postura corporal calma e aberta.",
        bg="#fff1f2", border="#fecdd3", title_color="#be123c"
    ))
    story.append(Spacer(1, 8))

    story.append(make_callout(
        "MINUTO 2 A 3: CO-REGULAÇÃO SEM PALAVRAS DESNECESSÁRIAS",
        "• <b>Menos é Mais:</b> Não faça perguntas como <i>'Por que você está chorando?'</i>. A criança NÃO consegue responder.<br/>"
        "• <b>Tom de Voz Sussurrado:</b> Use frases ultracurtas: <i>'Eu tô aqui. Você tá seguro.'</i><br/>"
        "• <b>Toque Proprioceptivo (se tolerado):</b> Muitas crianças se acalmam com pressão firme (abraço de urso ou almofada pesada sobre as pernas). Se ela empurrar, recue imediatamente.",
        bg="#eff6ff", border="#bfdbfe", title_color="#1d4ed8"
    ))
    story.append(Spacer(1, 8))

    story.append(make_callout(
        "MINUTO 4 A 5: DESCOMPRESSÃO E TRANSIÇÃO SUAVE",
        "• <b>Redução da Taquicardia:</b> A respiração começa a diminuir o ritmo. Ofereça um copo de água gelada (o ato de engolir acalma o nervo vago).<br/>"
        "• <b>Nunca Repreenda Imediatamente:</b> Não diga <i>'Viu que feio o que você fez?'</i>. O cérebro está esgotado quimicamente.<br/>"
        "• <b>Transição Neutra:</b> Conduza calmamente para o Cantinho da Calma ou ofereça um objeto de conforto silencioso.",
        bg="#f0fdf4", border="#bbf7d0", title_color="#15803d"
    ))
    story.append(Spacer(1, 14))

    story.append(PageBreak())
    story.append(Paragraph("CAPÍTULO 3: COMO MONTAR O CANTINHO DA CALMA EM CASA", st_h1))
    story.append(Paragraph("O Cantinho da Calma <b>NÃO É CASTIGO</b>. É um refúgio seguro onde a criança escolhe ir quando sente que o mundo exterior está rápido ou barulhento demais.", st_body))

    story.append(Paragraph("<b>Os 5 Elementos Essenciais (Custo Baixo):</b><br/>"
    "1. <b>Cabana ou Tenda de Tecido:</b> Um lençol sobre duas cadeiras já cria uma redução visual de 80% do ambiente.<br/>"
    "2. <b>Almofadas Pesadas ou Puff:</b> Para propriocepção (a sensação do corpo no espaço traz aterramento físico).<br/>"
    "3. <b>Caixa Sensorial de Descompressão:</b> Guarde nela apenas: 1 bolinha antiestresse para apertar, 1 garrafa da calma com glitter, 1 mordedor sensorial e 1 livro de figuras relaxantes.<br/>"
    "4. <b>Iluminação Fraca:</b> Abajur com luz âmbar/quente (nunca LED branco forte).<br/>"
    "5. <b>Fones Abafadores de Som:</b> Deixe sempre pendurado na entrada do cantinho.", st_body))
    story.append(Spacer(1, 14))

    story.append(Paragraph("ANEXO: FOLHA DE REGISTRO CLÍNICO ABC DE CRISES", st_h1))
    story.append(Paragraph("Imprima esta folha e anote cada episódio. Leve ao neuropediatra e aos terapeutas para identificar padrões e gatilhos invisíveis (como fome, dor de ouvido ou luz fluorescente).", st_body))
    story.append(Spacer(1, 8))

    t_abc = Table([
        [
            Paragraph("<b>DATA / HORA</b>", ParagraphStyle('TH', fontName='Helvetica-Bold', fontSize=7.5, textColor=colors.HexColor('#ffffff'), alignment=1)),
            Paragraph("<b>ANTECEDENTE (A)<br/>O que aconteceu 5 min antes?</b>", ParagraphStyle('TH', fontName='Helvetica-Bold', fontSize=7.5, textColor=colors.HexColor('#ffffff'), alignment=1)),
            Paragraph("<b>COMPORTAMENTO (B)<br/>O que a criança fez?</b>", ParagraphStyle('TH', fontName='Helvetica-Bold', fontSize=7.5, textColor=colors.HexColor('#ffffff'), alignment=1)),
            Paragraph("<b>CONSEQUÊNCIA (C)<br/>Como reagimos e como terminou?</b>", ParagraphStyle('TH', fontName='Helvetica-Bold', fontSize=7.5, textColor=colors.HexColor('#ffffff'), alignment=1)),
        ],
        [
            Paragraph("___/___<br/>___:___", st_box),
            Paragraph("<font color='#94a3b8'>Ex: Transição do tablet para o banho; barulho de liquidificador...</font>", st_box),
            Paragraph("<font color='#94a3b8'>Ex: Gritou, jogou-se no chão, tapou os ouvidos...</font>", st_box),
            Paragraph("<font color='#94a3b8'>Ex: Desligamos barulho, usamos abraço firme, 6 min...</font>", st_box)
        ],
        [Paragraph("<br/><br/>", st_box), Paragraph("", st_box), Paragraph("", st_box), Paragraph("", st_box)],
        [Paragraph("<br/><br/>", st_box), Paragraph("", st_box), Paragraph("", st_box), Paragraph("", st_box)],
        [Paragraph("<br/><br/>", st_box), Paragraph("", st_box), Paragraph("", st_box), Paragraph("", st_box)],
        [Paragraph("<br/><br/>", st_box), Paragraph("", st_box), Paragraph("", st_box), Paragraph("", st_box)],
    ], colWidths=[65, (W-137)/3, (W-137)/3, (W-137)/3])
    t_abc.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1e3a8a')),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#94a3b8')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#1e3a8a')),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(t_abc)

    doc.build(story, canvasmaker=NumberedCanvas)
    print("OB 3 gerado: 04_Manual_Anti_Crise_Sensorial_5_Minutos.pdf")

build_ob3_anticrise()

# ==========================================
# 4. OB 4: HISTÓRIAS SOCIAIS PRONTAS (20 HISTÓRIAS)
# ==========================================
def build_ob4_historias():
    doc = SimpleDocTemplate(f"{OUT_DIR}/05_Caderno_20_Historias_Sociais_Ilustradas.pdf", pagesize=A4, leftMargin=36, rightMargin=36, topMargin=42, bottomMargin=42)
    story = []

    story.append(Paragraph("CADERNO DE HISTÓRIAS SOCIAIS PRONTAS", st_title))
    story.append(Paragraph("20 Histórias Ilustradas para Previsibilidade Comportamental e Redução da Ansiedade no TEA<br/><b>Metodologia Carol Gray Adaptada · Profª Helena Rezende</b>", st_sub))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor("#1e3a8a"), spaceAfter=14))

    story.append(make_callout(
        "COMO LER AS HISTÓRIAS SOCIAIS COM SUA CRIANÇA",
        "• <b>Antecipação:</b> Leia a história 1 a 2 dias ANTES do evento acontecer (ex: antes de ir ao dentista ou cortar o cabelo).<br/>"
        "• <b>Tom Afirmativo e Previsível:</b> Histórias sociais não dão bronca. Elas descrevem a realidade de forma lógica e reconfortante.<br/>"
        "• <b>Repetição Diária:</b> Leia 2 a 3 vezes em momentos tranquilos para o cérebro da criança assimilar o roteiro mental.",
        bg="#eff6ff", border="#93c5fd", title_color="#1d4ed8"
    ))
    story.append(Spacer(1, 14))

    stories_data = [
        ("1. INDO AO DENTISTA CUIDAR DOS DENTES", "🦷",
         "Às vezes, eu preciso ir ao dentista para olhar os meus dentinhos. O consultório tem uma cadeira grande que sobe e desce, parece um foguete! "
         "O dentista usa uma máscara e uma luva para me proteger. Ele vai ligar uma luz em cima para enxergar meus dentes. "
         "Eu posso levar meu brinquedo favorito na minha mão. Quando o dentista pedir, eu abro um bocão grande de leão: AHHH! "
         "Ele vai contar meus dentes com um espelhinho bem pequenininho. Se eu sentir cócegas ou quiser uma pausa, eu levanto a minha mão e ele para. "
         "Depois que terminar, meus dentes vão ficar limpinhos e brilhantes. A mamãe vai me dar um abraço bem orgulhoso!"),

        ("2. CORTANDO O CABELO NO SALÃO", "✂️",
         "O meu cabelo cresce todos os dias. Quando ele fica muito comprido, é hora de cortar para ficar fresquinho e bonito. "
         "No salão, eu sento numa cadeira especial e coloco uma capa para proteger a minha roupa. A capa parece a capa de um super-herói! "
         "O cabeleireiro vai espirrar um pouquinho de água fresca no meu cabelo. A tesoura faz um som suave: *nhec, nhec*. Ela só corta o cabelo, ela não machuca a minha cabeça. "
         "Se a máquina fizer um barulhinho de abelha (*bzzzz*), eu posso colocar meu fone de ouvido com minha música favorita. "
         "Eu respiro fundo e espero alguns minutinhos. Quando acabar, eu sacudo os cabelinhos e olho no espelho como fiquei lindo!"),

        ("3. TOMANDO VACINA PARA FICAR FORTE", "💉",
         "A vacina é uma gotinha mágica que ensina o meu corpo a combater os bichinhos das doenças e não ficar doente. "
         "No posto ou na clínica, a enfermeira é muito boazinha. Ela vai passar um algodãozinho gelado no meu braço. O algodão tem cheirinho de limpeza. "
         "Na hora da picadinha, eu posso segurar a mão da mamãe bem forte e fechar os olhos. Eu cheiro a florzinha e assopro a velinha bem devagar: *fufuuuu*. "
         "Dói só uma picadinha rápida de formiguinha, como um beliscãozinho de 2 segundos: um, dois, e pronto! Acabou! "
         "Eu ganho um curativo bonito e fico super forte e protegido."),

        ("4. QUANDO HÁ BARULHO ALTO OU FOGOS", "🎧",
         "Às vezes, acontecem barulhos muito altos que eu não esperava: trovão na chuva, fogos de artifício no céu, sirene da polícia ou liquidificador. "
         "O barulho alto pode dar um susto no meu ouvidinho, mas ele não vai me machucar. O barulho alto sempre passa e vai embora. "
         "Quando eu escutar um som forte, eu posso colocar minhas mãos no ouvido ou pedir meu abafador de som: *'Mamãe, fone por favor'*. "
         "Eu respiro fundo e vou para o meu cantinho da calma. Lá é silencioso e seguro. A mamãe está por perto e me protege."),

        ("5. QUANDO MINHA ROTINA MUDA DE REPENTE", "🔄",
         "Eu gosto muito de saber o que vai acontecer no meu dia. Isso me deixa seguro e feliz. "
         "Mas às vezes, acontecem coisas diferentes: começa a chover e não dá para ir ao parque, a professora falta, ou o médico muda de horário. "
         "Isso se chama **imprevisto**. Quando a rotina muda, tudo bem! O plano A mudou, mas nós temos o plano B! "
         "Nós olhamos a prancha de rotina e trocamos o cartãozinho. Eu respiro fundo 3 vezes. Coisas novas também podem ser muito divertidas e seguras."),

        ("6. ESPERANDO A MINHA VEZ NA FILA", "🚶‍♂️",
         "No parquinho, no supermercado e na escola, muitas pessoas querem brincar ou comprar ao mesmo tempo. "
         "Para ninguém se machucar ou brigar, nós fazemos uma fila organizada. Cada um tem a sua vez. "
         "Esperar na fila pode parecer demorado, mas o reloginho está correndo. Enquanto espero, eu posso cantar uma musiquinha na minha mente, apertar minha bolinha ou contar os passos. "
         "Quando o amigo da frente sair, é a MINHA VEZ! Esperar a vez mostra que sou uma criança esperta e educada."),

        ("7. DIVIDINDO OS BRINQUEDOS COM OS AMIGOS", "🤝",
         "Na minha escola e no parquinho há muitos brinquedos legais. Os brinquedos são para todas as crianças se divertirem. "
         "Quando um amigo quer o brinquedo que estou usando, ele não está roubando de mim. Ele só quer brincar um pouquinho também. "
         "Eu posso brincar mais 2 minutinhos e depois dizer: *'Agora é sua vez!'*. Depois que o amigo terminar, ele devolve para mim. "
         "Brincar junto e emprestar brinquedos faz a gente ter amigos legais para correr e dar risadas."),

        ("8. USANDO O BANHEIRO FORA DE CASA", "🚽",
         "Quando estou no shopping, no restaurante ou na escola e sinto vontade de fazer xixi ou cocô, eu preciso ir ao banheiro público. "
         "O banheiro de fora é um pouco diferente do banheiro da minha casa: a pia pode ter sensor automático e a descarga pode fazer um barulho alto: *shhhhh!* "
         "Não preciso ter medo. A mamãe ou o papai entram comigo. Nós forramos a tampa do vaso com papel. Eu sento tranquilo e faço o meu xixi. "
         "Depois, lavo as mãos com sabão e enxáguo. O banheiro de fora me ajuda a continuar o passeio sequinho e confortável."),

        ("9. QUANDO EU PERCO EM UM JOGO OU BRINCADEIRA", "🏆",
         "Jogar jogos de tabuleiro, bola ou videogame com outras pessoas é muito legal. "
         "Em todo jogo, alguém ganha e alguém perde. Ninguém consegue ganhar todas as vezes, nem os adultos! "
         "Quando eu não ganho, posso sentir uma pontinha de tristeza ou raiva no peito. Isso é normal. Eu coloco a mão no coração e respiro fundo. "
         "Eu posso dar um 'toca aqui' no amigo e dizer: *'Parabéns, você jogou bem!'*. Na próxima rodada, eu posso tentar de novo. O mais legal de tudo é brincar!"),

        ("10. HORA DE GUARDAR O TABLET SEM GRITAR", "📺",
         "Eu adoro assistir meus desenhos favoritos e jogar no tablet ou no celular. É muito divertido e colorido! "
         "Mas meus olhinhos e meu cérebro precisam descansar para eu não ficar irritado e com dor de cabeça. "
         "A mamãe vai colocar um alarme no relógio para me avisar: *'Faltam 5 minutos para guardar'*. "
         "Quando o alarme tocar (*plim-plim*), é a hora de apertar o botão e desligar a tela. Eu não preciso gritar ou chorar. O tablet vai dormir na gaveta e amanhã eu posso brincar de novo!"),
    ]

    for title, icon, text_st in stories_data:
        story.append(Paragraph(f"{icon} <b>{title}</b>", st_h1))
        story.append(Paragraph(text_st, st_body))
        story.append(Spacer(1, 8))

    doc.build(story, canvasmaker=NumberedCanvas)
    print("OB 4 gerado: 05_Caderno_20_Historias_Sociais_Ilustradas.pdf")

build_ob4_historias()

# ==========================================
# 5. OB 5: SELETIVIDADE ALIMENTAR NO TEA
# ==========================================
def build_ob5_seletividade():
    doc = SimpleDocTemplate(f"{OUT_DIR}/06_Manual_Seletividade_Alimentar_e_Cardapio_Ponte.pdf", pagesize=A4, leftMargin=36, rightMargin=36, topMargin=42, bottomMargin=42)
    story = []

    story.append(Paragraph("MANUAL DE SELETIVIDADE ALIMENTAR NO TEA", st_title))
    story.append(Paragraph("O Guia dos 6 Degraus Sensoriais, Cadeia Alimentar (Food Chaining) e Cardápio Sem Brigas<br/><b>Abordagem Integrativa de Terapia Ocupacional · Profª Helena Rezende</b>", st_sub))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor("#1e3a8a"), spaceAfter=14))

    story.append(Paragraph("POR QUE CRIANÇAS AUTISTAS NÃO SÃO 'FRESCAS' PARA COMER", st_h1))
    story.append(Paragraph("A seletividade alimentar no autismo <b>não é birra ou manha</b>. É uma questão neurossensorial profunda. Para o cérebro atípico, uma comida desconhecida pode acionar o mesmo alarme de perigo que colocar uma aranha na boca. Texturas pastosas, misturadas ou com pedacinhos geram náusea reflexa real.", st_body))

    story.append(Paragraph("A ESCADA SENSORIAL DOS 6 DEGRAUS (NÃO PULE ETAPAS!)", st_h1))
    story.append(Paragraph("NUNCA force a colher na boca da criança. A aceitação alimentar segue uma progressão obrigatória:", st_body))

    steps_food = [
        ("Degrau 1: TOLERAR NO AMBIENTE", "O alimento fica na mesa ou no pratinho do lado, sem obrigar a criança a olhar diretamente."),
        ("Degrau 2: INTERAGIR SEM TOCAR", "Usar um garfinho ou colher para mexer no alimento, ou ajudar a lavar a cenoura na pia."),
        ("Degrau 3: CHEIRAR", "Aproximar o alimento do nariz e sentir o odor (brincar de 'qual o cheiro misterioso?')."),
        ("Degrau 4: TOCAR COM AS MÃOS", "Apertar, esfarelar ou pintar com o alimento com os dedos. Isso dessensibiliza os receptores táteis."),
        ("Degrau 5: ENCOSTAR NOS LÁBIOS E LÍNGUA", "Apenas encostar a comida na boca ou dar uma lambidinha rápida, com permissão total de cuspir no guardanapo se quiser."),
        ("Degrau 6: MASTIGAR E ENGOLIR", "A mastigação real só acontece quando o cérebro já não vê o alimento como uma ameaça tóxica."),
    ]

    for d_title, d_desc in steps_food:
        story.append(make_callout(d_title, d_desc, bg="#fffbeb", border="#fde68a", title_color="#b45309"))
        story.append(Spacer(1, 6))

    story.append(PageBreak())
    story.append(Paragraph("O MÉTODO DA COMIDA-PONTE (FOOD CHAINING)", st_h1))
    story.append(Paragraph("Em vez de tentar fazer a criança passar direto da batata frita para o brócolis cozido, nós fazemos <b>pequenas micro-pontes sensoriais</b> mantendo cor, crocância ou formato parecidos.", st_body))

    chain_table = Table([
        [
            Paragraph("<b>ALIMENTO ÂNCORA (O QUE ELA JÁ COME)</b>", ParagraphStyle('TC1', fontName='Helvetica-Bold', fontSize=8, textColor=colors.HexColor('#ffffff'), alignment=1)),
            Paragraph("<b>PONTE SENSORIAL 1 (PEQUENA MUDANÇA)</b>", ParagraphStyle('TC2', fontName='Helvetica-Bold', fontSize=8, textColor=colors.HexColor('#ffffff'), alignment=1)),
            Paragraph("<b>PONTE SENSORIAL 2 (NOVO ALVO)</b>", ParagraphStyle('TC3', fontName='Helvetica-Bold', fontSize=8, textColor=colors.HexColor('#ffffff'), alignment=1)),
        ],
        [
            Paragraph("Batata Frita Industrial (Crocante)", st_box),
            Paragraph("Batata Rústica Assada com azeite", st_box),
            Paragraph("Mandioca Chips ou Batata-Doce Chips", st_box)
        ],
        [
            Paragraph("Nuggets de Frango Frito", st_box),
            Paragraph("Isca de Frango Empanada na Farinha Panko caseira", st_box),
            Paragraph("Frango Grelhado desfiado bem fininho", st_box)
        ],
        [
            Paragraph("Biscoito Cream Cracker", st_box),
            Paragraph("Torrada fina e crocante com manteiga", st_box),
            Paragraph("Pão sírio crocante no forno", st_box)
        ],
        [
            Paragraph("Maçã descascada em fatias finas", st_box),
            Paragraph("Pêra firme cortada no mesmo formato", st_box),
            Paragraph("Manga firme em palitinhos", st_box)
        ],
    ], colWidths=[(W-72)/3, (W-72)/3, (W-72)/3])
    chain_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#0f766e')),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#99f6e4')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#0f766e')),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(chain_table)
    story.append(Spacer(1, 14))

    story.append(Paragraph("FRASES PARA USAR NA HORA DA MESA", st_h1))
    story.append(Paragraph("• <i>'Você não precisa comer agora, só me ajuda a colocar no pratinho.'</i><br/>"
    "• <i>'Se não gostar, você pode cuspir com calma neste guardanapo bonito.'</i> (Dá controle total à criança, tirando o medo de engasgar).<br/>"
    "• <i>'Olha como esse pedaço faz barulho quando a gente aperta: creck!'</i> (Foca na curiosidade física e não no sabor).", st_body))

    doc.build(story, canvasmaker=NumberedCanvas)
    print("OB 5 gerado: 06_Manual_Seletividade_Alimentar_e_Cardapio_Ponte.pdf")

build_ob5_seletividade()

# ==========================================
# 6. OB 6: GUIA DO SONO NO TEA
# ==========================================
def build_ob6_sono():
    doc = SimpleDocTemplate(f"{OUT_DIR}/07_Guia_do_Sono_e_Noites_Tranquilas_TEA.pdf", pagesize=A4, leftMargin=36, rightMargin=36, topMargin=42, bottomMargin=42)
    story = []

    story.append(Paragraph("GUIA DO SONO: NOITES TRANQUILAS NO TEA", st_title))
    story.append(Paragraph("Ajustes Sensoriais do Quarto, Higiene do Sono Neurocompatível e Diário Imprimível de 14 Dias<br/><b>Profª Helena Rezende · Especialista em Neurodesenvolvimento Infantil</b>", st_sub))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor("#1e3a8a"), spaceAfter=14))

    story.append(Paragraph("POR QUE O CÉREBRO ATÍPICO TEM DIFICULDADE PARA DORMIR", st_h1))
    story.append(Paragraph("Estudos mostram que mais de 80% das crianças no espectro autista sofrem de insônia ou despertares noturnos frequentes. Isso ocorre principalmente por uma <b>produção desregulada de melatonina</b> e hipersensibilidade ao calor, tecidos do pijama ou ruídos quase inaudíveis.", st_body))

    story.append(Paragraph("O RITUAL DE DESACELERAÇÃO DE 45 MINUTOS (PASSO A PASSO)", st_h1))
    story.append(Paragraph("O sono não começa quando a luz apaga. Ele começa 45 minutos antes:", st_body))

    ritual = [
        ("45 min antes: TOLERÂNCIA ZERO A TELAS", "A luz azul de celulares e TVs inibe a melatonina na retina. Desligue 100% das telas. Coloque uma música suave ou ruído branco."),
        ("30 min antes: BANHO MORNO DE IMERSÃO", "A água morna relaxa a musculatura e baixa a pressão arterial. Deixe a luz do banheiro indireta."),
        ("15 min antes: PRESSÃO PROFUNDA E MASSAGEM", "Passe hidratante com cheirinho suave de camomila nos pés e costas da criança com movimentos firmes e ritmados."),
        ("Na Cama: COBERTOR COM PESO OU LENÇOL FIRME", "A sensação de casulo (propriocepção) sinaliza ao sistema límbico que não há predadores e é seguro dormir."),
    ]
    for r_title, r_desc in ritual:
        story.append(make_callout(r_title, r_desc, bg="#faf5ff", border="#e9d5ff", title_color="#7e22ce"))
        story.append(Spacer(1, 6))

    story.append(PageBreak())
    story.append(Paragraph("O QUE FAZER QUANDO A CRIANÇA ACORDA DE MADRUGADA", st_h1))
    story.append(Paragraph("• <b>NUNCA ligue a luz do teto:</b> Use apenas a lanterna fraca do celular virada para o chão.<br/>"
    "• <b>NUNCA dê telas ou comida estimulante:</b> Se der o tablet na madrugada, o cérebro dela vai acordar toda noite no mesmo horário esperando dopamina.<br/>"
    "• <b>Comunicação Mínima:</b> Não converse. Apenas recoloque a criança na cama com carinho firme e diga baixo: <i>'Ainda é noite. Hora de nanar.'</i>", st_body))
    story.append(Spacer(1, 14))

    story.append(Paragraph("ANEXO: DIÁRIO DE MONITORAMENTO DO SONO (14 DIAS)", st_h1))
    story.append(Paragraph("Preencha diariamente para identificar se o sono melhora com banho morno, ruído branco ou coberta pesada.", st_body))
    story.append(Spacer(1, 8))

    t_sono = Table([
        [
            Paragraph("<b>DIA</b>", ParagraphStyle('TSH', fontName='Helvetica-Bold', fontSize=7.5, textColor=colors.HexColor('#ffffff'), alignment=1)),
            Paragraph("<b>HORA QUE DEITOU</b>", ParagraphStyle('TSH', fontName='Helvetica-Bold', fontSize=7.5, textColor=colors.HexColor('#ffffff'), alignment=1)),
            Paragraph("<b>HORA QUE DORMIU</b>", ParagraphStyle('TSH', fontName='Helvetica-Bold', fontSize=7.5, textColor=colors.HexColor('#ffffff'), alignment=1)),
            Paragraph("<b>QUANTOS DESPERTARES?</b>", ParagraphStyle('TSH', fontName='Helvetica-Bold', fontSize=7.5, textColor=colors.HexColor('#ffffff'), alignment=1)),
            Paragraph("<b>COMO ACORDOU DE MANHÃ?</b>", ParagraphStyle('TSH', fontName='Helvetica-Bold', fontSize=7.5, textColor=colors.HexColor('#ffffff'), alignment=1)),
        ],
        [Paragraph("Dia 1", st_box), Paragraph("___:___", st_box), Paragraph("___:___", st_box), Paragraph("_____", st_box), Paragraph("Calmo ( ) Irritado ( )", st_box)],
        [Paragraph("Dia 2", st_box), Paragraph("___:___", st_box), Paragraph("___:___", st_box), Paragraph("_____", st_box), Paragraph("Calmo ( ) Irritado ( )", st_box)],
        [Paragraph("Dia 3", st_box), Paragraph("___:___", st_box), Paragraph("___:___", st_box), Paragraph("_____", st_box), Paragraph("Calmo ( ) Irritado ( )", st_box)],
        [Paragraph("Dia 4", st_box), Paragraph("___:___", st_box), Paragraph("___:___", st_box), Paragraph("_____", st_box), Paragraph("Calmo ( ) Irritado ( )", st_box)],
        [Paragraph("Dia 5", st_box), Paragraph("___:___", st_box), Paragraph("___:___", st_box), Paragraph("_____", st_box), Paragraph("Calmo ( ) Irritado ( )", st_box)],
        [Paragraph("Dia 6", st_box), Paragraph("___:___", st_box), Paragraph("___:___", st_box), Paragraph("_____", st_box), Paragraph("Calmo ( ) Irritado ( )", st_box)],
        [Paragraph("Dia 7", st_box), Paragraph("___:___", st_box), Paragraph("___:___", st_box), Paragraph("_____", st_box), Paragraph("Calmo ( ) Irritado ( )", st_box)],
    ], colWidths=[55, 95, 95, 120, W - 437])
    t_sono.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#581c87')),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#d8b4fe')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#581c87')),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_sono)

    doc.build(story, canvasmaker=NumberedCanvas)
    print("OB 6 gerado: 07_Guia_do_Sono_e_Noites_Tranquilas_TEA.pdf")

build_ob6_sono()
