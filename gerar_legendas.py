#!/usr/bin/env python3
"""
Generate high-impact Meta Reels safe-zone ASS subtitles for TEA creative.
Target: 1080x1920, positioned inside the smooth dark backdrop (Y: 1370-1510, MarginV=410).
"""

ass_header = """[Script Info]
ScriptType: v4.00+
PlayResX: 1080
PlayResY: 1920
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Default,Arial Black,58,&H00FFFFFF,&H000000FF,&H00000000,&H00000000,-1,0,0,0,100,100,1,0,1,5,1,2,50,50,410,1
Style: Hook,Arial Black,62,&H0000FFFF,&H000000FF,&H00000000,&H00000000,-1,0,0,0,100,100,2,0,1,6,2,2,50,50,410,1
Style: Urgency,Arial Black,60,&H0033FFFF,&H000000FF,&H00000000,&H00000000,-1,0,0,0,100,100,1,0,1,6,2,2,50,50,410,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""

events = [
    # 0.00 - 9.15s: "Se o seu filho tem autismo ou atraso no desenvolvimento, me escuta com atenção: a janela de neuroplasticidade dele está aberta agora, mas o tempo não perdoa."
    ("0:00:00.10", "0:00:02.30", "Hook", "Se o seu filho tem autismo\\nou atraso no desenvolvimento..."),
    ("0:00:02.30", "0:00:04.50", "Urgency", "Me escuta com muita atenção:"),
    ("0:00:04.50", "0:00:07.10", "Default", "A janela de neuroplasticidade dele\\nestá aberta agora..."),
    ("0:00:07.10", "0:00:09.15", "Urgency", "MAS O TEMPO NÃO PERDOA!"),
    
    # 9.50 - 14.35s: "A cada mês que ele passa vidrado nas telas, conexões cerebrais preciosas são perdidas."
    ("0:00:09.50", "0:00:11.80", "Default", "A cada mês vidrado nas telas..."),
    ("0:00:11.80", "0:00:14.35", "Hook", "Conexões cerebrais preciosas\\nsão perdidas!"),
    
    # 14.80 - 21.73s: "E você sabe o medo que aperta o peito: o medo da fala não destravar, dele sofrer na escola e ficar isolado no próprio mundinho."
    ("0:00:14.80", "0:00:17.20", "Urgency", "E você sabe o medo\\nque aperta o peito:"),
    ("0:00:17.20", "0:00:19.40", "Default", "O medo da fala não destravar..."),
    ("0:00:19.40", "0:00:21.73", "Hook", "Dele sofrer na escola\\ne ficar isolado!"),
    
    # 22.10 - 24.79s: "As terapias são caras e a fila do SUS é demorada."
    ("0:00:22.10", "0:00:24.79", "Default", "As terapias são caríssimas\\ne a fila é demorada..."),
    
    # 25.10 - 29.33s: "Mas o cérebro dele aprende por estímulos visuais e sensoriais específicos."
    ("0:00:25.10", "0:00:27.20", "Default", "Mas o cérebro dele aprende..."),
    ("0:00:27.20", "0:00:29.33", "Hook", "Por estímulos visuais\\ne sensoriais certos!"),
    
    # 29.70 - 40.77s: "Reunimos mais de 300 Dinâmicas Lúdicas Adaptadas para você aplicar em apenas 15 minutos por dia, com materiais simples que já tem em casa, destravando o foco, a fala e acalmando crises."
    ("0:00:29.70", "0:00:32.40", "Urgency", "Reunimos mais de 300\\nDinâmicas Lúdicas Adaptadas!"),
    ("0:00:32.40", "0:00:35.10", "Default", "Apenas 15 minutos por dia..."),
    ("0:00:35.10", "0:00:37.60", "Default", "Com materiais simples\\nque você já tem em casa!"),
    ("0:00:37.60", "0:00:40.77", "Hook", "Destravando o foco, a fala\\ne acalmando crises!"),
    
    # 41.10 - 44.78s: "O kit completo está liberado hoje por apenas 14 e 90."
    ("0:00:41.10", "0:00:44.78", "Urgency", "Kit Completo + 5 Bônus\\nPOR APENAS R$ 14,90!"),
    
    # 45.10 - 50.08s: "Não deixe essa janela fechar. Toque em Saiba Mais aqui embaixo e garanta o seu agora mesmo."
    ("0:00:45.10", "0:00:47.30", "Default", "Não deixe essa janela fechar!"),
    ("0:00:47.30", "0:00:50.40", "Hook", "Toque em SAIBA MAIS aqui embaixo\\ne comece hoje mesmo! 👉")
]

with open("/home/pedrocoelho/Downloads/atividades-autismo/legendas_tea.ass", "w", encoding="utf-8") as f:
    f.write(ass_header)
    for start, end, style, text in events:
        f.write(f"Dialogue: 0,{start},{end},{style},,0,0,0,,{text}\n")

print("Legendas ASS atualizadas com MarginV=410!")
