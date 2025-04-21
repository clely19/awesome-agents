# slack-summarizer
Building a tool that uses AI agents to summarize Slack threads

## Setup

### 1. Slack App Configuration

1. Create a new Slack App at https://api.slack.com/apps
2. Enable Socket Mode
3. Add these bot token scopes:
   - app_mentions:read
   - channels:history
   - chat:write
   - users:read
4. Install the app to your workspace
5. Copy your Bot Token and App Token


### 2. Environment Setup

1. Clone the repository
2. Create and activate a virtual environment:
\`\`\`bash
#### Create virtual environment
python -m venv .venv

#### Activate virtual environment
##### On macOS/Linux:
source .venv/bin/activate
##### On Windows:
.venv\\Scripts\\activate
\`\`\`

3. Install dependencies:
\`\`\`bash
pip install -r requirements.txt
\`\`\`

4. Create a \`.env\` file:
\`\`\`bash
SLACK_BOT_TOKEN=xoxb-your-bot-token
SLACK_APP_TOKEN=xapp-your-app-token
GOOGLE_API_KEY=your-google-api-key
\`\`\`


### 3. Running the Bot

1. Ensure your virtual environment is activated
2. Run the bot:
\`\`\`bash
python main_pipeline.py
\`\`\`


## Usage

1. Invite the bot to your channel
2. Start or join a thread
3. Mention the bot with the word "summary" (e.g., "@SlackSummarizer summary")
4. The bot will analyze the thread and provide a concise summary
