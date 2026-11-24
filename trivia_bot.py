import socket, threading, time, re, openai

# === CONFIG ===
OPENAI_API_KEY = "TOKEN HERE"
TWITCH_TOKEN    = "oauth:TOKEN HERE"
BOT_NICK        = "BOT NAME HERE"
CHANNEL         = "BROADCASTER NAME HERE"

# === GAME STATE ===
game_active    = False
correct_answer = None
answered_users = set()
leaderboard    = {}

# === OPENAI CLIENT ===
client = openai.OpenAI(api_key=OPENAI_API_KEY)

# === CONNECT TO IRC ===
irc = socket.socket()
irc.connect(("irc.chat.twitch.tv", 6667))
irc.send(f"PASS {TWITCH_TOKEN}\r\n".encode())
irc.send(f"NICK {BOT_NICK}\r\n".encode())
irc.send(f"JOIN {CHANNEL}\r\n".encode())
print("🔌 Connected to Twitch IRC, joined", CHANNEL)

def send_message(msg: str):
    irc.send(f"PRIVMSG {CHANNEL} :{msg}\r\n".encode())

def fetch_question():
    resp = client.chat.completions.create(
        model="gpt-4o",
        messages=[
          {"role":"system","content":(
            "You are a trivia host. Ask exactly one  multiple-choice question about any video game and include all types of video games and do not repeat questions and limit the Legend of Zelda questions "
            "with options A), B), C), D) each on its own line, then 'Answer: X'."
          )},
          {"role":"user","content":"Give me one trivia question."}
        ]
    )
    text = resp.choices[0].message.content.strip()
    m = re.search(r'Answer[: ]+([A-D])', text, re.IGNORECASE)
    ans = m.group(1).upper() if m else "A"
    lines = [l for l in text.splitlines() if not l.lower().startswith("answer")]
    clean = [re.sub(r"^([A-D])[\):\.]", r"\1 :", l.strip()) for l in lines]
    return clean, ans

def start_trivia():
    global game_active, correct_answer, answered_users
    if game_active:
        return send_message("⚠️ A trivia is already running!")
    question, correct_answer = fetch_question()
    game_active = True
    answered_users.clear()

    send_message("🎮 VIDEO GAME TRIVIA TIME! <3")
    for line in question: send_message(line)
    send_message("⏳ You have 30 seconds! Type A, B, C, or D.")

    deadline = time.time() + 30
    while time.time() < deadline and game_active:
        time.sleep(0.1)
    if game_active:
        send_message(f"⏰ Time's up! The answer was **{correct_answer}**.")
        game_active = False

def show_leaderboard():
    if not leaderboard:
        return send_message("📉 No scores yet!")
    top = sorted(leaderboard.items(), key=lambda x: x[1], reverse=True)[:5]
    send_message("🏆 Leaderboard: " + " | ".join(f"{u}: {s}" for u,s in top))

def handle_privmsg(user, msg):
    global game_active, correct_answer, answered_users, leaderboard

    # commands
    if msg == "!trivia":
        threading.Thread(target=start_trivia, daemon=True).start()
        return
    if msg == "!leaderboard":
        return show_leaderboard()

    # answer checking
    if game_active:
        m = re.match(r'^([A-D])', msg.strip().upper())
        if m and user not in answered_users:
            answered_users.add(user)
            guess = m.group(1)
            if guess == correct_answer:
                leaderboard[user] = leaderboard.get(user, 0) + 1
                send_message(
                  f"🎉 {user} got it right! Answer was **{correct_answer}**. "
                  f"You now have {leaderboard[user]} point(s)."
                )
                game_active = False

# === MAIN LOOP ===
buf = ""
while True:
    data = irc.recv(2048).decode(errors="ignore")
    if not data: break
    buf += data
    while "\r\n" in buf:
        line, buf = buf.split("\r\n",1)
        if line.startswith("PING"):
            irc.send("PONG :tmi.twitch.tv\r\n".encode()); continue
        m = re.match(r'^:([^!]+)!.* PRIVMSG #[^ ]+ :(.+)$', line)
        if m:
            user, message = m.groups()
            print(f"[CHAT] {user}: {message}")
            handle_privmsg(user.lower(), message)
