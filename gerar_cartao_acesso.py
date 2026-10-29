#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gerador de Cartão de Acesso Digital para Wiapy
Gera o PDF de entrega com link clicável para abrir o Web App.
"""

import sys
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT

def gerar_cartao_acesso(pdf_path, app_url="https://1000dinamicastea.netlify.app/"):
    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=letter,
        rightMargin=36,
        leftMargin=36,
        topMargin=36,
        bottomMargin=36
    )

    styles = getSampleStyleSheet()

    # Brand Colors
    c_primary = colors.HexColor("#1E3A8A")     # Navy
    c_indigo = colors.HexColor("#4F46E5")      # Indigo
    c_emerald = colors.HexColor("#059669")     # Emerald
    c_emerald_dark = colors.HexColor("#047857")
    c_slate = colors.HexColor("#0F172A")
    c_muted = colors.HexColor("#64748B")
    c_bg_card = colors.HexColor("#F8FAFC")
    c_border = colors.HexColor("#E2E8F0")

    # Typography Styles
    style_badge = ParagraphStyle(
        'Badge',
        fontName='Helvetica-Bold',
        fontSize=11,
        textColor=c_emerald_dark,
        alignment=TA_CENTER,
        spaceAfter=6
    )

    style_title = ParagraphStyle(
        'Title',
        fontName='Helvetica-Bold',
        fontSize=24,
        leading=28,
        textColor=c_slate,
        alignment=TA_CENTER,
        spaceAfter=8
    )

    style_sub = ParagraphStyle(
        'Sub',
        fontName='Helvetica',
        fontSize=13,
        leading=18,
        textColor=c_muted,
        alignment=TA_CENTER,
        spaceAfter=20
    )

    style_button_text = ParagraphStyle(
        'BtnText',
        fontName='Helvetica-Bold',
        fontSize=15,
        leading=18,
        textColor=colors.white,
        alignment=TA_CENTER
    )

    style_url_sub = ParagraphStyle(
        'BtnSub',
        fontName='Helvetica',
        fontSize=10,
        leading=13,
        textColor=colors.HexColor("#D1FAE5"),
        alignment=TA_CENTER
    )

    style_h2 = ParagraphStyle(
        'H2',
        fontName='Helvetica-Bold',
        fontSize=14,
        leading=18,
        textColor=c_primary,
        alignment=TA_LEFT,
        spaceAfter=8
    )

    style_body = ParagraphStyle(
        'Body',
        fontName='Helvetica',
        fontSize=11,
        leading=16,
        textColor=colors.HexColor("#334155"),
        alignment=TA_LEFT
    )

    style_body_bold = ParagraphStyle(
        'BodyBold',
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=16,
        textColor=colors.HexColor("#1E293B"),
        alignment=TA_LEFT
    )

    style_tip = ParagraphStyle(
        'Tip',
        fontName='Helvetica',
        fontSize=10.5,
        leading=15,
        textColor=colors.HexColor("#854D0E"),
        alignment=TA_LEFT
    )

    story = []

    # 1. Header Badge
    story.append(Paragraph("🎉 PARABÉNS! SEU PEDIDO FOI CONFIRMADO", style_badge))
    story.append(Spacer(1, 4))

    # 2. Main Title
    story.append(Paragraph("Portal Estimula TEA", style_title))
    story.append(Paragraph("Seu acesso exclusivo ao Aplicativo Web com +350 Dinâmicas e todos os Bônus já está 100% liberado.", style_sub))
    story.append(Spacer(1, 8))

    # 3. Big Clickable Button (Table formatted with link)
    btn_link = f'<link href="{app_url}">👉 TOQUE AQUI PARA ABRIR O SEU APLICATIVO AGORA</link>'
    sub_link = f'<link href="{app_url}">{app_url}</link>'

    btn_content = [
        [Paragraph(btn_link, style_button_text)],
        [Paragraph(sub_link, style_url_sub)]
    ]

    btn_table = Table(btn_content, colWidths=[480])
    btn_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), c_emerald),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('TOPPADDING', (0, 0), (-1, 0), 16),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 4),
        ('TOPPADDING', (0, 1), (-1, 1), 0),
        ('BOTTOMPADDING', (0, 1), (-1, 1), 16),
        ('LEFTPADDING', (0, 0), (-1, -1), 20),
        ('RIGHTPADDING', (0, 0), (-1, -1), 20),
        ('CORNERPAD', (0, 0), (-1, -1), 12),
    ]))
    story.append(btn_table)
    story.append(Spacer(1, 24))

    # 4. Instructions Card
    card_rows = [
        [Paragraph("📱 Como Acessar a Plataforma Passo a Passo", style_h2)],
        [Paragraph("<b>1. Clique no botão verde acima:</b> O aplicativo abrirá imediatamente no navegador do seu celular ou computador.", style_body)],
        [Spacer(1, 4)],
        [Paragraph("<b>2. Digite o seu e-mail:</b> Utilize o mesmo e-mail que você cadastrou no momento da compra na Wiapy para validar seu acesso.", style_body)],
        [Spacer(1, 4)],
        [Paragraph("<b>3. Pronto!</b> Você terá acesso ilimitado a todas as categorias, dinâmicas guiadas, construtor de rotina visual e materiais para impressão.", style_body)]
    ]
    card_table = Table(card_rows, colWidths=[480])
    card_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), c_bg_card),
        ('BOX', (0, 0), (-1, -1), 1, c_border),
        ('PADDING', (0, 0), (-1, -1), 14),
        ('TOPPADDING', (0, 0), (-1, 0), 14),
    ]))
    story.append(card_table)
    story.append(Spacer(1, 18))

    # 5. Home Screen Tip Card (Add to home screen)
    pwa_rows = [
        [Paragraph("💡 Dica de Ouro: Instale como Aplicativo no Celular", ParagraphStyle('H2Gold', fontName='Helvetica-Bold', fontSize=13, textColor=colors.HexColor("#854D0E")))],
        [Paragraph("<b>No iPhone (Safari):</b> Com o site aberto, toque no botão de Compartilhar (o quadrado com uma setinha apontando para cima) e selecione a opção <b>'Adicionar à Tela de Início'</b>.", style_tip)],
        [Spacer(1, 3)],
        [Paragraph("<b>No Android (Chrome):</b> Com o site aberto, toque nos 3 pontinhos no canto superior direito e selecione a opção <b>'Adicionar à tela inicial'</b> ou <b>'Instalar aplicativo'</b>.", style_tip)],
        [Spacer(1, 3)],
        [Paragraph("Assim o aplicativo fica com ícone fixo na sua tela inicial, abrindo com 1 toque como qualquer outro app!", style_tip)]
    ]
    pwa_table = Table(pwa_rows, colWidths=[480])
    pwa_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor("#FEFCE8")),
        ('BOX', (0, 0), (-1, -1), 1, colors.HexColor("#FDE047")),
        ('PADDING', (0, 0), (-1, -1), 14),
    ]))
    story.append(pwa_table)
    story.append(Spacer(1, 24))

    # 6. Footer / Support
    story.append(HRFlowable(width="100%", thickness=1, color=c_border, spaceAfter=14))
    story.append(Paragraph(
        "Precisa de ajuda ou ficou com alguma dúvida? Envie uma mensagem para o nosso suporte oficial: <b>suporte@estimulatea.com.br</b><br/>"
        "<font size='9' color='#94A3B8'>Portal Estimula TEA © 2026 · Todos os direitos reservados. Material digital de apoio ao desenvolvimento neurofuncional.</font>",
        ParagraphStyle('Footer', fontName='Helvetica', fontSize=10, leading=14, textColor=c_muted, alignment=TA_CENTER)
    ))

    doc.build(story)
    print(f"✅ PDF gerado com sucesso em: {pdf_path}")

if __name__ == '__main__':
    url = sys.argv[1] if len(sys.argv) > 1 else "https://1000dinamicastea.netlify.app/"
    out = sys.argv[2] if len(sys.argv) > 2 else "/home/pedrocoelho/Downloads/atividades-autismo/CARTAO_DE_ACESSO_PORTAL_ESTIMULA_TEA.pdf"
    gerar_cartao_acesso(out, url)
