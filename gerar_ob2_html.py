#!/usr/bin/env python3
import os, subprocess, tempfile

OUT_DIR = "/home/pedrocoelho/Downloads/atividades-autismo/materiais_entrega"

pecs_data = [
    # Necessidades & Fisiologia (24)
    ("Água", "BÁSICO", "💧", "#0284c7", "#e0f2fe"),
    ("Fazer Xixi", "BÁSICO", "🚽", "#0284c7", "#e0f2fe"),
    ("Fazer Cocô", "BÁSICO", "🧻", "#0284c7", "#e0f2fe"),
    ("Comer / Fome", "BÁSICO", "🍽️", "#0284c7", "#e0f2fe"),
    ("Sede / Beber", "BÁSICO", "🥤", "#0284c7", "#e0f2fe"),
    ("Estou com Calor", "BÁSICO", "🥵", "#0284c7", "#e0f2fe"),
    ("Estou com Frio", "BÁSICO", "🥶", "#0284c7", "#e0f2fe"),
    ("Sono / Cansado", "BÁSICO", "🥱", "#0284c7", "#e0f2fe"),
    ("Dor de Cabeça", "DOR", "🤕", "#e11d48", "#ffe4e6"),
    ("Dor de Barriga", "DOR", "🤢", "#e11d48", "#ffe4e6"),
    ("Machucado", "DOR", "🩹", "#e11d48", "#ffe4e6"),
    ("Coceira", "DOR", "🦟", "#e11d48", "#ffe4e6"),
    ("Tomar Banho", "HIGIENE", "🛁", "#0284c7", "#e0f2fe"),
    ("Lavar as Mãos", "HIGIENE", "🧼", "#0284c7", "#e0f2fe"),
    ("Escovar Dente", "HIGIENE", "🪥", "#0284c7", "#e0f2fe"),
    ("Trocar Roupa", "HIGIENE", "👕", "#0284c7", "#e0f2fe"),
    ("Tirar o Sapato", "CONFORTO", "👞", "#0284c7", "#e0f2fe"),
    ("Cobertor", "CONFORTO", "🛌", "#0284c7", "#e0f2fe"),
    ("Travesseiro", "CONFORTO", "🛋️", "#0284c7", "#e0f2fe"),
    ("Luz Apagada", "CONFORTO", "🌑", "#0284c7", "#e0f2fe"),
    ("Silêncio", "CONFORTO", "🤫", "#0284c7", "#e0f2fe"),
    ("Abafador Som", "CONFORTO", "🎧", "#0284c7", "#e0f2fe"),
    ("Meu Mordedor", "CONFORTO", "🦷", "#0284c7", "#e0f2fe"),
    ("Ficar Sozinho", "CONFORTO", "🧘", "#0284c7", "#e0f2fe"),

    # Verbos de Ação & Controle (24)
    ("Eu Quero", "VERBO", "👉", "#16a34a", "#dcfce7"),
    ("Eu Não Quero", "VERBO", "🙅", "#dc2626", "#fee2e2"),
    ("Me Ajuda!", "URGENTE", "🆘", "#dc2626", "#fee2e2"),
    ("Mais", "PEDIDO", "➕", "#16a34a", "#dcfce7"),
    ("Chega / Parar", "PEDIDO", "🛑", "#dc2626", "#fee2e2"),
    ("Esperar", "PEDIDO", "⏳", "#d97706", "#fef3c7"),
    ("Sim", "RESPOSTA", "✅", "#16a34a", "#dcfce7"),
    ("Não", "RESPOSTA", "❌", "#dc2626", "#fee2e2"),
    ("Obrigado", "SOCIAL", "🙏", "#2563eb", "#dbeafe"),
    ("Por Favor", "SOCIAL", "🤝", "#2563eb", "#dbeafe"),
    ("Minha Vez", "SOCIAL", "🙋", "#2563eb", "#dbeafe"),
    ("Sua Vez", "SOCIAL", "👉", "#2563eb", "#dbeafe"),
    ("Olha Isso!", "ATENÇÃO", "👀", "#7c3aed", "#f3e8ff"),
    ("Escuta", "ATENÇÃO", "👂", "#7c3aed", "#f3e8ff"),
    ("Gostei Muito", "OPINIÃO", "👍", "#16a34a", "#dcfce7"),
    ("Não Gostei", "OPINIÃO", "👎", "#dc2626", "#fee2e2"),
    ("Vem Comigo", "AÇÃO", "🏃", "#16a34a", "#dcfce7"),
    ("Me Dá", "PEDIDO", "🤲", "#16a34a", "#dcfce7"),
    ("Guardar", "AÇÃO", "📦", "#d97706", "#fef3c7"),
    ("Abrir", "AÇÃO", "🔓", "#16a34a", "#dcfce7"),
    ("Fechar", "AÇÃO", "🔒", "#dc2626", "#fee2e2"),
    ("Subir", "AÇÃO", "⬆️", "#2563eb", "#dbeafe"),
    ("Descer", "AÇÃO", "⬇️", "#2563eb", "#dbeafe"),
    ("Acabou", "AÇÃO", "🏁", "#64748b", "#f1f5f9"),

    # Sentimentos & Pessoas (24)
    ("Estou Feliz", "SENTIMENTO", "😊", "#059669", "#d1fae5"),
    ("Estou Triste", "SENTIMENTO", "😢", "#0284c7", "#e0f2fe"),
    ("Estou Bravo", "SENTIMENTO", "😠", "#dc2626", "#fee2e2"),
    ("Estou Assustado", "SENTIMENTO", "😨", "#ea580c", "#ffedd5"),
    ("Muito Barulho", "SOBRECARGA", "🔊", "#ea580c", "#ffedd5"),
    ("Luz Muito Clara", "SOBRECARGA", "☀️", "#ea580c", "#ffedd5"),
    ("Cheiro Ruim", "SOBRECARGA", "👃", "#ea580c", "#ffedd5"),
    ("Roupa Pinicando", "SOBRECARGA", "🏷️", "#ea580c", "#ffedd5"),
    ("Quero Colo", "AFETO", "🤱", "#db2777", "#fce7f3"),
    ("Quero um Abraço", "AFETO", "🫂", "#db2777", "#fce7f3"),
    ("Quero um Beijo", "AFETO", "😘", "#db2777", "#fce7f3"),
    ("Minha Mamãe", "PESSOAS", "👩", "#db2777", "#fce7f3"),
    ("Meu Papai", "PESSOAS", "👨", "#2563eb", "#dbeafe"),
    ("Meu Irmão/ã", "PESSOAS", "👧", "#7c3aed", "#f3e8ff"),
    ("Minha Vovó", "PESSOAS", "👵", "#059669", "#d1fae5"),
    ("Meu Vovô", "PESSOAS", "👴", "#059669", "#d1fae5"),
    ("Professora", "PESSOAS", "👩‍🏫", "#d97706", "#fef3c7"),
    ("Terapeuta", "PESSOAS", "👩‍⚕️", "#0284c7", "#e0f2fe"),
    ("Meu Amiguinho", "PESSOAS", "🧒", "#2563eb", "#dbeafe"),
    ("Meu Cachorro", "ANIMAIS", "🐶", "#78350f", "#fef3c7"),
    ("Meu Gatinho", "ANIMAIS", "🐱", "#78350f", "#fef3c7"),
    ("Cantinho Calma", "CALMA", "🏕️", "#475569", "#f1f5f9"),
    ("Respira Florzinha", "CALMA", "🌸", "#0d9488", "#ccfbf1"),
    ("Estou Calmo", "CALMA", "😌", "#059669", "#d1fae5"),

    # Alimentos & Bebidas (24)
    ("Água Gelada", "BEBIDAS", "🥛", "#0284c7", "#e0f2fe"),
    ("Leite Morno", "BEBIDAS", "🥛", "#0284c7", "#e0f2fe"),
    ("Suco de Fruta", "BEBIDAS", "🧃", "#d97706", "#fef3c7"),
    ("Iogurte", "LANCHE", "🥣", "#db2777", "#fce7f3"),
    ("Maçã", "FRUTAS", "🍎", "#dc2626", "#fee2e2"),
    ("Banana", "FRUTAS", "🍌", "#eab308", "#fef9c3"),
    ("Uva Roxa", "FRUTAS", "🍇", "#7c3aed", "#f3e8ff"),
    ("Morango", "FRUTAS", "🍓", "#dc2626", "#fee2e2"),
    ("Laranja Doce", "FRUTAS", "🍊", "#ea580c", "#ffedd5"),
    ("Pão Quentinho", "LANCHE", "🍞", "#b45309", "#fef3c7"),
    ("Biscoito Crocante", "LANCHE", "🍪", "#b45309", "#fef3c7"),
    ("Torradinha", "LANCHE", "🥪", "#b45309", "#fef3c7"),
    ("Bolo de Cenoura", "LANCHE", "🍰", "#db2777", "#fce7f3"),
    ("Pipoca", "LANCHE", "🍿", "#eab308", "#fef9c3"),
    ("Arroz Soltinho", "REFEIÇÃO", "🍚", "#475569", "#f1f5f9"),
    ("Feijão", "REFEIÇÃO", "🍲", "#78350f", "#fef3c7"),
    ("Macarrão", "REFEIÇÃO", "🍝", "#ea580c", "#ffedd5"),
    ("Batata Frita/Assada", "REFEIÇÃO", "🥔", "#b45309", "#fef3c7"),
    ("Carninha Macia", "REFEIÇÃO", "🥩", "#991b1b", "#fee2e2"),
    ("Franguinho", "REFEIÇÃO", "🍗", "#b45309", "#fef3c7"),
    ("Ovo Mexido", "REFEIÇÃO", "🍳", "#eab308", "#fef9c3"),
    ("Queijinho", "LANCHE", "🧀", "#eab308", "#fef9c3"),
    ("Picolé / Sorvete", "DOCE", "🍦", "#0284c7", "#e0f2fe"),
    ("Chocolate", "DOCE", "🍫", "#78350f", "#fef3c7"),

    # Brinquedos & Lugares (24)
    ("Tablet / Desenho", "TELA", "📺", "#7c3aed", "#f3e8ff"),
    ("Celular", "TELA", "📱", "#7c3aed", "#f3e8ff"),
    ("Música Favorita", "SOM", "🎵", "#7c3aed", "#f3e8ff"),
    ("Massinha Modelar", "BRINCAR", "🟢", "#059669", "#d1fae5"),
    ("Bolha de Sabão", "BRINCAR", "🫧", "#0284c7", "#e0f2fe"),
    ("Carrinhos", "BRINCAR", "🏎️", "#dc2626", "#fee2e2"),
    ("Bonecos e Heróis", "BRINCAR", "🦸", "#2563eb", "#dbeafe"),
    ("Blocos de Encaixar", "BRINCAR", "🧱", "#eab308", "#fef9c3"),
    ("Quebra-Cabeça", "BRINCAR", "🧩", "#059669", "#d1fae5"),
    ("Desenhar / Giz", "BRINCAR", "🖍️", "#ea580c", "#ffedd5"),
    ("Livro Ilustrado", "BRINCAR", "📚", "#2563eb", "#dbeafe"),
    ("Pular / Cama Elástica", "MOTOR", "🦘", "#059669", "#d1fae5"),
    ("Balanço no Parque", "MOTOR", "🎪", "#d97706", "#fef3c7"),
    ("Escorregador", "MOTOR", "🛝", "#2563eb", "#dbeafe"),
    ("Bola de Chutar", "MOTOR", "⚽", "#475569", "#f1f5f9"),
    ("Bicicleta", "MOTOR", "🚲", "#059669", "#d1fae5"),
    ("Banho de Piscina", "MOTOR", "🏊", "#0284c7", "#e0f2fe"),
    ("Ir ao Parque", "LUGARES", "🌳", "#15803d", "#dcfce7"),
    ("Passear de Carro", "LUGARES", "🚗", "#2563eb", "#dbeafe"),
    ("Ir para a Escola", "LUGARES", "🏫", "#d97706", "#fef3c7"),
    ("Ir para Terapia", "LUGARES", "🏥", "#0284c7", "#e0f2fe"),
    ("Ir para Casa", "LUGARES", "🏠", "#15803d", "#dcfce7"),
    ("Passeio no Shopping", "LUGARES", "🛍️", "#7c3aed", "#f3e8ff"),
    ("Médico / Dentista", "LUGARES", "🩺", "#dc2626", "#fee2e2"),
]

def generate_ob2_html():
    pages_html = []
    
    # Capa & Guia
    pages_html.append("""
    <div class="page cover-page">
      <div class="cover-header">
        <span class="badge-gold">★ FONOAUDIOLOGIA & COMUNICAÇÃO ALTERNATIVA (CAA / PECS)</span>
        <h1>CARTÕES DE COMUNICAÇÃO<br>ALTERNATIVA E FUNCIONAL</h1>
        <p class="subtitle">120 Cartões Ilustrados Prontos para Uso Imediato + 2 Pranchas de Comunicação de Sentença</p>
        <p class="author">Profª Helena Rezende · Neurodesenvolvimento Infantil e Terapia Comportamental</p>
      </div>

      <div class="guide-box">
        <h3>🗣️ COMO USAR A COMUNICAÇÃO VISUAL PARA DESBLOQUEAR A FALA NATURAL</h3>
        <div class="guide-steps">
          <div class="g-step">
            <span class="step-num">1</span>
            <div><strong>Fase 1 (Troca Simples):</strong> Quando a criança quiser água, segure o cartão de ÁGUA na frente dela. Incentive-a a pegar o cartão e colocar na sua mão.</div>
          </div>
          <div class="g-step">
            <span class="step-num">2</span>
            <div><strong>Fase 2 (Reforço Imediato com Nomeação):</strong> Assim que receber o cartão, entregue a água no mesmo segundo dizendo: <em>"Á-GUA! Que lindo você pedir!"</em>.</div>
          </div>
          <div class="g-step">
            <span class="step-num">3</span>
            <div><strong>Desmistificando:</strong> Cartões visuais NÃO preguiçam a fala. Pelo contrário: eles reduzem a angústia de não ser compreendido e estimulam as áreas motoras de fonemas.</div>
          </div>
        </div>
      </div>

      <div class="categories-bar">
        <span class="cat-chip" style="background:#0284c7;">💧 BÁSICO & HIGIENE (24)</span>
        <span class="cat-chip" style="background:#16a34a;">👉 VERBOS & AÇÃO (24)</span>
        <span class="cat-chip" style="background:#e11d48;">😊 SENTIMENTOS (24)</span>
        <span class="cat-chip" style="background:#b45309;">🍎 ALIMENTOS (24)</span>
        <span class="cat-chip" style="background:#7c3aed;">🧸 BRINCAR & LUGARES (24)</span>
      </div>
      <div class="page-footer-note">Nas próximas páginas estão os 120 cartões PECS de alta resolução com bordas de recorte (✂️).</div>
    </div>
    """)

    # Páginas de 12 cartões (3x4)
    for p_idx in range(0, len(pecs_data), 12):
        batch = pecs_data[p_idx:p_idx+12]
        cards_html = ""
        for title, cat, icon, col, bg_col in batch:
            cards_html += f"""
            <div class="flashcard" style="border-color:{col};">
              <div class="cut-guide">✂️</div>
              <div class="card-tag" style="background:{col};">{cat}</div>
              <div class="card-icon-wrap" style="background:{bg_col}; border-color:{col}33;">
                <span class="card-emoji">{icon}</span>
              </div>
              <div class="card-title">{title}</div>
            </div>
            """
        pages_html.append(f"""
        <div class="page card-grid-page">
          <div class="grid-header">
            <span>MÉTODO ESTIMULA TEA · CARTÕES PECS DE COMUNICAÇÃO FUNCIONAL</span>
            <span>RECORTE NAS LINHAS PONTILHADAS ✂️</span>
          </div>
          <div class="cards-grid">
            {cards_html}
          </div>
          <div class="grid-footer">Dica: Plastifique e monte em um fichário com velcro ou prenda com anel de chaveiro!</div>
        </div>
        """)

    # PRANCHA 1 DE SENTENÇA: EU QUERO...
    pages_html.append("""
    <div class="page board-page">
      <div class="board-header">
        <h2>PRANCHA DE COMUNICAÇÃO ATIVA: 'EU QUERO...'</h2>
        <p>A tira de sentença oficial para estruturação de linguagem e comunicação funcional.</p>
      </div>

      <div class="sentence-strip-container">
        <div class="strip-header">TIRA DE SENTENÇA: PEDIDOS DIRETOS</div>
        <div class="strip-slots-row">
          <div class="fixed-card-box box-want">
            <span class="fixed-badge">FIXO</span>
            <span class="fixed-emoji">👉</span>
            <span class="fixed-title">EU QUERO</span>
          </div>

          <div class="strip-plus">+</div>

          <div class="strip-target-slot">
            <span class="slot-hint">[ COLE AQUI O CARTÃO DO PEDIDO ]<br>Ex: Água, Pão, Tablet, Brinquedo, Colo</span>
          </div>
        </div>
      </div>

      <div class="sentence-strip-container" style="margin-top:20px;">
        <div class="strip-header" style="background:#0284c7;">TIRA DE SENTENÇA: EXPRESSÃO DE SENTIMENTOS</div>
        <div class="strip-slots-row">
          <div class="fixed-card-box" style="background:#eff6ff; border-color:#0284c7;">
            <span class="fixed-badge" style="background:#0284c7;">FIXO</span>
            <span class="fixed-emoji">💙</span>
            <span class="fixed-title" style="color:#0284c7;">EU SINTO</span>
          </div>

          <div class="strip-plus" style="color:#0284c7;">+</div>

          <div class="strip-target-slot">
            <span class="slot-hint">[ COLE AQUI O CARTÃO DA SENSAÇÃO ]<br>Ex: Barulho Alto, Calor, Dor de Barriga, Bravo</span>
          </div>
        </div>
      </div>

      <div class="board-instruction" style="margin-top:16px;">
        <strong>COMO PRATICAR:</strong> A criança pega o cartão que deseja, cola na tira ao lado de <em>"EU QUERO"</em> e entrega a tira inteira na sua mão. Você aponta para as duas palavras lendo em voz alta: <em>"Eu quero... Maçã! Aqui está sua maçã!"</em>. Isso treina a formação da frase mental de 2 elementos!
      </div>
    </div>
    """)

    full_html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<title>Cartões de Comunicação Alternativa PECS - Estimula TEA</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@500;600;700;800;900&display=swap" rel="stylesheet">
<style>
  @page {{
    size: A4 portrait;
    margin: 0;
  }}
  * {{
    box-sizing: border-box;
    margin: 0;
    padding: 0;
    font-family: 'Plus Jakarta Sans', -apple-system, sans-serif;
  }}
  body {{
    background: #f1f5f9;
    color: #0f172a;
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
  }}
  .page {{
    width: 210mm;
    height: 297mm;
    page-break-after: always;
    position: relative;
    background: #ffffff;
    overflow: hidden;
    padding: 10mm 12mm;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }}

  /* Capa */
  .cover-page {{
    padding: 16mm 16mm;
    background: linear-gradient(180deg, #f0fdf4 0%, #e2e8f0 100%);
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }}
  .cover-header {{
    text-align: center;
  }}
  .badge-gold {{
    display: inline-block;
    background: #047857;
    color: #ffffff;
    font-size: 10px;
    font-weight: 800;
    padding: 5px 14px;
    border-radius: 9999px;
    letter-spacing: 0.5px;
    margin-bottom: 12px;
  }}
  .cover-header h1 {{
    font-size: 30px;
    font-weight: 900;
    color: #064e3b;
    line-height: 1.15;
    margin-bottom: 8px;
    letter-spacing: -0.5px;
  }}
  .cover-header .subtitle {{
    font-size: 13.5px;
    color: #334155;
    font-weight: 600;
    max-width: 500px;
    margin: 0 auto 6px;
    line-height: 1.4;
  }}
  .cover-header .author {{
    font-size: 12px;
    font-weight: 700;
    color: #0284c7;
  }}

  .guide-box {{
    background: #ffffff;
    border: 2px solid #a7f3d0;
    border-radius: 18px;
    padding: 18px 20px;
    box-shadow: 0 10px 25px -5px rgba(16, 185, 129, 0.08);
  }}
  .guide-box h3 {{
    font-size: 13px;
    font-weight: 900;
    color: #065f46;
    letter-spacing: 0.4px;
    margin-bottom: 12px;
    text-align: center;
  }}
  .guide-steps {{
    display: flex;
    flex-direction: column;
    gap: 10px;
  }}
  .g-step {{
    display: flex;
    align-items: flex-start;
    gap: 12px;
    font-size: 12px;
    line-height: 1.45;
    color: #334155;
  }}
  .step-num {{
    width: 24px;
    height: 24px;
    border-radius: 50%;
    background: #059669;
    color: #ffffff;
    font-size: 12px;
    font-weight: 800;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
  }}

  .categories-bar {{
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    justify-content: center;
  }}
  .cat-chip {{
    color: #ffffff;
    font-size: 10.5px;
    font-weight: 800;
    padding: 6px 12px;
    border-radius: 9999px;
  }}
  .page-footer-note {{
    text-align: center;
    font-size: 11px;
    color: #64748b;
    font-weight: 600;
  }}

  /* Grid dos Cartões */
  .grid-header {{
    display: flex;
    justify-content: space-between;
    font-size: 9px;
    font-weight: 800;
    color: #64748b;
    border-bottom: 1.5px solid #e2e8f0;
    padding-bottom: 6px;
    margin-bottom: 6px;
    letter-spacing: 0.4px;
  }}
  .grid-footer {{
    text-align: center;
    font-size: 9px;
    color: #94a3b8;
    font-weight: 700;
    border-top: 1.5px solid #e2e8f0;
    padding-top: 6px;
    margin-top: 6px;
  }}
  .cards-grid {{
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    grid-template-rows: repeat(4, 1fr);
    gap: 8px;
    flex: 1;
  }}
  .flashcard {{
    background: #ffffff;
    border: 2px dashed #94a3b8;
    border-radius: 14px;
    padding: 8px 6px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: space-between;
    position: relative;
    box-shadow: 0 2px 5px rgba(0,0,0,0.03);
  }}
  .cut-guide {{
    position: absolute;
    top: 3px;
    left: 4px;
    font-size: 8px;
    opacity: 0.6;
  }}
  .card-tag {{
    font-size: 8px;
    font-weight: 800;
    color: #ffffff;
    padding: 2px 8px;
    border-radius: 4px;
    letter-spacing: 0.4px;
    text-transform: uppercase;
  }}
  .card-icon-wrap {{
    width: 60px;
    height: 60px;
    border-radius: 16px;
    display: flex;
    align-items: center;
    justify-content: center;
    border: 1px solid transparent;
    margin: 4px 0;
  }}
  .card-emoji {{
    font-size: 34px;
    line-height: 1;
  }}
  .card-title {{
    font-size: 11.5px;
    font-weight: 800;
    color: #0f172a;
    text-align: center;
    line-height: 1.2;
    padding: 0 4px;
  }}

  /* Prancha de Sentença */
  .sentence-strip-container {{
    border: 2px solid #cbd5e1;
    border-radius: 18px;
    background: #f8fafc;
    padding: 16px;
  }}
  .strip-header {{
    background: #16a34a;
    color: #ffffff;
    font-size: 11px;
    font-weight: 900;
    padding: 6px 14px;
    border-radius: 8px;
    display: inline-block;
    margin-bottom: 12px;
    letter-spacing: 0.5px;
  }}
  .strip-slots-row {{
    display: flex;
    align-items: center;
    gap: 14px;
  }}
  .fixed-card-box {{
    width: 140px;
    height: 180px;
    border: 3px solid #16a34a;
    border-radius: 16px;
    background: #f0fdf4;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 8px;
  }}
  .fixed-badge {{
    background: #16a34a;
    color: #ffffff;
    font-size: 9px;
    font-weight: 800;
    padding: 2px 8px;
    border-radius: 4px;
  }}
  .fixed-emoji {{
    font-size: 42px;
  }}
  .fixed-title {{
    font-size: 16px;
    font-weight: 900;
    color: #15803d;
  }}
  .strip-plus {{
    font-size: 36px;
    font-weight: 900;
    color: #16a34a;
  }}
  .strip-target-slot {{
    flex: 1;
    height: 180px;
    border: 3px dashed #94a3b8;
    background: #ffffff;
    border-radius: 16px;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 16px;
  }}
  .slot-hint {{
    font-size: 11.5px;
    font-weight: 800;
    color: #64748b;
    text-align: center;
    line-height: 1.5;
  }}
</style>
</head>
<body>
{''.join(pages_html)}
</body>
</html>
"""
    return full_html

out_pdf = f"{OUT_DIR}/03_Cartoes_Comunicacao_Alternativa_PECS_120_Cartoes.pdf"
html = generate_ob2_html()

with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False, encoding="utf-8") as f:
    f.write(html)
    tmp_path = f.name

cmd = [
    "google-chrome",
    "--headless=new",
    "--disable-gpu",
    "--no-sandbox",
    "--run-all-compositor-stages-before-draw",
    f"--print-to-pdf={out_pdf}",
    tmp_path
]
subprocess.run(cmd, check=True)
print("Gerado:", out_pdf, os.path.getsize(out_pdf), "bytes")
os.remove(tmp_path)
