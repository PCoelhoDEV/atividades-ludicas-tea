#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gerador de Cartão de Acesso Digital para Wiapy
Gera o PDF de entrega com link 100% clicável para abrir o Web App.
Usa renderização moderna HTML/CSS com Chromium Headless para fidelidade visual e links clicáveis nativos.
"""

import sys
import os
import subprocess
import tempfile

def gerar_cartao_acesso(pdf_path, app_url="https://areaproftea.netlify.app/"):
    html_content = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<title>Cartão de Acesso - Portal Estimula TEA</title>
<style>
  @page {{
    size: A4 portrait;
    margin: 0;
  }}
  * {{
    box-sizing: border-box;
    margin: 0;
    padding: 0;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
  }}
  body {{
    width: 210mm;
    height: 297mm;
    background: #0f172a;
    color: #ffffff;
    padding: 14mm 16mm;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    overflow: hidden;
    position: relative;
  }}
  
  /* Decorative background glows */
  .bg-glow-1 {{
    position: absolute;
    top: -80px;
    right: -80px;
    width: 340px;
    height: 340px;
    background: radial-gradient(circle, rgba(16, 185, 129, 0.22) 0%, rgba(16, 185, 129, 0) 70%);
    border-radius: 50%;
    z-index: 0;
  }}
  .bg-glow-2 {{
    position: absolute;
    bottom: -60px;
    left: -60px;
    width: 320px;
    height: 320px;
    background: radial-gradient(circle, rgba(79, 70, 229, 0.22) 0%, rgba(79, 70, 229, 0) 70%);
    border-radius: 50%;
    z-index: 0;
  }}

  .content-container {{
    position: relative;
    z-index: 1;
    display: flex;
    flex-direction: column;
    height: 100%;
    justify-content: space-between;
  }}

  /* Header */
  .header {{
    text-align: center;
  }}
  .badge-top {{
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: rgba(16, 185, 129, 0.15);
    border: 1px solid rgba(16, 185, 129, 0.4);
    color: #34d399;
    padding: 6px 16px;
    border-radius: 9999px;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 0.5px;
    text-transform: uppercase;
    margin-bottom: 10px;
  }}
  .main-title {{
    font-size: 28px;
    font-weight: 800;
    color: #ffffff;
    line-height: 1.2;
    margin-bottom: 6px;
    letter-spacing: -0.5px;
  }}
  .subtitle {{
    font-size: 13.5px;
    color: #94a3b8;
    line-height: 1.45;
    max-width: 520px;
    margin: 0 auto;
  }}

  /* Main Action Card */
  .action-card {{
    background: linear-gradient(145deg, #1e293b 0%, #0f172a 100%);
    border: 1.5px solid #334155;
    border-radius: 20px;
    padding: 24px 22px;
    box-shadow: 0 15px 35px -5px rgba(0, 0, 0, 0.6);
    text-align: center;
  }}
  .card-pill {{
    display: inline-block;
    background: #0284c7;
    color: #ffffff;
    font-size: 10.5px;
    font-weight: 700;
    padding: 4px 12px;
    border-radius: 6px;
    text-transform: uppercase;
    letter-spacing: 0.6px;
    margin-bottom: 12px;
  }}
  .card-headline {{
    font-size: 17px;
    font-weight: 700;
    color: #f8fafc;
    margin-bottom: 16px;
  }}
  
  /* Big Clickable CTA Button */
  .btn-access {{
    display: block;
    width: 100%;
    background: linear-gradient(135deg, #10b981 0%, #059669 100%);
    color: #ffffff !important;
    text-decoration: none;
    padding: 18px 22px;
    border-radius: 14px;
    box-shadow: 0 6px 20px rgba(16, 185, 129, 0.45);
    border: 2px solid #34d399;
    text-align: center;
  }}
  .btn-text-main {{
    display: block;
    font-size: 18px;
    font-weight: 800;
    letter-spacing: 0.4px;
    text-transform: uppercase;
    color: #ffffff;
    line-height: 1.2;
  }}
  .btn-text-sub {{
    display: block;
    font-size: 12px;
    font-weight: 500;
    color: #d1fae5;
    margin-top: 5px;
    opacity: 0.95;
  }}
  .direct-url-hint {{
    margin-top: 14px;
    font-size: 11.5px;
    color: #64748b;
  }}
  .direct-url-hint a {{
    color: #38bdf8;
    text-decoration: underline;
    font-weight: 600;
  }}

  /* Two Columns: Steps + Bonus */
  .two-cols {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 14px;
  }}
  .info-box {{
    background: #1e293b;
    border: 1px solid #334155;
    border-radius: 14px;
    padding: 14px 16px;
  }}
  .info-box-title {{
    font-size: 12.5px;
    font-weight: 700;
    color: #38bdf8;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    margin-bottom: 10px;
    display: flex;
    align-items: center;
    gap: 6px;
  }}
  .steps-list {{
    list-style: none;
    font-size: 11.5px;
    line-height: 1.5;
    color: #cbd5e1;
  }}
  .steps-list li {{
    margin-bottom: 8px;
    position: relative;
    padding-left: 20px;
  }}
  .steps-list li:last-child {{
    margin-bottom: 0;
  }}
  .steps-list li::before {{
    content: "✓";
    position: absolute;
    left: 0;
    color: #10b981;
    font-weight: bold;
    font-size: 13px;
  }}
  .steps-list strong {{
    color: #ffffff;
  }}

  /* PWA Pin tip */
  .tip-box {{
    background: rgba(245, 158, 11, 0.08);
    border: 1.5px solid rgba(245, 158, 11, 0.35);
    border-radius: 14px;
    padding: 12px 16px;
    display: flex;
    align-items: flex-start;
    gap: 12px;
  }}
  .tip-icon {{
    font-size: 22px;
    line-height: 1;
  }}
  .tip-text {{
    font-size: 11px;
    line-height: 1.45;
    color: #fde68a;
  }}
  .tip-text strong {{
    color: #ffffff;
  }}

  /* Footer */
  .footer {{
    text-align: center;
    border-top: 1px solid #334155;
    padding-top: 12px;
    font-size: 10.5px;
    color: #64748b;
    line-height: 1.5;
  }}
  .footer strong {{
    color: #94a3b8;
  }}
</style>
</head>
<body>
  <div class="bg-glow-1"></div>
  <div class="bg-glow-2"></div>

  <div class="content-container">
    <!-- Header -->
    <div class="header">
      <div class="badge-top">✓ Pedido Confirmado · Acesso Vitalício</div>
      <h1 class="main-title">Portal Estimula TEA</h1>
      <p class="subtitle">Seu acesso exclusivo à plataforma interativa com +350 dinâmicas e todos os bônus já está 100% liberado!</p>
    </div>

    <!-- Main Access Card -->
    <div class="action-card">
      <span class="card-pill">Área de Membros Oficial</span>
      <h2 class="card-headline">Toque no botão abaixo para abrir o seu Web App agora:</h2>
      
      <a href="{app_url}" class="btn-access">
        <span class="btn-text-main">👉 TOQUE AQUI PARA ABRIR SEU APLICATIVO</span>
        <span class="btn-text-sub">Clique para acessar instantaneamente no seu navegador</span>
      </a>

      <p class="direct-url-hint">
        Link direto: <a href="{app_url}">{app_url}</a>
      </p>
    </div>

    <!-- 2 Columns: Steps & Included Features -->
    <div class="two-cols">
      <div class="info-box">
        <div class="info-box-title">⚡ Passo a Passo de Acesso</div>
        <ul class="steps-list">
          <li><strong>1. Toque no botão verde</strong> acima para abrir o portal no navegador do celular ou PC.</li>
          <li><strong>2. Use seu e-mail de compra:</strong> Ele é sua chave exclusiva para liberar o acesso.</li>
          <li><strong>3. Filtre por idade e nível:</strong> Selecione dinâmicas de 10 min para fazer hoje com itens de casa.</li>
        </ul>
      </div>

      <div class="info-box">
        <div class="info-box-title">🎁 O que está Liberado</div>
        <ul class="steps-list">
          <li><strong>+350 Dinâmicas Guiadas:</strong> Foco, fala, sensoriais, autonomia e motoras.</li>
          <li><strong>5 Bônus Exclusivos:</strong> Desfralde, Sono, Impressão, Direitos TEA e Comunidade.</li>
          <li><strong>Acesso Vitalício:</strong> Consulte quando quiser, sem renovações ou mensalidades.</li>
        </ul>
      </div>
    </div>

    <!-- Install as App Tip -->
    <div class="tip-box">
      <div class="tip-icon">💡</div>
      <div class="tip-text">
        <strong>Dica de Ouro: Como salvar na tela inicial como um Aplicativo (sem ocupar memória):</strong><br>
        • <strong>No iPhone (Safari):</strong> Abra o site, toque no botão de Compartilhar (quadrado com seta para cima) e selecione <em>"Adicionar à Tela de Início"</em>.<br>
        • <strong>No Android (Chrome):</strong> Abra o site, toque nos 3 pontinhos no canto superior direito e selecione <em>"Instalar aplicativo"</em> ou <em>"Adicionar à tela inicial"</em>.
      </div>
    </div>

    <!-- Footer Support -->
    <div class="footer">
      <p>Dúvidas ou suporte com seu acesso? Fale com nossa equipe: <strong>suporte@estimulatea.com.br</strong></p>
      <p style="margin-top: 4px; font-size: 9.5px; color: #475569;">Portal Estimula TEA © 2026 · Pagamento 100% Seguro Wiapy · Garantia Incondicional de 7 Dias</p>
    </div>
  </div>
</body>
</html>
"""

    with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False, encoding="utf-8") as f:
        f.write(html_content)
        temp_html = f.name

    try:
        cmd = [
            "google-chrome",
            "--headless=new",
            "--disable-gpu",
            "--no-sandbox",
            f"--print-to-pdf={pdf_path}",
            temp_html
        ]
        subprocess.run(cmd, check=True)
        print(f"✅ PDF gerado com sucesso em: {pdf_path}")
    finally:
        if os.path.exists(temp_html):
            os.remove(temp_html)

if __name__ == '__main__':
    url = sys.argv[1] if len(sys.argv) > 1 else "https://areaproftea.netlify.app/"
    out = sys.argv[2] if len(sys.argv) > 2 else "/home/pedrocoelho/Downloads/atividades-autismo/CARTAO_DE_ACESSO_PORTAL_ESTIMULA_TEA.pdf"
    gerar_cartao_acesso(out, url)
