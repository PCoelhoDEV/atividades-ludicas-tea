#!/usr/bin/env python3
import os, subprocess, tempfile

OUT_DIR = "/home/pedrocoelho/Downloads/atividades-autismo/materiais_entrega"

cards_data = [
    # Manhã (24)
    ("Acordar", "MANHÃ", "🌅", "#0284c7", "#e0f2fe"),
    ("Tirar o Pijama", "MANHÃ", "👕", "#0284c7", "#e0f2fe"),
    ("Ir ao Banheiro", "MANHÃ", "🚽", "#0284c7", "#e0f2fe"),
    ("Fazer Xixi", "MANHÃ", "💧", "#0284c7", "#e0f2fe"),
    ("Lavar o Rosto", "MANHÃ", "🧼", "#0284c7", "#e0f2fe"),
    ("Escovar os Dentes", "MANHÃ", "🪥", "#0284c7", "#e0f2fe"),
    ("Pentear o Cabelo", "MANHÃ", "🪮", "#0284c7", "#e0f2fe"),
    ("Tomar Café", "MANHÃ", "🥛", "#0284c7", "#e0f2fe"),
    ("Comer Fruta", "MANHÃ", "🍎", "#0284c7", "#e0f2fe"),
    ("Tomar Remédio", "MANHÃ", "💊", "#0284c7", "#e0f2fe"),
    ("Colocar a Roupa", "MANHÃ", "🧦", "#0284c7", "#e0f2fe"),
    ("Calçar as Meias", "MANHÃ", "🧦", "#0284c7", "#e0f2fe"),
    ("Calçar o Tênis", "MANHÃ", "👟", "#0284c7", "#e0f2fe"),
    ("Passar Protetor", "MANHÃ", "🧴", "#0284c7", "#e0f2fe"),
    ("Pegar a Mochila", "MANHÃ", "🎒", "#0284c7", "#e0f2fe"),
    ("Entrar no Carro", "MANHÃ", "🚗", "#0284c7", "#e0f2fe"),
    ("Entrar na Van", "MANHÃ", "🚌", "#0284c7", "#e0f2fe"),
    ("Andar a Pé", "MANHÃ", "🚶", "#0284c7", "#e0f2fe"),
    ("Chegar na Escola", "MANHÃ", "🏫", "#0284c7", "#e0f2fe"),
    ("Tchau pra Mamãe", "MANHÃ", "👋", "#0284c7", "#e0f2fe"),
    ("Guardar a Mochila", "MANHÃ", "🎒", "#0284c7", "#e0f2fe"),
    ("Sentar na Roda", "MANHÃ", "⭕", "#0284c7", "#e0f2fe"),
    ("Ouvir Professora", "MANHÃ", "👩‍🏫", "#0284c7", "#e0f2fe"),
    ("Hora da Atividade", "MANHÃ", "✏️", "#0284c7", "#e0f2fe"),

    # Escola & Aprendizado (24)
    ("Pintar com Lápis", "ESCOLA", "🎨", "#ea580c", "#ffedd5"),
    ("Cortar Tesoura", "ESCOLA", "✂️", "#ea580c", "#ffedd5"),
    ("Usar Cola", "ESCOLA", "🧴", "#ea580c", "#ffedd5"),
    ("Massinha de Modelar", "ESCOLA", "🟢", "#ea580c", "#ffedd5"),
    ("Hora da Leitura", "ESCOLA", "📖", "#ea580c", "#ffedd5"),
    ("Lanche da Escola", "ESCOLA", "🥪", "#ea580c", "#ffedd5"),
    ("Beber Água", "ESCOLA", "🥤", "#ea580c", "#ffedd5"),
    ("Lavar as Mãos", "ESCOLA", "🧼", "#ea580c", "#ffedd5"),
    ("Hora do Recreio", "ESCOLA", "🛝", "#ea580c", "#ffedd5"),
    ("Brincar no Pátio", "ESCOLA", "🏃", "#ea580c", "#ffedd5"),
    ("Esperar na Fila", "ESCOLA", "🚶‍♂️", "#ea580c", "#ffedd5"),
    ("Dividir Brinquedo", "ESCOLA", "🤝", "#ea580c", "#ffedd5"),
    ("Educação Física", "ESCOLA", "⚽", "#ea580c", "#ffedd5"),
    ("Hora da Música", "ESCOLA", "🎵", "#ea580c", "#ffedd5"),
    ("Guardar Material", "ESCOLA", "📦", "#ea580c", "#ffedd5"),
    ("Saída da Escola", "ESCOLA", "🚪", "#ea580c", "#ffedd5"),
    ("Encontrar Mamãe", "ESCOLA", "👩‍👦", "#ea580c", "#ffedd5"),
    ("Terapia ABA", "ESCOLA", "🧩", "#ea580c", "#ffedd5"),
    ("Fonoaudióloga", "ESCOLA", "🗣️", "#ea580c", "#ffedd5"),
    ("Terapeuta Ocup.", "ESCOLA", "🖐️", "#ea580c", "#ffedd5"),
    ("Psicóloga", "ESCOLA", "🧠", "#ea580c", "#ffedd5"),
    ("Fisioterapia", "ESCOLA", "🤸", "#ea580c", "#ffedd5"),
    ("Natação", "ESCOLA", "🏊", "#ea580c", "#ffedd5"),
    ("Musicoterapia", "ESCOLA", "🥁", "#ea580c", "#ffedd5"),

    # Tarde & Lazer (24)
    ("Almoçar", "TARDE", "🍽️", "#16a34a", "#dcfce7"),
    ("Comer Salada", "TARDE", "🥗", "#16a34a", "#dcfce7"),
    ("Comer Carninha", "TARDE", "🍗", "#16a34a", "#dcfce7"),
    ("Arroz e Feijão", "TARDE", "🍚", "#16a34a", "#dcfce7"),
    ("Limpar a Boca", "TARDE", "🧻", "#16a34a", "#dcfce7"),
    ("Descanso / Soneca", "TARDE", "🛋️", "#16a34a", "#dcfce7"),
    ("Lição de Casa", "TARDE", "📝", "#16a34a", "#dcfce7"),
    ("Brincar Livre", "TARDE", "🧸", "#16a34a", "#dcfce7"),
    ("Quebra-Cabeça", "TARDE", "🧩", "#16a34a", "#dcfce7"),
    ("Carrinhos", "TARDE", "🏎️", "#16a34a", "#dcfce7"),
    ("Bonecos / Heróis", "TARDE", "🦸", "#16a34a", "#dcfce7"),
    ("Blocos de Encaixar", "TARDE", "🧱", "#16a34a", "#dcfce7"),
    ("Hora do Tablet", "TARDE", "📺", "#16a34a", "#dcfce7"),
    ("Timer Apitou", "TARDE", "⏰", "#16a34a", "#dcfce7"),
    ("Desligar Tablet", "TARDE", "📴", "#16a34a", "#dcfce7"),
    ("Guardar Brinquedos", "TARDE", "🧺", "#16a34a", "#dcfce7"),
    ("Lanche da Tarde", "TARDE", "🍌", "#16a34a", "#dcfce7"),
    ("Passear no Parque", "TARDE", "🌳", "#16a34a", "#dcfce7"),
    ("Andar de Bicicleta", "TARDE", "🚲", "#16a34a", "#dcfce7"),
    ("Brincar com Pet", "TARDE", "🐕", "#16a34a", "#dcfce7"),
    ("Banho de Mangueira", "TARDE", "💦", "#16a34a", "#dcfce7"),
    ("Cama Elástica", "TARDE", "🦘", "#16a34a", "#dcfce7"),
    ("Visitar a Vovó", "TARDE", "👵", "#16a34a", "#dcfce7"),
    ("Supermercado", "TARDE", "🛒", "#16a34a", "#dcfce7"),

    # Noite & Higiene (24)
    ("Jantar em Família", "NOITE", "🍲", "#7c3aed", "#f3e8ff"),
    ("Tirar a Mesa", "NOITE", "🍽️", "#7c3aed", "#f3e8ff"),
    ("Hora do Banho", "NOITE", "🛁", "#7c3aed", "#f3e8ff"),
    ("Tirar Roupa Suja", "NOITE", "🧺", "#7c3aed", "#f3e8ff"),
    ("Lavar o Cabelo", "NOITE", "🧴", "#7c3aed", "#f3e8ff"),
    ("Enxaguar o Corpo", "NOITE", "🚿", "#7c3aed", "#f3e8ff"),
    ("Secar com Toalha", "NOITE", "🧖", "#7c3aed", "#f3e8ff"),
    ("Vestir o Pijama", "NOITE", "👕", "#7c3aed", "#f3e8ff"),
    ("Cortar a Unha", "NOITE", "💅", "#7c3aed", "#f3e8ff"),
    ("Limpar o Ouvido", "NOITE", "👂", "#7c3aed", "#f3e8ff"),
    ("Escovar Dentes", "NOITE", "🪥", "#7c3aed", "#f3e8ff"),
    ("Xixi Antes de Dormir", "NOITE", "🚽", "#7c3aed", "#f3e8ff"),
    ("Passar Hidratante", "NOITE", "🧴", "#7c3aed", "#f3e8ff"),
    ("Massagem Calma", "NOITE", "💆", "#7c3aed", "#f3e8ff"),
    ("Ouvir História", "NOITE", "📚", "#7c3aed", "#f3e8ff"),
    ("Música Relaxante", "NOITE", "🎶", "#7c3aed", "#f3e8ff"),
    ("Abraço de Boa Noite", "NOITE", "🤗", "#7c3aed", "#f3e8ff"),
    ("Beijo dos Pais", "NOITE", "😘", "#7c3aed", "#f3e8ff"),
    ("Deitar na Cama", "NOITE", "🛏️", "#7c3aed", "#f3e8ff"),
    ("Cobertor Pesado", "NOITE", "🛌", "#7c3aed", "#f3e8ff"),
    ("Abajur Ligado", "NOITE", "💡", "#7c3aed", "#f3e8ff"),
    ("Apagar a Luz", "NOITE", "🌑", "#7c3aed", "#f3e8ff"),
    ("Ficar no Quarto", "NOITE", "🚪", "#7c3aed", "#f3e8ff"),
    ("Dormir Noite Toda", "NOITE", "💤", "#7c3aed", "#f3e8ff"),

    # Emoções, Regulação & Transição (36)
    ("Estou Feliz", "EMOÇÃO", "😊", "#e11d48", "#ffe4e6"),
    ("Estou Triste", "EMOÇÃO", "😢", "#e11d48", "#ffe4e6"),
    ("Estou Bravo", "EMOÇÃO", "😠", "#e11d48", "#ffe4e6"),
    ("Estou Cansado", "EMOÇÃO", "🥱", "#e11d48", "#ffe4e6"),
    ("Estou com Medo", "EMOÇÃO", "😨", "#e11d48", "#ffe4e6"),
    ("Estou Assustado", "EMOÇÃO", "😱", "#e11d48", "#ffe4e6"),
    ("Barulho Muito Alto", "SOBRECARGA", "🙉", "#e11d48", "#ffe4e6"),
    ("Abafador de Ruído", "REGULAÇÃO", "🎧", "#e11d48", "#ffe4e6"),
    ("Luz Muito Forte", "SOBRECARGA", "🕶️", "#e11d48", "#ffe4e6"),
    ("Quero Silêncio", "REGULAÇÃO", "🤫", "#e11d48", "#ffe4e6"),
    ("Preciso de Abraço", "AFETO", "🫂", "#e11d48", "#ffe4e6"),
    ("Quero Colo", "AFETO", "🤱", "#e11d48", "#ffe4e6"),
    ("Respira Fundo", "CALMA", "🌸", "#0d9488", "#ccfbf1"),
    ("Assopra a Vela", "CALMA", "🎂", "#0d9488", "#ccfbf1"),
    ("Cantinho da Calma", "CALMA", "🏕️", "#0d9488", "#ccfbf1"),
    ("Apertar Bolinha", "CALMA", "🟢", "#0d9488", "#ccfbf1"),
    ("Garrafa da Calma", "CALMA", "✨", "#0d9488", "#ccfbf1"),
    ("Mordedor Sensorial", "CALMA", "🦷", "#0d9488", "#ccfbf1"),
    ("Ficar Sozinho", "CALMA", "🧘", "#0d9488", "#ccfbf1"),
    ("Estou Calmo Agora", "CALMA", "😌", "#0d9488", "#ccfbf1"),
    ("Primeiro", "TRANSIÇÃO", "1️⃣", "#4f46e5", "#e0e7ff"),
    ("Depois", "TRANSIÇÃO", "2️⃣", "#4f46e5", "#e0e7ff"),
    ("Agora", "TRANSIÇÃO", "⏰", "#4f46e5", "#e0e7ff"),
    ("Próximo", "TRANSIÇÃO", "➡️", "#4f46e5", "#e0e7ff"),
    ("Acabou / Fim", "TRANSIÇÃO", "🛑", "#4f46e5", "#e0e7ff"),
    ("Esperar 1 Minuto", "TRANSIÇÃO", "⏳", "#4f46e5", "#e0e7ff"),
    ("Mais Um Pouco", "TRANSIÇÃO", "➕", "#4f46e5", "#e0e7ff"),
    ("Trocar de Roupa", "TRANSIÇÃO", "👚", "#4f46e5", "#e0e7ff"),
    ("Guardar Tudo", "TRANSIÇÃO", "📦", "#4f46e5", "#e0e7ff"),
    ("Parabéns!", "REFORÇO", "⭐", "#d97706", "#fef3c7"),
    ("Ganhou Estrela", "REFORÇO", "🌟", "#d97706", "#fef3c7"),
    ("Muito Orgulho!", "REFORÇO", "🏆", "#d97706", "#fef3c7"),
    ("Toca Aqui! High Five", "REFORÇO", "✋", "#d97706", "#fef3c7"),
    ("Abraço Gostoso", "REFORÇO", "❤️", "#d97706", "#fef3c7"),
    ("Brincadeira Top", "REFORÇO", "🎮", "#d97706", "#fef3c7"),
    ("Passeio Especial", "REFORÇO", "🍦", "#d97706", "#fef3c7"),
]

def generate_ob1_html():
    pages_html = []
    
    # Capa & Guia
    pages_html.append("""
    <div class="page cover-page">
      <div class="cover-header">
        <span class="badge-gold">★ MATERIAL OFICIAL REGISTRADO · MÉTODO ESTIMULA TEA</span>
        <h1>KIT DE ROTINA VISUAL<br>& PREVISIBILIDADE</h1>
        <p class="subtitle">132 Cartões Ilustrados Prontos para Imprimir, Plastificar e Recortar + 3 Pranchas Estruturadas</p>
        <p class="author">Profª Helena Rezende · Pedagoga e Especialista em Neurodesenvolvimento</p>
      </div>

      <div class="guide-box">
        <h3>💡 GUIA RÁPIDO: COMO MONTAR E USAR SEUS CARTÕES</h3>
        <div class="guide-steps">
          <div class="g-step">
            <span class="step-num">1</span>
            <div><strong>Impressão de Qualidade:</strong> Imprima em papel sulfite comum 90g ou preferencialmente 120g/180g (fica bem firme).</div>
          </div>
          <div class="g-step">
            <span class="step-num">2</span>
            <div><strong>Plastificação Fácil:</strong> Use folhas de polaseal a quente ou simplesmente passe fita adesiva larga transparente nas duas faces.</div>
          </div>
          <div class="g-step">
            <span class="step-num">3</span>
            <div><strong>Velcro Adesivo:</strong> Cole velcro no verso de cada cartão e nos círculos das pranchas (nas páginas finais deste material).</div>
          </div>
          <div class="g-step">
            <span class="step-num">4</span>
            <div><strong>O Segredo das Transições:</strong> Mostre o cartão 5 minutos antes: <em>"Faltam 5 minutos para guardar o brinquedo e ir para o banho"</em>. Isso elimina as crises!</div>
          </div>
        </div>
      </div>

      <div class="categories-bar">
        <span class="cat-chip" style="background:#0284c7;">🌅 MANHÃ (24)</span>
        <span class="cat-chip" style="background:#ea580c;">🏫 ESCOLA (24)</span>
        <span class="cat-chip" style="background:#16a34a;">🌳 TARDE (24)</span>
        <span class="cat-chip" style="background:#7c3aed;">🌙 NOITE (24)</span>
        <span class="cat-chip" style="background:#e11d48;">❤️ EMOÇÕES (20)</span>
        <span class="cat-chip" style="background:#4f46e5;">⚡ TRANSIÇÃO (16)</span>
      </div>
      <div class="page-footer-note">Nas próximas páginas estão os 132 cartões em tamanho ideal para recorte (✂️).</div>
    </div>
    """)

    # Páginas de 12 cartões (3x4)
    for p_idx in range(0, len(cards_data), 12):
        batch = cards_data[p_idx:p_idx+12]
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
            <span>MÉTODO ESTIMULA TEA · CARTÕES DE ROTINA VISUAL</span>
            <span>RECORTE NAS LINHAS PONTILHADAS ✂️</span>
          </div>
          <div class="cards-grid">
            {cards_html}
          </div>
          <div class="grid-footer">Dica: Plastifique para durabilidade infinita e higienização fácil.</div>
        </div>
        """)

    # PRANCHA 1: PRIMEIRO / DEPOIS
    pages_html.append("""
    <div class="page board-page">
      <div class="board-header">
        <h2>PRANCHA ESTRUTURADA: PRIMEIRO E DEPOIS</h2>
        <p>A ferramenta #1 da metodologia TEACCH para eliminar resistência em tarefas essenciais.</p>
      </div>

      <div class="first-then-container">
        <div class="ft-box box-first">
          <div class="ft-title">1. PRIMEIRO</div>
          <div class="ft-sub">Tarefa Essencial (Ex: Almoçar, Banho, Guardar)</div>
          <div class="ft-slot">
            <span class="slot-circle">[ COLE O CARTÃO AQUI ]</span>
          </div>
        </div>

        <div class="ft-arrow">➔</div>

        <div class="ft-box box-then">
          <div class="ft-title">2. DEPOIS</div>
          <div class="ft-sub">Recompensa / Atividade Favorita (Ex: Parque, Massinha)</div>
          <div class="ft-slot">
            <span class="slot-circle">[ COLE O CARTÃO AQUI ]</span>
          </div>
        </div>
      </div>

      <div class="board-instruction">
        <strong>COMO USAR:</strong> Coloque o cartão da tarefa necessária em <em>PRIMEIRO</em> e a atividade desejada em <em>DEPOIS</em>. Aponte com calma e diga apenas: <em>"Primeiro guardar, depois parque."</em> Sem discussões. A previsibilidade visual desativa a birra na hora!
      </div>
    </div>
    """)

    # PRANCHA 2: MINHA ROTINA DO DIA (Manhã, Tarde, Noite)
    pages_html.append("""
    <div class="page board-page">
      <div class="board-header">
        <h2>PRANCHA COMPLETA: MINHA ROTINA DO DIA</h2>
        <p>Organize até 5 passos para cada período. Conforme a criança cumpre o passo, ela retira o cartão.</p>
      </div>

      <div class="routine-rows">
        <!-- Manhã -->
        <div class="routine-row row-morning">
          <div class="row-label">🌅 MANHÃ</div>
          <div class="row-slots">
            <div class="r-slot"><span>Passo 1</span></div>
            <div class="r-slot"><span>Passo 2</span></div>
            <div class="r-slot"><span>Passo 3</span></div>
            <div class="r-slot"><span>Passo 4</span></div>
            <div class="r-slot"><span>Passo 5</span></div>
          </div>
        </div>

        <!-- Tarde -->
        <div class="routine-row row-afternoon">
          <div class="row-label">🌳 TARDE</div>
          <div class="row-slots">
            <div class="r-slot"><span>Passo 1</span></div>
            <div class="r-slot"><span>Passo 2</span></div>
            <div class="r-slot"><span>Passo 3</span></div>
            <div class="r-slot"><span>Passo 4</span></div>
            <div class="r-slot"><span>Passo 5</span></div>
          </div>
        </div>

        <!-- Noite -->
        <div class="routine-row row-night">
          <div class="row-label">🌙 NOITE</div>
          <div class="row-slots">
            <div class="r-slot"><span>Passo 1</span></div>
            <div class="r-slot"><span>Passo 2</span></div>
            <div class="r-slot"><span>Passo 3</span></div>
            <div class="r-slot"><span>Passo 4</span></div>
            <div class="r-slot"><span>Passo 5</span></div>
          </div>
        </div>
      </div>

      <div class="board-instruction">
        <strong>DICA DE OURO:</strong> Coloque uma caixinha ou pote ao lado da prancha escrito "CONCLUÍDO". Quando a criança escovar os dentes, ela mesma tira o cartão da prancha e joga na caixa. O cérebro libera dopamina pelo dever cumprido!
      </div>
    </div>
    """)

    full_html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<title>Kit de Rotina Visual - Método Estimula TEA</title>
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
    background: linear-gradient(180deg, #f8fafc 0%, #e2e8f0 100%);
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }}
  .cover-header {{
    text-align: center;
  }}
  .badge-gold {{
    display: inline-block;
    background: #1e3a8a;
    color: #ffffff;
    font-size: 10px;
    font-weight: 800;
    padding: 5px 14px;
    border-radius: 9999px;
    letter-spacing: 0.5px;
    margin-bottom: 12px;
  }}
  .cover-header h1 {{
    font-size: 32px;
    font-weight: 900;
    color: #1e3a8a;
    line-height: 1.15;
    margin-bottom: 8px;
    letter-spacing: -0.5px;
  }}
  .cover-header .subtitle {{
    font-size: 14px;
    color: #475569;
    font-weight: 600;
    max-width: 500px;
    margin: 0 auto 6px;
    line-height: 1.4;
  }}
  .cover-header .author {{
    font-size: 12px;
    font-weight: 700;
    color: #059669;
  }}

  .guide-box {{
    background: #ffffff;
    border: 2px solid #cbd5e1;
    border-radius: 18px;
    padding: 18px 20px;
    box-shadow: 0 10px 25px -5px rgba(15, 23, 42, 0.08);
  }}
  .guide-box h3 {{
    font-size: 13px;
    font-weight: 900;
    color: #1e3a8a;
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
    background: #2563eb;
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

  /* Prancha Primeiro / Depois */
  .board-header {{
    text-align: center;
    margin-bottom: 16px;
  }}
  .board-header h2 {{
    font-size: 24px;
    font-weight: 900;
    color: #1e3a8a;
  }}
  .board-header p {{
    font-size: 12px;
    color: #64748b;
    font-weight: 600;
  }}
  .first-then-container {{
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 16px;
    flex: 1;
    margin-bottom: 16px;
  }}
  .ft-box {{
    flex: 1;
    height: 100%;
    border-radius: 24px;
    padding: 20px 16px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: space-between;
    text-align: center;
  }}
  .box-first {{
    background: #eff6ff;
    border: 4px solid #2563eb;
  }}
  .box-then {{
    background: #f0fdf4;
    border: 4px solid #16a34a;
  }}
  .ft-title {{
    font-size: 26px;
    font-weight: 900;
  }}
  .box-first .ft-title {{ color: #1e40af; }}
  .box-then .ft-title {{ color: #15803d; }}
  .ft-sub {{
    font-size: 11px;
    color: #475569;
    font-weight: 700;
    margin-top: 4px;
  }}
  .ft-slot {{
    width: 140px;
    height: 190px;
    border: 3px dashed #94a3b8;
    background: #ffffff;
    border-radius: 16px;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 10px;
  }}
  .slot-circle {{
    font-size: 11px;
    font-weight: 800;
    color: #94a3b8;
    text-align: center;
    line-height: 1.4;
  }}
  .ft-arrow {{
    font-size: 38px;
    color: #64748b;
    font-weight: 900;
  }}
  .board-instruction {{
    background: #f8fafc;
    border: 1.5px solid #cbd5e1;
    border-radius: 14px;
    padding: 12px 16px;
    font-size: 11.5px;
    color: #334155;
    line-height: 1.45;
  }}

  /* Prancha Completa da Rotina */
  .routine-rows {{
    display: flex;
    flex-direction: column;
    gap: 16px;
    flex: 1;
    justify-content: center;
  }}
  .routine-row {{
    border-radius: 20px;
    padding: 12px 16px;
    display: flex;
    flex-direction: column;
    gap: 10px;
  }}
  .row-morning {{ background: #eff6ff; border: 2.5px solid #2563eb; }}
  .row-afternoon {{ background: #f0fdf4; border: 2.5px solid #16a34a; }}
  .row-night {{ background: #faf5ff; border: 2.5px solid #7c3aed; }}

  .row-label {{
    font-size: 16px;
    font-weight: 900;
    letter-spacing: 0.5px;
  }}
  .row-morning .row-label {{ color: #1e40af; }}
  .row-afternoon .row-label {{ color: #15803d; }}
  .row-night .row-label {{ color: #6b21a8; }}

  .row-slots {{
    display: grid;
    grid-template-columns: repeat(5, 1fr);
    gap: 10px;
  }}
  .r-slot {{
    height: 90px;
    background: #ffffff;
    border: 2px dashed #94a3b8;
    border-radius: 12px;
    display: flex;
    align-items: center;
    justify-content: center;
  }}
  .r-slot span {{
    font-size: 10px;
    font-weight: 800;
    color: #94a3b8;
  }}
</style>
</head>
<body>
{''.join(pages_html)}
</body>
</html>
"""
    return full_html

out_pdf = f"{OUT_DIR}/02_Kit_Rotina_Visual_132_Cartoes_e_Pranchas.pdf"
html = generate_ob1_html()

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
