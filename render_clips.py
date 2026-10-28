import subprocess
import os

scenes = [
    {"file": "scene_01.jpg", "dur": 8.5, "zoom": "in"},
    {"file": "scene_02.jpg", "dur": 8.0, "zoom": "pan_down"},
    {"file": "scene_03.jpg", "dur": 8.0, "zoom": "in"},
    {"file": "scene_04.jpg", "dur": 8.5, "zoom": "out"},
    {"file": "scene_05.jpg", "dur": 8.5, "zoom": "in"},
    {"file": "scene_06.jpg", "dur": 9.4, "zoom": "in"}
]

os.chdir("/home/pedrocoelho/Downloads/atividades-autismo")

clip_files = []
for idx, s in enumerate(scenes):
    out_clip = f"clip_{idx+1}.mp4"
    clip_files.append(out_clip)
    fps = 30
    frames = int(s["dur"] * fps)
    
    # Zoompan or smooth scale
    # We do a subtle Ken Burns zoompan
    if s["zoom"] == "in":
        vf = f"scale=1200:2133,zoompan=z='min(zoom+0.0004,1.08)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={frames}:s=1080x1920:fps={fps}"
    elif s["zoom"] == "out":
        vf = f"scale=1200:2133,zoompan=z='if(lte(zoom,1.0),1.08,max(1.0,zoom-0.0004))':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={frames}:s=1080x1920:fps={fps}"
    else: # pan_down
        vf = f"scale=1200:2133,zoompan=z=1.05:x='iw/2-(iw/zoom/2)':y='min(y+0.3,ih/2)':d={frames}:s=1080x1920:fps={fps}"
        
    cmd = [
        "ffmpeg", "-y", "-loop", "1", "-i", s["file"],
        "-vf", vf,
        "-c:v", "libx264", "-t", str(s["dur"]),
        "-pix_fmt", "yuv420p", "-preset", "veryfast",
        out_clip
    ]
    print(f"Rendering {out_clip} ({s['dur']}s)...")
    subprocess.run(cmd, check=True)

# Write concat list
with open("concat_list.txt", "w") as f:
    for c in clip_files:
        f.write(f"file '{c}'\n")

print("Concatenating all clips...")
concat_cmd = [
    "ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", "concat_list.txt",
    "-c", "copy", "video_raw_concat.mp4"
]
subprocess.run(concat_cmd, check=True)

print("Merging audio and subtitles...")
final_cmd = [
    "ffmpeg", "-y",
    "-i", "video_raw_concat.mp4",
    "-i", "audio_final_tea.m4a",
    "-vf", "ass=legendas_tea.ass",
    "-c:v", "libx264", "-preset", "medium", "-crf", "18",
    "-c:a", "aac", "-b:a", "192k",
    "-shortest",
    "anuncio_video_tea_1080x1920.mp4"
]
subprocess.run(final_cmd, check=True)
print("SUCCESS: anuncio_video_tea_1080x1920.mp4 created!")
