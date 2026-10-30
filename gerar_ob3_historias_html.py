#!/usr/bin/env python3
import os, subprocess, tempfile

OUT_DIR = "/home/pedrocoelho/Downloads/atividades-autismo/materiais_entrega"

stories = [
    ("1. INDO AO DENTISTA CUIDAR DOS DENTES", "🦷", "#0284c7", "#e0f2fe",
     "Às vezes, eu preciso ir ao dentista para olhar os meus dentinhos. O consultório tem uma cadeira grande que sobe e desce, parece um foguete! "
     "O dentista usa uma máscara e uma luva para me proteger. Ele vai ligar uma luz em cima para enxergar meus dentes. "
     "Eu posso levar meu brinquedo favorito na minha mão. Quando o dentista pedir, eu abro um bocão grande de leão: AHHH! "
     "Ele vai contar meus dentes com um espelhinho bem pequenininho. Se eu sentir cócegas ou quiser uma pausa, eu levanto a minha mão e ele para. "
     "Depois que terminar, meus dentes vão ficar limpinhos e brilhantes. A mamãe vai me dar um abraço bem orgulhoso!"),

    ("2. CORTANDO O CABELO NO SALÃO", "✂️", "#ea580c", "#ffedd5",
     "O meu cabelo cresce todos os dias. Quando ele fica muito comprido, é hora de cortar para ficar fresquinho e bonito. "
     "No salão, eu sento numa cadeira especial e coloco uma capa para proteger a minha roupa. A capa parece a capa de um super-herói! "
     "O cabeleireiro vai espirrar um pouquinho de água fresca no meu cabelo. A tesoura faz um som suave: *nhec, nhec*. Ela só corta o cabelo, ela não machuca a minha cabeça. "
     "Se a máquina fizer um barulhinho de abelha (*bzzzz*), eu posso colocar meu fone de ouvido com minha música favorita. "
     "Eu respiro fundo e espero alguns minutinhos. Quando acabar, eu sacudo os cabelinhos e olho no espelho como fiquei lindo!"),

    ("3. TOMANDO VACINA PARA FICAR FORTE", "💉", "#16a34a", "#dcfce7",
     "A vacina é uma gotinha mágica que ensina o meu corpo a combater os bichinhos das doenças e não ficar doente. "
     "No posto ou na clínica, a enfermeira é muito boazinha. Ela vai passar um algodãozinho gelado no meu braço. O algodão tem cheirinho de limpeza. "
     "Na hora da picadinha, eu posso segurar a mão da mamãe bem forte e fechar os olhos. Eu cheiro a florzinha e assopro a velinha bem devagar: *fufuuuu*. "
     "Dói só uma picadinha rápida de formiguinha, como um beliscãozinho de 2 segundos: um, dois, e pronto! Acabou! "
     "Eu ganho um curativo bonito e fico super forte e protegido."),

    ("4. QUANDO HÁ BARULHO ALTO OU FOGOS", "🎧", "#7c3aed", "#f3e8ff",
     "Às vezes, acontecem barulhos muito altos que eu não esperava: trovão na chuva, fogos de artifício no céu, sirene da polícia ou liquidificador. "
     "O barulho alto pode dar um susto no meu ouvidinho, mas ele não vai me machucar. O barulho alto sempre passa e vai embora. "
     "Quando eu escutar um som forte, eu posso colocar minhas mãos no ouvido ou pedir meu abafador de som: *'Mamãe, fone por favor'*. "
     "Eu respiro fundo e vou para o meu cantinho da calma. Lá é silencioso e seguro. A mamãe está por perto e me protege."),

    ("5. QUANDO MINHA ROTINA MUDA DE REPENTE", "🔄", "#0d9488", "#ccfbf1",
     "Eu gosto muito de saber o que vai acontecer no meu dia. Isso me deixa seguro e feliz. "
     "Mas às vezes, acontecem coisas diferentes: começa a chover e não dá para ir ao parque, a professora falta, ou o médico muda de horário. "
     "Isso se chama **imprevisto**. Quando a rotina muda, tudo bem! O plano A mudou, mas nós temos o plano B! "
     "Nós olhamos a prancha de rotina e trocamos o cartãozinho. Eu respiro fundo 3 vezes. Coisas novas também podem ser muito divertidas e seguras."),

    ("6. ESPERANDO A MINHA VEZ NA FILA", "🚶‍♂️", "#2563eb", "#dbeafe",
     "No parquinho, no supermercado e na escola, muitas pessoas querem brincar ou comprar ao mesmo tempo. "
     "Para ninguém se machucar ou brigar, nós fazemos uma fila organizada. Cada um tem a sua vez. "
     "Esperar na fila pode parecer demorado, mas o reloginho está correndo. Enquanto espero, eu posso cantar uma musiquinha na minha mente, apertar minha bolinha ou contar os passos. "
     "Quando o amigo da frente sair, é a MINHA VEZ! Esperar a vez mostra que sou uma criança esperta e educada."),

    ("7. DIVIDINDO OS BRINQUEDOS COM OS AMIGOS", "🤝", "#b45309", "#fef3c7",
     "Na minha escola e no parquinho há muitos brinquedos legais. Os brinquedos são para todas as crianças se divertirem. "
     "Quando um amigo quer o brinquedo que estou usando, ele não está roubando de mim. Ele só quer brincar um pouquinho também. "
     "Eu posso brincar mais 2 minutinhos e depois dizer: *'Agora é sua vez!'*. Depois que o amigo terminar, ele devolve para mim. "
     "Brincar junto e emprestar brinquedos faz a gente ter amigos legais para correr e dar risadas."),

    ("8. USANDO O BANHEIRO FORA DE CASA", "🚽", "#0284c7", "#e0f2fe",
     "Quando estou no shopping, no restaurante ou na escola e sinto vontade de fazer xixi ou cocô, eu preciso ir ao banheiro público. "
     "O banheiro de fora é um pouco diferente do banheiro da minha casa: a pia pode ter sensor automático e a descarga pode fazer um barulho alto: *shhhhh!* "
     "Não preciso ter medo. A mamãe ou o papai entram comigo. Nós forramos a tampa do vaso com papel. Eu sento tranquilo e faço o meu xixi. "
     "Depois, lavo as mãos com sabão e enxáguo. O banheiro de fora me ajuda a continuar o passeio sequinho e confortável."),

    ("9. QUANDO EU PERCO EM UM JOGO OU BRINCADEIRA", "🏆", "#d97706", "#fef3c7",
     "Jogar jogos de tabuleiro, bola ou videogame com outras pessoas é muito legal. "
     "Em todo jogo, alguém ganha e alguém perde. Ninguém consegue ganhar todas as vezes, nem os adultos! "
     "Quando eu não ganho, posso sentir uma pontinha de tristeza ou raiva no peito. Isso é normal. Eu coloco a mão no coração e respiro fundo. "
     "Eu posso dar um 'toca aqui' no amigo e dizer: *'Parabéns, você jogou bem!'*. Na próxima rodada, eu posso tentar de novo. O mais legal de tudo é brincar!"),

    ("10. HORA DE GUARDAR O TABLET SEM GRITAR", "📺", "#7c3aed", "#f3e8ff",
     "Eu adoro assistir meus desenhos favoritos e jogar no tablet ou no celular. É muito divertido e colorido! "
     "Mas meus olhinhos e meu cérebro precisam descansar para eu não ficar irritado e com dor de cabeça. "
     "A mamãe vai colocar um alarme no relógio para me avisar: *'Faltam 5 minutos para guardar'*. "
     "Quando o alarme tocar (*plim-plim*), é a hora de apertar o botão e desligar a tela. Eu não preciso gritar ou chorar. O tablet vai dormir na gaveta e amanhã eu posso brincar de novo!"),
]

pages = []
# Capa
pages.append("""
<div class="page">
  <div class="top-bar">
    <span>MÉTODO ESTIMULA TEA · PREVISIBILIDADE COMPORTAMENTAL</span>
    <span>METODOLOGIA CAROL GRAY</span>
  </div>
  <div style="text-align:center; padding: 20mm 10mm;">
    <span class="badge-tag" style="background:#2563eb; color:#fff;">HISTÓRIAS SOCIAIS ILUSTRADAS</span>
    <h1 class="book-title" style="color:#1e3a8a; font-size:32px;">CADERNO DE HISTÓRIAS<br>SOCIAIS PRONTAS</h1>
    <p class="book-sub" style="font-size:14px; max-width:480px; margin:0 auto 16px;">20 Histórias Ilustradas para Reduzir a Ansiedade e Antecipar Situações Desafiadoras no TEA</p>
    <p style="font-size:12px; font-weight:700; color:#059669;">Profª Helena Rezende · Pedagoga e Especialista em Intervenção Precoce</p>
  </div>
  <div style="background:#eff6ff; border:2px solid #bfdbfe; border-radius:16px; padding:16px 20px;">
    <h3 style="font-size:12px; font-weight:800; color:#1e40af; margin-bottom:8px;">💡 COMO LER COM SUA CRIANÇA:</h3>
    <p class="text">• Leia 1 a 2 dias ANTES da situação acontecer (ex: antes de ir ao dentista ou cortar o cabelo).<br>
    • Leia em tom calmo, acolhedor e afirmativo, apontando para as ilustrações.<br>
    • Repita 2 a 3 vezes. A previsibilidade mental constrói segurança neurobiológica imediata.</p>
  </div>
  <div class="foot-bar">
    <span>© Portal Estimula TEA</span>
    <span>Capa Oficial</span>
  </div>
</div>
""")

# 2 histórias por página
for i in range(0, len(stories), 2):
    pair = stories[i:i+2]
    cards_html = ""
    for title, icon, col, bg_col, text_content in pair:
        cards_html += f"""
        <div style="background:#ffffff; border:2px solid {col}; border-radius:16px; padding:16px; box-shadow:0 4px 12px rgba(0,0,0,0.04); margin-bottom:12px;">
          <div style="display:flex; align-items:center; gap:10px; margin-bottom:8px;">
            <div style="width:40px; height:40px; border-radius:10px; background:{bg_col}; display:flex; align-items:center; justify-content:center; font-size:22px; flex-shrink:0;">{icon}</div>
            <div style="font-size:13px; font-weight:900; color:{col};">{title}</div>
          </div>
          <p style="font-size:10.5px; line-height:1.55; color:#334155; text-align:justify;">{text_content}</p>
        </div>
        """
    pages.append(f"""
    <div class="page">
      <div class="top-bar">
        <span>MÉTODO ESTIMULA TEA · CADERNO DE HISTÓRIAS SOCIAIS</span>
        <span>HISTÓRIAS #{i+1} E #{i+2}</span>
      </div>
      <div style="flex:1; display:flex; flex-direction:column; justify-content:center;">
        {cards_html}
      </div>
      <div class="foot-bar">
        <span>Profª Helena Rezende · Neurodesenvolvimento Infantil</span>
        <span>Página {int(i/2)+2} de 6</span>
      </div>
    </div>
    """)

html_full = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<title>Caderno de Histórias Sociais - Estimula TEA</title>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@500;600;700;800;900&display=swap" rel="stylesheet">
<style>
  @page {{ size: A4 portrait; margin: 0; }}
  * {{ box-sizing: border-box; margin: 0; padding: 0; font-family: 'Plus Jakarta Sans', -apple-system, sans-serif; }}
  body {{ background: #f8fafc; color: #0f172a; -webkit-print-color-adjust: exact; print-color-adjust: exact; }}
  .page {{ width: 210mm; height: 297mm; page-break-after: always; position: relative; background: #ffffff; overflow: hidden; padding: 14mm 16mm; display: flex; flex-direction: column; justify-content: space-between; }}
  .top-bar {{ display: flex; justify-content: space-between; font-size: 8.5px; font-weight: 800; color: #64748b; border-bottom: 1.5px solid #e2e8f0; padding-bottom: 6px; letter-spacing: 0.5px; text-transform: uppercase; }}
  .foot-bar {{ display: flex; justify-content: space-between; font-size: 8.5px; font-weight: 700; color: #94a3b8; border-top: 1.5px solid #e2e8f0; padding-top: 6px; }}
  .badge-tag {{ display: inline-block; font-size: 9.5px; font-weight: 800; padding: 4px 12px; border-radius: 9999px; letter-spacing: 0.5px; text-transform: uppercase; margin-bottom: 8px; }}
  h1.book-title {{ font-size: 28px; font-weight: 900; line-height: 1.15; letter-spacing: -0.5px; margin-bottom: 6px; }}
  p.book-sub {{ font-size: 13px; font-weight: 600; color: #475569; line-height: 1.4; margin-bottom: 14px; }}
  p.text {{ font-size: 11px; line-height: 1.55; color: #334155; margin-bottom: 8px; }}
</style>
</head>
<body>
{''.join(pages)}
</body>
</html>
"""

out_pdf = f"{OUT_DIR}/05_Caderno_20_Historias_Sociais_Ilustradas.pdf"
with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False, encoding="utf-8") as f:
    f.write(html_full)
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
print(f"✅ Gerado com sucesso: {out_pdf} ({os.path.getsize(out_pdf)/1024:.1f} KB)")
os.remove(tmp_path)
