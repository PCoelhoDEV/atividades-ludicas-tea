#!/usr/bin/env python3
import os
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, HRFlowable
from reportlab.pdfgen import canvas

W, H = A4
OUT_DIR = "/home/pedrocoelho/Downloads/atividades-autismo/materiais_entrega"

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
            self.drawRightString(W - 36, H - 28, "GUIA CLÍNICO E PRÁTICO · USO EXCLUSIVO")
            self.setStrokeColor(colors.HexColor("#cbd5e1"))
            self.setLineWidth(0.6)
            self.line(36, H - 32, W - 36, H - 32)

        self.setStrokeColor(colors.HexColor("#cbd5e1"))
        self.setLineWidth(0.6)
        self.line(36, 30, W - 36, 30)
        self.setFont("Helvetica", 8)
        self.setFillColor(colors.HexColor("#64748b"))
        self.drawString(36, 18, "© Portal Estimula TEA · Todos os direitos reservados.")
        self.setFont("Helvetica-Bold", 8)
        self.setFillColor(colors.HexColor("#1e3a8a"))
        self.drawRightString(W - 36, 18, f"Página {self._pageNumber} de {total_pages}")
        self.restoreState()

styles = getSampleStyleSheet()
st_title = ParagraphStyle('T', fontName='Helvetica-Bold', fontSize=22, leading=26, textColor=colors.HexColor('#1e3a8a'), alignment=1, spaceAfter=6)
st_sub = ParagraphStyle('S', fontName='Helvetica', fontSize=11, leading=15, textColor=colors.HexColor('#475569'), alignment=1, spaceAfter=14)
st_h1 = ParagraphStyle('H1', fontName='Helvetica-Bold', fontSize=13, leading=17, textColor=colors.HexColor('#1e3a8a'), spaceBefore=12, spaceAfter=6, keepWithNext=True)
st_body = ParagraphStyle('B', fontName='Helvetica', fontSize=9, leading=13.5, textColor=colors.HexColor('#1e293b'), spaceAfter=5)
st_box = ParagraphStyle('BX', fontName='Helvetica', fontSize=8.5, leading=12.5, textColor=colors.HexColor('#334155'))

def make_callout(title, text, bg="#f8fafc", border="#cbd5e1", title_color="#0f766e"):
    p_t = Paragraph(f"<b>{title}</b>", ParagraphStyle('CallT', fontName='Helvetica-Bold', fontSize=9.5, textColor=colors.HexColor(title_color), spaceAfter=3))
    p_b = Paragraph(text, st_box)
    t = Table([[ [p_t, p_b] ]], colWidths=[W - 72])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor(bg)),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor(border)),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
    ]))
    return t

# 1. DESMAME DE TELAS
def build_desmame():
    doc = SimpleDocTemplate(f"{OUT_DIR}/03_Guia_Desmame_de_Telas_sem_Crises.pdf", pagesize=A4, leftMargin=36, rightMargin=36, topMargin=42, bottomMargin=42)
    story = []
    story.append(Paragraph("GUIA DE DESMAME DE TELAS SEM CRISES", st_title))
    story.append(Paragraph("Protocolo Clínico de Redução Gradual de Celular e Tablet para Crianças no TEA<br/><b>Profª Helena Rezende · Neurodesenvolvimento Infantil</b>", st_sub))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor("#1e3a8a"), spaceAfter=14))

    story.append(Paragraph("O EFEITO DO HIPERESTÍMULO DAS TELAS NO CÉREBRO ATÍPICO", st_h1))
    story.append(Paragraph("Crianças autistas têm um sistema dopaminérgico altamente sensível. Desenhos hiperestimulantes (cortes rápidos a cada 2 segundos, cores hipersaturadas e sons agudos) colocam o cérebro em estado de <b>hipnose artificial</b>. Quando você puxa o tablet da mão dela de surpresa, o nível de dopamina cai a zero em milissegundos, disparando um colapso emocional violento.", st_body))

    phases = [
        ("FASE 1: TROCA DE CONTEÚDO (DIAS 1 A 5)",
         "Não tire o tempo de tela ainda! Mude apenas O QUE ela assiste. Troque desenhos frenéticos por animações lentas com fundo neutro, ritmo calmo e música instrumental. O cérebro começa a desacelerar sem crise."),
        ("FASE 2: PREVISIBILIDADE COM TIMER VISUAL (DIAS 6 A 10)",
         "Coloque um relógio visual (timer de ampulheta ou aplicativo com círculo que vai sumindo). Mostre que quando a cor vermelha sumir, a tela vai dormir. A criança entende o tempo visualmente, e não como uma imposição arbitrária do adulto."),
        ("FASE 3: A REGRA DA COMIDA-PONTE SENSORIAL (DIAS 11 A 20)",
         "NUNCA desligue a tela para o tédio. Sempre prepare uma atividade de alto engajamento sensorial ANTES de desligar (ex: bacia com água e sabão na pia, massinha fresca ou pista de carrinhos com fita adesiva no chão). Desligou a tela -> Conduziu para a água."),
        ("FASE 4: ZONAS SAGRADAS LIVRES DE TELA (DIAS 21 A 30)",
         "Estabeleça 3 locais da casa onde a tela NUNCA entra: mesa de refeição, quarto de dormir e banheiro. A criança reconecta com os sentidos reais e o sono melhora em até 70%."),
    ]
    for p_title, p_desc in phases:
        story.append(make_callout(p_title, p_desc, bg="#eff6ff", border="#bfdbfe", title_color="#1e40af"))
        story.append(Spacer(1, 6))

    story.append(Spacer(1, 10))
    story.append(Paragraph("CONTRATO VISUAL DE COMBINADOS DA TELA", st_h1))
    story.append(Paragraph("Imprima esta folha e marque com um carimbo ou adesivo toda vez que a criança guardar o tablet sem gritar.", st_body))
    story.append(Spacer(1, 8))

    t_contract = Table([
        [Paragraph("<b>REGRA DA CASA</b>", ParagraphStyle('TR1', fontName='Helvetica-Bold', fontSize=8, textColor=colors.HexColor('#ffffff'), alignment=1)),
         Paragraph("<b>TEMPO MÁXIMO</b>", ParagraphStyle('TR2', fontName='Helvetica-Bold', fontSize=8, textColor=colors.HexColor('#ffffff'), alignment=1)),
         Paragraph("<b>CUMPRIU HOJE?</b>", ParagraphStyle('TR3', fontName='Helvetica-Bold', fontSize=8, textColor=colors.HexColor('#ffffff'), alignment=1))],
        [Paragraph("Tablet após o almoço", st_box), Paragraph("20 minutos com timer", st_box), Paragraph("[  ] SIM  [  ] CONSEGUIU!", st_box)],
        [Paragraph("Tablet no final da tarde", st_box), Paragraph("20 minutos com timer", st_box), Paragraph("[  ] SIM  [  ] CONSEGUIU!", st_box)],
        [Paragraph("Sem telas na hora de comer", st_box), Paragraph("Zero tela", st_box), Paragraph("[  ] SIM  [  ] CONSEGUIU!", st_box)],
        [Paragraph("Sem telas 1 hora antes de dormir", st_box), Paragraph("Zero tela", st_box), Paragraph("[  ] SIM  [  ] CONSEGUIU!", st_box)],
    ], colWidths=[200, 160, W - 432])
    t_contract.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1e40af')),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#bfdbfe')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#1e40af')),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(t_contract)

    doc.build(story, canvasmaker=NumberedCanvas)
    print("Guia Desmame de Telas gerado!")

build_desmame()

# 2. PLANO DE 30 DIAS
def build_plano30():
    doc = SimpleDocTemplate(f"{OUT_DIR}/04_Plano_30_Dias_de_Estimulos_TEA.pdf", pagesize=A4, leftMargin=36, rightMargin=36, topMargin=42, bottomMargin=42)
    story = []
    story.append(Paragraph("PLANO DE 30 DIAS DE ESTIMULAÇÃO DIÁRIA", st_title))
    story.append(Paragraph("Cronograma Diário Passo a Passo para Desenvolvimento da Fala, Foco e Vínculo<br/><b>Profª Helena Rezende · Método Estimula TEA</b>", st_sub))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor("#1e3a8a"), spaceAfter=14))

    story.append(Paragraph("COMO EXECUTAR SEU CALENDÁRIO DE 30 DIAS", st_h1))
    story.append(Paragraph("Cada dia possui uma <b>Missão Principal de 10 minutos</b>. Não sobrecarregue a rotina. O progresso neurobiológico no autismo se dá pela constância diária e pelo afeto seguro.", st_body))
    story.append(Spacer(1, 10))

    # Tabela com os 30 dias organizados em 4 semanas
    semanas = [
        ("SEMANA 1: CONEXÃO, OLHAR E IMITAÇÃO MOTORA", [
            ("Dia 1", "O Espelho dos Fonemas", "Brincar de fazer bicos e caretas na frente do espelho (estimula neurônios-espelho)."),
            ("Dia 2", "Cadê o Brinquedo? Achou!", "Esconder um carrinho sob um pano na frente da criança e esperar ela puxar."),
            ("Dia 3", "Bolinhas de Sabão com Pausa", "Assoprar 1 bolha e esperar a criança fazer um som ou apontar antes da próxima."),
            ("Dia 4", "Passa-Passa com Meia", "Rolar uma bolinha de meia no chão um para o outro, treinando troca de turno."),
            ("Dia 5", "Massinha das Texturas", "Esconder moedas grandes ou tampinhas dentro da massinha para ela resgatar."),
            ("Dia 6", "Pintura com Dedinhos na Água", "Pintar os azulejos do box no banho com água colorida de anilina."),
            ("Dia 7", "Dia do Abraço Firme", "Pressão proprioceptiva suave com almofada na sala ouvindo música calma."),
        ]),
        ("SEMANA 2: LINGUAGEM, PEDIDOS E INTENÇÃO COMUNICATIVA", [
            ("Dia 8", "A Caixa do Desejo Físico", "Colocar o biscoito ou brinquedo em pote transparente fechado; estimular o apontar."),
            ("Dia 9", "O Som dos Bichinhos", "Imitar latido, miado e mugido com fantoches ou bichos de pelúcia."),
            ("Dia 10", "A Escada das Cores com Copos", "Empilhar copos descartáveis coloridos falando o nome da cor em voz alta."),
            ("Dia 11", "Música com Parada Súbita", "Cantar 'Palma, palma, pé, pé' e pausar antes da última palavra para ela completar."),
            ("Dia 12", "Cartão PECS na Geladeira", "Treinar entregar o cartão de ÁGUA antes de abrir a porta da geladeira."),
            ("Dia 13", "Pescaria com Colher de Pau", "Pescar tampinhas plásticas em uma bacia com água usando uma colher."),
            ("Dia 14", "Dia de Caminhada Sensorial", "Andar descalço na grama, no tapete e no piso frio sentindo as diferenças."),
        ]),
        ("SEMANA 3: COORDENAÇÃO, GRAFOMOTRICIDADE E FOCO", [
            ("Dia 15", "O Varal dos Prendedores", "Prender grampos de roupa na borda de uma caixa de papelão (pinça fina)."),
            ("Dia 16", "Rasgando Folhas Coloridas", "Rasgar revistas velhas em tiras e fazer chuvinha de papel picado."),
            ("Dia 17", "Labirinto de Fita Crepe", "Fazer uma linha reta no chão e empurrar o carrinho sem sair da faixa."),
            ("Dia 18", "Separando os Grãos", "Separar feijões pretos de grãos de milho em dois potes com os dedos."),
            ("Dia 19", "Macarrão no Espaguete", "Enfiar macarrão penne furadinho em hastes de espaguete cru fincadas na massinha."),
            ("Dia 20", "Desenho na Farinha", "Espalhar farinha em uma assadeira e desenhar círculos e cobrinhas com o dedo."),
            ("Dia 21", "Dia do Banho Espumoso", "Brincar de lavar as bonecas ou carrinhos com esponja e sabão."),
        ]),
        ("SEMANA 4: AUTONOMIA, ROTINA E DESCOMPRESSÃO", [
            ("Dia 22", "Vestindo o Sapatinho", "Ensinar a enfiar o pé no tênis com velcro e puxar a aba com autonomia."),
            ("Dia 23", "Organizando a Gaveta com Figuras", "Guardar as meias na gaveta marcada com o desenho da meia."),
            ("Dia 24", "Garrafa Sensorial da Calma", "Montar juntos uma garrafinha com água, óleo e glitter para observar."),
            ("Dia 25", "O Circuito de Almofadas no Chão", "Pular de uma almofada para outra sem pisar no chão ('o chão é lava!')."),
            ("Dia 26", "Degustação sem Pressão", "Cheirar e tocar uma fruta nova sem obrigação de colocar na boca."),
            ("Dia 27", "Prancha Primeiro e Depois", "Montar juntos a rotina da noite usando os cartões impressos."),
            ("Dia 28", "História Social Antes de Dormir", "Ler a história 'Hora de Dormir' com iluminação âmbar."),
            ("Dia 29", "Brincadeira da Sombra com Lanterna", "Apagar a luz e fazer coelhinho e pássaro com as mãos na parede."),
            ("Dia 30", "Festa da Vitória!", "Comemoração dos 30 dias com o doce favorito e medalha simbólica de orgulho!"),
        ]),
    ]

    for sem_title, dias in semanas:
        story.append(Paragraph(f"<b>{sem_title}</b>", st_h1))
        t_sem_rows = [[
            Paragraph("<b>DIA</b>", ParagraphStyle('TMD', fontName='Helvetica-Bold', fontSize=8, textColor=colors.HexColor('#ffffff'), alignment=1)),
            Paragraph("<b>ATIVIDADE</b>", ParagraphStyle('TMA', fontName='Helvetica-Bold', fontSize=8, textColor=colors.HexColor('#ffffff'), alignment=1)),
            Paragraph("<b>OBJETIVO E PASSO A PASSO</b>", ParagraphStyle('TMO', fontName='Helvetica-Bold', fontSize=8, textColor=colors.HexColor('#ffffff'), alignment=1)),
        ]]
        for d_id, d_name, d_obj in dias:
            t_sem_rows.append([
                Paragraph(f"<b>{d_id}</b>", st_box),
                Paragraph(f"<b>{d_name}</b>", st_box),
                Paragraph(d_obj, st_box)
            ])
        t_sem = Table(t_sem_rows, colWidths=[55, 140, W - 267])
        t_sem.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1e3a8a')),
            ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#cbd5e1')),
            ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#1e3a8a')),
            ('TOPPADDING', (0,0), (-1,-1), 4),
            ('BOTTOMPADDING', (0,0), (-1,-1), 4),
            ('LEFTPADDING', (0,0), (-1,-1), 6),
            ('RIGHTPADDING', (0,0), (-1,-1), 6),
        ]))
        story.append(t_sem)
        story.append(Spacer(1, 10))

    doc.build(story, canvasmaker=NumberedCanvas)
    print("Plano 30 Dias gerado!")

build_plano30()
