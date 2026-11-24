# FrizzQuiz
A trivia bot powered by OpenAI that encourages community engagement on Twitch


# 🎮 FrizzQuiz – AI-Powered Twitch Trivia Bot

FrizzQuiz is an interactive, AI-powered trivia bot developed in Python for Twitch live-streaming communities. The bot integrates Twitch's Internet Relay Chat (IRC) protocol with the OpenAI API to generate video game trivia questions and encourage real-time audience participation.

## Project Motivation

As a Twitch Partner since 2018 and a Computer Science graduate pursuing a Master's degree in Computer Science, I wanted to combine my passion for gaming, software development, and artificial intelligence to create an interactive experience for my streaming community.

FrizzQuiz was developed to enhance viewer engagement through live trivia games, friendly competition, and AI-generated content.

## Features

- AI-generated video game trivia questions using GPT-4o.
- Real-time Twitch chat integration through IRC.
- Multiple-choice questions with four possible answers.
- Timed trivia rounds with a 30-second response window.
- Automated answer validation and scoring.
- One answer attempt per viewer per round.
- Session-based leaderboard displaying the top five players.
- Multithreaded trivia execution to keep chat processing responsive.
- Twitch IRC PING/PONG handling.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core application development |
| OpenAI API | AI-generated trivia questions |
| GPT-4o | Natural language generation |
| Twitch IRC | Real-time chat communication |
| Socket Programming | Network communication |
| Threading | Concurrent trivia execution |
| Regular Expressions | Message parsing and answer extraction |
| Python Dictionaries and Sets | Score tracking and game state management |

## How It Works

1. A viewer enters `!trivia` in Twitch chat.
2. The bot requests a video game trivia question from the OpenAI API.
3. The generated question and four answer choices are displayed in chat.
4. Viewers have 30 seconds to submit an answer.
5. The first viewer to answer correctly earns a point.
6. Viewers can display the top five players using `!leaderboard`.

## Chat Commands

| Command | Description |
|---|---|
| `!trivia` | Starts a new trivia round |
| `!leaderboard` | Displays the top five players |
| `A`, `B`, `C`, `D` | Submits a trivia answer |

## Installation

### 1. Clone the repository

Clone this repository to your local machine using Git or GitHub Desktop.

### 2. Install dependencies

```bash
pip install openai
```

### 3. Configure the bot

The application requires the following configuration values:

- OpenAI API key
- Twitch OAuth token
- Twitch bot username
- Twitch channel name (including the # prefix)

The source code contains placeholder credentials for demonstration purposes. Never commit real API keys or authentication tokens to a public repository.

### 4. Run the application

```bash
python trivia_bot.py
```

## Technical Concepts Demonstrated

- API integration
- Generative artificial intelligence
- Network and socket programming
- Concurrent programming
- Real-time event processing
- String parsing and regular expressions
- Game state management
- Interactive application development

## Current Limitations

- Leaderboard scores are stored in memory and reset when the application restarts.
- AI-generated questions may occasionally repeat or contain inaccuracies.
- The current implementation requires manual configuration.

## Future Improvements

- Persistent leaderboard storage using a database.
- Trivia categories and difficulty levels.
- Duplicate question detection.
- Environment variable-based credential management.
- Improved error handling and automatic reconnection.
- Secure IRC connections using TLS.
- Thread-safe game state management.
- Customizable trivia settings for streamers.
- Web-based dashboard for bot configuration and statistics.

## Author

**Constance Rios**

- B.S. in Computer Science, Cum Laude
- M.S. in Computer Science — In Progress
- NSF ExCELS Scholar
- Twitch Partner since 2018
- Former competitive Call of Duty player

GitHub: https://github.com/ConstanceR1

---

Developed with a passion for gaming, artificial intelligence, and building interactive experiences for online communities.
