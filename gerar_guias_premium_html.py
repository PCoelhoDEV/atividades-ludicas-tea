#!/usr/bin/env python3
import os, subprocess, tempfile

OUT_DIR = "/home/pedrocoelho/Downloads/atividades-autismo/materiais_entrega"

def render_pdf(html_str, out_path):
    with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False, encoding="utf-8") as f:
        f.write(html_str)
        tmp = f.name
    try:
        cmd = [
            "google-chrome",
            "--headless=new",
            "--disable-gpu",
            "--no-sandbox",
            "--run-all-compositor-stages-before-draw",
            f"--print-to-pdf={out_path}",
            tmp
        ]
        subprocess.run(cmd, check=True)
        print(f"✅ Gerado com sucesso: {out_path} ({os.path.getsize(out_path)/1024:.1f} KB)")
    finally:
        if os.path.exists(tmp):
            os.remove(tmp)

CSS_BASE = """
  @page { size: A4 portrait; margin: 0; }
  * { box-sizing: border-box; margin: 0; padding: 0; font-family: 'Plus Jakarta Sans', -apple-system, sans-serif; }
  body { background: #f8fafc; color: #0f172a; -webkit-print-color-adjust: exact; print-color-adjust: exact; }
  .page { width: 210mm; height: 297mm; page-break-after: always; position: relative; background: #ffffff; overflow: hidden; padding: 14mm 16mm; display: flex; flex-direction: column; justify-content: space-between; }
  
  .top-bar { display: flex; justify-content: space-between; font-size: 8.5px; font-weight: 800; color: #64748b; border-bottom: 1.5px solid #e2e8f0; padding-bottom: 6px; letter-spacing: 0.5px; text-transform: uppercase; }
  .foot-bar { display: flex; justify-content: space-between; font-size: 8.5px; font-weight: 700; color: #94a3b8; border-top: 1.5px solid #e2e8f0; padding-top: 6px; }
  
  .badge-tag { display: inline-block; font-size: 9.5px; font-weight: 800; padding: 4px 12px; border-radius: 9999px; letter-spacing: 0.5px; text-transform: uppercase; margin-bottom: 8px; }
  h1.book-title { font-size: 28px; font-weight: 900; line-height: 1.15; letter-spacing: -0.5px; margin-bottom: 6px; }
  p.book-sub { font-size: 13px; font-weight: 600; color: #475569; line-height: 1.4; margin-bottom: 14px; }
  h2.sec-title { font-size: 16px; font-weight: 900; letter-spacing: -0.3px; margin: 10px 0 6px; }
  p.text { font-size: 11px; line-height: 1.55; color: #334155; margin-bottom: 8px; }
  
  .callout { border-radius: 14px; padding: 12px 14px; margin-bottom: 10px; }
  .callout-title { font-size: 12px; font-weight: 800; margin-bottom: 4px; display: flex; align-items: center; gap: 6px; }
  .callout-p { font-size: 10.5px; line-height: 1.5; color: #334155; }
"""

# ==========================================
# OB 4: MANUAL ANTI-CRISE (5 PRIMEIROS MINUTOS)
# ==========================================
def generate_ob4():
    html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<title>Manual Anti-Crise - Método Estimula TEA</title>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@500;600;700;800;900&display=swap" rel="stylesheet">
<style>
{CSS_BASE}
  .poster-box {{ background: linear-gradient(145deg, #1e293b 0%, #0f172a 100%); color: #ffffff; border-radius: 18px; padding: 16px; margin: 10px 0; border: 2px solid #334155; box-shadow: 0 10px 30px rgba(0,0,0,0.15); }}
  .poster-header {{ text-align: center; margin-bottom: 12px; }}
  .poster-header h3 {{ font-size: 18px; font-weight: 900; color: #f8fafc; letter-spacing: 0.5px; }}
  .poster-header p {{ font-size: 10.5px; color: #94a3b8; font-weight: 600; }}
  
  .time-block {{ border-radius: 12px; padding: 10px 12px; margin-bottom: 8px; display: flex; gap: 12px; align-items: flex-start; }}
  .tb-red {{ background: rgba(225, 29, 72, 0.15); border: 1.5px solid #f43f5e; }}
  .tb-blue {{ background: rgba(2, 132, 199, 0.15); border: 1.5px solid #38bdf8; }}
  .tb-green {{ background: rgba(16, 185, 129, 0.15); border: 1.5px solid #34d399; }}
  
  .time-badge {{ font-size: 11px; font-weight: 900; padding: 4px 10px; border-radius: 8px; white-space: nowrap; flex-shrink: 0; }}
  .tb-red .time-badge {{ background: #f43f5e; color: #fff; }}
  .tb-blue .time-badge {{ background: #38bdf8; color: #0f172a; }}
  .tb-green .time-badge {{ background: #34d399; color: #064e3b; }}
  
  .time-desc {{ font-size: 10px; line-height: 1.45; color: #e2e8f0; }}
  .time-desc strong {{ color: #ffffff; }}
  
  .say-grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin-top: 8px; }}
  .say-card {{ border-radius: 12px; padding: 10px 12px; }}
  .say-dont {{ background: #fef2f2; border: 1.5px solid #fca5a5; }}
  .say-do {{ background: #f0fdf4; border: 1.5px solid #86efac; }}
  .say-title {{ font-size: 11px; font-weight: 900; margin-bottom: 6px; display: flex; align-items: center; gap: 6px; }}
  .say-dont .say-title {{ color: #991b1b; }}
  .say-do .say-title {{ color: #166534; }}
  .say-list {{ list-style: none; font-size: 9.5px; line-height: 1.45; color: #334155; }}
  .say-list li {{ margin-bottom: 5px; }}
  
  .calm-items {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 8px; margin: 10px 0; }}
  .c-item {{ background: #f8fafc; border: 1.5px solid #cbd5e1; border-radius: 12px; padding: 8px; text-align: center; }}
  .c-item .c-icon {{ font-size: 24px; margin-bottom: 4px; }}
  .c-item .c-title {{ font-size: 10.5px; font-weight: 800; color: #1e3a8a; }}
  .c-item .c-desc {{ font-size: 8.5px; color: #64748b; line-height: 1.3; margin-top: 2px; }}
</style>
</head>
<body>
  <!-- PÁGINA 1: PÔSTER EMERGENCIAL DE GELADEIRA -->
  <div class="page">
    <div class="top-bar">
      <span>MÉTODO ESTIMULA TEA · INTERVENÇÃO EMERGENCIAL</span>
      <span>PÔSTER DE GELADEIRA (SOS CRISES)</span>
    </div>

    <div>
      <span class="badge-tag" style="background:#dc2626; color:#fff;">SOS EMERGENCIAL · COLE NA GELADEIRA</span>
      <h1 class="book-title" style="color:#991b1b;">MANUAL ANTI-CRISE:<br>OS 5 PRIMEIROS MINUTOS</h1>
      <p class="book-sub">O que fazer minuto a minuto no descontrole sensorial para proteger a criança e desativar o meltdown.</p>

      <div class="poster-box">
        <div class="poster-header">
          <h3>⚡ PROTOCOLO MINUTO A MINUTO (CRÉDITO CLÍNICO)</h3>
          <p>O cérebro pensante está desligado. Não adianta argumentar. Siga a ordem exata:</p>
        </div>

        <div class="time-block tb-red">
          <div class="time-badge">MINUTO 0 A 1</div>
          <div class="time-desc">
            <strong>SEGURANÇA E CORTE RADICAL DE ESTÍMULOS:</strong><br>
            • Afaste imediatamente quinas, vidros e objetos perigosos.<br>
            • Desligue TV, música e apague a luz do teto. Peça para outras pessoas se afastarem.<br>
            • Coloque o fone abafador de ruído se a criança aceitar.
          </div>
        </div>

        <div class="time-block tb-blue">
          <div class="time-badge">MINUTO 2 A 3</div>
          <div class="time-desc">
            <strong>CO-REGULAÇÃO SEM PALAVRAS DESNECESSÁRIAS:</strong><br>
            • Abaixe-se na altura dos olhos dela a 1 metro de distância. Não toque sem permissão.<br>
            • Use apenas frases sussurradas: <em>"Eu tô aqui. Você tá seguro."</em><br>
            • Se tolerar: abraço de urso firme ou almofada pesada sobre as pernas (propriocepção).
          </div>
        </div>

        <div class="time-block tb-green">
          <div class="time-badge">MINUTO 4 A 5</div>
          <div class="time-desc">
            <strong>DESCOMPRESSÃO E ATIVAÇÃO DO NERVO VAGO:</strong><br>
            • Ofereça um copo de água gelada (o ato de engolir sincroniza os batimentos cardíacos).<br>
            • Conduza para o Cantinho da Calma. Nunca dê bronca ou sermão após o término da crise.
          </div>
        </div>
      </div>

      <div class="say-grid">
        <div class="say-card say-dont">
          <div class="say-title">❌ O QUE NUNCA DIZER / FAZER</div>
          <ul class="say-list">
            <li>• <strong>"Para de graça!"</strong> (O choro é neuroquímico e involuntário).</li>
            <li>• <strong>"Olha pra mim agora!"</strong> (O contato visual dói fisicamente).</li>
            <li>• <strong>Gritar mais alto</strong> (Soma mais decibéis ao cérebro em colapso).</li>
            <li>• <strong>Segurar à força</strong> se ela estiver tentando se soltar.</li>
          </ul>
        </div>

        <div class="say-card say-do">
          <div class="say-title">✅ FRASES QUE ACALMAM O CÉREBRO</div>
          <ul class="say-list">
            <li>• <strong>"Eu tô aqui cuidando de você."</strong> (Segurança límbica).</li>
            <li>• <strong>"Pode respirar, já tá passando."</strong> (Previsibilidade de fim).</li>
            <li>• <strong>"Você tá seguro comigo."</strong> (Tom de voz baixo e firme).</li>
            <li>• <strong>Silêncio acolhedor:</strong> Apenas presença física tranquila.</li>
          </ul>
        </div>
      </div>
    </div>

    <div class="foot-bar">
      <span>Profª Helena Rezende · Neurodesenvolvimento Infantil</span>
      <span>Página 1 de 2</span>
    </div>
  </div>

  <!-- PÁGINA 2: CANTINHO DA CALMA & FOLHA DE REGISTRO ABC -->
  <div class="page">
    <div class="top-bar">
      <span>MÉTODO ESTIMULA TEA · REGISTRO & PREVENÇÃO</span>
      <span>CANTINHO DA CALMA & RASTREIO CLÍNICO</span>
    </div>

    <div>
      <h2 class="sec-title" style="color:#1e3a8a;">🏕️ COMO MONTAR O CANTINHO DA CALMA (CUSTO ZERO)</h2>
      <p class="text">O Cantinho da Calma é um refúgio sensorial seguro, <strong>nunca castigo</strong>. Monte com 6 itens que você já tem em casa:</p>

      <div class="calm-items">
        <div class="c-item">
          <div class="c-icon">⛺</div>
          <div class="c-title">Cabana de Lençol</div>
          <div class="c-desc">Um lençol sobre 2 cadeiras reduz 80% do excesso visual do ambiente.</div>
        </div>
        <div class="c-item">
          <div class="c-icon">🛋️</div>
          <div class="c-title">Almofadas Pesadas</div>
          <div class="c-desc">Pressão nas costas e pernas para aterramento proprioceptivo.</div>
        </div>
        <div class="c-item">
          <div class="c-icon">✨</div>
          <div class="c-title">Garrafa da Calma</div>
          <div class="c-desc">Garrafinha com água, óleo e purpurina para rastreio visual lento.</div>
        </div>
        <div class="c-item">
          <div class="c-icon">🎧</div>
          <div class="c-title">Fones Abafadores</div>
          <div class="c-desc">Deixe pendurado na entrada do refúgio para corte acústico rápido.</div>
        </div>
        <div class="c-item">
          <div class="c-icon">🦷</div>
          <div class="c-title">Mordedor Macio</div>
          <div class="c-desc">A mordida descarrega a tensão muscular na mandíbula sem machucar.</div>
        </div>
        <div class="c-item">
          <div class="c-icon">💡</div>
          <div class="c-title">Luz Âmbar Baixa</div>
          <div class="c-desc">Luz indireta amarelada para baixar o cortisol e induzir relaxamento.</div>
        </div>
      </div>

      <h2 class="sec-title" style="color:#1e3a8a; margin-top:14px;">📋 FOLHA CLÍNICA DE REGISTRO ABC DE CRISES</h2>
      <p class="text">Anote cada crise para identificar padrões invisíveis (fome, cansaço, som agudo). Leve este quadro ao neuropediatra e terapeuta:</p>

      <table style="width:100%; border-collapse:collapse; font-size:9.5px; border-radius:10px; overflow:hidden; border:1px solid #cbd5e1; margin-top:6px;">
        <tr style="background:#1e3a8a; color:#fff; font-weight:800; text-align:center;">
          <th style="padding:6px; border:1px solid #cbd5e1; width:70px;">DATA/HORA</th>
          <th style="padding:6px; border:1px solid #cbd5e1;">ANTECEDENTE (A)<br><span style="font-weight:400; font-size:8px;">O que aconteceu 5 min antes?</span></th>
          <th style="padding:6px; border:1px solid #cbd5e1;">COMPORTAMENTO (B)<br><span style="font-weight:400; font-size:8px;">O que a criança fez?</span></th>
          <th style="padding:6px; border:1px solid #cbd5e1;">CONSEQUÊNCIA (C)<br><span style="font-weight:400; font-size:8px;">Como encerrou a crise?</span></th>
        </tr>
        <tr style="background:#f8fafc; color:#64748b; font-style:italic;">
          <td style="padding:6px; border:1px solid #cbd5e1;">Exemplo:<br>18:30</td>
          <td style="padding:6px; border:1px solid #cbd5e1;">Desligamos a TV e chamamos para o banho sem avisar.</td>
          <td style="padding:6px; border:1px solid #cbd5e1;">Gritou, deitou no chão e tapou os ouvidos.</td>
          <td style="padding:6px; border:1px solid #cbd5e1;">Luz apagada, abraço firme, água gelada (6 min).</td>
        </tr>
        <tr style="height:32px;"><td style="border:1px solid #cbd5e1;"></td><td style="border:1px solid #cbd5e1;"></td><td style="border:1px solid #cbd5e1;"></td><td style="border:1px solid #cbd5e1;"></td></tr>
        <tr style="height:32px;"><td style="border:1px solid #cbd5e1;"></td><td style="border:1px solid #cbd5e1;"></td><td style="border:1px solid #cbd5e1;"></td><td style="border:1px solid #cbd5e1;"></td></tr>
        <tr style="height:32px;"><td style="border:1px solid #cbd5e1;"></td><td style="border:1px solid #cbd5e1;"></td><td style="border:1px solid #cbd5e1;"></td><td style="border:1px solid #cbd5e1;"></td></tr>
      </table>
    </div>

    <div class="foot-bar">
      <span>Profª Helena Rezende · Neurodesenvolvimento Infantil</span>
      <span>Página 2 de 2</span>
    </div>
  </div>
</body>
</html>
"""
    render_pdf(html, f"{OUT_DIR}/04_Manual_Anti_Crise_Sensorial_5_Minutos.pdf")

# ==========================================
# OB 5: SELETIVIDADE ALIMENTAR
# ==========================================
def generate_ob5():
    html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<title>Seletividade Alimentar sem Brigas - Estimula TEA</title>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@500;600;700;800;900&display=swap" rel="stylesheet">
<style>
{CSS_BASE}
  .stair-container {{ display: flex; flex-direction: column; gap: 6px; margin: 10px 0; }}
  .stair-step {{ border-radius: 12px; padding: 8px 12px; display: flex; align-items: center; gap: 12px; border: 1.5px solid transparent; }}
  .step-badge {{ font-size: 11px; font-weight: 900; color: #fff; width: 28px; height: 28px; border-radius: 50%; display: flex; align-items: center; justify-content: center; flex-shrink: 0; }}
  .step-info {{ flex: 1; }}
  .step-title {{ font-size: 11.5px; font-weight: 800; }}
  .step-desc {{ font-size: 9.5px; color: #475569; line-height: 1.35; }}

  .chain-grid {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px; margin: 10px 0; }}
  .chain-card {{ background: #ffffff; border: 1.5px solid #cbd5e1; border-radius: 14px; padding: 10px; }}
  .chain-title {{ font-size: 11px; font-weight: 800; color: #0d9488; margin-bottom: 6px; text-transform: uppercase; }}
  .chain-item {{ font-size: 9.5px; line-height: 1.45; color: #334155; margin-bottom: 4px; padding-left: 12px; position: relative; }}
  .chain-item::before {{ content: "➔"; position: absolute; left: 0; color: #0d9488; font-weight: bold; font-size: 9px; }}
</style>
</head>
<body>
  <!-- PÁGINA 1: A ESCADA DOS 6 DEGRAUS SENSORIAIS -->
  <div class="page">
    <div class="top-bar">
      <span>MÉTODO ESTIMULA TEA · NUTRIÇÃO & TERAPIA OCUPACIONAL</span>
      <span>A ESCADA SENSORIAL DOS 6 DEGRAUS</span>
    </div>

    <div>
      <span class="badge-tag" style="background:#0d9488; color:#fff;">TERAPIA OCUPACIONAL INTEGRATIVA</span>
      <h1 class="book-title" style="color:#115e59;">SELETIVIDADE ALIMENTAR<br>SEM BRIGAS NO TEA</h1>
      <p class="book-sub">Como expandir o cardápio da criança respeitando os limites neurossensoriais de textura e cheiro.</p>

      <div class="callout" style="background:#f0fdfa; border:1.5px solid #99f6e4;">
        <div class="callout-title" style="color:#0f766e;">💡 A VERDADE QUE NINGUÉM CONTA SOBRE A SELETIVIDADE</div>
        <p class="callout-p">Crianças autistas NÃO são "frescas" para comer. Para um cérebro atípico, uma textura nova e gosmenta (como purê ou fruta mole) pode ativar no cérebro a mesma área de náusea reflexa de engolir um inseto tóxico. Forçar a colher gera trauma alimentar imediato.</p>
      </div>

      <h2 class="sec-title" style="color:#0f766e;">🪜 A ESCADA SENSORIAL DE APROXIMAÇÃO (NÃO PULE DEGRAUS!)</h2>
      <div class="stair-container">
        <div class="stair-step" style="background:#f0fdf4; border-color:#86efac;">
          <div class="step-badge" style="background:#16a34a;">1</div>
          <div class="step-info">
            <div class="step-title" style="color:#166534;">TOLERAR NO AMBIENTE</div>
            <div class="step-desc">O novo alimento fica na mesa ou no prato do adulto. A criança não precisa tocar ou olhar diretamente.</div>
          </div>
        </div>

        <div class="stair-step" style="background:#ecfdf5; border-color:#6ee7b7;">
          <div class="step-badge" style="background:#059669;">2</div>
          <div class="step-info">
            <div class="step-title" style="color:#065f46;">INTERAGIR SEM TOCAR COM O CORPO</div>
            <div class="step-desc">Usar um garfinho ou colher para empurrar, ou ajudar a lavar a fruta na pia segurando na casca.</div>
          </div>
        </div>

        <div class="stair-step" style="background:#fffbeb; border-color:#fde68a;">
          <div class="step-badge" style="background:#d97706;">3</div>
          <div class="step-info">
            <div class="step-title" style="color:#92400e;">CHEIRAR (BRINCADEIRA DO CHEIRINHO)</div>
            <div class="step-desc">Aproximar do nariz de olhos fechados e adivinhar o aroma. Apenas brincadeira, sem pressão de comer.</div>
          </div>
        </div>

        <div class="stair-step" style="background:#fff7ed; border-color:#fed7aa;">
          <div class="step-badge" style="background:#ea580c;">4</div>
          <div class="step-info">
            <div class="step-title" style="color:#9a3412;">TOCAR COM OS DEDOS</div>
            <div class="step-desc">Apertar, esfarelar ou fazer carimbo com a cenoura. Isso dessensibiliza os receptores táteis da mão.</div>
          </div>
        </div>

        <div class="stair-step" style="background:#eff6ff; border-color:#bfdbfe;">
          <div class="step-badge" style="background:#2563eb;">5</div>
          <div class="step-info">
            <div class="step-title" style="color:#1e40af;">ENCOSTAR NOS LÁBIOS E LÍNGUA</div>
            <div class="step-desc">Dar uma lambidinha rápida, com permissão total de cuspir com calma num guardanapo bonito se não gostar.</div>
          </div>
        </div>

        <div class="stair-step" style="background:#faf5ff; border-color:#e9d5ff;">
          <div class="step-badge" style="background:#7c3aed;">6</div>
          <div class="step-info">
            <div class="step-title" style="color:#6b21a8;">MASTIGAR E ENGOLIR</div>
            <div class="step-desc">Acontece naturalmente após o cérebro registrar que a comida não representa uma ameaça ao corpo.</div>
          </div>
        </div>
      </div>
    </div>

    <div class="foot-bar">
      <span>Profª Helena Rezende · Método Estimula TEA</span>
      <span>Página 1 de 2</span>
    </div>
  </div>

  <!-- PÁGINA 2: O MÉTODO FOOD CHAINING (COMIDA-PONTE) -->
  <div class="page">
    <div class="top-bar">
      <span>MÉTODO ESTIMULA TEA · ESTRATÉGIA DE EXPANSÃO</span>
      <span>O MÉTODO DA COMIDA-PONTE (FOOD CHAINING)</span>
    </div>

    <div>
      <h2 class="sec-title" style="color:#0f766e;">🌉 O MÉTODO DA COMIDA-PONTE (FOOD CHAINING)</h2>
      <p class="text">Nunca tente passar de batata frita para brócolis cozido em um salto. Nós mantemos a cor, o formato ou a crocância parecidos e mudamos apenas 1 característica por vez:</p>

      <div class="chain-grid">
        <div class="chain-card">
          <div class="chain-title">🍟 PONTE DA BATATA</div>
          <div class="chain-item"><strong>Base:</strong> Batata Frita Industrial (Crocante)</div>
          <div class="chain-item"><strong>Ponte 1:</strong> Batata Rústica Assada no Forno</div>
          <div class="chain-item"><strong>Ponte 2:</strong> Mandioca Chips / Batata Doce</div>
          <div class="chain-item"><strong>Alvo:</strong> Purê de Mandioquinha Macio</div>
        </div>

        <div class="chain-card">
          <div class="chain-title">🍗 PONTE DO FRANGO</div>
          <div class="chain-item"><strong>Base:</strong> Nuggets Frito Tradicional</div>
          <div class="chain-item"><strong>Ponte 1:</strong> Frango Empanado Caseiro (Panko)</div>
          <div class="chain-item"><strong>Ponte 2:</strong> Frango Grelhado desfiado crocante</div>
          <div class="chain-item"><strong>Alvo:</strong> Franguinho com milho cozido</div>
        </div>

        <div class="chain-card">
          <div class="chain-title">🍎 PONTE DA FRUTA</div>
          <div class="chain-item"><strong>Base:</strong> Biscoito Doce Crocante</div>
          <div class="chain-item"><strong>Ponte 1:</strong> Maçã desidratada crocante (Chips)</div>
          <div class="chain-item"><strong>Ponte 2:</strong> Maçã in natura fatiada bem fininha</div>
          <div class="chain-item"><strong>Alvo:</strong> Pêra firme fatiada no mesmo corte</div>
        </div>
      </div>

      <h2 class="sec-title" style="color:#0f766e; margin-top:14px;">💬 FRASES MÁGICAS PARA A HORA DA REFEIÇÃO</h2>
      <div style="background:#f8fafc; border:1.5px solid #cbd5e1; border-radius:14px; padding:12px 14px;">
        <p class="text" style="margin-bottom:6px;">• <strong>"Você não precisa comer agora, só me ajuda a colocar este pedacinho no prato."</strong> (Tira 100% da pressão do almoço).</p>
        <p class="text" style="margin-bottom:6px;">• <strong>"Olha como esse faz creck quando aperta!"</strong> (Desvia o foco do sabor e conecta com a curiosidade física tátil).</p>
        <p class="text">• <strong>"Se você não gostar, pode cuspir neste guardanapo bonito."</strong> (Dá controle à criança, eliminando o pavor de engasgo).</p>
      </div>
    </div>

    <div class="foot-bar">
      <span>Profª Helena Rezende · Método Estimula TEA</span>
      <span>Página 2 de 2</span>
    </div>
  </div>
</body>
</html>
"""
    render_pdf(html, f"{OUT_DIR}/06_Manual_Seletividade_Alimentar_e_Cardapio_Ponte.pdf")

# ==========================================
# OB 6: GUIA DO SONO NO TEA
# ==========================================
def generate_ob6():
    html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<title>Guia do Sono no TEA - Estimula TEA</title>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@500;600;700;800;900&display=swap" rel="stylesheet">
<style>
{CSS_BASE}
  .timeline-container {{ display: flex; flex-direction: column; gap: 8px; margin: 10px 0; }}
  .tl-card {{ background: #ffffff; border: 1.5px solid #d8b4fe; border-radius: 14px; padding: 10px 14px; display: flex; align-items: center; gap: 14px; }}
  .tl-time {{ background: #7c3aed; color: #fff; font-size: 11px; font-weight: 900; padding: 6px 12px; border-radius: 10px; white-space: nowrap; flex-shrink: 0; }}
  .tl-content {{ flex: 1; }}
  .tl-title {{ font-size: 12px; font-weight: 800; color: #581c87; margin-bottom: 2px; }}
  .tl-desc {{ font-size: 9.5px; color: #475569; line-height: 1.4; }}

  .sleep-check-grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin: 10px 0; }}
  .sc-box {{ background: #faf5ff; border: 1.5px solid #e9d5ff; border-radius: 12px; padding: 10px 12px; }}
  .sc-box h4 {{ font-size: 11px; font-weight: 800; color: #6b21a8; margin-bottom: 6px; display: flex; align-items: center; gap: 6px; }}
  .sc-box p {{ font-size: 9.5px; color: #334155; line-height: 1.45; }}
</style>
</head>
<body>
  <!-- PÁGINA 1: O RITUAL DE DESACELERAÇÃO DE 45 MINUTOS -->
  <div class="page">
    <div class="top-bar">
      <span>MÉTODO ESTIMULA TEA · HIGIENE DO SONO NEUROCOMPATÍVEL</span>
      <span>O RITUAL DE 45 MINUTOS PARA DORMIR</span>
    </div>

    <div>
      <span class="badge-tag" style="background:#7c3aed; color:#fff;">NOITES TRANQUILAS SEM DESPERTARES</span>
      <h1 class="book-title" style="color:#581c87;">GUIA DO SONO NO TEA:<br>NOITES TRANQUILAS</h1>
      <p class="book-sub">A ciência neurológica da melatonina e o protocolo passo a passo para adormecer sem choro e dormir a noite toda.</p>

      <div class="callout" style="background:#faf5ff; border:1.5px solid #e9d5ff;">
        <div class="callout-title" style="color:#6b21a8;">🌙 POR QUE O CÉREBRO ATÍPICO TEM DIFICULDADE PARA DORMIR?</div>
        <p class="callout-p">Mais de 80% das crianças com TEA têm uma síntese biológica reduzida de melatonina. Além disso, o cérebro atípico capta o menor estalo da madeira, a etiqueta do pijama ou uma luz LED fraca como se fosse um alarme de incêndio ligado.</p>
      </div>

      <h2 class="sec-title" style="color:#6b21a8;">⏰ O RITUAL DE DESACELERAÇÃO (PASSO A PASSO)</h2>
      <div class="timeline-container">
        <div class="tl-card">
          <div class="tl-time">19:15 · 45 MIN ANTES</div>
          <div class="tl-content">
            <div class="tl-title">TOLERÂNCIA ZERO A TELAS</div>
            <div class="tl-desc">Desligue 100% de celulares, tablets e TVs. A luz azul bloqueia a produção de melatonina na retina. Coloque ruído branco ou música instrumental suave.</div>
          </div>
        </div>

        <div class="tl-card">
          <div class="tl-time">19:30 · 30 MIN ANTES</div>
          <div class="tl-content">
            <div class="tl-title">BANHO MORNO DE IMERSÃO</div>
            <div class="tl-desc">Água morna com luz indireta no banheiro. Ao sair do banho, a temperatura do corpo cai suavemente, enviando ao hipotálamo o sinal biológico de adormecer.</div>
          </div>
        </div>

        <div class="tl-card">
          <div class="tl-time">19:45 · 15 MIN ANTES</div>
          <div class="tl-content">
            <div class="tl-title">MASSAGEM E PRESSÃO PROFUNDA</div>
            <div class="tl-desc">Passe hidratante com óleo essencial de lavanda ou camomila nas pernas e costas da criança com pressão firme e ritmada. Acalma o sistema límbico.</div>
          </div>
        </div>

        <div class="tl-card">
          <div class="tl-time">20:00 · HORA DE DEITAR</div>
          <div class="tl-content">
            <div class="tl-title">COBERTOR PESADO OU CASULO</div>
            <div class="tl-desc">Prenda bem o lençol sob o colchão para criar a sensação de abraço contínuo (propriocepção). Leia 1 história curta em voz sussurrada e apague a luz.</div>
          </div>
        </div>
      </div>
    </div>

    <div class="foot-bar">
      <span>Profª Helena Rezende · Neurodesenvolvimento Infantil</span>
      <span>Página 1 de 2</span>
    </div>
  </div>

  <!-- PÁGINA 2: O QUE FAZER NA MADRUGADA & DIÁRIO DE 14 DIAS -->
  <div class="page">
    <div class="top-bar">
      <span>MÉTODO ESTIMULA TEA · PROTOCOLO DA MADRUGADA</span>
      <span>DESPERTARES NOTURNOS & MONITORAMENTO</span>
    </div>

    <div>
      <h2 class="sec-title" style="color:#6b21a8;">🚨 O QUE FAZER SE A CRIANÇA ACORDAR DE MADRUGADA</h2>
      <div class="sleep-check-grid">
        <div class="sc-box">
          <h4>❌ O QUE EVITAR A TODO CUSTO</h4>
          <p>• <strong>Nunca acenda a luz do teto:</strong> Use a lanterna fraca do celular apontada para o chão.<br>
          • <strong>Nunca dê o tablet ou celular:</strong> Se der tela às 3h da manhã, o cérebro dela vai acordar toda noite esperando dopamina.<br>
          • <strong>Não converse ou brinque:</strong> Estimula o córtex e espanta o sono.</p>
        </div>

        <div class="sc-box">
          <h4>✅ O PROTOCOLO DA CALMA</h4>
          <p>• <strong>Frase única sussurrada:</strong> <em>"Ainda é de noite. Hora de nanar."</em><br>
          • <strong>Pressão firme:</strong> Coloque a mão pesada e morna sobre o peito ou costas dela até a respiração desacelerar.<br>
          • <strong>Ruído contínuo:</strong> Mantenha o ventilador ou som de chuva ligado.</p>
        </div>
      </div>

      <h2 class="sec-title" style="color:#6b21a8; margin-top:14px;">📊 DIÁRIO DE MONITORAMENTO DO SONO (14 DIAS)</h2>
      <p class="text">Preencha diariamente para identificar padrões de melhora e levar ao neuropediatra:</p>

      <table style="width:100%; border-collapse:collapse; font-size:9.5px; border-radius:10px; overflow:hidden; border:1px solid #d8b4fe; margin-top:6px;">
        <tr style="background:#6b21a8; color:#fff; font-weight:800; text-align:center;">
          <th style="padding:6px; border:1px solid #d8b4fe; width:55px;">NOITE</th>
          <th style="padding:6px; border:1px solid #d8b4fe;">HORA QUE DEITOU</th>
          <th style="padding:6px; border:1px solid #d8b4fe;">HORA QUE DORMIU</th>
          <th style="padding:6px; border:1px solid #d8b4fe;">DESPERTARES?</th>
          <th style="padding:6px; border:1px solid #d8b4fe;">ACORDOU DE MANHÃ</th>
        </tr>
        <tr style="height:26px; text-align:center;"><td style="border:1px solid #d8b4fe; font-weight:bold;">Noite 1</td><td style="border:1px solid #d8b4fe;">___:___</td><td style="border:1px solid #d8b4fe;">___:___</td><td style="border:1px solid #d8b4fe;">[ ] Zero [ ] 1x [ ] 2x+</td><td style="border:1px solid #d8b4fe;">[ ] Calmo [ ] Cansado</td></tr>
        <tr style="height:26px; text-align:center;"><td style="border:1px solid #d8b4fe; font-weight:bold;">Noite 2</td><td style="border:1px solid #d8b4fe;">___:___</td><td style="border:1px solid #d8b4fe;">___:___</td><td style="border:1px solid #d8b4fe;">[ ] Zero [ ] 1x [ ] 2x+</td><td style="border:1px solid #d8b4fe;">[ ] Calmo [ ] Cansado</td></tr>
        <tr style="height:26px; text-align:center;"><td style="border:1px solid #d8b4fe; font-weight:bold;">Noite 3</td><td style="border:1px solid #d8b4fe;">___:___</td><td style="border:1px solid #d8b4fe;">___:___</td><td style="border:1px solid #d8b4fe;">[ ] Zero [ ] 1x [ ] 2x+</td><td style="border:1px solid #d8b4fe;">[ ] Calmo [ ] Cansado</td></tr>
        <tr style="height:26px; text-align:center;"><td style="border:1px solid #d8b4fe; font-weight:bold;">Noite 4</td><td style="border:1px solid #d8b4fe;">___:___</td><td style="border:1px solid #d8b4fe;">___:___</td><td style="border:1px solid #d8b4fe;">[ ] Zero [ ] 1x [ ] 2x+</td><td style="border:1px solid #d8b4fe;">[ ] Calmo [ ] Cansado</td></tr>
        <tr style="height:26px; text-align:center;"><td style="border:1px solid #d8b4fe; font-weight:bold;">Noite 5</td><td style="border:1px solid #d8b4fe;">___:___</td><td style="border:1px solid #d8b4fe;">___:___</td><td style="border:1px solid #d8b4fe;">[ ] Zero [ ] 1x [ ] 2x+</td><td style="border:1px solid #d8b4fe;">[ ] Calmo [ ] Cansado</td></tr>
      </table>
    </div>

    <div class="foot-bar">
      <span>Profª Helena Rezende · Neurodesenvolvimento Infantil</span>
      <span>Página 2 de 2</span>
    </div>
  </div>
</body>
</html>
"""
    render_pdf(html, f"{OUT_DIR}/07_Guia_do_Sono_e_Noites_Tranquilas_TEA.pdf")

generate_ob4()
generate_ob5()
generate_ob6()
