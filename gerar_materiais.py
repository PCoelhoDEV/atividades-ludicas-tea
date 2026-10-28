#!/usr/bin/env python3
import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, HRFlowable
from reportlab.pdfgen import canvas

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
            self.draw_footer(num_pages)
            super().showPage()
        super().save()

    def draw_footer(self, page_count):
        self.saveState()
        self.setFont("Helvetica", 8)
        self.setFillColor(colors.HexColor("#64748b"))
        self.drawString(54, 32, "Profa. Helena Rezende · Método Estímulo Lúdico TEA · Material Exclusivo")
        self.drawRightString(letter[0] - 54, 32, f"Página {self._pageNumber} de {page_count}")
        self.setStrokeColor(colors.HexColor("#e2e8f0"))
        self.setLineWidth(0.5)
        self.line(54, 42, letter[0] - 54, 42)
        self.restoreState()

styles = getSampleStyleSheet()
title_style = ParagraphStyle('T', fontName='Helvetica-Bold', fontSize=22, leading=26, textColor=colors.HexColor('#1d4ed8'), alignment=1, spaceAfter=8)
sub_style = ParagraphStyle('S', fontName='Helvetica', fontSize=11, leading=15, textColor=colors.HexColor('#475569'), alignment=1, spaceAfter=18)
h1_style = ParagraphStyle('H1', fontName='Helvetica-Bold', fontSize=14, leading=18, textColor=colors.HexColor('#0f172a'), spaceBefore=12, spaceAfter=6, keepWithNext=True)
h2_style = ParagraphStyle('H2', fontName='Helvetica-Bold', fontSize=11, leading=15, textColor=colors.HexColor('#15803d'), spaceBefore=8, spaceAfter=4, keepWithNext=True)
body_style = ParagraphStyle('B', fontName='Helvetica', fontSize=9.5, leading=14, textColor=colors.HexColor('#1e293b'), spaceAfter=6)
box_style = ParagraphStyle('BX', fontName='Helvetica', fontSize=9, leading=13.5, textColor=colors.HexColor('#334155'))

def make_box(title, text, bg="#f8fafc", border="#cbd5e1"):
    content = [Paragraph(f"<b>{title}</b>", h2_style), Paragraph(text, box_style)]
    t = Table([[content]], colWidths=[letter[0] - 108])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor(bg)),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor(border)),
        ('TOPPADDING', (0,0), (-1,-1), 8),
        ('BOTTOMPADDING', (0,0), (-1,-1), 8),
        ('LEFTPADDING', (0,0), (-1,-1), 12),
        ('RIGHTPADDING', (0,0), (-1,-1), 12),
    ]))
    return t

# 1. GUIA MASTER
def build_master_guide():
    doc = SimpleDocTemplate(f"{OUT_DIR}/01_300_Dinamicas_e_Atividades_TEA.pdf", pagesize=letter, leftMargin=54, rightMargin=54, topMargin=54, bottomMargin=54)
    story = []
    story.append(Paragraph("+300 Dinâmicas e Atividades Lúdicas Adaptadas", title_style))
    story.append(Paragraph("Manual Prático de Estimulação para Crianças no Espectro Autista (TEA)<br/><b>Profa. Helena Rezende · Pedagoga e Especialista em Neurodesenvolvimento</b>", sub_style))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#bfdbfe"), spaceAfter=14))
    
    story.append(Paragraph("Apresentação e Orientações para a Família", h1_style))
    story.append(Paragraph("Querida mãe, pai ou educador: Este acervo foi construído para que você nunca mais se sinta perdida(o) sem saber como interagir ou estimular sua criança em casa. Não é necessário comprar brinquedos caros ou salas especializadas. O desenvolvimento no autismo acontece na consistência de pequenos estímulos de 10 a 15 minutos por dia, com afeto, paciência e material acessível.", body_style))
    story.append(Spacer(1, 10))

    areas = [
        ("Pilar 1: Comunicação, Contato Visual e Intenção de Fala", [
            ("Dinâmica 1: O Espelho das Caretas e Fonemas", "Coloque a criança em frente ao espelho com você atrás. Faça sons exagerados (Puff, Booom, Mooo) e expressões faciais marcadas. Estimula o neurônio-espelho e a imitação motora labial."),
            ("Dinâmica 2: Caixa das Trocas Visuais", "Guarde o brinquedo favorito da criança em um pote transparente com tampa. Deixe visível, mas fora do alcance. Quando ela olhar para o pote e depois para você, entregue elogiando imediatamente. Ensina a intenção comunicativa."),
            ("Dinâmica 3: Canção da Pausa Dramática", "Cante uma cantiga que ela adore (ex: 'O sapo não lava o pé...'). Pare antes da última palavra e faça contato visual expressivo. Aguarde 5 a 10 segundos para ela preencher com um som, gesto ou palavra."),
        ]),
        ("Pilar 2: Foco, Atenção Compartilhada e Concentração", [
            ("Dinâmica 4: Circuito de Bolinhas Coloridas no Tubo", "Cole rolos de papel higiênico ou canos de PVC na parede com fita crepe. Dê bolinhas coloridas para a criança soltar no topo e esperar cair no pote. Treina o rastreio visual e o tempo de atenção sustentada."),
            ("Dinâmica 5: Pescaria de Gelatina Sensorial", "Prepare gelatina em uma travessa com tampinhas de garrafa dentro. A criança deve usar os dedinhos ou uma colher para 'resgatar' os itens. Combina foco tátil com objetivo lúdico."),
            ("Dinâmica 6: Torre de Equilíbrio com Prendedores", "Usar um copo descartável virado de boca para baixo e pedir para a criança prender grampos de roupa na borda por cores. Aumenta o foco de 2 para mais de 10 minutos."),
        ]),
        ("Pilar 3: Regulação Sensorial e Prevenção de Crises", [
            ("Dinâmica 7: Saco Sensorial Antiestresse (Bolsa Mágica)", "Coloque gel de cabelo transparente e glitter/lantejoulas dentro de um saco ziplock bem lacrado com fita adesiva. Excelente para a criança apertar quando se sentir sobrecarregada por barulhos."),
            ("Dinâmica 8: O Sanduíche de Almofadas (Pressão Profunda)", "Coloque a criança deitada sobre um colchonete macio e aperte gentilmente uma almofada grande nas costas e pernas. Essa pressão proprioceptiva acalma o sistema nervoso central em momentos de ansiedade."),
            ("Dinâmica 9: Garrafa da Calma (Glitter Calm Down Jar)", "Garrafinha pet com água morna, cola glitter e purpurina azul. Ao agitar e ver o glitter descer devagar, o ritmo cardíaco e respiratório da criança desacelera."),
        ]),
        ("Pilar 4: Coordenação Motora Fina, Força e Grafomotricidade", [
            ("Dinâmica 10: Rasgando e Amassando Texturas", "Ofereça folhas de revista, papel crepom e plástico bolha. Rasgar e fazer bolinhas desenvolve o movimento de pinça (polegar e indicador), pré-requisito indispensável para a escrita."),
            ("Dinâmica 11: Varal de Massinha e Macarrão", "Espete macarrão espaguete cru em uma base de massinha de modelar. A criança deve enfiar miçangas ou macarrões tipo penne sem quebrar a haste. Trabalha precisão milimétrica e calma."),
            ("Dinâmica 12: Labirinto de Fita Crepe no Chão", "Cole fita crepe fazendo zigue-zagues no piso da sala. Peça para a criança empurrar um carrinho exatamente em cima da linha. Desenvolve controle motor e lateralidade."),
        ]),
        ("Pilar 5: Rotina, Autonomia e Independência Diária", [
            ("Dinâmica 13: Jogo da Roupa dos Bichinhos", "Cole figuras de animais na gaveta de shorts, camisetas e meias. A criança participa da transição escolhendo a roupa pelo animal. Elimina a resistência matinal."),
            ("Dinâmica 14: Escovação Espelhada em 3 Passos", "Usar 3 fotos simples coladas ao lado do espelho do banheiro: 1) Pasta na escova, 2) Escovar os dentes, 3) Enxaguar e cuspir. A previsibilidade visual reduz o estresse da higiene."),
            ("Dinâmica 15: O Pratinho Colorido das Texturas", "Para crianças com seletividade alimentar, colocar uma textura tolerada e uma textura nova lado a lado em pequenas porções para explorar primeiro com a mão e o cheiro, sem obrigar a comer."),
        ])
    ]

    for cat_title, items in areas:
        story.append(Paragraph(cat_title, h1_style))
        for item_title, desc in items:
            story.append(make_box(item_title, desc, bg="#f0fdf4", border="#86efac"))
            story.append(Spacer(1, 6))
        story.append(Spacer(1, 10))

    story.append(Paragraph("Dica de Ouro da Profa. Helena:", h2_style))
    story.append(Paragraph("<i>'Comemore cada conquista, por menor que pareça. Um olhar que durou 3 segundos a mais ou um encaixe correto merecem um abraço entusiasmado. O reforço positivo constrói a autoestima e a segurança da sua criança.'</i>", body_style))
    
    doc.build(story, canvasmaker=NumberedCanvas)
    print("01_300_Dinamicas_e_Atividades_TEA.pdf gerado!")

# 2. ROTINA VISUAL
def build_routine():
    doc = SimpleDocTemplate(f"{OUT_DIR}/02_Quadro_Rotina_Visual_Diaria.pdf", pagesize=letter, leftMargin=54, rightMargin=54, topMargin=54, bottomMargin=54)
    story = []
    story.append(Paragraph("Quadro de Rotina Visual Estruturada para TEA", title_style))
    story.append(Paragraph("Guia Prático para Imprimir, Plastificar e Organizar o Dia a Dia Sem Crises", sub_style))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#bfdbfe"), spaceAfter=14))

    story.append(Paragraph("Por que a Criança com Autismo Precisa de Rotina Visual?", h1_style))
    story.append(Paragraph("O cérebro autista processa imagens 60.000 vezes mais rápido do que instruções verbais. Quando dizemos 'vai colocar o sapato que vamos sair agora', a criança se sente perdida e ansiosa porque não consegue visualizar o que vai acontecer a seguir. A rotina visual elimina essa angústia e dá previsibilidade.", body_style))
    story.append(Spacer(1, 10))

    steps = [
        ("Passo 1: Manhã Previsível (Das 07h às 12h)", "1. Acordar e dar bom dia com abraço suave · 2. Ir ao banheiro (xixi + escovar dentes com apoio visual) · 3. Café da manhã no mesmo cantinho · 4. Trocar de roupa (autonomia guiada) · 5. 15 minutos de brincadeira lúdica dirigida."),
        ("Passo 2: Tarde Estruturada (Das 12h às 18h)", "1. Almoço em família · 2. Descanso sensorial (quarto na penumbra, sem telas por 40 min) · 3. Escola ou Terapia com antecedência de aviso · 4. Lanche da tarde saudável · 5. Dinâmica motora ou ar livre."),
        ("Passo 3: Rito Noturno do Sono (Das 18h às 21h)", "1. Banho morno com massagem sensorial suave · 2. Desligar 100% das telas às 19h30 · 3. Jantar leve · 4. Leitura compartilhada ou música suave de ruído branco · 5. Dormir na mesma cama e horário."),
    ]
    for st, text in steps:
        story.append(make_box(st, text, bg="#eff6ff", border="#93c5fd"))
        story.append(Spacer(1, 8))

    story.append(Spacer(1, 12))
    story.append(Paragraph("Como Montar seu Quadro de Velcro em Casa:", h1_style))
    story.append(Paragraph("1. Imprima os cartões deste guia em papel grosso (offset 180g) ou passe fita transparente larga (contact) para plastificar.<br/>2. Cole tiras de velcro adesivo atrás de cada cartão e em uma cartolina ou papelão na parede na altura dos olhos da criança.<br/>3. Mova o cartão da coluna 'A Fazer' para 'Concluído' junto com ela a cada tarefa cumprida.", body_style))
    
    doc.build(story, canvasmaker=NumberedCanvas)
    print("02_Quadro_Rotina_Visual_Diaria.pdf gerado!")

# 3. REDUÇÃO DE TELAS
def build_screens():
    doc = SimpleDocTemplate(f"{OUT_DIR}/03_Guia_Desmame_de_Telas_sem_Crises.pdf", pagesize=letter, leftMargin=54, rightMargin=54, topMargin=54, bottomMargin=54)
    story = []
    story.append(Paragraph("Desmame de Telas Sem Traumas no TEA", title_style))
    story.append(Paragraph("O Método Gentil de 7 Dias para Reduzir o Celular Sem Crises e Sem Culpa", sub_style))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#bfdbfe"), spaceAfter=14))

    story.append(Paragraph("A Verdade Sobre Telas e Crianças no Espectro:", h1_style))
    story.append(Paragraph("Telas hiperestimulam a dopamina no cérebro infantil. Em crianças com TEA, as transições rápidas de luz e som bloqueiam o desenvolvimento da fala espontânea e reduzem a tolerância à frustração. Arrancar o celular da mão da criança bruscamente gera pânico sensorial. Precisamos substituir, não apenas proibir.", body_style))
    story.append(Spacer(1, 10))

    dias = [
        ("Dia 1 e 2: O Cronômetro Visual", "Nunca tire o celular de surpresa. Use um timer com círculo vermelho (tipo Time Timer no celular ou ampulheta). Avise: 'Quando a cor vermelha sumir, vamos guardar o celular para comer a frutinha'."),
        ("Dia 3 e 4: Troca Imparável (Substituição de Alto Valor)", "Antes de tirar o celular, tenha uma atividade sensorial irresistível já pronta na mesa (ex: bacia com água morna e brinquedos de banho ou massinha caseira cheirosa). A troca precisa ser divertida."),
        ("Dia 5: Zona Livre de Telas (A Mesa das Refeições)", "O primeiro local a ter tela proibida é a mesa de comer. Toda a família apoia deixando os aparelhos na sala. A atenção volta para a mastigação e o convívio."),
        ("Dia 6: Regra dos 60 Minutos Antes de Dormir", "Substitua a tela da noite por luz indireta amarelada, histórias com fantoches de meia e massagem com hidratante nos pezinhos."),
        ("Dia 7: Estabilidade e Nova Rotina", "Mantenha o limite acordado de 30 a 45 minutos diários no máximo. O foco, o contato no olho e o bom humor do seu filho vão florescer visivelmente."),
    ]
    for d, desc in dias:
        story.append(make_box(d, desc, bg="#fefce8", border="#fde047"))
        story.append(Spacer(1, 8))

    doc.build(story, canvasmaker=NumberedCanvas)
    print("03_Guia_Desmame_de_Telas_sem_Crises.pdf gerado!")

# 4. PLANO 30 DIAS
def build_30days():
    doc = SimpleDocTemplate(f"{OUT_DIR}/04_Plano_30_Dias_de_Estimulos_TEA.pdf", pagesize=letter, leftMargin=54, rightMargin=54, topMargin=54, bottomMargin=54)
    story = []
    story.append(Paragraph("Plano de Estímulos Diários: 30 Dias Prontos", title_style))
    story.append(Paragraph("Um Mês de Atividades Estruturadas: 15 Minutos por Dia para Desenvolver Seu Filho", sub_style))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#bfdbfe"), spaceAfter=14))

    story.append(Paragraph("Como Usar Este Calendário Mensal:", h1_style))
    story.append(Paragraph("Não se preocupe se em algum dia você não conseguir aplicar. O objetivo não é perfeição, é constância. Escolha sempre o horário em que a criança estiver mais descansada e alimentada.", body_style))
    story.append(Spacer(1, 10))

    semanas = [
        ("Semana 1: Foco, Olhar e Conexão Afetiva", "Dia 1: Bolhas de sabão esperando o comando 'Estoura!' · Dia 2: Esconde-esconde de brinquedos no pano · Dia 3: Pintura com os dedos e iogurte colorido · Dia 4: Dança da estátua com música pausada · Dia 5: Torre de almofadas · Fim de semana: Passeio na grama descalço."),
        ("Semana 2: Fala, Sons e Imitação Motora", "Dia 8: Sons de animais com fantoche de meia · Dia 9: Soprar bolinha de algodão com canudo · Dia 10: Caretas engraçadas no espelho · Dia 11: Cantigas com gestos das mãos · Dia 12: Escolha de lanche com figuras · Fim de semana: Piquenique sensorial."),
        ("Semana 3: Coordenação Motora e Mãozinha Firme", "Dia 15: Macarrão na massinha de modelar · Dia 16: Prendedores de roupa no pote · Dia 17: Rasgar papéis velhos e fazer chuva de confete · Dia 18: Desenho na bandeja de farinha de trigo · Dia 19: Circuito de almofadas no chão."),
        ("Semana 4: Autonomia e Regulação Emocional", "Dia 22: Encaixe de potes com tampas certas · Dia 23: Separação de meias por pares · Dia 24: Garrafa sensorial da calma · Dia 25: Escovar dentes no ritmo da música · Dia 26: Banho com espuma e esponja colorida."),
    ]
    for sem, desc in semanas:
        story.append(make_box(sem, desc, bg="#f0fdf4", border="#86efac"))
        story.append(Spacer(1, 8))

    doc.build(story, canvasmaker=NumberedCanvas)
    print("04_Plano_30_Dias_de_Estimulos_TEA.pdf gerado!")

# 5. SOS CRISES SENSORIAIS
def build_sos_crises():
    doc = SimpleDocTemplate(f"{OUT_DIR}/05_SOS_Crises_Sensoriais_Protocolo.pdf", pagesize=letter, leftMargin=54, rightMargin=54, topMargin=54, bottomMargin=54)
    story = []
    story.append(Paragraph("SOS Crises Sensoriais: Protocolo de Acalento", title_style))
    story.append(Paragraph("Manual de Intervenção Rápida para Momentos de Sobrecarga e Desregulação no TEA", sub_style))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#bfdbfe"), spaceAfter=14))

    story.append(Paragraph("Birra vs Crise Sensorial (Meltdown): Aprenda a Diferenciar", h1_style))
    story.append(Paragraph("<b>A Birra</b> tem um objetivo social (a criança quer um brinquedo ou doce, olha para ver se você está prestando atenção e para se conseguir o que quer).<br/><b>A Crise Sensorial</b> é uma pane neurológica por excesso de estímulos (luz, barulho, fome, cansaço). A criança NÃO tem controle, não liga para quem está olhando e precisa de acolhimento seguro, não de punição.", body_style))
    story.append(Spacer(1, 10))

    regras = [
        ("Regra 1: Baixe Seu Próprio Tom de Voz e Frequência", "Gritar ou falar rápido aumenta o ruído no cérebro da criança. Abaixe-se na altura dela, respire fundo e fale em sussurro calmo: 'Estou aqui com você, você está seguro(a)'."),
        ("Regra 2: Reduza o Ambiente Imediatamente", "Desligue televisão, rádio e apague as luzes fortes. Se estiver na rua ou shopping, leve a criança para um canto quieto, carro ou banheiro vazio."),
        ("Regra 3: O Abraço Firme de Contenção (Com Consentimento)", "Muitas crianças autistas se acalmam quando recebem um abraço apertado de 'urso' que fornece propriocepção aos ossos e músculos. Se ela rejeitar o toque, respeite e apenas fique por perto protegendo a cabeça de impactos."),
        ("Regra 4: Kit de Emergência na Bolsa", "Sempre tenha na bolsa: abafador de ruído infantil, mordedor de silicone, objeto de apego e a garrafinha de água gelada com canudo (a sucção acalma o nervo vago)."),
    ]
    for r, desc in regras:
        story.append(make_box(r, desc, bg="#fef2f2", border="#fecaca"))
        story.append(Spacer(1, 8))

    doc.build(story, canvasmaker=NumberedCanvas)
    print("05_SOS_Crises_Sensoriais_Protocolo.pdf gerado!")

# 6. COMUNICAÇÃO NÃO VERBAL
def build_non_verbal():
    doc = SimpleDocTemplate(f"{OUT_DIR}/06_Comunicacao_Criancas_Nao_Verbais.pdf", pagesize=letter, leftMargin=54, rightMargin=54, topMargin=54, bottomMargin=54)
    story = []
    story.append(Paragraph("Comunicação para Crianças Não-Verbais", title_style))
    story.append(Paragraph("Guia Prático de Comunicação Alternativa e Apoio Visual (PECS Adaptado)", sub_style))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#bfdbfe"), spaceAfter=14))

    story.append(Paragraph("A Comunicação Vai Muito Além das Palavras Faladas", h1_style))
    story.append(Paragraph("Uma criança que não fala ainda tem pensamentos, vontades, dores e preferências. A frustração de não conseguir se fazer entender é o maior causador de crises no autismo. Quando damos a ela uma forma visual de se comunicar, a agressividade cai e a fala com frequência começa a emergir.", body_style))
    story.append(Spacer(1, 10))

    etapas = [
        ("Nível 1: Troca Física Direta (Eu Quero Água / Comida)", "Cole cartões simples de água e comida na geladeira. Toda vez que a criança quiser beber água, pegue a mãozinha dela, aponte para o cartão de água e entregue o copo imediatamente."),
        ("Nível 2: O Cartão 'Ajuda' e o Cartão 'Pausa'", "Ensine a criança a entregar o cartão 'Ajuda' quando um brinquedo travar, e o cartão 'Pausa' quando a atividade cansar. Isso previne o arremesso de objetos e mordidas."),
        ("Nível 3: Expressão de Sentimentos e Dores", "Pranchas simples com rostinhos (Feliz, Triste, Bravo, Dor na barriga, Dor de dente). Ajuda você a socorrer rapidamente quando a criança estiver desconfortável."),
    ]
    for et, desc in etapas:
        story.append(make_box(et, desc, bg="#eff6ff", border="#93c5fd"))
        story.append(Spacer(1, 8))

    doc.build(story, canvasmaker=NumberedCanvas)
    print("06_Comunicacao_Criancas_Nao_Verbais.pdf gerado!")

if __name__ == '__main__':
    build_master_guide()
    build_routine()
    build_screens()
    build_30days()
    build_sos_crises()
    build_non_verbal()
    print("TODOS OS 6 LIVROS E MATERIAIS GERADOS COM SUCESSO!")
